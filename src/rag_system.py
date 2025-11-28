import os
import re
import torch
import warnings
from pathlib import Path
from typing import Dict, List, Tuple, Optional
from collections import defaultdict
from sentence_transformers import CrossEncoder
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import re
import time
import numpy as np
import faiss
import torch
import pandas as pd
from typing import List, Dict, Optional, Tuple, Any, Set
from collections import defaultdict
from dataclasses import dataclass, field
from rank_bm25 import BM25Okapi
from sentence_transformers import SentenceTransformer, CrossEncoder
from transformers import AutoModelForCausalLM, AutoTokenizer
from langchain.text_splitter import RecursiveCharacterTextSplitter

warnings.filterwarnings("ignore")


class DocumentLoader:
    """Load documents từ cấu trúc folder Public_XXX/main.md"""
    
    def __init__(self, root_folder: str):
        self.root_folder = Path(root_folder)
        self.encodings = ['utf-8', 'latin1', 'cp1252', 'utf-16']
    
    def load_all(self) -> Tuple[Dict[str, str], Dict[str, str]]:
        """
        Load tất cả documents từ folder
        
        Returns:
            (extracted_contents, file_id_mapping)
            extracted_contents: {full_path: content}
            file_id_mapping: {file_id: full_path}
        """
        if not self.root_folder.exists():
            raise FileNotFoundError(f"Folder không tồn tại: {self.root_folder}")
        
        extracted_contents = {}
        file_id_mapping = {}
        
        for folder in self.root_folder.iterdir():
            if not folder.is_dir():
                continue
            
            if not self._is_valid_folder(folder.name):
                continue
            
            content = self._read_document(folder)
            if content:
                file_id = self._extract_file_id(folder.name)
                file_path = str(folder / "main.md")
                extracted_contents[file_path] = content
                file_id_mapping[file_id] = file_path
        
        return extracted_contents, file_id_mapping
    
    def _is_valid_folder(self, folder_name: str) -> bool:
        """Kiểm tra folder có đúng format Public_XXX hoặc Private_XXX"""
        return bool(re.match(r'^(Public|Private)_\d+', folder_name, re.IGNORECASE))
    
    def _extract_file_id(self, folder_name: str) -> str:
        """Chuẩn hóa file_id: Public_001, Private_002"""
        match = re.search(r'(Public|Private)_(\d+)', folder_name, re.IGNORECASE)
        if match:
            prefix = match.group(1).capitalize()
            number = match.group(2)
            return f"{prefix}_{number}"
        return folder_name
    
    def _read_document(self, folder: Path) -> Optional[str]:
        """Đọc nội dung file main.md với fallback encoding"""
        main_md = folder / "main.md"
        
        if not main_md.exists():
            return None
        
        for encoding in self.encodings:
            try:
                return main_md.read_text(encoding=encoding)
            except UnicodeDecodeError:
                continue
        
        # Fallback cuối cùng: ignore errors
        return main_md.read_text(encoding='utf-8', errors='ignore')


def auto_generate_data(root_folder: str, device: str = None) -> Tuple[Dict[str, str], Dict[str, str]]:
    loader = DocumentLoader(root_folder)
    raw_contents, file_mapping = loader.load_all()
    
    extracted_contents = {}
    
    for file_id, file_path in file_mapping.items():
        content = raw_contents[file_path]
        output_key = f"{file_id}.md"
        extracted_contents[output_key] = content
    
    # Trả về dict rỗng cho document_types để tương thích
    return extracted_contents

@dataclass
class ChunkMetadata:
    """Metadata for each chunk"""
    file_id: str
    file_path: str
    global_idx: int
    chunk_idx_in_file: int
    heading_level: int
    heading_text: str
    parent_headings: List[str]
    content_type: str  # 'heading', 'content', 'nested', 'child_content', 'parent_chunk'
    section_type: Optional[str] = None

@dataclass
class SearchResult:
    """Search result with rich metadata"""
    chunk: str
    score: float
    file_id: str
    chunk_idx: int
    heading_level: int
    heading_text: str
    parent_headings: List[str]
    search_mode: str
    retrieval_score: float
    rerank_score: float
    section_type: Optional[str] = None

@dataclass
class DocumentNode:
    """Class to store parent-child chunk relationship"""
    parent_chunk: str
    parent_metadata: ChunkMetadata
    child_chunks: List[str]
    child_metadata: List[ChunkMetadata]

import re
import json
import torch
from typing import List
from transformers import AutoTokenizer, AutoModelForCausalLM

