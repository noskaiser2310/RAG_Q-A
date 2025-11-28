import pandas as pd
import numpy as np
from dataclasses import dataclass
from typing import Set, Dict, List, Optional
from pathlib import Path
import json
import re

model_configs = [
    {
        'name':  'Qwen4B-qwen',  
        'output': r'val\model_Qwen3-4b_results_vn.csv'
    },
    {
        'name':  'Qwen4B-qwen',  
        'output': r'val\model_Qwen3-4b_results.csv'
    },
    {
        'name':  'Qwen2.5-3B',  
        'output': r'val\model_Qwen2.5-3B_results.csv'
    },
]



# === Cấu hình  ===
GT_CSV = "ground_truth.csv"      
MODEL_RESULTS = model_configs 
OUT_DIR = Path("evaluate_all")
VER = "v1"


# === Utilities ===
OPTION_PATTERN = re.compile(r"[A-D]", re.IGNORECASE)
VALID_OPTIONS = ("A","B","C","D")

def parse_answers(ans: Optional[str]) -> Set[str]:
    if ans is None:
        return set()
    if isinstance(ans, float) and np.isnan(ans):
        return set()
    s = str(ans)
    picks = set(ch.upper() for ch in OPTION_PATTERN.findall(s))
    return picks


@dataclass
class HalvesOutcome:
    k: int
    correct_set: Set[str]
    pred_set: Set[str]
    c: int
    w: int
    e: int
    score: float


def halves_method_score(k: int, correct_set: Set[str], pred_set: Set[str]) -> HalvesOutcome:
    c = len(pred_set & correct_set)
    w = len(pred_set - correct_set)
    e = (k - c) + w
    score = 1.0 if e == 0 else (0.5 if e == 1 else 0.0)
    return HalvesOutcome(k, correct_set, pred_set, c, w, e, score)


def error_type(k: int, c: int, w: int) -> str:
    miss = (k - c)
    if miss == 0 and w == 0:
        return "exact_match"
    if miss > 0 and w == 0:
        return "missing_only"
    if miss == 0 and w > 0:
        return "overselect_only"
    return "missing_and_overselect"


def to_multilabel_vectors(correct_set: Set[str], pred_set: Set[str], options=VALID_OPTIONS):
    y_true = [1 if o in correct_set else 0 for o in options]
    y_pred = [1 if o in pred_set else 0 for o in options]
    return y_true, y_pred


def multilabel_report(y_true_all: List[List[int]], y_pred_all: List[List[int]]):
    Yt = np.array(y_true_all)
    Yp = np.array(y_pred_all)
    if len(Yt) == 0:
        return {k:0.0 for k in ["micro_precision","micro_recall","micro_f1","macro_precision","macro_recall","macro_f1","subset_accuracy"]}
    tp = np.logical_and(Yt==1, Yp==1).sum()
    fp = np.logical_and(Yt==0, Yp==1).sum()
    fn = np.logical_and(Yt==1, Yp==0).sum()
    micro_p = tp / (tp + fp) if (tp + fp) > 0 else 0.0
    micro_r = tp / (tp + fn) if (tp + fn) > 0 else 0.0
    micro_f1 = 2 * micro_p * micro_r / (micro_p + micro_r) if (micro_p + micro_r) > 0 else 0.0

    per_opt = []
    for j in range(Yt.shape[1]):
        tpj = np.logical_and(Yt[:, j] == 1, Yp[:, j] == 1).sum()
        fpj = np.logical_and(Yt[:, j] == 0, Yp[:, j] == 1).sum()
        fnj = np.logical_and(Yt[:, j] == 1, Yp[:, j] == 0).sum()
        pj = tpj / (tpj + fpj) if (tpj + fpj) > 0 else 0.0
        rj = tpj / (tpj + fnj) if (tpj + fnj) > 0 else 0.0
        f1j = 2 * pj * rj / (pj + rj) if (pj + rj) > 0 else 0.0
        per_opt.append((pj, rj, f1j))
    macro_p = float(np.mean([p for p, _, _ in per_opt])) if per_opt else 0.0
    macro_r = float(np.mean([r for _, r, _ in per_opt])) if per_opt else 0.0
    macro_f1 = float(np.mean([f for *_, f in per_opt])) if per_opt else 0.0

    subset_acc = float((Yt == Yp).all(axis=1).mean())

    return {
        "micro_precision": micro_p,
        "micro_recall": micro_r,
        "micro_f1": micro_f1,
        "macro_precision": macro_p,
        "macro_recall": macro_r,
        "macro_f1": macro_f1,
        "subset_accuracy": subset_acc,
    }


