import pandas as pd
import numpy as np
from typing import List, Dict, Tuple
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, f1_score
import warnings
warnings.filterwarnings('ignore')
from lightgbm import LGBMClassifier

# ============================================================================
# PART 1: DATA LOADING (CORRECTED)
# ============================================================================

def load_ground_truth(gt_csv: str) -> pd.DataFrame:
    """
    Load ground truth (only num_correct and answers)
    
    Format:
        num_correct,answers
        1,A
        1,C
        2,AB
    """
    df = pd.read_csv(gt_csv)
    
    # Validate columns
    if 'num_correct' not in df.columns or 'answers' not in df.columns:
        raise ValueError("Ground truth must have 'num_correct' and 'answers' columns")
    
    # Add question_id if not present
    if 'question_id' not in df.columns:
        df.insert(0, 'question_id', range(len(df)))
    
    print(f"✓ Loaded ground truth: {len(df)} questions")
    return df


def load_model_predictions(csv_path: str, model_name: str, n_questions: int) -> pd.DataFrame:
    """
    Load model predictions with probabilities
    
    Format:
        question_id,num_correct,answers,prob_A,prob_B,prob_C,prob_D
        0,1,B,0.0190,0.0370,0.0325,0.0294
    """
    try:
        df = pd.read_csv(csv_path)
        
        # Validate required columns
        required = ['prob_A', 'prob_B', 'prob_C', 'prob_D']
        if not all(col in df.columns for col in required):
            print(f"  [WARN] {model_name}: Missing probability columns, using uniform")
            return create_uniform_predictions(n_questions, model_name)
        
        # Ensure question_id exists
        if 'question_id' not in df.columns:
            df.insert(0, 'question_id', range(len(df)))
        
        # Validate size
        if len(df) != n_questions:
            print(f"  [WARN] {model_name}: Size mismatch ({len(df)} vs {n_questions})")
            if len(df) < n_questions:
                # Pad with uniform
                missing = n_questions - len(df)
                uniform_df = create_uniform_predictions(missing, model_name)
                uniform_df['question_id'] = range(len(df), n_questions)
                df = pd.concat([df, uniform_df], ignore_index=True)
            else:
                df = df.iloc[:n_questions]
        
        print(f"  ✓ {model_name}: Loaded {len(df)} predictions")
        return df
        
    except FileNotFoundError:
        print(f"  [ERROR] {model_name}: File not found, using uniform fallback")
        return create_uniform_predictions(n_questions, model_name)
    except Exception as e:
        print(f"  [ERROR] {model_name}: {str(e)}, using uniform fallback")
        return create_uniform_predictions(n_questions, model_name)


def create_uniform_predictions(n_questions: int, model_name: str) -> pd.DataFrame:
    """Create uniform probability predictions (fallback for crashed models)"""
    print(f"  [INFO] Creating uniform predictions for {model_name}")
    return pd.DataFrame({
        'question_id': range(n_questions),
        'num_correct': [1] * n_questions,
        'answers': ['A'] * n_questions,
        'prob_A': [0.25] * n_questions,
        'prob_B': [0.25] * n_questions,
        'prob_C': [0.25] * n_questions,
        'prob_D': [0.25] * n_questions,
    })


def load_all_models(csv_files: List[Dict[str, str]], n_questions: int) -> List[pd.DataFrame]:
    """
    Load all model predictions with robust error handling
    
    Args:
        csv_files: [{'name': 'model1', 'path': 'model1.csv'}, ...]
        n_questions: Expected number of questions
    """
    print(f"\n{'='*80}")
    print(f"LOADING {len(csv_files)} MODEL PREDICTIONS")
    print(f"{'='*80}")
    
    dfs = []
    for cfg in csv_files:
        df = load_model_predictions(cfg['path'], cfg['name'], n_questions)
        dfs.append(df)
    
    print(f"✓ Loaded {len(dfs)} models\n")
    return dfs

from sklearn.linear_model import LogisticRegression

# ============================================================================
# PART 2: META-MODEL (CORRECTED)
# ============================================================================
from sklearn.neural_network import MLPClassifier

