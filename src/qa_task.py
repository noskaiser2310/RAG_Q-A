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
from qa_system import run_single_model, ensemble_multiple_csvs
warnings.filterwarnings("ignore")


extracted_contents = auto_generate_data("working/output_mineru_test")

rag_system = AdvancedRAGSystem(
    extracted_contents=extracted_contents,
    embedding_model="AITeamVN/Vietnamese_Embedding_v2"
)

# Step 2: Load questions
print("\n[STEP 2] Loading questions...")

df = pd.read_csv('private_test/input/question.csv')

questions = []
for idx, row in df.iterrows():
    questions.append({
        'question_id': idx,
        'question': row['Question'],
        'options': {
            'A': row['A'],
            'B': row['B'],
            'C': row['C'],
            'D': row['D']
        }
    })

print(f"✓ Loaded {len(questions)} questions")

# Step 3: Run models sequentially
model_configs = [
    {
        'name':  'Qwen/Qwen3-4B-Instruct-2507',  
        'output': 'test\model_Qwen3-4b_qwen.csv'
    },
]

csv_files = []

for i, config in enumerate(model_configs, 1):
    print(f"\n[STEP {3+i-1}] Running Model {i}/{len(model_configs)}...")

    run_single_model(
        model_name=config['name'],
        questions=questions,
        rag=rag_system,
        output_csv=config['output'],
        batch_size=10  # Adjust based on GPU memory
    )

    csv_files.append(config['output'])

# # Step 4: Final ensemble
# weights = [1]

# ensemble_multiple_csvs(
#     csv_files=csv_files,
#     output_csv='submission.csv',
#     threshold=0.70 ,
#     weights=weights
# )

print("\n" + "="*80)
print("✓ PIPELINE COMPLETE")