def df_to_md_table(df: pd.DataFrame) -> str:
    if df.empty:
        return "| (empty) |\n| --- |\n"
    cols = list(df.columns)
    lines = []
    lines.append("| " + " | ".join(str(c) for c in cols) + " |")
    lines.append("| " + " | ".join("---" for _ in cols) + " |")
    for _, row in df.iterrows():
        lines.append("| " + " | ".join(str(row[c]) for c in cols) + " |")
    return "\n".join(lines)


# === Core evaluation function ===
def evaluate_halves_both_two_cols(gt_csv_path: str, pred_csv_path: str):
    df_gt = pd.read_csv(gt_csv_path)
    df_pd = pd.read_csv(pred_csv_path)

    for need in ("num_correct", "answers"):
        if need not in df_gt.columns:
            raise ValueError(f"GT CSV must contain '{need}' column.")
        if need not in df_pd.columns:
            raise ValueError(f"Prediction CSV must contain '{need}' column.")

    if 'question_id' in df_gt.columns:
        df_gt = df_gt.sort_values('question_id').reset_index(drop=True)
    else:
        df_gt = df_gt.reset_index(drop=True)

    if 'question_id' in df_pd.columns:
        df_pd = df_pd.sort_values('question_id').reset_index(drop=True)
    else:
        df_pd = df_pd.reset_index(drop=True)

    n = min(len(df_gt), len(df_pd))
    df_gt = df_gt.iloc[:n]
    df_pd = df_pd.iloc[:n]

    rows = []
    y_true_all, y_pred_all = [], []
    for i in range(n):
        k = int(df_gt.loc[i, 'num_correct'])
        correct_set = parse_answers(df_gt.loc[i, 'answers'])
        pred_set = parse_answers(df_pd.loc[i, 'answers'])

        out = halves_method_score(k, correct_set, pred_set)
        etype = error_type(out.k, out.c, out.w)

        miss_letters = sorted(list(out.correct_set - out.pred_set))
        over_letters = sorted(list(out.pred_set - out.correct_set))

        rows.append({
            "ques": i+1,
            "k": out.k,
            "correct_letters": "".join(sorted(out.correct_set)),
            "pred_letters": "".join(sorted(out.pred_set)),
            "c": out.c,
            "w": out.w,
            "e": out.e,
            "halves_score": out.score,
            "exact_match": int(etype == "exact_match"),
            "error_type": etype,
            "missing_letters": "".join(miss_letters),
            "overselect_letters": "".join(over_letters),
        })

        yt, yp = to_multilabel_vectors(correct_set, pred_set)
        y_true_all.append(yt)
        y_pred_all.append(yp)

    per_q_df = pd.DataFrame(rows)
    official_mean = per_q_df["halves_score"].mean() if n > 0 else 0.0
    exact_acc = per_q_df["exact_match"].mean() if n > 0 else 0.0
    one_error_rate = float((per_q_df["e"] == 1).mean()) if n > 0 else 0.0
    two_plus_error_rate = float((per_q_df["e"] >= 2).mean()) if n > 0 else 0.0

    by_k = per_q_df.groupby("k", as_index=False).agg(
        n = ("ques", "count"),
        halves = ("halves_score", "mean"),
        exact = ("exact_match", "mean"),
        e1 = ("e", lambda s: (s == 1).mean()),
        e2p = ("e", lambda s: (s >= 2).mean())
    )

    ml = multilabel_report(y_true_all, y_pred_all)

    summary = {
        "official_halves_mean": float(official_mean),
        "exact_match_accuracy": float(exact_acc),
        "one_error_rate": float(one_error_rate),
        "two_plus_error_rate": float(two_plus_error_rate),
        **ml
    }

    return per_q_df, by_k, summary, int(n)


