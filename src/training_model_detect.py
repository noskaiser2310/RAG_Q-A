import pymupdf
import numpy as np
import pandas as pd
from pathlib import Path
from typing import List, Dict, Tuple, Optional, Any
from dataclasses import dataclass
import re
from difflib import SequenceMatcher
import lightgbm as lgb
from sklearn.model_selection import train_test_split, StratifiedKFold
from sklearn.metrics import precision_recall_fscore_support, confusion_matrix, classification_report, accuracy_score
from sklearn.utils.class_weight import compute_class_weight
import joblib
import warnings
import hashlib
import json
from datetime import datetime
import matplotlib.pyplot as plt
import seaborn as sns
warnings.filterwarnings('ignore')


@dataclass
class TextLine:
    text: str
    font_size: float
    font_name: str
    is_bold: bool
    x0: float
    y0: float
    x1: float
    y1: float
    page: int
    page_height: float
    page_width: float

class ThresholdOptimizer:
    """Optimize prediction thresholds for each class to maximize F1-score"""
    
    def __init__(self):
        self.optimal_thresholds = {}
        
    def find_optimal_threshold(self, y_true: np.ndarray, y_probs: np.ndarray, class_label: int) -> float:
        """Find optimal threshold for a specific class to maximize F1-score"""
        if class_label not in np.unique(y_true):
            return 0.
            
        # Get probabilities for this class
        prob_class = y_probs[:, class_label]
        
        # Define objective function to minimize (negative F1)
        def objective(threshold):
            y_pred_class = (prob_class >= threshold).astype(int)
            true_class = (y_true == class_label).astype(int)
            
            if np.sum(y_pred_class) == 0 or np.sum(true_class) == 0:
                return 1.0  # Worst possible F1
                
            precision, recall, f1, _ = precision_recall_fscore_support(
                true_class, y_pred_class, average='binary', zero_division=0
            )
            return -f1  # Minimize negative F1
        
        # Find optimal threshold
        try:
            result = minimize_scalar(objective, bounds=(0.1, 0.9), method='bounded')
            return max(0.1, min(0.9, result.x))
        except:
            return 0.85
    
    def optimize_all_thresholds(self, y_true: np.ndarray, y_probs: np.ndarray, classes: List[int]) -> Dict[int, float]:
        """Optimize thresholds for all specified classes"""
        optimal_thresholds = {}
        
        for class_label in classes:
            if class_label > 0:  # Only optimize for heading classes (1-4)
                threshold = self.find_optimal_threshold(y_true, y_probs, class_label)
                optimal_thresholds[class_label] = threshold
                print(f"  Class {class_label}: optimal threshold = {threshold:.3f}")
        
        return optimal_thresholds
class DataValidator:
    """Validate and verify training data quality"""
    
    def __init__(self):
        self.validation_results = {}
        
    def validate_data_quality(self, X: np.ndarray, y: np.ndarray, feature_names: List[str]) -> Dict[str, Any]:
        """Comprehensive data quality validation"""
        validation_report = {}
        
        # Basic statistics
        validation_report['total_samples'] = len(X)
        validation_report['total_features'] = X.shape[1] if len(X) > 0 else 0
        
        # Class distribution - convert numpy types to Python native types
        unique_classes, class_counts = np.unique(y, return_counts=True)
        class_dist = {}
        for cls, count in zip(unique_classes, class_counts):
            class_dist[int(cls)] = int(count)  # Convert to native Python types
        validation_report['class_distribution'] = class_dist
        
        # Calculate imbalance ratio only for heading classes (1-4)
        heading_counts = [count for cls, count in zip(unique_classes, class_counts) if cls > 0]
        if len(heading_counts) > 1:
            validation_report['heading_imbalance_ratio'] = float(max(heading_counts) / min(heading_counts))
        else:
            validation_report['heading_imbalance_ratio'] = 1.0
        
        # Feature statistics
        feature_stats = {}
        for i, feature_name in enumerate(feature_names):
            if len(X) > 0 and i < X.shape[1]:
                feature_data = X[:, i]
                feature_stats[feature_name] = {
                    'mean': float(np.mean(feature_data)),
                    'std': float(np.std(feature_data)),
                    'min': float(np.min(feature_data)),
                    'max': float(np.max(feature_data)),
                    'missing_values': int(np.sum(np.isnan(feature_data)))
                }
        validation_report['feature_statistics'] = feature_stats
        
        # Data quality flags - FOCUS ON HEADING CLASSES
        validation_report['quality_flags'] = {
            'has_sufficient_samples': len(X) >= 100,
            'has_multiple_heading_classes': len([cls for cls in unique_classes if cls > 0]) > 1,
            'no_missing_values': all(stats['missing_values'] == 0 for stats in feature_stats.values()),
            'reasonable_heading_imbalance': validation_report['heading_imbalance_ratio'] < 10,
            'feature_variance_adequate': all(stats['std'] > 0.01 for stats in feature_stats.values() 
                                           if feature_names[i] not in ['is_bold', 'font_differs', 'is_first', 'ends_period', 'starts_number', 'numbered_pattern', 'all_caps', 'placeholder'])
        }
        
        # Overall quality score
        quality_score = sum(validation_report['quality_flags'].values()) / len(validation_report['quality_flags'])
        validation_report['overall_quality_score'] = float(quality_score)
        
        return validation_report
    
    def cross_verify_predictions(self, detector: 'MLHeadingDetector', X: np.ndarray, y: np.ndarray, 
                               lines: List[TextLine], sample_size: int = 50) -> Dict[str, Any]:
        """Cross-verify predictions with manual inspection logic - ONLY AFTER TRAINING"""
        if len(X) == 0 or detector.model is None:
            print("  ⚠ Skipping cross-verification: Model not trained yet")
            return {}
            
        # Get predictions with optimized thresholds
        y_probs = detector.model.predict_proba(X)
        preds = detector._predict_with_thresholds(X, y_probs)
        
        verification_results = {
            'high_confidence_samples': [],
            'low_confidence_samples': [],
            'potential_misclassifications': [],
            'pattern_analysis': {}
        }
        
        # Analyze confidence scores - ONLY FOR HEADING CLASSES
        heading_indices = preds > 0
        if np.any(heading_indices):
            heading_confidences = np.max(y_probs[heading_indices], axis=1)
            high_confidence_threshold = 0.8
            low_confidence_threshold = 0.6
            
            for i, (true_label, pred_label) in enumerate(zip(y, preds)):
                if i >= sample_size:
                    break
                    
                # Only analyze heading predictions
                if pred_label > 0:
                    confidence = float(y_probs[i, pred_label])
                    
                    line_data = {
                        'text': lines[i].text if i < len(lines) else '',
                        'true_label': int(true_label),
                        'predicted_label': int(pred_label),
                        'confidence': confidence,
                        'is_correct': bool(true_label == pred_label)
                    }
                    
                    if confidence >= high_confidence_threshold:
                        verification_results['high_confidence_samples'].append(line_data)
                    elif confidence <= low_confidence_threshold:
                        verification_results['low_confidence_samples'].append(line_data)
                        
                    if true_label != pred_label and confidence > 0.7:  # High confidence but wrong
                        verification_results['potential_misclassifications'].append(line_data)
        
        # Pattern analysis for numbered headings
        numbered_patterns_analysis = self._analyze_numbered_patterns(lines, y, preds)
        verification_results['pattern_analysis'] = numbered_patterns_analysis
        
        return verification_results

    def validate_data_before_training(self, X: np.ndarray, y: np.ndarray, feature_names: List[str]) -> bool:
        """Quick validation before training to ensure data is usable - FOCUS ON HEADINGS"""
        if len(X) == 0:
            print("  ✗ No training data available")
            return False
            
        # Check for sufficient heading classes (at least 2 heading classes)
        heading_classes = [cls for cls in np.unique(y) if cls > 0]
        if len(heading_classes) < 2:
            print("  ✗ Need at least 2 heading classes for training")
            return False
            
        # Check for sufficient samples per heading class
        unique, counts = np.unique(y, return_counts=True)
        min_samples_per_class = 5
        for cls, count in zip(unique, counts):
            if cls > 0 and count < min_samples_per_class:  # Only check heading classes
                print(f"  ✗ Heading class {cls} has only {count} samples (min: {min_samples_per_class})")
                return False
                
        print("  ✓ Data validation passed - ready for training")
        return True
    
    def _analyze_numbered_patterns(self, lines: List[TextLine], y_true: np.ndarray, 
                                 y_pred: np.ndarray) -> Dict[str, Any]:
        """Analyze numbered pattern detection accuracy - ONLY HEADINGS"""
        analysis = {
            'true_positives': 0,
            'false_positives': 0,
            'false_negatives': 0,
            'pattern_examples': []
        }
        
        numbered_pattern = re.compile(r'^\d+(\.\d+)*\.?\s')
        
        for i, (line, true, pred) in enumerate(zip(lines, y_true, y_pred)):
            if i >= 100:  # Limit analysis to first 100 samples
                break
                
            has_numbered_pattern = bool(numbered_pattern.match(line.text.strip()))
            
            if has_numbered_pattern:
                if true > 0 and pred > 0:  # Correctly detected as heading
                    analysis['true_positives'] += 1
                elif true > 0 and pred == 0:  # Missed heading
                    analysis['false_negatives'] += 1
                    analysis['pattern_examples'].append({
                        'text': line.text,
                        'true_label': int(true),
                        'predicted_label': int(pred),
                        'type': 'false_negative'
                    })
                elif true == 0 and pred > 0:  # False positive
                    analysis['false_positives'] += 1
                    analysis['pattern_examples'].append({
                        'text': line.text,
                        'true_label': int(true),
                        'predicted_label': int(pred),
                        'type': 'false_positive'
                    })
        
        return analysis