class HalvesOptimizedMetaEnsemble:
    """
    Two-stage meta-ensemble for halves scoring
    
    Training:
    - Features: Model probabilities (prob_A, prob_B, prob_C, prob_D from each model)
    - Labels: Ground truth (num_correct, answers)
    
    Inference:
    - Stage 1: Predict num_correct
    - Stage 2: Predict which options are correct
    - Stage 3: Select answers with halves-aware strategy
    """
    
    def __init__(self):
        # Stage 1: Predict num_correct (1, 2, or 3)


        # Stage 1: Dự đoán số câu đúng
        self.num_correct_model = MLPClassifier(
            hidden_layer_sizes=(8, 4),
            activation='relu',
            alpha=1e-3,
            learning_rate_init=1e-3,
            max_iter=2000,
            early_stopping=True,
            n_iter_no_change=20,
            random_state=42
        )

        # Stage 2: Bộ phân loại nhị phân cho từng lựa chọn
        self.option_models = {
            'A': MLPClassifier(hidden_layer_sizes=(8, 4), activation='relu', alpha=1e-3,
                            learning_rate_init=1e-3, max_iter=2000, early_stopping=True,
                            n_iter_no_change=20, random_state=42),
            'B': MLPClassifier(hidden_layer_sizes=(8, 4), activation='relu', alpha=1e-3,
                            learning_rate_init=1e-3, max_iter=2000, early_stopping=True,
                            n_iter_no_change=20, random_state=42),
            'C': MLPClassifier(hidden_layer_sizes=(8, 4), activation='relu', alpha=1e-3,
                            learning_rate_init=1e-3, max_iter=2000, early_stopping=True,
                            n_iter_no_change=20, random_state=42),
            'D': MLPClassifier(hidden_layer_sizes=(8, 4), activation='relu', alpha=1e-3,
                            learning_rate_init=1e-3, max_iter=2000, early_stopping=True,
                            n_iter_no_change=20, random_state=42)
        }

        
        self.scaler_num = StandardScaler()
        self.scaler_opt = StandardScaler()
        self.trained = False
    
    def extract_num_correct_features(self, dfs: List[pd.DataFrame], idx: int) -> np.ndarray:
        """
        Extract features for predicting num_correct
        
        Uses ONLY model probabilities (no ground truth info)
        """
        features = []
        n_models = len(dfs)
        
        # Collect all probabilities from all models
        all_probs = []
        for df in dfs:
            row = df.iloc[idx]
            probs = [row['prob_A'], row['prob_B'], row['prob_C'], row['prob_D']]
            all_probs.append(probs)
        
        all_probs = np.array(all_probs)  # Shape: (n_models, 4)
        
        # Feature 1: Raw probabilities from each model (flattened)
        features.extend(all_probs.flatten())
        
        # Feature 2: Per-model statistics
        max_per_model = all_probs.max(axis=1)
        features.extend([
            max_per_model.mean(),
            max_per_model.std(),
            max_per_model.max(),
            max_per_model.min()
        ])
        
        # Feature 3: Confidence gap (top-1 vs top-2) per model
        gaps = []
        for probs in all_probs:
            sorted_probs = np.sort(probs)[::-1]
            gap = sorted_probs[0] - sorted_probs[1] if len(sorted_probs) > 1 else sorted_probs[0]
            gaps.append(gap)
        
        features.extend([
            np.mean(gaps),
            np.std(gaps),
            np.max(gaps),
            np.min(gaps)
        ])
        
        # Feature 4: High-confidence counts
        for threshold in [0.4, 0.5, 0.6, 0.7]:
            high_conf = (all_probs > threshold).sum()
            features.append(high_conf / (n_models * 4))
        
        # Feature 5: Per-option aggregated stats (cross-model)
        for opt_idx in range(4):
            opt_probs = all_probs[:, opt_idx]
            features.extend([
                opt_probs.mean(),
                opt_probs.std(),
                opt_probs.max(),
                opt_probs.min(),
                (opt_probs > 0.5).sum() / n_models
            ])
        
        # Feature 6: Distribution statistics
        avg_probs = all_probs.mean(axis=0)
        avg_probs_norm = avg_probs / (avg_probs.sum() + 1e-10)
        entropy = -np.sum(avg_probs_norm * np.log(avg_probs_norm + 1e-10))
        features.append(entropy)
        
        # Feature 7: Model agreement
        if n_models > 1:
            corrs = []
            for i in range(n_models):
                for j in range(i+1, n_models):
                    corr = np.corrcoef(all_probs[i], all_probs[j])[0, 1]
                    corrs.append(corr if not np.isnan(corr) else 0.0)
            features.extend([
                np.mean(corrs),
                np.std(corrs)
            ])
        else:
            features.extend([0.0, 0.0])
        
        return np.array(features)
    
    def extract_option_features(self, dfs: List[pd.DataFrame], idx: int, option: str) -> np.ndarray:
        """
        Extract features for predicting if specific option is correct
        
        Uses ONLY model probabilities
        """
        features = []
        n_models = len(dfs)
        
        # Raw probabilities for this option from all models
        opt_probs = [df.iloc[idx][f'prob_{option}'] for df in dfs]
        features.extend(opt_probs)
        
        # Statistics
        features.extend([
            np.mean(opt_probs),
            np.std(opt_probs),
            np.max(opt_probs),
            np.min(opt_probs),
            np.median(opt_probs)
        ])
        
        # Agreement
        for threshold in [0.4, 0.5, 0.6]:
            features.append(sum([1 for p in opt_probs if p > threshold]) / n_models)
        
        # Relative ranking
        rankings = []
        for df in dfs:
            row = df.iloc[idx]
            probs = [row['prob_A'], row['prob_B'], row['prob_C'], row['prob_D']]
            rank = sorted(range(4), key=lambda i: probs[i], reverse=True).index(ord(option) - ord('A'))
            rankings.append(rank)
        
        features.extend([
            np.mean(rankings),
            np.std(rankings),
            (np.array(rankings) == 0).sum() / n_models,  # Top-1 rate
            (np.array(rankings) <= 1).sum() / n_models   # Top-2 rate
        ])
        
        # Comparative features (vs other options)
        all_probs = []
        for df in dfs:
            row = df.iloc[idx]
            all_probs.append([row['prob_A'], row['prob_B'], row['prob_C'], row['prob_D']])
        
        all_probs = np.array(all_probs)
        opt_idx = ord(option) - ord('A')
        
        # Gaps to other options
        gaps_to_others = []
        for other_idx in range(4):
            if other_idx != opt_idx:
                gap = (all_probs[:, opt_idx] - all_probs[:, other_idx]).mean()
                gaps_to_others.append(gap)
        
        features.extend([
            np.mean(gaps_to_others),
            np.max(gaps_to_others),
            np.min(gaps_to_others)
        ])
        
        return np.array(features)
    
    def train(self, dfs_train: List[pd.DataFrame], gt_df: pd.DataFrame):
        """
        Train meta-model
        
        Args:
            dfs_train: Model predictions (with probabilities)
            gt_df: Ground truth (only num_correct and answers)
        """
        print(f"\n{'='*80}")
        print("TRAINING HALVES-OPTIMIZED META-ENSEMBLE")
        print(f"{'='*80}")
        
        n_questions = len(gt_df)
        
        # Validate alignment
        if len(dfs_train[0]) != n_questions:
            raise ValueError(f"Size mismatch: models={len(dfs_train[0])}, gt={n_questions}")
        
        # ===== STAGE 1: Train num_correct predictor =====
        print("\n[Stage 1] Training num_correct predictor...")
        
        X_num = []
        y_num = []
        
        for i in range(n_questions):
            features = self.extract_num_correct_features(dfs_train, i)
            X_num.append(features)
            
            # Label from ground truth
            y_num.append(int(gt_df.iloc[i]['num_correct']))
        
        X_num = np.array(X_num)
        y_num = np.array(y_num)
        
        # Normalize
        X_num = self.scaler_num.fit_transform(X_num)
        
        # Train
        self.num_correct_model.fit(X_num, y_num)
        
        # Evaluate
        y_num_pred = self.num_correct_model.predict(X_num)
        acc = accuracy_score(y_num, y_num_pred)
        print(f"  ✓ num_correct train accuracy: {acc:.4f}")
        
        # Distribution
        unique, counts = np.unique(y_num, return_counts=True)
        print(f"  True distribution: {dict(zip(unique, counts))}")
        unique_pred, counts_pred = np.unique(y_num_pred, return_counts=True)
        print(f"  Pred distribution: {dict(zip(unique_pred, counts_pred))}")
        
        # ===== STAGE 2: Train per-option models =====
        print("\n[Stage 2] Training per-option models...")
        
        for option in ['A', 'B', 'C', 'D']:
            X_opt = []
            y_opt = []
            
            for i in range(n_questions):
                features = self.extract_option_features(dfs_train, i, option)
                X_opt.append(features)
                
                # Label: 1 if option is in ground truth answers, 0 otherwise
                gt_answers = str(gt_df.iloc[i]['answers']).upper()
                y_opt.append(1 if option in gt_answers else 0)
            
            X_opt = np.array(X_opt)
            y_opt = np.array(y_opt)
            
            # Normalize
            X_opt = self.scaler_opt.fit_transform(X_opt)
            
            # Train
            self.option_models[option].fit(X_opt, y_opt)
            
            # Evaluate
            y_opt_pred = self.option_models[option].predict(X_opt)
            acc = accuracy_score(y_opt, y_opt_pred)
            f1 = f1_score(y_opt, y_opt_pred, zero_division=0)
            pos_rate = y_opt.mean()
            
            print(f"  ✓ Option {option}: acc={acc:.4f}, f1={f1:.4f}, pos_rate={pos_rate:.3f}")
        
        self.trained = True
        print(f"\n✓ Meta-model training complete\n")
    
    def predict_with_halves_optimization(self, dfs_test: List[pd.DataFrame], 
                                        conservative_factor: float = 0.15) -> pd.DataFrame:
        """
        Predict with halves-aware strategy
        """
        if not self.trained:
            raise RuntimeError("Model not trained. Call train() first.")
        
        n_questions = len(dfs_test[0])
        results = []
        
        for i in range(n_questions):
            # Stage 1: Predict num_correct
            features_num = self.extract_num_correct_features(dfs_test, i)
            features_num = self.scaler_num.transform([features_num])
            
            predicted_num = self.num_correct_model.predict(features_num)[0]
            num_correct_probs = self.num_correct_model.predict_proba(features_num)[0]
            
            # Stage 2: Get option probabilities
            option_probs = {}
            for option in ['A', 'B', 'C', 'D']:
                features_opt = self.extract_option_features(dfs_test, i, option)
                features_opt = self.scaler_opt.transform([features_opt])
                prob = self.option_models[option].predict_proba(features_opt)[0][1]
                option_probs[option] = float(prob)
            
            # Stage 3: Halves-optimized selection
            sorted_options = sorted(option_probs.items(), key=lambda x: x[1], reverse=True)
            
            # Strategy: Evaluate expected halves score for k=1,2,3
            best_selection = []
            best_score = -1
            
            for k in range(1, 4):  # Try 1, 2, or 3 options
                selected = [opt for opt, _ in sorted_options[:k]]
                selected_probs = [option_probs[opt] for opt in selected]
                
                # Expected metrics
                expected_correct = sum(selected_probs)
                expected_wrong = k - expected_correct
                
                # Penalty for mismatch with predicted_num
                num_penalty = abs(k - predicted_num) * 0.3
                
                # Expected halves score
                expected_error = num_penalty + expected_wrong
                
                if expected_error < 0.7:
                    score = 1.0 - conservative_factor * (k - 1)
                elif expected_error < 1.5:
                    score = 0.5 - conservative_factor * (k - 1)
                else:
                    score = 0.0 - conservative_factor * k
                
                if score > best_score:
                    best_score = score
                    best_selection = selected
            
            # Fallback
            if not best_selection:
                best_selection = [sorted_options[0][0]]
            
            # Cap at 3 answers
            if len(best_selection) > 3:
                best_selection = best_selection[:3]
            
            results.append({
                'question_id': i,
                'num_correct': len(best_selection),
                'answers': ''.join(sorted(best_selection)),
                'prob_A': option_probs['A'],
                'prob_B': option_probs['B'],
                'prob_C': option_probs['C'],
                'prob_D': option_probs['D']
            })
        
        return pd.DataFrame(results)


