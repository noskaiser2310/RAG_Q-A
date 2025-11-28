import os
import re
import gc
import csv
import time
import warnings
from pathlib import Path
from collections import defaultdict
from dataclasses import dataclass, field
from typing import List, Dict, Tuple, Optional, Any, Set

import numpy as np
import pandas as pd
import torch
import faiss

from rank_bm25 import BM25Okapi
from sentence_transformers import SentenceTransformer, CrossEncoder
from transformers import (
    AutoModelForCausalLM,
    AutoTokenizer,
    AutoModelForSequenceClassification,
)
from langchain.text_splitter import RecursiveCharacterTextSplitter

from rag_system import AdvancedRAGSystem, auto_generate_data
# ===========================================================================
# PART 2: OPTIMIZED QA SYSTEM (SEQUENTIAL + BATCH + MEMORY CLEANUP)
# ============================================================================

class OptimizedQASystem:
    """
    Optimized QA with:
    - Batch processing
    - Soft probabilities
    - Conservative selection
    - Memory cleanup
    """

    def __init__(self, model_name: str, device="cuda"):
        self.model_name = model_name
        self.device = device
        self.model = None
        self.tokenizer = None
        self.pipe = None

    def load_model(self):
        """Load model into memory"""
        print(f"\n[QA] Loading {self.model_name}...")

        self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
        self.model = AutoModelForCausalLM.from_pretrained(
            self.model_name,
            torch_dtype=torch.float16,
            device_map="auto",
            low_cpu_mem_usage=True
        )

        self.pipe = pipeline(
            "text-generation",
            model=self.model,
            tokenizer=self.tokenizer,
            max_new_tokens=100,
            temperature=0.1,
            do_sample=False,
            return_full_text=False
        )

        print(f"✓ Model loaded: {self.model_name}")

    def unload_model(self):
        """Unload model and free memory"""
        print(f"\n[QA] Unloading {self.model_name}...")

        if self.model is not None:
            del self.model
        if self.tokenizer is not None:
            del self.tokenizer
        if self.pipe is not None:
            del self.pipe

        self.model = None
        self.tokenizer = None
        self.pipe = None

        # Clean GPU memory
        if torch.cuda.is_available():
            torch.cuda.empty_cache()

        # Clean system memory
        gc.collect()

        print("✓ Model unloaded, memory cleaned")

    def _detect_question_complexity(self, question: str, context: str) -> str:
        """
        Detect question type and return reasoning complexity
        
        Returns: 'simple', 'calculation', 'comparison', 'inference'
        """
        q = question.lower()
        # Từ khóa cho các loại câu hỏi
        calculation_keywords = ['tính', 'bao nhiêu', 'phần trăm', 'số', 'đếm', 'tổng']
        comparison_keywords = ['so sánh', 'khác nhau', 'giống nhau', 'hơn', 'thấp hơn', 'cao hơn']
        inference_keywords = ['suy ra', 'kết luận', 'có thể', 'dẫn đến', 'vì vậy', 'do đó']
        
        if any(kw in q for kw in calculation_keywords):
            return 'calculation'
        if any(kw in q for kw in comparison_keywords):
            return 'comparison'
        if any(kw in q for kw in inference_keywords):
            return 'inference'
        return 'simple'


    def _get_reasoning_steps(self, complexity: str) -> str:
        """
        Return reasoning steps string based on the complexity type
        """
        steps = {
            'simple': (
                "1. Tìm thông tin liên quan trong bối cảnh.\n"
                "2. So sánh với đáp án cần đánh giá.\n"
                "3. Kết luận đáp án đúng (Y) hay sai (N)."
            ),
            'calculation': (
                "1. Xác định các số liệu liên quan trong bối cảnh.\n"
                "2. Xác định phép tính cần thực hiện.\n"
                "3. Tính toán và kiểm tra kết quả.\n"
                "4. So sánh với đáp án.\n"
                "5. Kết luận đáp án đúng (Y) hay sai (N)."
            ),
            'comparison': (
                "1. Xác định các đối tượng cần so sánh.\n"
                "2. Liệt kê đặc điểm, số liệu của các đối tượng.\n"
                "3. Phân tích điểm giống và khác.\n"
                "4. So sánh với đáp án.\n"
                "5. Kết luận đáp án đúng (Y) hay sai (N)."
            ),
            'inference': (
                "1. Xác định các tiền đề trong bối cảnh.\n"
                "2. Áp dụng quy luật logic hoặc sự kiện liên quan.\n"
                "3. Thực hiện các bước suy diễn logic.\n"
                "4. So sánh với đáp án.\n"
                "5. Kết luận đáp án đúng (Y) hay sai (N)."
            )
        }
        return steps.get(complexity, steps['simple'])
    
    
    def evaluate_single_option(self, question: str, option_letter: str,
                               option_text: str, context: str = "") -> float:
        """
        Adaptive reasoning evaluation with dynamic prompt structure
        
        Returns: confidence score float in [0,1]
        """
        try:
            complexity = self._detect_question_complexity(question, context)
            reasoning_steps = self._get_reasoning_steps(complexity)
    
            prompt = f"""Bạn là chuyên gia phân tích đáp án trắc nghiệm tiếng việt, có khả năng đánh giá chính xác từng lựa chọn dựa trên câu hỏi, ngữ cảnh và hướng dẫn suy luận. Nhiệm vụ của bạn là xác định liệu đáp án được đưa ra là đúng (Y) hay sai (N) — không cần giải thích lý do.

##Nguyên tắc đánh giá:
- Tập trung tuyệt đối vào phần “CÂU HỎI” để xác định yêu cầu chính của đề bài.
- Ngữ cảnh đầu vào có thể chứa thông tin nhiễu, nên chỉ sử dụng các chi tiết thật sự liên quan đến câu hỏi.
- Đối chiếu đáp án với câu hỏi và hướng dẫn suy luận để xác định tính đúng/sai.
- Phân tích thật kỹ trước khi đưa ra câu trả lời cho câu hỏi và phải xác minh thật chuẩn và chính xác 
- Chỉ đưa ra kết quả cuối cùng là đúng(Y) hoặc sai(N) thôi không kèm theo gì cái gì khác 
## BỐI CẢNH
{context[:2500]}

## CÂU HỎI 
{question}

## ĐÁP ÁN CẦN ĐÁNH GIÁ 
{option_letter}. {option_text}

=== HƯỚNG DẪN ĐÁNH GIÁ (Loại câu hỏi: {complexity.upper()}) ===
{reasoning_steps}

Chỉ trả lời cuối cùng: Y (đúng) hoặc N (sai)

Trả lời:"""
    
            inputs = self.tokenizer(prompt, return_tensors="pt").to(self.device)
    
            with torch.no_grad():
                outputs = self.model.generate(
                    inputs.input_ids,
                    max_new_tokens=1,
                    output_scores=True,
                    return_dict_in_generate=True,
                    temperature=0.7,
                    do_sample=False,
                    pad_token_id=self.tokenizer.eos_token_id
                )
    
            if not hasattr(outputs, 'scores') or len(outputs.scores) == 0:
                return 0.5
    
            first_token_logits = outputs.scores[0][0]
    
            y_tokens, n_tokens = [], []
    
            for y_var in ["Y", "y", " Y", " y"]:
                ids = self.tokenizer.encode(y_var, add_special_tokens=False)
                if len(ids) > 0:
                    y_tokens.append(ids[0])
    
            for n_var in ["N", "n", " N", " n"]:
                ids = self.tokenizer.encode(n_var, add_special_tokens=False)
                if len(ids) > 0:
                    n_tokens.append(ids[0])
    
            y_tokens = list(set(y_tokens))
            n_tokens = list(set(n_tokens))
    
            if not y_tokens or not n_tokens:
                return 0.5
    
            probs = torch.softmax(first_token_logits, dim=-1)
    
            y_prob = max([probs[tid].item() for tid in y_tokens])
            n_prob = max([probs[tid].item() for tid in n_tokens])
    
            total = y_prob + n_prob
            confidence = y_prob / total if total > 0 else 0.5
    
            confidence = max(0.0, min(1.0, confidence))
    
            return confidence
    
        except Exception as e:
            print(f"    [WARN] Logit extraction failed for {option_letter}: {str(e)[:80]}")
    
            try:
                response = self.pipe(
                    prompt,
                    max_new_tokens=1,
                    temperature=0.7
                )[0]['generated_text'].strip().upper()
    
                if response.startswith('Y'):
                    return 0.75
                elif response.startswith('N'):
                    return 0.25
                else:
                    return 0.5
            except:
                return 0.5


    def process_batch(self, questions: List[dict], rag: AdvancedRAGSystem,
                     batch_size: int = 5) -> List[dict]:
        """
        Process batch of questions

        Args:
            questions: List of {question, options_dict}
            rag: RAG system for context retrieval
            batch_size: Number of questions to process together

        Returns:
            List of results with soft probabilities
        """

        if self.model is None:
            raise RuntimeError("Model not loaded. Call load_model() first.")

        results = []
        total = len(questions)

        print(f"\n[QA] Processing {total} questions in batches of {batch_size}...")

        for start_idx in range(0, total, batch_size):
            end_idx = min(start_idx + batch_size, total)
            batch = questions[start_idx:end_idx]

            # Process batch
            for i, q_data in enumerate(batch):
                question = q_data['question']
                options = q_data['options']

                # Get context from RAG
                try:
                    retrieved = rag.retrieve(question, top_k=3)
                    context = "\n\n".join([r.chunk for r in retrieved])
                except:
                    context = ""

                # Evaluate each option
                option_scores = {}
                for opt_letter, opt_text in options.items():
                    score = self.evaluate_single_option(
                        question, opt_letter, opt_text, context
                    )
                    option_scores[opt_letter] = score

                # Conservative selection
                selected = self._select_conservative(option_scores, threshold=0.65)

                results.append({
                    'question_id': q_data['question_id'],
                    'question': question,
                    'option_scores': option_scores,
                    'selected_answers': selected,
                    'num_correct': len(selected),
                    'answers': ''.join(sorted(selected))
                })

                if (start_idx + i + 1) % 50 == 0:
                    print(f"  ✓ Processed {start_idx + i + 1}/{total}")

        print(f"  ✓ Batch processing complete: {len(results)} results")

        return results

    def _select_conservative(self, scores: Dict[str, float],
                            threshold: float = 0.65) -> List[str]:
        """
        Conservative answer selection

        Strategy:
        - High threshold to avoid penalty
        - Max 2 answers
        - Prefer fewer over many wrong
        """

        sorted_opts = sorted(scores.items(), key=lambda x: x[1], reverse=True)

        selected = []
        for opt, score in sorted_opts:
            if score >= threshold:
                selected.append(opt)

        # Safety: at least 1 answer
        if not selected:
            selected = [sorted_opts[0][0]]

        # Safety: max 2 answers
        if len(selected) > 2:
            selected = selected[:2]

        return sorted(selected)