class DataManager:
    """Manage training data caching and loading"""
    
    def __init__(self, cache_dir: str = "working/training_cache"):
        self.cache_dir = Path(cache_dir)
        self.cache_dir.mkdir(parents=True, exist_ok=True)
        
    def get_cache_key(self, input_dir: str, gt_dir: str) -> str:
        """Generate unique cache key based on input directories"""
        dir_info = f"{input_dir}_{gt_dir}"
        return hashlib.md5(dir_info.encode()).hexdigest()[:16]
    
    def save_training_data(self, cache_key: str, X: np.ndarray, y: np.ndarray, 
                         metadata: Dict[str, Any]) -> str:
        """Save training data to cache"""
        cache_file = self.cache_dir / f"{cache_key}_data.npz"
        metadata_file = self.cache_dir / f"{cache_key}_metadata.json"
        
        # Save data
        np.savez(cache_file, X=X, y=y)
        
        # Convert metadata to JSON-serializable format
        serializable_metadata = self._convert_to_serializable(metadata)
        serializable_metadata['saved_at'] = datetime.now().isoformat()
        serializable_metadata['data_shape'] = X.shape if X is not None else None
        
        # Convert class distribution to serializable format
        if 'class_distribution' in serializable_metadata:
            serializable_metadata['class_distribution'] = {
                str(k): int(v) for k, v in serializable_metadata['class_distribution'].items()
            }
        
        with open(metadata_file, 'w', encoding='utf-8') as f:
            json.dump(serializable_metadata, f, indent=2, ensure_ascii=False)
            
        return str(cache_file)
    
    def _convert_to_serializable(self, obj: Any) -> Any:
        """Convert numpy types to Python native types for JSON serialization"""
        if isinstance(obj, (np.integer, np.int32, np.int64)):
            return int(obj)
        elif isinstance(obj, (np.floating, np.float32, np.float64)):
            return float(obj)
        elif isinstance(obj, np.ndarray):
            return obj.tolist()
        elif isinstance(obj, dict):
            return {str(k): self._convert_to_serializable(v) for k, v in obj.items()}
        elif isinstance(obj, list):
            return [self._convert_to_serializable(item) for item in obj]
        elif isinstance(obj, tuple):
            return tuple(self._convert_to_serializable(item) for item in obj)
        else:
            return obj
    
    def load_training_data(self, cache_key: str) -> Tuple[Optional[np.ndarray], Optional[np.ndarray], Dict[str, Any]]:
        """Load training data from cache"""
        cache_file = self.cache_dir / f"{cache_key}_data.npz"
        metadata_file = self.cache_dir / f"{cache_key}_metadata.json"
        
        if not cache_file.exists() or not metadata_file.exists():
            return None, None, {}
            
        try:
            # Load data
            data = np.load(cache_file)
            X, y = data['X'], data['y']
            
            # Load metadata
            with open(metadata_file, 'r', encoding='utf-8') as f:
                metadata = json.load(f)
                
            print(f"✓ Loaded cached training data: {X.shape[0]} samples")
            return X, y, metadata
            
        except Exception as e:
            print(f"✗ Error loading cached data: {e}")
            return None, None, {}
    
    def get_cache_info(self) -> Dict[str, Any]:
        """Get information about cached data"""
        cache_files = list(self.cache_dir.glob("*_data.npz"))
        cache_info = {
            'total_cached_datasets': len(cache_files),
            'cache_files': []
        }
        
        for cache_file in cache_files:
            metadata_file = cache_file.with_name(cache_file.stem.replace('_data', '_metadata') + '.json')
            if metadata_file.exists():
                try:
                    with open(metadata_file, 'r', encoding='utf-8') as f:
                        metadata = json.load(f)
                    cache_info['cache_files'].append({
                        'file': cache_file.name,
                        'saved_at': metadata.get('saved_at', 'unknown'),
                        'data_shape': metadata.get('data_shape', 'unknown'),
                        'class_distribution': metadata.get('class_distribution', {})
                    })
                except:
                    continue
                    
        return cache_info