def write_markdown_report(md_path: str, pred_basename: str, ver: str, n: int, summary: Dict, by_k_df: pd.DataFrame):
    md_path = Path(md_path)
    md_path.parent.mkdir(parents=True, exist_ok=True)
    lines = []
    lines.append(f"# QA Evaluation Result — {pred_basename} (ver={ver})")
    lines.append("")
    lines.append(f"- **Questions evaluated**: {n}")
    lines.append(f"- **Official Halves Mean**: {summary['official_halves_mean']:.6f}")
    lines.append(f"- **Exact Match Accuracy**: {summary['exact_match_accuracy']:.6f}")
    lines.append(f"- **One-Error Rate (e=1)**: {summary['one_error_rate']:.6f}")
    lines.append(f"- **Two-Plus Error Rate (e≥2)**: {summary['two_plus_error_rate']:.6f}")
    lines.append("")
    lines.append("## Multi-label Metrics (per option A/B/C/D)")
    lines.append(f"- Micro P/R/F1: {summary['micro_precision']:.6f} / {summary['micro_recall']:.6f} / {summary['micro_f1']:.6f}")
    lines.append(f"- Macro P/R/F1: {summary['macro_precision']:.6f} / {summary['macro_recall']:.6f} / {summary['macro_f1']:.6f}")
    lines.append(f"- Subset Accuracy (option-level exact set): {summary['subset_accuracy']:.6f}")
    lines.append("")
    lines.append("## Breakdown by k")
    lines.append(df_to_md_table(by_k_df))
    md_path.write_text("\n".join(lines), encoding="utf-8")


import re

def sanitize_model_name(name: str) -> str:
    # Thay thế các ký tự không thích hợp thành underscore _
    sanitized = re.sub(r'[^a-zA-Z0-9]+', '_', name)
    # Xóa các ký tự _ thừa đầu/cuối hoặc nối tiếp
    sanitized = re.sub(r'_+', '_', sanitized).strip('_')
    return sanitized

# Thay đổi bên trong run_eval_multiple_models
def run_eval_multiple_models(gt_csv: str, model_outputs: List[Dict], out_dir: str, ver: str):
    out_dir = Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    results_summary = []

    for model_info in model_outputs:
        pred_csv = model_info['output']
        model_name = model_info['name']
        print(f"\nEvaluating model: {model_name}")

        per_q_df, by_k_df, summary, n = evaluate_halves_both_two_cols(gt_csv, pred_csv)

        pred_base = sanitize_model_name(model_name)

        per_q_path = out_dir / f"{pred_base}_per_question_{ver}.csv"
        wrong_path = out_dir / f"{pred_base}_wrong_{ver}.csv"
        byk_path = out_dir / f"{pred_base}_byk_{ver}.csv"
        json_path = out_dir / f"{pred_base}_result_{ver}.json"
        md_path = out_dir / f"{pred_base}_report_{ver}.md"

        per_q_df.to_csv(per_q_path, index=False)
        wrong_df = per_q_df[per_q_df["halves_score"] < 1.0].copy()
        wrong_df.to_csv(wrong_path, index=False)
        by_k_df.to_csv(byk_path, index=False)

        # Lưu JSON tổng hợp
        examples = []
        for _, r in wrong_df.head(20).iterrows():
            ex = {
                "ques": int(r["ques"]),
                "error_type": r.get("error_type", ""),
                "correct_letters": r.get("correct_letters", ""),
                "pred_letters": r.get("pred_letters", ""),
                "missing_letters": r.get("missing_letters", ""),
                "overselect_letters": r.get("overselect_letters", ""),
            }
            examples.append(ex)

        payload = {
            "file": pred_base,
            "version": ver,
            "n_questions": n,
            "summary": summary,
            "by_k": json.loads(by_k_df.to_json(orient="records")),
            "wrong_examples": examples
        }
        json_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")

        write_markdown_report(md_path, pred_base, ver, n, summary, by_k_df)

        print(f"  ✓ Saved results for {model_name} in {out_dir}")

        results_summary.append({
            "model_name": model_name,
            "per_question_csv": str(per_q_path),
            "wrong_only_csv": str(wrong_path),
            "by_k_csv": str(byk_path),
            "json_summary": str(json_path),
            "markdown_report": str(md_path),
            "n_questions": n,
            "official_halves_mean": summary["official_halves_mean"]
        })

    return results_summary



# === Main chạy ----
if __name__ == "__main__":
    summary = run_eval_multiple_models(GT_CSV, MODEL_RESULTS, OUT_DIR, VER)

    for res in summary:
        print(f"\nModel: {res['model_name']}")
        print(f"Questions evaluated: {res['n_questions']}")
        print(f"Official Halves Mean Score: {res['official_halves_mean']:.4f}")
        print(f"Markdown report: {res['markdown_report']}")