# ============================================================================
# PART 3: SEQUENTIAL ENSEMBLE PIPELINE
# ============================================================================

def run_single_model(model_name: str, questions: List[dict], rag: AdvancedRAGSystem,
                     output_csv: str, batch_size: int = 5):
    """
    Run single model on all questions

    Pipeline:
    1. Load model
    2. Process all questions in batches
    3. Save results to CSV
    4. Unload model and clean memory
    """

    print(f"\n{'='*80}")
    print(f"RUNNING MODEL: {model_name}")
    print(f"{'='*80}")

    # Initialize QA system
    qa = OptimizedQASystem(model_name, device="cuda")

    # Load model
    qa.load_model()

    # Process all questions
    results = qa.process_batch(questions, rag, batch_size=batch_size)

    # Save to CSV with soft probabilities
    save_results_with_probabilities(results, output_csv)

    # Unload and cleanup
    qa.unload_model()

    print(f"\n✓ Model {model_name} complete")
    print(f"✓ Results saved to: {output_csv}")

    return results


def save_results_with_probabilities(results: List[dict], output_path: str):
    """Save results with soft probabilities"""

    with open(output_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)

        # Header
        writer.writerow([
            'question_id', 'num_correct', 'answers',
            'prob_A', 'prob_B', 'prob_C', 'prob_D'
        ])

        # Data
        for r in results:
            scores = r['option_scores']
            writer.writerow([
                r['question_id'],
                r['num_correct'],
                r['answers'],
                f"{scores['A']:.4f}",
                f"{scores['B']:.4f}",
                f"{scores['C']:.4f}",
                f"{scores['D']:.4f}"
            ])

    print(f"  ✓ Saved {len(results)} results to {output_path}")