# ============================================================================
# COMPLETE PIPELINE WITH EVALUATION
# ============================================================================

def run_meta_ensemble_with_evaluation(
    csv_files: List[Dict[str, str]],
    gt_csv: str,
    output_csv: str,
    conservative_factor: float = 0.15
):
    """
    Complete pipeline: Train → Predict → Evaluate
    """
    print(f"\n{'='*80}")
    print("META-ENSEMBLE PIPELINE WITH EVALUATION")
    print(f"{'='*80}")
    
    # Load ground truth
    gt_df = load_ground_truth(gt_csv)
    n_questions = len(gt_df)
    
    # Load model predictions
    dfs = load_all_models(csv_files, n_questions)
    
    # Train meta-ensemble
    ensemble = HalvesOptimizedMetaEnsemble()
    ensemble.train(dfs, gt_df)
    
    # Predict
    result_df = ensemble.predict_with_halves_optimization(
        dfs, 
        conservative_factor=conservative_factor
    )
    
    # Save
    result_df.to_csv(output_csv, index=False)
    print(f"✓ Saved predictions to: {output_csv}\n")
    
    # Evaluate
    per_q_df, by_k_df, summary, n = evaluate_halves_optimized(gt_csv, output_csv)
    print_evaluation_report(summary, by_k_df)
    
    # Save evaluation results
    per_q_df.to_csv(output_csv.replace('.csv', '_per_question.csv'), index=False)
    wrong_df = per_q_df[per_q_df['halves_score'] < 1.0]
    wrong_df.to_csv(output_csv.replace('.csv', '_wrong.csv'), index=False)
    
    return ensemble, result_df, summary