class FeatureExtractor:
    """Extract 22 features from each text line with ENHANCED numbered pattern detection"""

    def __init__(self):
        self.doc_stats = None
        # ENHANCED: Strict numbered patterns - chỉ tập trung vào 1., 1.1, 1.1.1, etc.
        self.numbered_patterns = [
            r'^\d+\.\s+[A-Za-zÀ-ỹ]',  # 1. Text (bắt đầu bằng số, dấu chấm, khoảng trắng, rồi chữ)
            r'^\d+\.\d+\s+[A-Za-zÀ-ỹ]',  # 1.1 Text
            r'^\d+\.\d+\.\d+\s+[A-Za-zÀ-ỹ]',  # 1.1.1 Text  
            r'^\d+\.\d+\.\d+\.\d+\s+[A-Za-zÀ-ỹ]',  # 1.1.1.1 Text
        ]
        
        # ENHANCED: Strong exclusion patterns
        self.exclude_patterns = [
            r'^.*(hình|figure|bảng|table|biểu đồ|chart|trang|page).*\d',
            r'^.*\d+\s*[-–]\s*\d+.*',  # Number ranges like "1-2"
            r'^\d+$',  # Chỉ có số đơn thuần
            r'^.*[\.:]\d+$',  # Kết thúc bằng .số hoặc :số
        ]

    def compute_document_stats(self, lines: List[TextLine]) -> Dict:
        """Compute document-level statistics"""
        if not lines:
            self.doc_stats = {
                'median_font': 12.0, 'mean_font': 12.0, 'std_font': 1.0,
                'dominant_font': 'unknown', 'median_gap': 10.0, 
                'mean_gap': 10.0, 'std_gap': 5.0
            }
            return self.doc_stats

        font_sizes = [line.font_size for line in lines]
        font_names = [line.font_name for line in lines]

        # Compute gaps
        lines_sorted = sorted(lines, key=lambda l: (l.page, l.y0))
        gaps = []
        for i in range(1, len(lines_sorted)):
            if lines_sorted[i].page == lines_sorted[i-1].page:
                gap = lines_sorted[i].y0 - lines_sorted[i-1].y1
                if gap > 0:
                    gaps.append(gap)

        self.doc_stats = {
            'median_font': float(np.median(font_sizes)),
            'mean_font': float(np.mean(font_sizes)),
            'std_font': float(np.std(font_sizes)) if len(font_sizes) > 1 else 1.0,
            'dominant_font': max(set(font_names), key=font_names.count) if font_names else 'unknown',
            'median_gap': float(np.median(gaps)) if gaps else 10.0,
            'mean_gap': float(np.mean(gaps)) if gaps else 10.0,
            'std_gap': float(np.std(gaps)) if gaps else 5.0,
        }

        return self.doc_stats

    def is_likely_numbered_heading(self, text: str) -> bool:
        """ENHANCED: Strict detection of numbered headings while avoiding false positives"""
        text_clean = text.strip()
        
        # Check exclusion patterns first (tables, figures, etc.)
        for exclude_pattern in self.exclude_patterns:
            if re.match(exclude_pattern, text_clean, re.IGNORECASE):
                return False
        
        # Check inclusion patterns (must be at start and followed by text)
        for pattern in self.numbered_patterns:
            if re.match(pattern, text_clean):
                # EXTRA VALIDATION: text after numbers should be meaningful
                text_after_numbers = re.sub(r'^\d+(\.\d+)*\s*', '', text_clean).strip()
                if (len(text_after_numbers) >= 3 and 
                    any(c.isalpha() for c in text_after_numbers) and
                    not text_after_numbers.lower().startswith(('hình', 'bảng', 'biểu đồ', 'table', 'figure', 'chart'))):
                    return True
                    
        return False

    def extract_features(self, line: TextLine, prev_line: TextLine = None, 
                        next_line: TextLine = None) -> np.ndarray:
        """Extract 22 features from a text line with improved numbered pattern detection"""

        if self.doc_stats is None:
            raise ValueError("Call compute_document_stats first!")

        features = []
        text = line.text

        # === FONT FEATURES (5) ===
        features.append(line.font_size)  # f1: absolute font size

        font_ratio = line.font_size / self.doc_stats['median_font'] if self.doc_stats['median_font'] > 0 else 1.0
        features.append(font_ratio)  # f2: relative to median

        z_score = (line.font_size - self.doc_stats['mean_font']) / self.doc_stats['std_font'] if self.doc_stats['std_font'] > 0 else 0
        features.append(z_score)  # f3: standardized

        features.append(1.0 if line.is_bold else 0.0)  # f4: is bold

        font_differs = 1.0 if line.font_name != self.doc_stats['dominant_font'] else 0.0
        features.append(font_differs)  # f5: font differs from dominant

        # === POSITION FEATURES (6) ===
        relative_y = line.y0 / line.page_height if line.page_height > 0 else 0.5
        features.append(relative_y)  # f6: relative y position (0=top, 1=bottom)

        relative_x = line.x0 / line.page_width if line.page_width > 0 else 0.0
        features.append(relative_x)  # f7: relative x position

        features.append(line.x0)  # f8: distance from left margin (pixels)

        # Gap before
        gap_before = 0.0
        if prev_line and prev_line.page == line.page:
            gap_before = line.y0 - prev_line.y1
        features.append(gap_before)  # f9: gap before line

        # Gap after
        gap_after = 0.0
        if next_line and next_line.page == line.page:
            gap_after = next_line.y0 - line.y1
        features.append(gap_after)  # f10: gap after line

        is_first = 1.0 if (prev_line is None or prev_line.page != line.page) else 0.0
        features.append(is_first)  # f11: is first line of page

        # === TEXT FEATURES (8) ===
        features.append(len(text))  # f12: text length

        word_count = len(text.split())
        features.append(word_count)  # f13: word count

        # Capital word ratio (first letter)
        capital_words = sum(1 for word in text.split() if word and word[0].isupper())
        capital_ratio = capital_words / word_count if word_count > 0 else 0
        features.append(capital_ratio)  # f14: capital word ratio

        # NEW: Uppercase character ratio in entire text
        alpha_chars = sum(1 for c in text if c.isalpha())
        upper_chars = sum(1 for c in text if c.isupper())
        upper_ratio = upper_chars / alpha_chars if alpha_chars > 0 else 0
        features.append(upper_ratio)  # f15: uppercase character ratio

        punct_count = sum(1 for c in text if c in '.,;:!?')
        features.append(punct_count)  # f16: punctuation count

        # NEW: Period count specifically
        period_count = text.count('.')
        features.append(period_count)  # f17: period count

        ends_period = 1.0 if text.endswith('.') else 0.0
        features.append(ends_period)  # f18: ends with period

        starts_number = 1.0 if text and text[0].isdigit() else 0.0
        features.append(starts_number)  # f19: starts with number

        # === PATTERN FEATURES (3) ===
        # ENHANCED: Use strict numbered pattern detection
        matches_numbered = 1.0 if self.is_likely_numbered_heading(text) else 0.0
        features.append(matches_numbered)  # f20: numbered pattern

        is_all_caps = 1.0 if text.isupper() and len(text) > 3 else 0.0
        features.append(is_all_caps)  # f21: ALL CAPS

        # Removed keywords feature to avoid FP
        features.append(0.0)  # f22: placeholder (removed keywords)

        return np.array(features, dtype=np.float32)