def ensemble_multiple_csvs(csv_files: List[str], 
                          output_csv: str,
                          threshold: float = 0.70,
                          weights: Optional[List[float]] = None):
    
    print(f"\n{'='*80}")
    print(f"FINAL ENSEMBLE FROM {len(csv_files)} MODELS")
    print(f"{'='*80}")
    
    # Validate and normalize weights
    if weights is None:
        weights = [1.0 / len(csv_files)] * len(csv_files)
        print(f"Using equal weights: {weights}")
    else:
        assert len(weights) == len(csv_files), \
            f"Weights length ({len(weights)}) != Models count ({len(csv_files)})"
        
        # Normalize
        total = sum(weights)
        weights = [w / total for w in weights]
        print(f"Normalized weights: {[f'{w:.4f}' for w in weights]}")
    
    # Load all predictions
    dfs = [pd.read_csv(f) for f in csv_files]
    
    final_results = []
    
    for idx in range(len(dfs[0])):
        # Weighted aggregation
        all_probs = {'A': [], 'B': [], 'C': [], 'D': []}
        
        for df in dfs:
            row = df.iloc[idx]
            all_probs['A'].append(float(row['prob_A']))
            all_probs['B'].append(float(row['prob_B']))
            all_probs['C'].append(float(row['prob_C']))
            all_probs['D'].append(float(row['prob_D']))
        
        # Weighted average
        final_probs = {}
        for opt in ['A', 'B', 'C', 'D']:
            final_probs[opt] = sum(w * p for w, p in zip(weights, all_probs[opt]))
        
        # Select answers
        sorted_opts = sorted(final_probs.items(), key=lambda x: x[1], reverse=True)
        
        selected = []
        for opt, prob in sorted_opts:
            if prob >= threshold:
                selected.append(opt)
        
        if not selected:
            selected = [sorted_opts[0][0]]
        
        if len(selected) > 2:
            selected = selected[:2]
        
        final_results.append({
            'question_id': idx,
            'num_correct': len(selected),
            'answers': ''.join(sorted(selected))
        })
    
    # Save
    pd.DataFrame(final_results).to_csv(output_csv, index=False)
    print(f"\n✓ Saved to: {output_csv}")