def tune_conservative_factor(
    ensemble: HalvesOptimizedMetaEnsemble,
    dfs: List[pd.DataFrame],
    gt_csv: str,
    output_dir: str = '.'
):
    """
    Grid search for best conservative_factor
    """
    print(f"\n{'='*80}")
    print("TUNING CONSERVATIVE FACTOR")
    print(f"{'='*80}")
    
    results = []
    
    for cf in [0.0,0.3,0.6,0.9]:
        # Predict with this factor
        pred_df = ensemble.predict_with_halves_optimization(dfs, conservative_factor=cf)
        pred_path = f'{output_dir}/pred_cf_{cf:.2f}.csv'
        pred_df.to_csv(pred_path, index=False)
        
        # Evaluate
        _, _, summary, _ = evaluate_halves_optimized(gt_csv, pred_path)
        
        results.append({
            'conservative_factor': cf,
            'halves_score': summary['official_halves_mean'],
            'exact_match': summary['exact_match_accuracy'],
            'one_error': summary['one_error_rate'],
            'two_plus_error': summary['two_plus_error_rate']
        })
        
        print(f"CF={cf:.2f}: Halves={summary['official_halves_mean']:.4f}, "
              f"Exact={summary['exact_match_accuracy']:.4f}, "
              f"e≥2={summary['two_plus_error_rate']:.4f}")
    
    # Find best
    results_df = pd.DataFrame(results)
    best_idx = results_df['halves_score'].idxmax()
    best_cf = results_df.iloc[best_idx]['conservative_factor']
    best_score = results_df.iloc[best_idx]['halves_score']
    
    print(f"\n✓ Best conservative_factor: {best_cf:.2f} (score: {best_score:.4f})")
    
    # Save tuning results
    results_df.to_csv(f'{output_dir}/tuning_results.csv', index=False)
    
    return best_cf, results_df