class ModelManager:
    """Manage multiple model versions and save all trained models"""
    
    def __init__(self, models_dir: str = "working/models"):
        self.models_dir = Path(models_dir)
        self.models_dir.mkdir(parents=True, exist_ok=True)
        
    def save_model_version(self, detector: 'MLHeadingDetector', version_suffix: str = "", 
                         metrics: Dict[str, Any] = None, training_info: Dict[str, Any] = None) -> str:
        """Save model with versioning and metadata"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        version_name = f"heading_detector_{timestamp}"
        if version_suffix:
            version_name += f"_{version_suffix}"
            
        model_dir = self.models_dir / version_name
        model_dir.mkdir(parents=True, exist_ok=True)
        
        # Save main model
        model_path = model_dir / "model.pkl"
        joblib.dump({
            'model': detector.model,
            'feature_names': detector.feature_names,
            'feature_extractor': detector.feature_extractor
        }, model_path)
        
        # Save metadata
        metadata = {
            'version': version_name,
            'saved_at': datetime.now().isoformat(),
            'feature_count': len(detector.feature_names),
            'feature_names': detector.feature_names
        }
        
        if metrics:
            metadata['metrics'] = {k: float(v) if isinstance(v, (np.floating, float)) else v 
                                 for k, v in metrics.items()}
            
        if training_info:
            metadata['training_info'] = training_info
            
        with open(model_dir / "metadata.json", 'w', encoding='utf-8') as f:
            json.dump(metadata, f, indent=2, ensure_ascii=False)
            
        print(f"✓ Model version saved: {version_name}")
        return str(model_dir)
    
    def get_all_models(self) -> List[Dict[str, Any]]:
        """Get information about all saved models"""
        model_dirs = [d for d in self.models_dir.iterdir() if d.is_dir() and d.name.startswith("heading_detector_")]
        models_info = []
        
        for model_dir in model_dirs:
            metadata_file = model_dir / "metadata.json"
            if metadata_file.exists():
                try:
                    with open(metadata_file, 'r', encoding='utf-8') as f:
                        metadata = json.load(f)
                    models_info.append({
                        'name': model_dir.name,
                        'path': str(model_dir),
                        'metadata': metadata
                    })
                except Exception as e:
                    print(f"Error loading metadata for {model_dir}: {e}")
                    
        return sorted(models_info, key=lambda x: x['metadata']['saved_at'], reverse=True)
    
    def load_latest_model(self) -> Optional[Dict]:
        """Load the most recent model"""
        all_models = self.get_all_models()
        if not all_models:
            return None
            
        latest_model = all_models[0]
        try:
            model_path = Path(latest_model['path']) / "model.pkl"
            detector_data = joblib.load(model_path)
            return {
                'detector_data': detector_data,
                'metadata': latest_model['metadata'],
                'path': latest_model['path']
            }
        except Exception as e:
            print(f"Error loading model {latest_model['name']}: {e}")
            return None
    
    def cleanup_old_models(self, keep_count: int = 5):
        """Keep only the most recent models"""
        all_models = self.get_all_models()
        if len(all_models) <= keep_count:
            return
            
        for model_info in all_models[keep_count:]:
            try:
                import shutil
                shutil.rmtree(model_info['path'])
                print(f"✓ Removed old model: {model_info['name']}")
            except Exception as e:
                print(f"✗ Error removing model {model_info['name']}: {e}")


class MLHeadingDetector:
    """ENHANCED ML-based heading detector with LightGBM (Multi-class)"""

    def __init__(self):
        self.feature_extractor = FeatureExtractor()
        self.data_validator = DataValidator()
        self.data_manager = DataManager()
        self.model_manager = ModelManager()
        self.threshold_optimizer = ThresholdOptimizer()
        self.model = None
        self.feature_names = [
            'font_size', 'font_ratio', 'z_score', 'is_bold', 'font_differs',
            'y_position', 'x_position', 'left_margin', 'gap_before', 'gap_after', 'is_first',
            'text_length', 'word_count', 'capital_ratio', 'upper_ratio', 'punct_count', 
            'period_count', 'ends_period', 'starts_number', 'numbered_pattern', 
            'all_caps', 'placeholder'
        ]
        self.optimal_thresholds = {1: 0.5, 2: 0.5, 3: 0.5, 4: 0.5}  # Default thresholds


    def extract_lines(self, pdf_path: str) -> List[TextLine]:
        """Extract all text lines from PDF"""

        doc = pymupdf.open(pdf_path)
        all_lines = []

        for page_num, page in enumerate(doc, start=1):
            text_dict = page.get_text("dict")
            page_height = page.rect.height
            page_width = page.rect.width

            for block in text_dict["blocks"]:
                if block["type"] != 0:
                    continue

                for line in block.get("lines", []):
                    line_text = ""
                    font_sizes = []
                    font_names = []

                    for span in line.get("spans", []):
                        line_text += span["text"]
                        font_sizes.append(span["size"])
                        font_names.append(span["font"])

                    line_text = line_text.strip()
                    if not line_text:
                        continue

                    all_lines.append(TextLine(
                        text=line_text,
                        font_size=float(np.median(font_sizes)) if font_sizes else 12.0,
                        font_name=max(set(font_names), key=font_names.count) if font_names else 'unknown',
                        is_bold=any('bold' in f.lower() or 'heavy' in f.lower() for f in font_names),
                        x0=line['bbox'][0],
                        y0=line['bbox'][1],
                        x1=line['bbox'][2],
                        y1=line['bbox'][3],
                        page=page_num,
                        page_height=page_height,
                        page_width=page_width
                    ))

        doc.close()
        return all_lines

    def generate_training_data(self, pdf_path: str, gt_md_path: str) -> Tuple[np.ndarray, np.ndarray, List[TextLine]]:
        """FIXED: Generate features and labels - CHỈ gắn nhãn cho các heading markdown từ file GT"""

        # Extract lines
        lines = self.extract_lines(pdf_path)

        if not lines:
            print(f"  No lines extracted from {pdf_path}")
            return np.array([]), np.array([]), []

        # Compute document stats
        self.feature_extractor.compute_document_stats(lines)

        # Parse ground truth headings with levels - CHỈ lấy các heading markdown (#, ##, ###, ####)
        gt_headings = self._parse_markdown_with_levels(gt_md_path)
        
        if not gt_headings:
            print(f"  No markdown headings found in {gt_md_path}")
            return np.array([]), np.array([]), []

        # Extract features and labels
        X = []
        y = []

        for i, line in enumerate(lines):
            prev_line = lines[i-1] if i > 0 else None
            next_line = lines[i+1] if i < len(lines) - 1 else None

            features = self.feature_extractor.extract_features(line, prev_line, next_line)
            X.append(features)

            heading_level = self._fuzzy_match_with_level(line.text, gt_headings, threshold=0.8)
            y.append(heading_level)

        return np.array(X), np.array(y), lines

    def _fuzzy_match_with_level(self, text: str, gt_headings: List[Dict], threshold: float = 0.8) -> int:
        """Check if text matches any ground truth heading and return its level"""
        
        text_lower = text.lower().strip()
        best_score = 0
        best_level = 0  # Default: not a heading

        for gt_heading in gt_headings:
            gt_text = gt_heading['text'].lower().strip()
            score = SequenceMatcher(None, text_lower, gt_text).ratio()
            
            if score > best_score and score >= threshold:
                best_score = score
                best_level = gt_heading['level']

        return best_level

    def _parse_markdown_with_levels(self, md_path: str) -> List[Dict]:
        """Parse markdown to extract headings with levels (1-4) - CHỈ lấy markdown headings"""
        
        if not Path(md_path).exists():
            print(f"  Markdown file not found: {md_path}")
            return []

        try:
            with open(md_path, 'r', encoding='utf-8') as f:
                content = f.read()

            headings = []
            for line in content.split('\n'):
                line = line.strip()
                if not line:
                    continue

                # FIXED: CHỈ match markdown headings: # Heading 1, ## Heading 2, etc.
                # Bỏ qua tất cả các dòng không phải heading markdown
                match = re.match(r'^(#{1,4})\s+(.+)$', line)
                if match:
                    level = len(match.group(1))
                    text = match.group(2).strip()
                    headings.append({'text': text, 'level': level})

            print(f"  Extracted {len(headings)} markdown headings from {md_path}")
            return headings
        except Exception as e:
            print(f"  Error parsing markdown {md_path}: {e}")
            return []

    def train(self, X_train: np.ndarray, y_train: np.ndarray, X_val: np.ndarray = None, y_val: np.ndarray = None):
        """ENHANCED: Train LightGBM model with focus on heading recall and threshold optimization"""

        print(f"Training samples: {len(X_train)}")
        
        # Calculate class distribution - FOCUS ON HEADING CLASSES
        unique, counts = np.unique(y_train, return_counts=True)
        class_dist = {}
        for cls, count in zip(unique, counts):
            class_dist[int(cls)] = int(count)
        print("Class distribution:")
        for level, count in class_dist.items():
            if level == 0:
                print(f"  Level {level} (Not heading): {count} samples ({count/len(y_train)*100:.2f}%)")
            else:
                print(f"  Level {level}: {count} samples ({count/len(y_train)*100:.2f}%)")

        # Handle class imbalance - less aggressive merging
        y_train_adj = self._adjust_rare_classes_enhanced(y_train)
        
        # Recalculate class distribution after adjustment
        unique_adj, counts_adj = np.unique(y_train_adj, return_counts=True)
        print("\nAdjusted class distribution:")
        for level, count in zip(unique_adj, counts_adj):
            if level == 0:
                print(f"  Level {level} (Not heading): {count} samples ({count/len(y_train_adj)*100:.2f}%)")
            else:
                print(f"  Level {level}: {count} samples ({count/len(y_train_adj)*100:.2f}%)")

        # ENHANCED: Compute class weights with manual boost for headings
        class_weights = compute_class_weight(
            class_weight='balanced',
            classes=np.unique(y_train_adj),
            y=y_train_adj
        )
        
        # MANUAL BOOST: Increase weight for heading classes (1-4)
        class_weight_dict = {}
        for i, cls in enumerate(np.unique(y_train_adj)):
            base_weight = float(class_weights[i])
            if cls > 0:  # Heading classes
                boosted_weight = base_weight * 3.0  # Triple the importance
                class_weight_dict[int(cls)] = boosted_weight
            else:
                class_weight_dict[int(cls)] = base_weight
                
        print(f"Enhanced Class weights: {class_weight_dict}")

        # ENHANCED: LightGBM with focus on recall
        self.model = lgb.LGBMClassifier(
            n_estimators=300,
            max_depth=10,
            learning_rate=0.05,
            num_leaves=31,
            min_child_samples=10,
            subsample=0.7,
            colsample_bytree=0.7,
            reg_alpha=0.1,
            reg_lambda=0.1,
            class_weight=class_weight_dict,
            random_state=42,
            n_jobs=-1,
            verbose=-1,
            boosting_type='gbdt'
        )

        # Train with validation set if provided
        if X_val is not None and y_val is not None:
            self.model.fit(
                X_train, y_train_adj,
                eval_set=[(X_val, y_val)],
                eval_metric='multi_logloss',
            )
        else:
            self.model.fit(X_train, y_train_adj)

        # Optimize thresholds on validation set or training set
        if X_val is not None and y_val is not None:
            print("\nOptimizing thresholds on validation set...")
            y_val_probs = self.model.predict_proba(X_val)
            self.optimal_thresholds = self.threshold_optimizer.optimize_all_thresholds(
                y_val, y_val_probs, [1, 2, 3, 4]
            )
        else:
            print("\nOptimizing thresholds on training set...")
            y_train_probs = self.model.predict_proba(X_train)
            self.optimal_thresholds = self.threshold_optimizer.optimize_all_thresholds(
                y_train_adj, y_train_probs, [1, 2, 3, 4]
            )

        # Print feature importance
        print("\nTop 15 Important Features:")
        importances = self.model.feature_importances_
        indices = np.argsort(importances)[::-1][:15]

        for i, idx in enumerate(indices):
            print(f"  {i+1}. {self.feature_names[idx]:20s}: {importances[idx]:.4f}")

        return y_train_adj

    def _predict_with_thresholds(self, X: np.ndarray, y_probs: np.ndarray = None) -> np.ndarray:
        """Predict with optimized thresholds for heading classes"""
        if y_probs is None:
            y_probs = self.model.predict_proba(X)
        
        # Get default predictions (highest probability)
        default_preds = np.argmax(y_probs, axis=1)
        
        # Apply thresholds for heading classes
        for i in range(len(default_preds)):
            pred_class = default_preds[i]
            if pred_class in self.optimal_thresholds:
                if y_probs[i, pred_class] < self.optimal_thresholds[pred_class]:
                    # If probability below threshold, set to non-heading
                    default_preds[i] = 0
        
        return default_preds
    def _adjust_rare_classes_enhanced(self, y: np.ndarray) -> np.ndarray:
        """ENHANCED: Less aggressive class merging - preserve heading classes"""
        unique, counts = np.unique(y, return_counts=True)
        y_adj = y.copy()
        
        # Only merge extremely rare classes (less than 5 samples) - ONLY FOR HEADINGS
        for level, count in zip(unique, counts):
            if count < 5 and level > 0:  # Only merge rare heading classes
                # Find nearest heading level with sufficient samples
                possible_targets = [l for l in unique if l > 0 and np.sum(y == l) >= 10]
                if possible_targets:
                    target_level = min(possible_targets, key=lambda x: abs(x - level))
                    print(f"  Merging level {level} ({count} samples) into level {target_level}")
                    y_adj[y_adj == level] = target_level
                else:
                    # Fallback: merge into level 1
                    print(f"  Merging level {level} ({count} samples) into level 1")
                    y_adj[y_adj == level] = 1
        
        return y_adj
    def evaluate(self, X_test: np.ndarray, y_test: np.ndarray) -> Dict:
        """Evaluate model performance - FOCUS ON HEADING CLASSES (1-4)"""

        # Adjust test labels same as training
        y_test_adj = self._adjust_rare_classes_enhanced(y_test)
        
        # Get predictions with optimized thresholds
        y_probs = self.model.predict_proba(X_test)
        preds = self._predict_with_thresholds(X_test, y_probs)

        # FOCUS ON HEADING CLASSES: Filter out class 0 for heading-specific metrics
        heading_indices = y_test_adj > 0
        heading_preds = preds[heading_indices]
        heading_true = y_test_adj[heading_indices]
        
        if len(heading_true) > 0:
            # Heading-specific metrics
            heading_accuracy = accuracy_score(heading_true, heading_preds)
            heading_precision, heading_recall, heading_f1, _ = precision_recall_fscore_support(
                heading_true, heading_preds, average='weighted', zero_division=0
            )
            
            # Per-class metrics for headings only
            heading_classes = sorted(np.unique(heading_true))
            per_class_metrics = precision_recall_fscore_support(
                heading_true, heading_preds, average=None, zero_division=0, labels=heading_classes
            )
            
            # Heading confusion matrix
            heading_cm = confusion_matrix(heading_true, heading_preds, labels=heading_classes)
        else:
            heading_accuracy = heading_precision = heading_recall = heading_f1 = 0.0
            per_class_metrics = ([], [], [], [])
            heading_cm = np.array([])
            heading_classes = []

        # Overall metrics (including non-headings) for reference
        overall_accuracy = accuracy_score(y_test_adj, preds)

        print("\n" + "="*70)
        print("EVALUATION RESULTS - FOCUS ON HEADING CLASSES (1-4)")
        print("="*70)
        print(f"Overall Accuracy (all classes): {overall_accuracy:.4f}")
        print(f"Heading-only Accuracy:          {heading_accuracy:.4f}")
        print(f"Heading-only Precision:         {heading_precision:.4f}")
        print(f"Heading-only Recall:            {heading_recall:.4f}")
        print(f"Heading-only F1 Score:          {heading_f1:.4f}")
        
        if heading_classes:
            print(f"\nPer-class Metrics (Headings only):")
            for i, cls in enumerate(heading_classes):
                print(f"  Level {cls}: Precision={per_class_metrics[0][i]:.4f}, "
                      f"Recall={per_class_metrics[1][i]:.4f}, F1={per_class_metrics[2][i]:.4f}")

            print(f"\nConfusion Matrix (Headings only):")
            print(heading_cm)

        # Show some misclassified heading examples
        heading_misclassified = np.where((heading_true != heading_preds) & (heading_true > 0))[0]
        if len(heading_misclassified) > 0 and len(heading_misclassified) <= 10:
            print(f"\nSample heading misclassifications ({len(heading_misclassified)} total):")
            for idx in heading_misclassified[:5]:
                print(f"  True: {heading_true[idx]}, Predicted: {heading_preds[idx]}")

        return {
            'overall_accuracy': float(overall_accuracy),
            'heading_accuracy': float(heading_accuracy),
            'heading_precision': float(heading_precision),
            'heading_recall': float(heading_recall),
            'heading_f1': float(heading_f1),
            'heading_confusion_matrix': heading_cm.tolist() if len(heading_cm) > 0 else [],
            'heading_classes': [int(cls) for cls in heading_classes],
            'per_class_metrics': [metric.tolist() for metric in per_class_metrics] if heading_classes else []
        }

    def evaluate_heading_detection(self, X_test: np.ndarray, y_test: np.ndarray, lines_test: List[TextLine]) -> Dict:
        """ENHANCED: Heading-specific evaluation metrics with threshold optimization"""
        
        # Get predictions with optimized thresholds
        y_probs = self.model.predict_proba(X_test)
        preds = self._predict_with_thresholds(X_test, y_probs)
        
        # FOCUS ON HEADING DETECTION (classes 1-4)
        heading_indices_true = y_test > 0
        heading_indices_pred = preds > 0
        
        total_headings = np.sum(heading_indices_true)
        detected_headings = np.sum(heading_indices_pred)
        correct_detections = np.sum(heading_indices_true & heading_indices_pred)
        
        # Calculate detection metrics
        detection_precision = correct_detections / detected_headings if detected_headings > 0 else 0
        detection_recall = correct_detections / total_headings if total_headings > 0 else 0
        detection_f1 = 2 * (detection_precision * detection_recall) / (detection_precision + detection_recall) if (detection_precision + detection_recall) > 0 else 0
        
        # Level-wise accuracy for correctly detected headings
        correctly_detected_indices = heading_indices_true & heading_indices_pred
        if np.any(correctly_detected_indices):
            level_accuracy = accuracy_score(
                y_test[correctly_detected_indices], 
                preds[correctly_detected_indices]
            )
        else:
            level_accuracy = 0.0

        print("\n" + "="*70)
        print("ENHANCED HEADING DETECTION EVALUATION")
        print("="*70)
        print(f"Detection Metrics:")
        print(f"  Precision: {detection_precision:.4f}")
        print(f"  Recall:    {detection_recall:.4f}")
        print(f"  F1-Score:  {detection_f1:.4f}")
        print(f"  Level Accuracy: {level_accuracy:.4f}")
        
        print(f"\nDetection Analysis:")
        print(f"  Total headings in test set: {total_headings}")
        print(f"  Detected as headings: {detected_headings}")
        print(f"  Correctly detected: {correct_detections}")
        print(f"  Heading Detection Rate: {detection_recall*100:.1f}%" if total_headings > 0 else "  Heading Detection Rate: N/A")
        
        # Analyze false negatives
        false_negatives = np.where(heading_indices_true & ~heading_indices_pred)[0]
        if len(false_negatives) > 0:
            print(f"\nFalse Negatives Analysis ({len(false_negatives)} missed headings):")
            for idx in false_negatives[:5]:  # Show first 5
                print(f"  Level {y_test[idx]}: {lines_test[idx].text[:80]}...")
        
        return {
            'detection_precision': float(detection_precision),
            'detection_recall': float(detection_recall),
            'detection_f1': float(detection_f1),
            'level_accuracy': float(level_accuracy),
            'total_headings': int(total_headings),
            'detected_headings': int(detected_headings),
            'correct_detections': int(correct_detections),
            'false_negatives': int(len(false_negatives))
        }
    
    def cross_validate(self, X: np.ndarray, y: np.ndarray, cv_folds: int = 5) -> Dict[str, Any]:
        """Perform cross-validation for more reliable evaluation with small data"""
        print(f"\nPerforming {cv_folds}-fold cross-validation...")
        
        # Adjust labels for consistency
        y_adj = self._adjust_rare_classes_enhanced(y)
        
        # Use stratified k-fold for imbalanced data
        skf = StratifiedKFold(n_splits=cv_folds, shuffle=True, random_state=42)
        
        cv_scores = {
            'accuracy': [],
            'precision': [],
            'recall': [],
            'f1': []
        }
        
        fold = 1
        for train_idx, val_idx in skf.split(X, y_adj):
            print(f"  Fold {fold}/{cv_folds}...")
            
            X_train, X_val = X[train_idx], X[val_idx]
            y_train, y_val = y_adj[train_idx], y_adj[val_idx]
            
            # Train temporary model
            temp_model = lgb.LGBMClassifier(
                n_estimators=100,
                max_depth=10,
                random_state=42,
                verbose=-1
            )
            temp_model.fit(X_train, y_train)
            
            # Evaluate
            preds = temp_model.predict(X_val)
            cv_scores['accuracy'].append(float(accuracy_score(y_val, preds)))
            precision, recall, f1, _ = precision_recall_fscore_support(
                y_val, preds, average='weighted', zero_division=0
            )
            cv_scores['precision'].append(float(precision))
            cv_scores['recall'].append(float(recall))
            cv_scores['f1'].append(float(f1))
            
            fold += 1
        
        # Print CV results
        print(f"\nCross-Validation Results ({cv_folds}-fold):")
        for metric, scores in cv_scores.items():
            mean_score = float(np.mean(scores))
            std_score = float(np.std(scores))
            print(f"  {metric.capitalize()}: {mean_score:.4f} ± {std_score:.4f}")
        
        return cv_scores

    def predict(self, pdf_path: str) -> List[Dict]:
        """ENHANCED: Predict heading levels with rule-based fallback"""
        return self.enhanced_predict(pdf_path)

    def enhanced_predict(self, pdf_path: str) -> List[Dict]:
        """ENHANCED: Predict heading levels with rule-based fallback and minimum heading guarantee"""

        lines = self.extract_lines(pdf_path)
        if not lines:
            return []

        self.feature_extractor.compute_document_stats(lines)

        # ML Prediction
        X = []
        for i, line in enumerate(lines):
            prev_line = lines[i-1] if i > 0 else None
            next_line = lines[i+1] if i < len(lines) - 1 else None
            features = self.feature_extractor.extract_features(line, prev_line, next_line)
            X.append(features)

        X = np.array(X)
        preds = self.model.predict(X)
        probs = self.model.predict_proba(X)

        headings = []
        
        # RULE-BASED ENHANCEMENT: Ensure all numbered headings are detected
        for i, (line, pred, prob) in enumerate(zip(lines, preds, probs)):
            confidence = float(prob[pred])
            
            # RULE 1: If has numbered pattern but model missed it -> FORCE as heading
            if (self.feature_extractor.is_likely_numbered_heading(line.text) and 
                pred == 0 and confidence < 0.8):
                
                # Determine level based on dot count
                dot_count = line.text.strip().split(' ')[0].count('.')
                forced_level = min(4, max(1, dot_count))
                
                headings.append({
                    'text': line.text,
                    'level': forced_level,
                    'page': line.page,
                    'probability': 0.95,  # High confidence for rule-based
                    'font_size': line.font_size,
                    'detection_method': 'rule_based'
                })
                continue
                
            # RULE 2: ML prediction with lower confidence threshold
            if pred > 0 and confidence > 0.3:  # Lower threshold to catch more headings
                headings.append({
                    'text': line.text,
                    'level': int(pred),
                    'page': line.page,
                    'probability': confidence,
                    'font_size': line.font_size,
                    'detection_method': 'ml'
                })

        # RULE 3: Ensure minimum headings per document
        headings = self._ensure_minimum_headings(lines, headings)
        
        # Remove duplicates
        unique_headings = []
        seen_texts = set()
        for heading in headings:
            if heading['text'] not in seen_texts:
                unique_headings.append(heading)
                seen_texts.add(heading['text'])
        
        return unique_headings

    def _ensure_minimum_headings(self, lines: List[TextLine], headings: List[Dict]) -> List[Dict]:
        """ENHANCED: Ensure each document has at least 6 headings"""
        if len(headings) >= 6:  # Already has sufficient headings
            return headings
            
        # Find potential headings that were missed
        potential_headings = []
        
        # for i, line in enumerate(lines):
        #     # Skip if already detected
        #     if any(h['text'] == line.text for h in headings):
        #         continue
                
        #     # Characteristics of actual headings
        #     is_likely_heading = (
        #         self.feature_extractor.is_likely_numbered_heading(line.text) or
        #         (line.font_size > self.feature_extractor.doc_stats['median_font'] * 1.1 and 
        #          len(line.text.split()) <= 15 and  # Headings are usually short
        #          any(c.isupper() for c in line.text) and  # Has uppercase letters
        #          not line.text.endswith('.') and  # Doesn't end with period
        #          not line.text[-1].isdigit())  # Doesn't end with digit
        #     )
            
        #     if is_likely_heading:
        #         dot_count = line.text.strip().split(' ')[0].count('.')
        #         level = min(4, max(1, dot_count + 1))
                
        #         potential_headings.append({
        #             'text': line.text,
        #             'level': level,
        #             'page': line.page,
        #             'probability': 0.7,
        #             'font_size': line.font_size,
        #             'detection_method': 'fallback'
        #         })
        
        # Add potential headings if current count is too low
        if len(headings) < 6 and potential_headings:
            needed = min(6 - len(headings), len(potential_headings))
            headings.extend(potential_headings[:needed])
        
        return headings

    def save_all_models(self, metrics: Dict[str, Any] = None, training_info: Dict[str, Any] = None):
        """Save all model versions with metadata"""
        # Save main model
        main_model_path = self.model_manager.save_model_version(
            self, "main", metrics, training_info
        )
        
        # Also save a simplified version for quick loading
        simple_model_path = self.model_manager.save_model_version(
            self, "simple", metrics, training_info
        )
        
        print(f"✓ All model versions saved:")
        print(f"  - Main model: {main_model_path}")
        print(f"  - Simple model: {simple_model_path}")
        
        # Clean up old models (keep only 5 most recent)
        self.model_manager.cleanup_old_models(keep_count=5)
        
        return main_model_path

    def load_latest_model(self):
        """Load the most recent model"""
        model_data = self.model_manager.load_latest_model()
        if model_data is None:
            print("✗ No trained model found")
            return False
            
        try:
            detector_data = model_data['detector_data']
            self.model = detector_data['model']
            self.feature_names = detector_data['feature_names']
            self.feature_extractor = detector_data['feature_extractor']
            print(f"✓ Loaded model: {model_data['metadata']['version']}")
            return True
        except Exception as e:
            print(f"✗ Error loading model: {e}")
            return False


# ============================================================
# ENHANCED TRAINING PIPELINE - LIGHTGBM VERSION
# ============================================================

def train_and_evaluate(
    input_dir: str = r'input',
    gt_dir: str = r'output',
    output_dir: str = 'working/ml_heading_model_lgb',
    train_ratio: float = 0.75,  # Reduced to have more validation data
    val_ratio: float = 0.15,   # Added validation split
    use_cached_data: bool = True,
    enable_cross_validation: bool = True,
    enable_data_validation: bool = True,
    optimize_thresholds: bool = True  # New parameter for threshold optimization
):
    """Enhanced training pipeline with threshold optimization"""

    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    detector = MLHeadingDetector()
    
    # Check cache first
    cache_key = detector.data_manager.get_cache_key(input_dir, gt_dir)
    X_all, y_all, metadata = None, None, {}
    
    if use_cached_data:
        X_all, y_all, metadata = detector.data_manager.load_training_data(cache_key)
    
    # If no cached data or not using cache, generate new data
    if X_all is None or y_all is None:
        print("Generating new training data...")
        
        # Load dataset with proper path handling
        input_path = Path(input_dir)
        gt_path = Path(gt_dir)

        pdf_files = sorted(input_path.glob('*.pdf'))
        print(f"Found {len(pdf_files)} PDF files")

        # Generate training data with error handling
        print("\nGenerating training data...")
        X_all_parts = []
        y_all_parts = []
        all_lines = []
        processed_count = 0

        for i, pdf_file in enumerate(pdf_files):
            doc_id = pdf_file.stem
            
            # Look for markdown file
            possible_md_locations = [
                gt_path / f"{doc_id}.md",
                gt_path / doc_id / "main.md", 
                gt_path / doc_id / f"{doc_id}.md",
                gt_path / f"{doc_id}" / "main.md"
            ]
            
            gt_md_path = None
            for location in possible_md_locations:
                if location.exists():
                    gt_md_path = location
                    break
            
            if gt_md_path is None:
                print(f"  Skipping {doc_id}: No markdown file found")
                continue

            try:
                X_batch, y_batch, lines_batch = detector.generate_training_data(str(pdf_file), str(gt_md_path))
                
                if len(X_batch) > 0:
                    X_all_parts.append(X_batch)
                    y_all_parts.append(y_batch)
                    all_lines.extend(lines_batch)
                    processed_count += 1
                    print(f"  ✓ Processed {doc_id}: {len(X_batch)} samples")
                else:
                    print(f"  ⚠ No samples from {doc_id}")
                    
            except Exception as e:
                print(f"  ✗ Error with {doc_id}: {e}")
                continue

            if (i + 1) % 10 == 0:
                print(f"  Progress: {i+1}/{len(pdf_files)} files")

        # Check if we have any data
        if not X_all_parts:
            print("\n❌ ERROR: No training data generated!")
            return None, None

        # Combine all data
        try:
            X_all = np.vstack(X_all_parts)
            y_all = np.hstack(y_all_parts)
            
            # Save to cache for future use
            metadata = {
                'source_files': len(pdf_files),
                'processed_files': processed_count,
                'generated_at': datetime.now().isoformat()
            }
            detector.data_manager.save_training_data(cache_key, X_all, y_all, metadata)
            print(f"✓ Training data cached with key: {cache_key}")
            
        except ValueError as e:
            print(f"\n❌ ERROR combining data: {e}")
            return None, None

        print(f"\n✅ Successfully processed {processed_count}/{len(pdf_files)} files")
        print(f"Total samples: {len(X_all)}")
    else:
        print("✓ Using cached training data")
        all_lines = []  # Lines not available from cache

    # Show class distribution - FOCUS ON HEADINGS
    unique, counts = np.unique(y_all, return_counts=True)
    print("\nFinal Class Distribution:")
    total_samples = len(y_all)
    for level, count in zip(unique, counts):
        if level == 0:
            print(f"  Level {level} (Not heading): {count} samples ({count/total_samples*100:.2f}%)")
        else:
            print(f"  Level {level}: {count} samples ({count/total_samples*100:.2f}%)")
    
    heading_samples = np.sum(y_all > 0)
    print(f"Total heading samples: {heading_samples}/{total_samples} ({heading_samples/total_samples*100:.2f}%)")

    # Data Validation and Quality Check - FOCUS ON HEADINGS
    if enable_data_validation and len(X_all) > 0:
        print("\n" + "="*70)
        print("DATA QUALITY VALIDATION - HEADING FOCUS")
        print("="*70)
        
        validation_report = detector.data_validator.validate_data_quality(
            X_all, y_all, detector.feature_names
        )
        
        print(f"Overall Quality Score: {validation_report['overall_quality_score']:.2f}/1.00")
        print("\nQuality Flags (Heading Focus):")
        for flag, value in validation_report['quality_flags'].items():
            status = "✓" if value else "✗"
            print(f"  {status} {flag}: {value}")
        
        # Quick validation to ensure data is trainable - FOCUS ON HEADINGS
        is_data_ready = detector.data_validator.validate_data_before_training(X_all, y_all, detector.feature_names)
        if not is_data_ready:
            print("\n❌ Data validation failed - cannot proceed with training")
            return None, None
        
        # Save validation report
        with open(output_path / 'data_validation_report.json', 'w', encoding='utf-8') as f:
            json.dump(validation_report, f, indent=2, ensure_ascii=False)

    # Split train/val/test with indices
    indices = np.arange(len(X_all))
    
    # First split: train + temp vs test
    X_train_val, X_test, y_train_val, y_test, indices_train_val, indices_test = train_test_split(
        X_all, y_all, indices, test_size=1-train_ratio-val_ratio, random_state=42, stratify=y_all
    )
    
    # Second split: train vs val
    X_train, X_val, y_train, y_val, indices_train, indices_val = train_test_split(
        X_train_val, y_train_val, indices_train_val, test_size=val_ratio/(train_ratio+val_ratio), 
        random_state=42, stratify=y_train_val
    )

    print(f"\nDataset split:")
    print(f"  Training:   {len(X_train)} samples")
    print(f"  Validation: {len(X_val)} samples (for threshold optimization)")
    print(f"  Testing:    {len(X_test)} samples")

    # Cross-Validation for small datasets
    cv_results = {}
    if enable_cross_validation and len(X_train) > 0:
        cv_results = detector.cross_validate(X_train, y_train, cv_folds=min(5, len(X_train)//10))
        
        # Save CV results
        with open(output_path / 'cross_validation_results.json', 'w', encoding='utf-8') as f:
            json.dump(cv_results, f, indent=2, ensure_ascii=False)

    # Train model with validation set for threshold optimization
    print("\n" + "="*70)
    print("TRAINING LIGHTGBM WITH THRESHOLD OPTIMIZATION")
    print("="*70)

    if optimize_thresholds:
        y_train_adj = detector.train(X_train, y_train, X_val, y_val)
    else:
        y_train_adj = detector.train(X_train, y_train)

    # Evaluate
    print("\n" + "="*70)
    print("EVALUATION ON TEST SET - HEADING FOCUS")
    print("="*70)

    # Standard evaluation - FOCUS ON HEADINGS
    metrics = detector.evaluate(X_test, y_test)
    
    # ENHANCED: Heading-specific evaluation
    if len(X_test) > 0 and all_lines:  # Only if we have lines data
        # Get test lines for enhanced evaluation using precomputed indices_test
        test_lines = [all_lines[i] for i in indices_test]
        
        if test_lines:
            heading_metrics = detector.evaluate_heading_detection(X_test, y_test, test_lines)
            metrics['heading_detection'] = heading_metrics

    # POST-TRAINING CROSS-VERIFICATION (only after model is trained)
    if enable_data_validation and len(X_test) > 0 and all_lines:
        print("\n" + "="*70)
        print("POST-TRAINING CROSS-VERIFICATION - HEADING FOCUS")
        print("="*70)
        
        # Use the precomputed indices_test to get test lines
        test_lines = [all_lines[i] for i in indices_test]
        
        if test_lines:
            verification_results = detector.data_validator.cross_verify_predictions(
                detector, X_test, y_test, test_lines
            )
            
            print(f"High confidence heading samples: {len(verification_results.get('high_confidence_samples', []))}")
            print(f"Low confidence heading samples: {len(verification_results.get('low_confidence_samples', []))}")
            print(f"Potential heading misclassifications: {len(verification_results.get('potential_misclassifications', []))}")
            
            # Save verification results
            with open(output_path / 'cross_verification_report.json', 'w', encoding='utf-8') as f:
                json.dump(verification_results, f, indent=2, ensure_ascii=False)
        else:
            print("  ⚠ No test lines available for cross-verification")

    # Save all model versions and training info
    training_info = {
        'training_date': datetime.now().isoformat(),
        'dataset_info': {
            'total_samples': len(X_all),
            'training_samples': len(X_train),
            'validation_samples': len(X_val),
            'test_samples': len(X_test),
            'class_distribution': {str(k): int(v) for k, v in zip(unique, counts)},
            'optimal_thresholds': detector.optimal_thresholds
        },
        'model_metrics': metrics,
        'cross_validation_results': cv_results,
        'cache_key': cache_key,
        'data_validation': {
            'overall_quality_score': validation_report.get('overall_quality_score', 0) if enable_data_validation else 'not_performed'
        }
    }
    
    # Save all model versions
    main_model_path = detector.save_all_models(metrics, training_info)

    # Save training info separately
    with open(output_path / 'training_info.json', 'w', encoding='utf-8') as f:
        json.dump(training_info, f, indent=2, ensure_ascii=False)

    # Save metrics as CSV - FOCUS ON HEADING METRICS
    metrics_df = pd.DataFrame([{
        'overall_accuracy': metrics['overall_accuracy'],
        'heading_accuracy': metrics['heading_accuracy'],
        'heading_precision': metrics['heading_precision'],
        'heading_recall': metrics['heading_recall'],
        'heading_f1': metrics['heading_f1']
    }])
    metrics_df.to_csv(output_path / 'metrics_lgb.csv', index=False)

    # Print optimal thresholds
    print(f"\nOptimal Thresholds for Heading Classes:")
    for level, threshold in detector.optimal_thresholds.items():
        print(f"  Level {level}: {threshold:.3f}")

    print("\n✅ Enhanced Training with Threshold Optimization complete!")

    return detector, metrics


if __name__ == "__main__":
    try:
        # Enhanced training with threshold optimization
        detector, metrics = train_and_evaluate(
            use_cached_data=True,
            enable_cross_validation=True,
            enable_data_validation=True,
            optimize_thresholds=True  # Enable threshold optimization
        )
        if detector is None:
            print("\nTraining failed - no data processed")
    except Exception as e:
        print(f"❌ Training failed: {e}")
        import traceback
        traceback.print_exc()