class LLMQueryExpander:
    def __init__(self, model_path: str = "Qwen/Qwen2.5-3B-Instruct"):
        print(f"Khởi tạo LLM Query Expander với model: {model_path}")
        self.tokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True)
        self.model = AutoModelForCausalLM.from_pretrained(
            model_path,
            torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32,
            device_map="cuda",
            trust_remote_code=True,
            low_cpu_mem_usage=True
        )
        self.model.eval()
        
        self.expansion_patterns = {
            'là gì': ['nghĩa là gì', 'định nghĩa', 'khái niệm', 'giải thích'],
            'là bao nhiêu': ['bằng bao nhiêu', 'giá trị', 'cụ thể là'],
            'như thế nào': ['ra sao', 'thế nào', 'cách nào'],
            'có độ phức tạp': ['độ phức tạp thuật toán', 'phức tạp thời gian'],
            'cách': ['làm thế nào để', 'phương pháp', 'hướng dẫn']
        }
    
    def expand_query(self, query: str, max_expansions: int = 2) -> List[str]:
        try:
            llm_variants = self._llm_expand(query, max_expansions)
            
            if llm_variants:
                final_results = [query] if query not in llm_variants else []
                final_results.extend([v for v in llm_variants if v != query])
                return final_results[:max_expansions + 1]
            
            rule_variants = self._rule_based_expand(query, max_expansions)
            final_results = [query]
            final_results.extend([v for v in rule_variants if v != query])
            return final_results[:max_expansions + 1]
            
        except Exception:
            return [query]
    
    def _llm_expand(self, query: str, max_expansions: int) -> List[str]:
        try:
            prompt = f"""Bạn là trợ lý NLP chuyên viết lại câu hỏi để cải thiện tìm kiếm.

NHIỆM VỤ:
- Từ câu hỏi đầu vào (gọi là "câu gốc"), hãy viết lại CHÍNH XÁC {max_expansions} phiên bản khác nhau nhưng GIỮ NGUYÊN Ý NGHĨA.
- Chỉ sử dụng TIẾNG VIỆT THUẦN (không pha ngôn ngữ khác, không phiên âm, không ký hiệu lạ/emoji).

BẢO TOÀN NGHIĨA & CHỦ THỂ (INVARIANTS) — BẮT BUỘC:
1) GIỮ NGUYÊN CHỦ THỂ/TRỌNG TÂM của câu gốc (người/vật/thực thể/chủ đề chính). Không thay thế, không đổi hướng.
2) GIỮ NGUYÊN CÁC THỰC THỂ ĐẶC THÙ: tên riêng (người/tổ chức/thuật toán/mẫu/phiên bản/ký hiệu), chính tả và hoa-thường.
3) GIỮ CÁC RÀNG BUỘC NGỮ CẢNH: thời gian (năm/tháng/ngày), miền/phạm vi, đơn vị đo (Hz, MHz, ms, %, kg, km…), điều kiện/giới hạn (≤, ≥, >, <), ngôn ngữ/khung (ví dụ: “trong Python”, “trên Windows”, “ở Việt Nam”).
4) GIỮ CỰC TÍNH/PHỦ ĐỊNH: không đổi khẳng định ↔ phủ định, so sánh ↔ không so sánh.
5) KHÔNG thêm/bỏ thực thể, con số, đơn vị, điều kiện; KHÔNG khái quát hoá hay cụ thể hoá hơn câu gốc.
6) KHÔNG đổi loại câu hỏi và lưu ý đầu ra luôn là câu hỏi tuyệt đối không tra lời nó(định nghĩa ↔ so sánh ↔ giải thích ↔ cách làm…); giữ mục đích hỏi giống nhau.

ĐA DẠNG DIỄN ĐẠT:
- Đa dạng cấu trúc/cụm từ, nhưng không đổi nội dung cốt lõi.
- Dùng từ phổ thông, rõ ràng; giữ dạng câu hỏi (dấu “?” khi phù hợp).
- Mỗi biến thể 3–20 từ, ≤150 ký tự, không xuống dòng, không markdown/HTML.

CẤM TUYỆT ĐỐI:
- Không in ra lời giải thích, tiêu đề, chú thích, “ví dụ”, “candidates”, “explanation”, thẻ như <think>, hoặc khối ```…```.
- Không trả về placeholder (A1, B2, …), không viết “dan” thay “và”, không chèn tiếng Anh/Trung hay ký tự điều khiển.
- Không lặp lại gần như y hệt; mỗi biến thể phải có khác biệt ngôn ngữ hữu ích cho tìm kiếm.

ĐẦU RA DUY NHẤT HỢP LỆ:
- CHỈ một JSON array gồm CHÍNH XÁC {max_expansions} chuỗi tiếng Việt.
- Không được in kèm bất cứ ký tự nào ngoài JSON.

QUY TRÌNH (thực hiện nội bộ, KHÔNG in ra):
1) Trích xuất các bất biến: chủ thể chính; tên riêng/thuật ngữ; ràng buộc thời gian/phạm vi/đơn vị/điều kiện; cực tính; loại câu hỏi.
2) Sinh nhiều bản nháp diễn đạt khác nhau.
3) TỰ KIỂM (self-check) từng biến thể: có giữ đủ bất biến không? có thêm/bớt gì không? tiếng Việt thuần? độ dài hợp lệ? kết thúc bằng “?” khi cần?
4) Loại bản vi phạm; khử trùng lặp; nếu thiếu số lượng, sinh bổ sung rồi kiểm tra lại.

CÂU GỐC:
"{query}"

HÃY TRẢ VỀ NGAY MỘT JSON ARRAY CHỨA CHÍNH XÁC {max_expansions} CHUỖI TIẾNG VIỆT, KHÔNG THÊM GÌ KHÁC.
Ví dụ định dạng (chỉ là minh hoạ về cấu trúc, KHÔNG dùng nội dung sau):
["biến thể 1", "biến thể 2"]
"""
            
            messages = [{"role": "user", "content": prompt}]
            text = self.tokenizer.apply_chat_template(
                messages,
                tokenize=False,
                add_generation_prompt=True
            )
            inputs = self.tokenizer([text], return_tensors="pt").to(self.model.device)
            
            with torch.no_grad():
                outputs = self.model.generate(
                    **inputs,
                    max_new_tokens=526,
                    temperature=0.3,
                    top_p=0.75,
                    do_sample=True,
                    pad_token_id=self.tokenizer.eos_token_id,
                    repetition_penalty=1.2
                )
            
            response = self.tokenizer.decode(
                outputs[0][inputs.input_ids.shape[1]:],
                skip_special_tokens=True
            ).strip()
            
            variants = self._parse_json_response(response, query, max_expansions)
            vietnamese_variants = [v for v in variants if self._is_vietnamese(v)]
            
            return vietnamese_variants
            
        except Exception:
            return []
    
    def _is_vietnamese(self, text: str) -> bool:
        if not text or len(text) < 3:
            return False
        
        if re.search(r'[\u4e00-\u9fff\u3400-\u4dbf]', text):
            return False
        
        vietnamese_chars = r'[àáảãạăằắẳẵặâầấẩẫậèéẻẽẹêềếểễệìíỉĩịòóỏõọôồốổỗộơờớởỡợùúủũụưừứửữựỳýỷỹỵđ]'
        has_vietnamese_chars = bool(re.search(vietnamese_chars, text.lower()))
        
        vietnamese_keywords = [
            'là', 'của', 'và', 'có', 'trong', 'được', 'cho', 'với', 'để',
            'thuật toán', 'độ phức tạp', 'cách', 'phương pháp', 'gì', 'nào',
            'như thế nào', 'bao nhiêu', 'thế nào'
        ]
        has_vietnamese_words = any(keyword in text.lower() for keyword in vietnamese_keywords)
        
        english_keywords = [
            'how to', 'what is', 'steps for', 'method for', 'algorithm',
            'the', 'a ', 'an ', 'is ', 'are ', 'for ', 'of '
        ]
        has_english_keywords = any(keyword in text.lower() for keyword in english_keywords)
        
        if has_english_keywords and not has_vietnamese_chars:
            return False
        
        return has_vietnamese_chars or has_vietnamese_words
    
    def _parse_json_response(self, response: str, original_query: str, expected_count: int) -> List[str]:
        response = re.sub(r'</?think>.*?(?=\n|$)', '', response, flags=re.DOTALL).strip()
        
        try:
            data = json.loads(response)
            if isinstance(data, list):
                variants = [str(item).strip() for item in data if isinstance(item, str)]
                variants = [v for v in variants if 8 <= len(v) <= 150 and v != original_query]
                return variants[:expected_count]
        except json.JSONDecodeError:
            pass
        
        json_match = re.search(r'\[([^\[\]]+)\]', response)
        if json_match:
            try:
                json_str = json_match.group(0)
                data = json.loads(json_str)
                if isinstance(data, list):
                    variants = [str(item).strip() for item in data if isinstance(item, str)]
                    variants = [v for v in variants if 8 <= len(v) <= 150 and v != original_query]
                    return variants[:expected_count]
            except json.JSONDecodeError:
                pass
        
        return self._extract_variants_freetext(response, original_query, expected_count)
    
    def _extract_variants_freetext(self, response: str, original_query: str, max_variants: int) -> List[str]:
        if not response or len(response) < 5:
            return []
        
        noise_patterns = [
            r'^(Đây là|Dưới đây là|Tôi đã viết|Có thể viết lại|Các cách viết).*?:\s*',
            r'(Hay còn nói cách khác|Nhớ rằng|Lưu ý|Chú ý).*$',
        ]
        
        cleaned_response = response
        for pattern in noise_patterns:
            cleaned_response = re.sub(pattern, '', cleaned_response, flags=re.IGNORECASE | re.MULTILINE)
        
        lines = cleaned_response.split('\n')
        variants = []
        
        for line in lines:
            line = line.strip()
            if not line or len(line) < 8:
                continue
            
            cleaned = re.sub(r'^(Cách\s*\d+[\:\.\)]?\s*|[\d]+[\.\)\:]\s*|[-•*]\s*)', '', line, flags=re.IGNORECASE)
            cleaned = cleaned.strip(' "\'')
            
            if 8 <= len(cleaned) <= 150:
                if not re.search(r'(là\s+O\(|bằng\s+\d|độ phức tạp.*(là|bằng)\s+\w+\()', cleaned):
                    if cleaned != original_query and cleaned not in variants:
                        variants.append(cleaned)
            
            if len(variants) >= max_variants:
                break
        
        return variants
    
    def _rule_based_expand(self, query: str, max_expansions: int) -> List[str]:
        variants = []
        query_lower = query.lower()
        
        for pattern, replacements in self.expansion_patterns.items():
            if pattern in query_lower:
                for replacement in replacements[:max_expansions]:
                    variant = re.sub(
                        re.escape(pattern),
                        replacement,
                        query,
                        count=1,
                        flags=re.IGNORECASE
                    )
                    if variant != query and variant not in variants:
                        variants.append(variant)
                    
                    if len(variants) >= max_expansions:
                        break
                break
        
        if not variants:
            synonyms = {
                'thuật toán': 'algorithm',
                'độ phức tạp': 'complexity',
                'cách': 'phương pháp',
                'là gì': 'nghĩa là gì'
            }
            
            for original, synonym in synonyms.items():
                if original in query_lower:
                    variant = re.sub(
                        re.escape(original),
                        synonym,
                        query,
                        count=1,
                        flags=re.IGNORECASE
                    )
                    if variant != query:
                        variants.append(variant)
                        break
        
        return variants[:max_expansions]