import pandas as pd
import numpy as np
import pickle
from typing import List, Dict , Optional
from pathlib import Path


# ============================================================================
# PART 1: SAVE/LOAD TRAINED MODEL
# ============================================================================

def save_trained_ensemble(ensemble, save_path: str):
    """
    Save trained meta-ensemble to disk
    
    Args:
        ensemble: Trained HalvesOptimizedMetaEnsemble or AdvancedHalvesMetaEnsemble
        save_path: Path to save (e.g., 'trained_models/ensemble.pkl')
    """
    if not ensemble.trained:
        raise RuntimeError("Cannot save untrained model")
    
    # Create directory if not exists
    Path(save_path).parent.mkdir(parents=True, exist_ok=True)
    
    # Save entire object
    with open(save_path, 'wb') as f:
        pickle.dump(ensemble, f, protocol=pickle.HIGHEST_PROTOCOL)
    
    print(f"✓ Saved trained ensemble to: {save_path}")
    print(f"  Model type: {type(ensemble).__name__}")
    print(f"  File size: {Path(save_path).stat().st_size / 1024:.2f} KB")


def load_trained_ensemble(load_path: str):
    """
    Load trained meta-ensemble from disk
    
    Args:
        load_path: Path to saved model
    
    Returns:
        Trained ensemble object
    """
    if not Path(load_path).exists():
        raise FileNotFoundError(f"Model file not found: {load_path}")
    
    with open(load_path, 'rb') as f:
        ensemble = pickle.load(f)
    
    if not ensemble.trained:
        raise RuntimeError("Loaded model is not trained")
    
    print(f"✓ Loaded trained ensemble from: {load_path}")
    print(f"  Model type: {type(ensemble).__name__}")
    
    return ensemble


