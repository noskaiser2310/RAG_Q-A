# -*- coding: utf-8 -*-
import re
from pathlib import Path
import pandas as pd


# ======= CẤU HÌNH =======
CSV_PATH = r"test\model_Qwen3-4b_qwen.csv"  
MD_PATH  = r"working\anwser.md"                              
HEADER   = "### TASK QA"                                 
# =========================


df = pd.read_csv(CSV_PATH, dtype={"num_correct": str, "answers": str})

for col in ["num_correct", "answers"]:
    df[col] = (
        df[col]
        .astype(str)
        .str.replace(r"[\r\n]+", "", regex=True)
        .str.strip()
    )


VALID_CHOICES = set("ABCD")

def check_answers_valid(ans: str):
    core = ans.strip('"').strip()
    parts = list(core)
    for p in parts:
        if p not in VALID_CHOICES:
            raise ValueError(f"'{core}' không hợp lệ (chỉ A,B,C,D) trong output")

check_errors = []
for idx, ans in enumerate(df["answers"], 1):
    try:
        check_answers_valid(ans)
    except ValueError as err:
        check_errors.append((idx, str(err)))

if check_errors:
    errors_messages = '\n'.join([f"Dòng {idx}: {msg}" for idx, msg in check_errors])
    raise ValueError(f"Lỗi phát hiện trong file CSV:\n{errors_messages}")


def format_answers(ans: str) -> str:
    core = ans.strip('"').strip()
    if "," in core:
        parts = [p.strip() for p in core.split(",") if p.strip()]
        return '"' + ",".join(parts) + '"'
    else:
        parts = list(core)
        if len(parts) > 1 and all(p in VALID_CHOICES for p in parts):
            return '"' + ",".join(parts) + '"'
        return core

df["answers"] = df["answers"].apply(format_answers)

lines = [f"{nc},{ans}" for nc, ans in df[["num_correct", "answers"]].itertuples(index=False, name=None)]
qa_block = HEADER + "\n" + "num_correct,answers\n" + "\n".join(lines)


md_path = Path(MD_PATH)
old_text = md_path.read_text(encoding="utf-8") if md_path.exists() else ""

m = re.search(r"(?m)^### TASK QA[^\n]*\n", old_text)
if m:
    new_text = old_text[:m.start()] + qa_block
else:
    if old_text and not old_text.endswith("\n"):
        old_text += "\n"
    new_text = old_text + qa_block


with open(MD_PATH, "w", encoding="utf-8", newline="\n") as f:
    f.write(new_text)


print("cập nhật file markdown:", MD_PATH)