class HierarchicalChunker:
    """
    Smart chunking that respects hierarchical heading structure
    Strategy:
    - H1 (title): Skip or use as document title
    - H2 (section): Create chunks per section
    - H3 (subsection): Group content under subsection
    - Content: Chunk by size but keep heading context
    - Special handling for tables, formulas, and long text
    """
    def __init__(self, 
                 parent_chunk_size: int = 1024,  # Kích thước chunk cha
                 child_chunk_size: int = 256,    # Kích thước chunk con
                 overlap_size: int = 50,         # Overlap cho chunk con
                 min_chunk_size: int = 50):
        self.parent_chunk_size = parent_chunk_size
        self.child_chunk_size = child_chunk_size
        self.overlap_size = overlap_size
        self.min_chunk_size = min_chunk_size
        self.heading_pattern = re.compile(r'^(#{1,6})\s+(.+)$', re.MULTILINE)
        self.list_pattern = re.compile(r'^[ \s]*[-*+]\s+', re.MULTILINE)
        # Khởi tạo text splitter cho child chunks
        self.child_splitter = RecursiveCharacterTextSplitter(
            chunk_size=self.child_chunk_size,
            chunk_overlap=self.overlap_size,
            separators=["\n\n", "\n", " ", ""]
        )
    
    def _extract_tables(self, text: str) -> List[str]:
        """
        Trích xuất các bảng từ văn bản HTML/Markdown
        Giữ nguyên vẹn từng bảng để tránh chia cắt không hợp lý
        """
        tables = []
        # Pattern 1: Bảng HTML (<table>...</table>)
        table_pattern = r'<table[^>]*>.*?</table>'
        html_tables = re.findall(table_pattern, text, re.DOTALL | re.IGNORECASE)
        tables.extend(html_tables)
        # Pattern 2: Bảng Markdown (|-|-| và |-|-|-|)
        markdown_pattern = r'(\|[^\\n]+\|[^\\n]*\n(\|[^\\n]+\|[^\\n]*\n)+)'
        markdown_tables = re.findall(markdown_pattern, text)
        for match in markdown_tables:
            if isinstance(match, tuple):
                tables.append(match[0])
            else:
                tables.append(match)
        # Pattern 3: Bảng được định dạng bằng dấu gạch ngang và dấu pipe
        ascii_pattern = r'((?:.*?\|.*?\n){2,}(?:-+\|[-+\s]+\n)(?:.*?\|.*?\n)+)'
        ascii_tables = re.findall(ascii_pattern, text)
        tables.extend(ascii_tables)
        # Loại bỏ các bảng trùng lặp
        unique_tables = []
        for table in tables:
            if table not in unique_tables:
                unique_tables.append(table)
        return unique_tables
    
    def _chunk_section_content(self, 
                              content: str, 
                              section_header: str,
                              section_type: str,
                              context_prefix: str,
                              file_id: str,
                              base_size: int,
                              overlap: int) -> List[Tuple[str, ChunkMetadata]]:
        """Chunk nội dung của một section với kích thước lớn hơn"""
        lines = content.split('\n')
        chunks = []
        current_chunk = []
        current_size = 0
        chunk_counter = 0
        
        # Các mẫu để xác định điểm phân chia tự nhiên
        natural_break_patterns = [
            r'^\s*[-•*]\s',           # Danh sách
            r'^\d+\.\s',              # Danh sách đánh số
            r'^\s*[A-Z][a-z]+\s*:\s', # Định nghĩa
            r'\.\s*$',                # Cuối câu
        ]
        
        for line in lines:
            stripped = line.strip()
            if not stripped:
                continue
            
            words = stripped.split()
            current_chunk.append(line)
            current_size += len(words)
            
            # Điểm phân chia tự nhiên
            is_natural_break = (
                (current_size >= base_size and 
                 any(re.search(pattern, line) for pattern in natural_break_patterns)) or
                (current_size >= base_size * 1.2)  # Giới hạn cứng
            )
            
            if is_natural_break:
                chunk_text = '\n'.join(current_chunk)
                meta = ChunkMetadata(
                    file_id=file_id,
                    file_path=f"chunk_{chunk_counter}",
                    global_idx=-1,
                    chunk_idx_in_file=chunk_counter,
                    heading_level=len(section_header.split('#')) if section_header.startswith('#') else 2,
                    heading_text=section_header,
                    parent_headings=[section_header],
                    content_type='content',
                    section_type=section_type,
                )
                chunks.append((context_prefix + chunk_text, meta))
                chunk_counter += 1
                
                # Keep overlap - giữ lại phần cuối để context
                overlap_lines = current_chunk[-(overlap // 8):]
                current_chunk = overlap_lines
                current_size = sum(len(l.split()) for l in overlap_lines)
        
        # Last chunk
        if current_chunk:
            chunk_text = '\n'.join(current_chunk)
            meta = ChunkMetadata(
                file_id=file_id,
                file_path=f"chunk_{chunk_counter}",
                global_idx=-1,
                chunk_idx_in_file=chunk_counter,
                heading_level=len(section_header.split('#')) if section_header.startswith('#') else 2,
                heading_text=section_header,
                parent_headings=[section_header],
                content_type='content',
                section_type=section_type,
            )
            chunks.append((context_prefix + chunk_text, meta))
        
        return chunks
    
    def _split_by_structure(self, text: str, struct_info: Dict[str, Any]) -> List[Dict]:
        """
        Chia văn bản thành các phần dựa trên cấu trúc tài liệu
        """
        sections = []
        

        section_pattern = r'(?:#\s+(.*?)(?:\n|$))|(?:##\s+(.*?)(?:\n|$))|(?:###\s+(.*?)(?:\n|$))'
        
        # Tìm các section trong văn bản
        current_section = {
            'header': 'Introduction',
            'content': '',
            'type': 'introduction'
        }
        
        lines = text.split('\n')
        in_section = False
        current_header = ''
        
        for line in lines:
            header_match = re.match(r'^(#{1,3})\s+(.+)$', line.strip())
            if header_match:
                # Lưu section hiện tại nếu có nội dung
                if current_section['content'].strip():
                    sections.append(current_section.copy())
                
                # Bắt đầu section mới
                level = len(header_match.group(1))
                header_text = header_match.group(2)
                current_header = header_text
                
                section_type = 'main_section' if level == 1 else 'subsection'
                if 'bảng' in header_text.lower() or 'table' in header_text.lower():
                    section_type = 'table_section'
                elif 'công thức' in header_text.lower() or 'formula' in header_text.lower():
                    section_type = 'formula_section'
                
                current_section = {
                    'header': header_text,
                    'content': '',
                    'type': section_type
                }
                in_section = True
            else:
                if in_section:
                    current_section['content'] += line + '\n'
                else:
                    current_section['content'] += line + '\n'
        
        # Thêm section cuối cùng
        if current_section['content'].strip():
            sections.append(current_section)
        
        return sections
    
    def _generate_document_summary(self, content: str) -> str:
        """
        Generate robust document summary based on structure and content patterns
        
        Strategy:
        1. Identify first substantial paragraph after structural elements
        2. Skip headings, lists, tables, and technical artifacts
        3. Extract meaningful sentences with proper truncation
        4. Multiple fallbacks for different document structures
        """
        # Chuẩn bị lines và loại bỏ dòng trống
        lines = [line.strip() for line in content.split('\n') if line.strip()]
        
        # Các mẫu cấu trúc cần bỏ qua
        structural_patterns = [
            r'^#{1,6}\s',       # Markdown headings (# đến ######)
            r'^[-*+]\s',        # Danh sách bullet
            r'^\d+\.\s',        # Danh sách đánh số
            r'^\|',             # Bảng Markdown
            r'^```',            # Code blocks
            r'^<table',         # Bảng HTML
            r'^<div',           # HTML containers
            r'^>',              # Blockquotes
            r'^!\[',            # Hình ảnh
            r'^\[',             # Liên kết/tham chiếu
            r'^[\*\_]{3,}',     # Đường phân cách
            r'^\s*$',           # Dòng trống
        ]
        
        # Bước 1: Tìm đoạn văn bản thực sự đầu tiên
        main_content = []
        capture_started = False
        
        for line in lines:
            # Kiểm tra xem dòng có phải là phần cấu trúc không
            is_structural = any(re.match(pattern, line, re.IGNORECASE) for pattern in structural_patterns)
            
            # Bắt đầu capture khi gặp dòng nội dung thực sự đầu tiên
            if not capture_started and not is_structural and len(line.split()) >= 8:
                capture_started = True
            
            # Thu thập nội dung sau khi bắt đầu capture
            if capture_started and not is_structural:
                # Bỏ qua các dòng quá ngắn hoặc có tính chất metadata
                if len(line.split()) >= 5 and not re.match(r'^(Ngày|Date|Version|Tác giả|Author):', line, re.IGNORECASE):
                    main_content.append(line)
            
            # Dừng khi đã có đủ nội dung
            if len(main_content) >= 4 or (main_content and len(' '.join(main_content)) > 400):
                break
        
        # Bước 2: Xử lý và tạo tóm tắt từ nội dung thu thập được
        if main_content:
            text = ' '.join(main_content)
            
            # Tách thành các câu và lấy 1-2 câu đầu tiên
            sentences = re.split(r'(?<=[.!?])\s+', text.strip())
            meaningful_sentences = []
            
            for sent in sentences:
                # Lọc các câu có ý nghĩa (tránh câu quá ngắn hoặc fragment)
                if len(sent.split()) >= 6 and not re.match(r'^\W*$', sent):
                    meaningful_sentences.append(sent.strip())
                if len(meaningful_sentences) >= 2:
                    break
            
            if meaningful_sentences:
                summary = ' '.join(meaningful_sentences[:2])
                
                # Cắt gọn ở ranh giới câu nếu quá dài
                if len(summary) > 350:
                    # Tìm điểm kết thúc câu gần nhất trước vị trí 300
                    safe_point = max(
                        summary[:300].rfind('.'),
                        summary[:300].rfind('!'),
                        summary[:300].rfind('?')
                    )
                    if safe_point > 100:  # Đảm bảo phần tóm tắt có ý nghĩa
                        summary = summary[:safe_point+1] + '...'
                    else:
                        summary = summary[:300] + '...'
                return summary.strip()
        
        # Fallback 1: Lấy 2-3 dòng đầu tiên không phải cấu trúc
        fallback_lines = []
        for line in lines:
            if not any(re.match(pattern, line, re.IGNORECASE) for pattern in structural_patterns):
                if len(line.split()) >= 4 and not re.match(r'^(File|Document|ID):', line, re.IGNORECASE):
                    fallback_lines.append(line)
            if len(fallback_lines) >= 3:
                break
        
        if fallback_lines:
            summary = ' '.join(fallback_lines[:2])
            return summary[:350] + '...' if len(summary) > 350 else summary
        
        # Fallback 2: Sử dụng metadata hoặc mô tả mặc định
        return "Tài liệu kỹ thuật không có phần giới thiệu rõ ràng. Vui lòng tham khảo các section cụ thể để tìm thông tin chi tiết."
        
    def chunk_document_to_nodes(self, 
                               text: str, 
                               file_id: str,
                               struct_info: Optional[Dict[str, Any]] = None) -> List[DocumentNode]:
        """
        Tạo ra các node tài liệu, mỗi node chứa chunk cha và các chunk con.
        Strategy Small-to-Large:
        - Chunk cha (parent): 1024 tokens - để trả về làm context
        - Chunk con (child): 256 tokens - để tìm kiếm
        """

        
        doc_summary = self._generate_document_summary(text)  # Dùng hàm mới
        
        # Prefix context cho tất cả chunk
        file_context = f"[TÀI LIỆU: {file_id}] "
        
        nodes = []
        global_parent_idx = 0
        global_child_idx = 0
        
        # Bước 1: Xử lý bảng trước - giữ nguyên vẹn từng bảng
        tables = self._extract_tables(text)
        for i, table in enumerate(tables):
            if len(table) > 50:  # Chỉ xử lý bảng có nội dung đáng kể
                # Tạo parent chunk cho bảng (nguyên vẹn)
                parent_meta = ChunkMetadata(
                    file_id=file_id,
                    file_path=f"table_{i}",
                    global_idx=global_parent_idx,
                    chunk_idx_in_file=i,
                    heading_level=3,
                    heading_text=f"Bảng {i+1}",
                    parent_headings=[],
                    content_type='parent_chunk',
                    section_type='table_data',
                )
                parent_chunk = file_context + f"[BẢNG {i+1}] {table}"
                
                # Chia bảng thành các child chunks nhỏ hơn nếu cần
                child_chunks = self.child_splitter.split_text(parent_chunk)
                child_metadata = []
                
                for j, child_text in enumerate(child_chunks):
                    child_meta = ChunkMetadata(
                        file_id=file_id,
                        file_path=f"table_{i}_child_{j}",
                        global_idx=global_child_idx,
                        chunk_idx_in_file=j,
                        heading_level=3,
                        heading_text=f"Bảng {i+1} - Phần {j+1}",
                        parent_headings=[f"Bảng {i+1}"],
                        content_type='child_content',
                        section_type='table_data',
                    )
                    child_metadata.append(child_meta)
                    global_child_idx += 1
                
                # Tạo node và thêm vào danh sách
                node = DocumentNode(
                    parent_chunk=parent_chunk,
                    parent_metadata=parent_meta,
                    child_chunks=child_chunks,
                    child_metadata=child_metadata
                )
                nodes.append(node)
                global_parent_idx += 1
        
        
        # Bước 3: Chia text thành các phần lớn dựa trên cấu trúc
        sections = self._split_by_structure(text, struct_info)
        
        # Bước 4: Tạo parent và child chunks cho từng section
        for section in sections:
            section_header = section['header']
            section_content = section['content']
            section_type = section['type']
            
            # Tạo context string cho section
            section_context = f"[PHẦN: {section_header}] [LOẠI: {section_type}] "
            
            # Tạo parent chunk từ toàn bộ section
            parent_content = section_context + section_content
            parent_chunk = file_context + parent_content
            
            parent_meta = ChunkMetadata(
                file_id=file_id,
                file_path=f"section_{global_parent_idx}",
                global_idx=global_parent_idx,
                chunk_idx_in_file=global_parent_idx,
                heading_level=len(section_header.split('#')) if section_header.startswith('#') else 2,
                heading_text=section_header,
                parent_headings=[section_header],
                content_type='parent_chunk',
                section_type=section_type,
            )
            
            # Chia thành các child chunks
            child_chunks = self.child_splitter.split_text(parent_chunk)
            child_metadata = []
            
            for j, child_text in enumerate(child_chunks):
                child_meta = ChunkMetadata(
                    file_id=file_id,
                    file_path=f"section_{global_parent_idx}_child_{j}",
                    global_idx=global_child_idx,
                    chunk_idx_in_file=j,
                    heading_level=len(section_header.split('#')) if section_header.startswith('#') else 2,
                    heading_text=f"{section_header} - Phần {j+1}",
                    parent_headings=[section_header],
                    content_type='child_content',
                    section_type=section_type,
                )
                child_metadata.append(child_meta)
                global_child_idx += 1
            
            node = DocumentNode(
                parent_chunk=parent_chunk,
                parent_metadata=parent_meta,
                child_chunks=child_chunks,
                child_metadata=child_metadata
            )
            nodes.append(node)
            global_parent_idx += 1
        
        return nodes

class AdvancedRAGSystem:
    """
    Advanced RAG system with:
    - Parent Document Retriever (Small-to-Large strategy)
    - Optimized reranking logic (prioritizing cross-encoder scores)
    - LLM-based query expansion
    - Hierarchical document chunking with table handling
    - Adaptive retrieval strategies
    - Document type aware processing
    - Integration with LLM for QA
    """
    def __init__(self, 
                 extracted_contents: Dict[str, str],
                 embedding_model: str = "AITeamVN/Vietnamese_Embedding_v2",
                 reranker_model: str = "namdp-ptit/ViRanker",
                 llm_model_path: str = "Qwen/Qwen2.5-3B-Instruct",
                 embedding_dim: int = 728,
                 device: str = "cuda" if torch.cuda.is_available() else "cpu"):
        """
        Initialize Advanced RAG System
        Args:
            extracted_contents: {file_path: markdown_content}
            embedding_model: Qwen model to use
            reranker_model: Cross-encoder for reranking
            llm_model_path: Path to LLM model for query expansion and QA
            embedding_dim: Output dimension for embeddings
            device: 'cuda' or 'cpu'
        """
        self.device = device
        self.embedding_dim = embedding_dim
        self.ready = False
        
        print("\n" + "="*100)
        print("INITIALIZING ADVANCED RAG SYSTEM WITH PARENT DOCUMENT RETRIEVER")
        print("="*100)
        
        if not extracted_contents:
            print("❌ No documents provided")
            return
        
        # Initialize query expander
        print(f"\n[0/6] Loading LLM Query Expander...")
        self.query_expander = LLMQueryExpander(model_path=llm_model_path)
        print("  ✓ LLM Query Expander ready")
        
        print(f"\n[1/6] Loading embedding model: {embedding_model}")
        self.embedding_model = SentenceTransformer(embedding_model, device=device)
        print(f"  ✓ Loaded on device: {device}")
        
        print(f"\n[2/6] Processing documents with hierarchical chunking (Parent-Child strategy)...")
        self._process_documents_hierarchically(extracted_contents)
        
        print(f"\n[3/6] Building dense index (FAISS) for child chunks...")
        self._build_dense_index()
        
        print(f"\n[4/6] Building sparse index (BM25) for child chunks...")
        self._build_sparse_index()
        
        print(f"\n[5/6] Loading reranker: {reranker_model}")
        self.reranker = CrossEncoder(reranker_model, device=device)
        print(f"  ✓ Reranker ready")
        
        print(f"\n[6/6] System ready for queries")
        self.ready = True
        self._print_stats()
    
    def _extract_file_id(self, file_path: str) -> str:
        """Extract file ID from path (Public_XXX, Private_XXX, etc)"""
        match = re.search(r'(Public_\d+|Private_\d+)', file_path, re.IGNORECASE)
        if match:
            return match.group(1)
        # Fallback: use folder name
        parts = file_path.replace('\\', '/').split('/')
        if len(parts) >= 2:
            return parts[-2]
        return file_path.split('/')[-1].replace('.md', '')
    
    
    def _process_documents_hierarchically(self, extracted_contents: Dict[str, str]):
        """Process documents into parent-child chunk hierarchy"""
        # Structures for parent-child relationship
        self.parent_chunks_store = {}  # parent_idx -> parent_chunk_text
        self.parent_metadata_store = {}  # parent_idx -> parent_metadata
        self.child_to_parent_map = {}  # child_global_idx -> parent_idx
        self.child_chunks = []  # List of all child chunks for indexing
        self.child_metadata_list = []  # Metadata for each child chunk
        
        self.file_id_to_chunks = defaultdict(list)  # file_id -> list of child indices
        self.file_metadata = {}  # file_id -> metadata
        
        chunker = HierarchicalChunker(
            parent_chunk_size=768,  # Kích thước chunk cha
            child_chunk_size=256,    # Kích thước chunk con
            overlap_size=64,         # Overlap cho chunk con
            min_chunk_size=64
        )
        
        global_parent_idx_counter = 0
        
        for file_path, content in extracted_contents.items():
            if not content or not content.strip():
                continue
            
            file_id = self._extract_file_id(file_path)            
            # Prepare structure info for smart chunking
            struct_info = {
                'metadata': {
                    'document_summary': self._generate_document_summary(content)
                }
            }
            
            # Chunk with hierarchical awareness and structure handling
            document_nodes = chunker.chunk_document_to_nodes(content, file_id, struct_info)
            
            file_child_indices = []
            
            # Process each document node (parent-child relationship)
            for node in document_nodes:
                parent_idx = global_parent_idx_counter
                
                # Store parent chunk and metadata
                self.parent_chunks_store[parent_idx] = node.parent_chunk
                self.parent_metadata_store[parent_idx] = node.parent_metadata
                
                # Process child chunks
                for child_idx_in_node, (child_text, child_meta) in enumerate(zip(node.child_chunks, node.child_metadata)):
                    global_child_idx = len(self.child_chunks)
                    
                    # Set proper indices
                    child_meta.global_idx = global_child_idx
                    child_meta.chunk_idx_in_file = child_idx_in_node
                    
                    # Store child chunk and metadata
                    self.child_chunks.append(child_text)
                    self.child_metadata_list.append(child_meta)
                    
                    # Map child to parent
                    self.child_to_parent_map[global_child_idx] = parent_idx
                    
                    # Track file-specific chunks
                    file_child_indices.append(global_child_idx)
                
                global_parent_idx_counter += 1
            
            # Store file metadata
            self.file_id_to_chunks[file_id] = file_child_indices
            self.file_metadata[file_id] = {
                'path': file_path,
                'num_parents': len(document_nodes),
                'num_children': len(file_child_indices)
            }
        
        # Set chunks to child chunks for indexing
        self.chunks = self.child_chunks
        self.chunk_metadata_list = self.child_metadata_list
        
        print(f"  ✓ Processed {len(self.file_metadata)} files")
        print(f"  ✓ Total parent chunks: {len(self.parent_chunks_store)}")
        print(f"  ✓ Total child chunks (for indexing): {len(self.chunks)}")
        
        # Show distribution
        if self.file_metadata:
            parent_counts = [meta['num_parents'] for meta in self.file_metadata.values()]
            child_counts = [meta['num_children'] for meta in self.file_metadata.values()]
            
            print(f"  • Min parents/file: {min(parent_counts)}")
            print(f"  • Max parents/file: {max(parent_counts)}")
            print(f"  • Avg parents/file: {np.mean(parent_counts):.1f}")
            
            print(f"  • Min children/file: {min(child_counts)}")
            print(f"  • Max children/file: {max(child_counts)}")
            print(f"  • Avg children/file: {np.mean(child_counts):.1f}")
    
    def _generate_document_summary(self, content: str) -> str:
        """
        Tóm tắt thông minh không phụ thuộc document type:
        1. Lấy nội dung sau heading đầu tiên
        2. Giới hạn 2-3 câu đầu tiên
        3. Loại bỏ bảng/formula phức tạp
        """
        # Bước 1: Tách phần giới thiệu sau title
        lines = [line.strip() for line in content.split('\n') if line.strip()]
        
        # Bỏ qua các heading (#, ##) và metadata
        body_lines = []
        in_body = False
        
        for line in lines:
            if line.startswith('#'):
                continue
            if re.match(r'^\s*[-*]\s|^\d+\.', line):  # Danh sách
                continue
            if '|' in line and '-' in line:  # Bảng Markdown
                continue
            if line.startswith('<table') or line.startswith('</table'):  # HTML table
                continue
                
            if len(line.split()) > 5:  # Chỉ lấy dòng có nội dung thực
                body_lines.append(line)
            
            if len(body_lines) >= 5:  # Giới hạn 5 dòng đầu
                break
        
        # Bước 2: Ghép thành đoạn và xử lý
        summary = ' '.join(body_lines[:3])  # Chỉ lấy 3 dòng đầu
        
        # Xử lý độ dài
        summary = summary[:400]  # Giới hạn 400 ký tự
        if len(summary) > 380:
            summary = summary[:summary.rfind(' ', 0, 380)] + '...'
        
        # Fallback nếu không có nội dung
        if len(summary.strip()) < 20:
            return "Tài liệu kỹ thuật không có phần giới thiệu."
        
        return summary
    
    def _match_by_document_type(self, query: str) -> Optional[str]:
        """Match file dựa trên loại tài liệu được đề cập trong query"""
        return None
    
    def _build_dense_index(self):
        """Build FAISS index for dense retrieval (on child chunks)"""
        # Add instruction prefix for better Vietnamese understanding
        instruction = "Represent this passage for retrieval: "
        chunks_with_instruction = [instruction + chunk for chunk in self.chunks]
        
        print(f"  Encoding {len(chunks_with_instruction)} child chunks...")
        self.chunk_embeddings = self.embedding_model.encode(
            chunks_with_instruction,
            show_progress_bar=True,
            batch_size=32,
            normalize_embeddings=True,
            convert_to_numpy=True,
            device=self.device
        )
        print(f"  ✓ Embeddings shape: {self.chunk_embeddings.shape}")
        
        # Build FAISS index
        dimension = self.chunk_embeddings.shape[1]
        self.faiss_index = faiss.IndexFlatIP(dimension)
        self.faiss_index.add(self.chunk_embeddings.astype('float32'))
        print(f"  ✓ FAISS index: {self.faiss_index.ntotal} vectors, dim={dimension}")
    
    def _build_sparse_index(self):
        """Build BM25 index for keyword search (on child chunks)"""
        tokenized_chunks = [chunk.lower().split() for chunk in self.chunks]
        self.bm25 = BM25Okapi(tokenized_chunks)
        print(f"  ✓ BM25 index: {len(tokenized_chunks)} documents")
    
    def _detect_file_id_from_query(self, query: str) -> Optional[str]:
        """
        Detect file ID from query with TD651 → Public_651 mapping
        Only maps TD prefix to Public_ (not other prefixes)
        """
        query_lower = query.lower()
        
        # Strategy 1: Look for TD + numbers pattern (only TD maps to Public_)
        td_match = re.search(r'\btd\s*(\d+)\b', query_lower)
        if td_match:
            number = td_match.group(1)
            candidate_id = f"Public_{number}"
            if candidate_id in self.file_metadata:
                return candidate_id
        
        # Strategy 2: Look for explicit Public_XXX patterns
        public_match = re.search(r'\b(public[_\s]*\d+)\b', query_lower)
        if public_match:
            raw_id = public_match.group(1)
            # Normalize format to Public_XXX
            number = re.search(r'\d+', raw_id).group(0)
            candidate_id = f"Public_{number}"
            if candidate_id in self.file_metadata:
                return candidate_id
        
        return None

    def _expand_query(self, query: str, max_expansions: int = 2) -> List[str]:
        """
        Enhanced query expansion with LLM
        Falls back to rule-based expansion if LLM fails
        """
        # Try LLM-based expansion first
        expanded_queries = self.query_expander.expand_query(query, max_expansions=max_expansions)
        
        # Fallback to rule-based if LLM fails
        if len(expanded_queries) <= 1:
            return self._rule_based_query_expansion(query, max_expansions)
        
        return expanded_queries
    
    def _rule_based_query_expansion(self, query: str, max_expansions: int = 2) -> List[str]:
        """Fallback rule-based query expansion with Vietnamese synonyms"""
        expanded = [query]
        synonyms = {
            'bao nhiêu': ['số lượng', 'giá trị'],
            'là gì': ['định nghĩa', 'khái niệm', 'ý nghĩa'],
            'nào': ['những', 'các'],
            'khi nào': ['điều kiện', 'thời điểm'],
            'nguyên nhân': ['lý do', 'tại sao'],
            'phân loại': ['loại', 'nhóm'],
            'độ phức tạp': ['thời gian chạy', 'độ khó'],
            'bài toán': ['vấn đề', 'nhiệm vụ'],
            'phương pháp': ['cách thức', 'giải pháp'],
            'tối ưu': ['hiệu quả', 'cải tiến']
        }
        
        query_lower = query.lower()
        for term, syns in synonyms.items():
            if term in query_lower:
                for syn in syns[:1]:  # Only take first synonym
                    if len(expanded) < max_expansions + 1:
                        new_query = query_lower.replace(term, syn)
                        expanded.append(new_query)
        
        return expanded[:max_expansions + 1]
    
    # Hàm _get_adaptive_alpha - chỉ dựa trên query
    def _get_adaptive_alpha(self, query: str, file_id: Optional[str] = None) -> float:
        """Loại bỏ logic dựa trên document type"""
        query_lower = query.lower()
        keyword_patterns = ['năm', 'ngày', 'số', 'bao nhiêu', 'mã', 'giá trị', 'kích thước']
        if any(kw in query_lower for kw in keyword_patterns):
            return 0.3  # Ưu tiên BM25 cho truy vấn số
        
        semantic_patterns = ['là gì', 'định nghĩa', 'tại sao', 'như thế nào', 'giải thích']
        if any(kw in query_lower for kw in semantic_patterns):
            return 0.8  # Ưu tiên dense vector
        
        return 0.6  # Cân bằng
    
    def retrieve(self,
                 query: str,
                 top_k: int = 10,
                 rerank_candidates: int = 25,
                 use_instruction: bool = True,
                 alpha: Optional[float] = None,
                 verbose: bool = True) -> List[SearchResult]:
        """
        Retrieve relevant chunks using Parent Document Retriever strategy
        Enhanced with optimized reranking (prioritizing cross-encoder scores)
        """
        if not self.ready:
            return []
        
        start_time = time.time()
        
        # PHASE 1: Detect search mode
        target_file_id = self._detect_file_id_from_query(query)
        if target_file_id:
            search_indices = self.file_id_to_chunks[target_file_id]
            search_mode = "FILE-SPECIFIC"
            effective_top_k = min(top_k * 2, len(search_indices))
            effective_rerank = min(rerank_candidates * 2, len(search_indices))
        else:
            search_indices = list(range(len(self.chunks)))
            search_mode = "GLOBAL"
            effective_top_k = top_k
            effective_rerank = rerank_candidates
        
        if verbose:
            print(f"\n{'='*80}")
            print(f"🔍 RETRIEVAL: {search_mode} MODE")
            print(f"{'='*80}")
            if target_file_id:
                print(f"Target file: {target_file_id}")
                print(f"Search space: {len(search_indices)} child chunks")
            else:
                print(f"Search space: {len(search_indices)} child chunks (global)")
        
        # PHASE 2: Expand query using LLM
        queries = self._expand_query(query, max_expansions=2)
        if verbose and len(queries) > 1:
            print(f"Query expansions ({len(queries)}):")
            for i, q in enumerate(queries):
                print(f"  {i+1}. {q}")
        
        # PHASE 3: Hybrid retrieval (on child chunks)
        all_candidates = {}
        
        for q in queries:
            # Add instruction for consistency (Qwen3 uses last-token pooling)
            q_with_instruction = f"Represent this query for retrieval: {q}" if use_instruction else q
            
            # Dense search
            q_embedding = self.embedding_model.encode(
                [q_with_instruction],
                normalize_embeddings=True,
                convert_to_numpy=True,
                device=self.device
            )
            
            if search_mode == "FILE-SPECIFIC":
                dense_scores = []
                for idx in search_indices:
                    score = float(np.dot(q_embedding[0], self.chunk_embeddings[idx]))
                    dense_scores.append((idx, score))
                dense_scores.sort(key=lambda x: x[1], reverse=True)
                top_dense = dense_scores[:effective_top_k * 3]
            else:
                scores, indices = self.faiss_index.search(
                    q_embedding.astype('float32'),
                    effective_top_k * 3
                )
                top_dense = [(int(idx), float(score)) 
                             for idx, score in zip(indices[0], scores[0])]
            
            for idx, score in top_dense:
                if idx not in all_candidates:
                    all_candidates[idx] = {'dense': 0.0, 'bm25': 0.0}
                all_candidates[idx]['dense'] = max(all_candidates[idx]['dense'], score)
            
            # Sparse (BM25) search
            tokenized_q = q.lower().split()
            bm25_scores = self.bm25.get_scores(tokenized_q)
            
            if search_mode == "FILE-SPECIFIC":
                file_bm25 = [(idx, float(bm25_scores[idx])) for idx in search_indices]
                file_bm25.sort(key=lambda x: x[1], reverse=True)
                top_bm25 = file_bm25[:effective_top_k * 3]
            else:
                top_bm25_indices = np.argsort(bm25_scores)[-(effective_top_k * 3):][::-1]
                top_bm25 = [(int(idx), float(bm25_scores[idx])) for idx in top_bm25_indices]
            
            for idx, score in top_bm25:
                if idx not in all_candidates:
                    all_candidates[idx] = {'dense': 0.0, 'bm25': 0.0}
                all_candidates[idx]['bm25'] = max(all_candidates[idx]['bm25'], score)
        
        if not all_candidates:
            return []
        
        # PHASE 4: Score fusion
        max_dense = max((c['dense'] for c in all_candidates.values()), default=1.0)
        max_bm25 = max((c['bm25'] for c in all_candidates.values()), default=1.0)
        
        if max_dense > 0:
            for idx in all_candidates:
                all_candidates[idx]['dense'] /= max_dense
        
        if max_bm25 > 0:
            for idx in all_candidates:
                all_candidates[idx]['bm25'] /= max_bm25
        
        # Adaptive weighting
        if alpha is None:
            alpha = self._get_adaptive_alpha(query, target_file_id)
        
        combined = [
            (idx, alpha * scores['dense'] + (1 - alpha) * scores['bm25'])
            for idx, scores in all_candidates.items()
        ]
        combined.sort(key=lambda x: x[1], reverse=True)
        top_candidates = combined[:effective_rerank]
        
        if verbose:
            print(f"Candidates after fusion: {len(top_candidates)}")
            print(f"Dense/Sparse weight: {alpha:.2f}/{1-alpha:.2f}")
        
        # PHASE 5: Reranking - CẢI TIẾN QUAN TRỌNG: ƯU TIÊN ĐIỂM CỦA RERANKER
        if not top_candidates:
            return []
        
        pairs = [[query, self.chunks[idx]] for idx, _ in top_candidates]
        rerank_scores = self.reranker.predict(pairs, batch_size=32)
        
        # Gắn điểm rerank vào các ứng viên ban đầu
        reranked_candidates = [
            (top_candidates[i][0], rerank_scores[i])  
            for i in range(len(top_candidates))
        ]
        
        # Sắp xếp lại danh sách ứng viên chỉ dựa trên rerank_score
        reranked_candidates.sort(key=lambda x: x[1], reverse=True)
        # =============================================================
        
        if verbose:
            print(f"Reranked candidates: {len(reranked_candidates)} (sorted by reranker score only)")
        
        # PHASE 6: Parent Chunk Expansion
        final_parent_chunks = {}  # parent_idx -> {chunk, max_score, metadata}
        seen_hashes = set()
        
        for child_idx, score in reranked_candidates:
            # Lấy parent index từ map
            parent_idx = self.child_to_parent_map.get(child_idx)
            
            if parent_idx is not None and parent_idx in self.parent_chunks_store:
                # Tạo hash để kiểm tra trùng lặp
                parent_hash = hash(self.parent_chunks_store[parent_idx][:200])
                
                if parent_hash not in seen_hashes:
                    seen_hashes.add(parent_hash)
                    
                    # Lấy metadata của parent
                    parent_meta = self.parent_metadata_store[parent_idx]
                    
                    # Lưu trữ parent chunk với điểm số cao nhất
                    if parent_idx not in final_parent_chunks or score > final_parent_chunks[parent_idx]["score"]:
                        final_parent_chunks[parent_idx] = {
                            "chunk": self.parent_chunks_store[parent_idx],
                            "score": score,
                            "metadata": parent_meta
                        }
            
            # Dừng khi đã đủ số lượng kết quả
            if len(final_parent_chunks) >= top_k:
                break
        
        if verbose:
            print(f"Unique parent chunks after expansion: {len(final_parent_chunks)}")
        
        # Format kết quả cuối cùng
        results = []
        sorted_parents = sorted(final_parent_chunks.items(), key=lambda x: x[1]["score"], reverse=True)
        
        for parent_idx, parent_data in sorted_parents[:top_k]:
            meta = parent_data["metadata"]
            
            # Truy xuất điểm retrieval gốc của child chunks tương ứng
            retrieval_score = 0.0
            for child_idx, score in top_candidates:
                if self.child_to_parent_map.get(child_idx) == parent_idx:
                    retrieval_score = score
                    break
            
            result = SearchResult(
                chunk=parent_data["chunk"],
                score=float(parent_data["score"]),
                file_id=meta.file_id,
                chunk_idx=meta.chunk_idx_in_file,
                heading_level=meta.heading_level,
                heading_text=meta.heading_text,
                parent_headings=meta.parent_headings,
                search_mode=search_mode,
                retrieval_score=float(retrieval_score),
                rerank_score=float(parent_data["score"]),
                section_type=meta.section_type
            )
            results.append(result)
        
        elapsed = time.time() - start_time
        if verbose:
            print(f"\nResults: {len(results)} parent chunks (in {elapsed:.2f}s)")
            if results:
                print(f"Top score: {results[0].score:.4f}")
                print(f"Top chunk section type: {results[0].section_type}")
                print(f"Top chunk heading: {results[0].heading_text}")
        
        return results
    
    def _print_stats(self):
        """Print system statistics"""
        print(f"\n{'='*100}")
        print("SYSTEM READY ✓")
        print(f"{'='*100}")
        print(f"\nSystem Configuration:")
        print(f"  Model: Qwen3-Embedding-0.6B")
        print(f"  Device: {self.device}")
        print(f"  Embedding Dim: {self.embedding_dim}")
        print(f"  Files: {len(self.file_metadata)}")
        print(f"  Parent Chunks: {len(self.parent_chunks_store)}")
        print(f"  Child Chunks: {len(self.chunks)}")
        print(f"  Dense Index: FAISS (IP)")
        print(f"  Sparse Index: BM25")
        
        if self.file_metadata:
            parent_counts = [m['num_parents'] for m in self.file_metadata.values()]
            child_counts = [m['num_children'] for m in self.file_metadata.values()]
            
            print(f"\nParent Chunk Distribution:")
            print(f"  Min: {min(parent_counts)}")
            print(f"  Max: {max(parent_counts)}")
            print(f"  Avg: {np.mean(parent_counts):.1f}")
            print(f"  Total: {sum(parent_counts)}")
            
            print(f"\nChild Chunk Distribution:")
            print(f"  Min: {min(child_counts)}")
            print(f"  Max: {max(child_counts)}")
            print(f"  Avg: {np.mean(child_counts):.1f}")
            print(f"  Total: {sum(child_counts)}")
            