# ============================================================================
# PART 2: INFERENCE ON TEST SET (NO GROUND TRUTH)
# ============================================================================

def inference_on_test_set(
    ensemble,
    test_csv_files: List[Dict[str, str]],
    output_csv: str,
    conservative_factor: float = 0.10,
    n_questions: Optional[int] = None
):
    """
    Inference on test set using trained ensemble
    
    Args:
        ensemble: Trained meta-ensemble (loaded or just trained)
        test_csv_files: [{'name': 'model1', 'path': 'test/model1.csv'}, ...]
        output_csv: Output predictions path
        conservative_factor: Conservative factor (from tuning)
        n_questions: Number of questions (auto-detect if None)
    
    Returns:
        DataFrame with predictions
    """
    print(f"\n{'='*80}")
    print("INFERENCE ON TEST SET")
    print(f"{'='*80}")
    
    # Auto-detect n_questions from first valid file
    if n_questions is None:
        for cfg in test_csv_files:
            try:
                df_temp = pd.read_csv(cfg['path'])
                n_questions = len(df_temp)
                print(f"Auto-detected {n_questions} questions from {cfg['name']}")
                break
            except:
                continue
        
        if n_questions is None:
            raise ValueError("Cannot auto-detect n_questions. Please provide manually.")
    
    # Load test predictions
    print(f"\nLoading {len(test_csv_files)} test model predictions...")
    test_dfs = load_all_models(test_csv_files, n_questions)
    
    # Predict
    print(f"\nRunning inference with CF={conservative_factor:.2f}...")
    
    # Choose prediction method based on ensemble type
    if hasattr(ensemble, 'predict_with_adaptive_strategy'):
        # AdvancedHalvesMetaEnsemble
        result_df = ensemble.predict_with_adaptive_strategy(
            test_dfs, 
            conservative_factor=conservative_factor
        )
    else:
        # HalvesOptimizedMetaEnsemble
        result_df = ensemble.predict_with_halves_optimization(
            test_dfs,
            conservative_factor=conservative_factor
        )
    
    # Save
    result_df.to_csv(output_csv, index=False)
    print(f"\n✓ Saved test predictions to: {output_csv}")
    print(f"  Total questions: {len(result_df)}")
    
    # Distribution analysis
    num_correct_dist = result_df['num_correct'].value_counts().sort_index()
    print(f"\nPredicted num_correct distribution:")
    for k, count in num_correct_dist.items():
        print(f"  k={k}: {count} questions ({count/len(result_df)*100:.1f}%)")
    
    return result_df


# ============================================================================
# PART 3: COMPLETE WORKFLOW
# ============================================================================

