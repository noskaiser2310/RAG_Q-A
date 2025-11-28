# RAG-based QA Submission (MinerU + RAG + Qwen)

Hệ thống thiết kế là một pipeline đầy đủ để:

1. Nhận PDF đề thi/tài liệu kỹ thuật.
2. Làm sạch PDF (xoá header/footer, watermark, bảng rác…).
3. Chuyển PDF → Markdown bằng MinerU và hậu xử lý (heading, bảng, font).
4. Xây dựng RAG (BM25 + dense embedding + reranker).
5. Dùng Qwen + RAG để trả lời câu hỏi trắc nghiệm nhiều lựa chọn.
6. Sinh file `answer.md` đúng format để nộp.

---

## 1. Cấu trúc thư mục

```bash
├── run_extract.sh               # Task 1: PDF → Markdown + build RAG + answer.md (TASK EXTRACT)
├── run_choose_answer.sh         # Task 2: Trả lời câu hỏi + update answer.md (TASK QA)
├── requirements.txt             # Dependencies python

├── src/
│   ├── clean_headler.py         # Tiền xử lý PDF, xoá header/footer, watermark, bảng rác
│   ├── pdf_extractor_mineru.py  # Gọi MinerU, convert PDF đã clean → raw Markdown
│   ├── clean_data_mineru.py     # Làm sạch Markdown MinerU (gộp dòng, format heading/bullet,…)
│   ├── detect_font.py           # Phân tích font / size / style cho từng block trong PDF
│   ├── detect_healder.py        # Dùng ML (LightGBM) detect các dòng heading
│   ├── matching_headler.py      # Ghép heading với nội dung, chuẩn hoá cấu trúc section
│   ├── table_clean_final.py     # Làm sạch bảng text, chèn lại bảng chuẩn vào main.md
│   ├── rag_system.py            # Advanced RAG (BM25 + dense + reranker + query expansion)
│   ├── qa_system.py             # LLM-based QA: sinh prompt, gọi Qwen, chọn đáp án “conservative”
│   ├── qa_task.py               # Đọc question.csv, chạy QA với RAG, xuất CSV kết quả
│   ├── create_late_file.py      
│   ├── ensemble_model.py        # (tuỳ chọn) ensemble nhiều file CSV (nếu dùng nhiều model)
│   ├── model_headling_detect.py 
│   ├── training_model_detect.py 
│   ├── zip.py                   
│   └── __pycache__/             # Cache python

├── working/
│   ├── cleaned_pdfs_test/           # PDF sau khi clean_headler.py
│   ├── output_mineru_raw_test/      # Raw Markdown từ MinerU
│   ├── output_mineru_test/          # Markdown đã clean, thêm heading + bảng đầy đủ
│   ├── output_markdown_detect_test/ # Markdown có thông tin heading cho debug
│   ├── Font_CrossBlock_Context_Filtered/
│   ├── logs/
│   ├── ml_heading_model_lgb/        # Model detect heading đã train
│   ├── models/                      # Cache model RAG/LLM/embedding
│   ├── reports_table_removal/       # Báo cáo bảng bị xoá/thay thế
│   └── training_cache/              # Cache RAG (extracted_contents, index, mapping, ...)

├── test/
│   ├── model_Qwen3-4b_qwen.csv      # Kết quả QA từng câu hỏi (num_correct, answers,…)
│   └── ...                         

├── val/                             # dữ liệu validation

├── answer.md                        # File kết quả cuối (TASK EXTRACT + TASK QA)
├── main.py                     
└── submission_output.zip            # File nộp cuối cùng cho BTC 
```

---

## 2. Cách chạy

### 2.1. Cài đặt môi trường yêu cầu (Python 3.11)

```bash
pip install -r requirements.txt
```

Yêu cầu phần cứng:

* GPU ~8GB VRAM (để chạy Qwen 3B ổn định).
* Ổ cứng đủ chỗ cho model + cache (~10–15GB).

### 2.2. Chuẩn bị dữ liệu

Đảm bảo cấu trúc:

```bash
private_test/input/
├── *.pdf
└── question.csv
```

---

## 3. Task 1 – Extract & Build RAG

Chạy:

```bash
bash run_extract.sh
```

Pipeline :

1. **Làm sạch PDF**

   * `src/clean_headler.py`
   * Input: `private_test/input/*.pdf`
   * Output: `working/cleaned_pdfs_test/`

2. **PDF → Raw Markdown (MinerU)**

   * `src/pdf_extractor_mineru.py`
   * Input: `working/cleaned_pdfs_test/`
   * Output: `working/output_mineru_raw_test/`

3. **Làm sạch Markdown**

   * `src/clean_data_mineru.py`, `src/add_healder.py`
   * Chuẩn hoá heading, bullet, fix xuống dòng, thêm header `Public_xxx`,…

4. **Phân tích font & heading**

   * `src/detect_font.py`, `src/detect_healder.py`, `src/matching_headler.py`, `src/inject_font.py`
   * Model LightGBM dựa trên font/position để detect heading các cấp.

5. **Xử lý bảng**

   * `src/inject_table.py`, `src/table_clean_final.py`
   * Lấy bảng chuẩn từ PDF, loại bỏ bảng ASCII xấu, chèn lại vào Markdown.

6. **Gộp Markdown**

   * `src/combie.py`

     * Gộp các `main.md` trong `working/output_mineru_test/` thành block `### TASK EXTRACT` trong `answer.md`.
   * `src/load_and_index_task.py`

**Kết quả sau Task 1**

* Markdown cuối cùng mỗi PDF: `working/output_mineru_test/Public_xxx/main.md`
* Cache RAG: trong `working/training_cache/`
* File `answer.md` mới chỉ có phần:

  ```markdown
  ### TASK EXTRACT
  # [pdf_name_1]
  ...
  ```

---

## 4. Task 2 – Answer Questions (QA)

Chạy:

```bash
bash run_choose_answer.sh
```

Pipeline:

1. **Load RAG & dữ liệu câu hỏi**

   * Đọc `private_test/input/question.csv`.

2. **Giải trắc nghiệm với Qwen + RAG**

   * `src/qa_task.py` + `src/qa_system.py` + `src/rag_system.py`

   * Với mỗi câu hỏi:

     * Truy vấn RAG để lấy context phù hợp.
     * Sinh prompt cho Qwen (`Qwen/Qwen3-4B-Instruct-2507` hoặc model cấu hình trong code).
     * Tính điểm/tin cậy cho các lựa chọn A/B/C/D.
     * Áp dụng chiến lược chọn đáp án **“conservative”**: chỉ chọn những option có xác suất cao, có thể là 1 hoặc nhiều đáp án tuỳ `num_correct`.

   * Kết quả trung gian:

     * `test/model_Qwen3-4b_qwen.csv`

3. **Ghi đáp án vào answer.md**

   * `src/create_late_file.py`
   * Đọc `test/model_Qwen3-4b_qwen.csv`, kiểm tra lỗi định dạng, chuẩn hoá cột `answers`,
     sau đó **chèn/ghi đè** block:

     ```markdown
     ### TASK QA
     num_correct,answers
     ...
     ```

     vào cuối `answer.md`.

4. **(Tuỳ chọn) Ensemble nhiều model**

   * `src/ensemble_model.py` nếu chạy nhiều model và muốn trộn kết quả.

**Kết quả sau Task 2**

* `test/model_Qwen3-4b_qwen.csv` – bảng chi tiết đáp án.
* `answer.md` – file đầy đủ theo format BTC (TASK EXTRACT + TASK QA).
* `submission_output.zip` - file nén chứa toàn bộ nội dung

---

## 5. Format `answer.md`

File cuối `answer.md` có dạng:

```markdown
### TASK EXTRACT
# [pdf_name_1]

[Markdown content đã được xử lý...]

# [pdf_name_2]

[Markdown content...]

### TASK QA
num_correct,answers
1,A
2,"A,C"
1,B
...
```

Trong đó:

* `num_correct` là số đáp án đúng của câu hỏi (cung cấp trong question.csv).
* `answers` là các lựa chọn mà model dự đoán (A/B/C/D),
  nếu nhiều hơn một đáp án thì ghi `"A,C"` (có ngoặc kép, phân tách bởi dấu phẩy).

---