def train_and_save_workflow(
    train_csv_files: List[Dict[str, str]],
    gt_csv: str,
    model_save_path: str = 'trained_models/ensemble.pkl',
    tune_cf: bool = True
):
    """
    Complete training workflow:
    1. Train on validation set
    2. Tune conservative_factor
    3. Save trained model
    4. Return best CF
    """
    print(f"\n{'='*80}")
    print("TRAINING WORKFLOW")
    print(f"{'='*80}")
    
    # Load data
    gt_df = load_ground_truth(gt_csv)
    train_dfs = load_all_models(train_csv_files, len(gt_df))
    
    # Train
    print("\n[Step 1/3] Training meta-ensemble...")
    ensemble = HalvesOptimizedMetaEnsemble()  # or AdvancedHalvesMetaEnsemble()
    ensemble.train(train_dfs, gt_df)
    
    # Tune CF
    best_cf = 0.10  # Default
    if tune_cf:
        print("\n[Step 2/3] Tuning conservative_factor...")
        best_cf, _ = tune_conservative_factor(
            ensemble=ensemble,
            dfs=train_dfs,
            gt_csv=gt_csv,
            output_dir='tuning'
        )
    
    # Save
    print("\n[Step 3/3] Saving trained model...")
    save_trained_ensemble(ensemble, model_save_path)
    
    print(f"\n{'='*80}")
    print("TRAINING COMPLETE")
    print(f"{'='*80}")
    print(f"Model saved to: {model_save_path}")
    print(f"Best conservative_factor: {best_cf:.2f}")
    
    return ensemble, best_cf


def inference_workflow(
    model_path: str,
    test_csv_files: List[Dict[str, str]],
    output_csv: str,
    conservative_factor: float = 0.10
):
    """
    Complete inference workflow:
    1. Load trained model
    2. Run inference on test set
    3. Save predictions
    """
    print(f"\n{'='*80}")
    print("INFERENCE WORKFLOW")
    print(f"{'='*80}")
    
    # Load trained model
    print("[Step 1/2] Loading trained model...")
    ensemble = load_trained_ensemble(model_path)
    
    # Inference
    print("\n[Step 2/2] Running inference...")
    result_df = inference_on_test_set(
        ensemble=ensemble,
        test_csv_files=test_csv_files,
        output_csv=output_csv,
        conservative_factor=conservative_factor
    )
    
    print(f"\n{'='*80}")
    print("INFERENCE COMPLETE")
    print(f"{'='*80}")
    print(f"Predictions saved to: {output_csv}")
    
    return result_df


# ============================================================================
# MAIN USAGE - TWO SCENARIOS
# ============================================================================

if __name__ == "__main__":

    val_csv_files = [
        {'name': 'model1', 'path': 'val/model_Qwen3-4b_results_vn.csv'},
        {'name': 'model2', 'path': 'val/Qwen2.5-3B.csv'},
        {'name': 'model3', 'path': 'val/model_Qwen3-4b_results.csv'},
    ]
    
    # Train and save
    trained_ensemble, best_cf = train_and_save_workflow(
        train_csv_files=val_csv_files,
        gt_csv='ground_truth.csv',
        model_save_path='trained_models/meta_ensemble.pkl',
        tune_cf=True  # Tune conservative_factor
    )
    # ========================================================================
    # SCENARIO 2: INFERENCE PHASE (PRODUCTION)
    # ========================================================================
    
    print("\n" + "="*80)
    print("SCENARIO 2: INFERENCE PHASE")
    print("="*80)
    
# Test set predictions (KHÔNG có ground truth)
test_csv_files = [
    {'name': 'model1', 'path': 'test/model_Qwen3-4b_results_vn.csv'},
    {'name': 'model2', 'path': 'test/Qwen2.5-3B.csv'},
    {'name': 'model3', 'path': 'test/model_Qwen3-4b_results.csv'}
]

# Load trained model and inference
test_predictions = inference_workflow(
    model_path='trained_models/meta_ensemble.pkl',
    test_csv_files=test_csv_files,
    output_csv='test_predictions.csv',
    conservative_factor=best_cf  # Use best CF from training
)

print("\n✓ ALL DONE!")
print(f"\nFiles created:")
print(f"  - trained_models/meta_ensemble.pkl (trained model)")
print(f"  - test_predictions.csv (final submission)")
