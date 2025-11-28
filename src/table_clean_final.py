from bs4 import BeautifulSoup
import re
from pathlib import Path
from collections import Counter


class AdvancedTableProcessor:
    def __init__(self, html_string, verbose=True):
        self.html = html_string
        self.verbose = verbose
        self.raw_matrix = []
        self.cleaned_matrix = []
            
    def parse_raw_html(self):
        soup = BeautifulSoup(self.html, 'html.parser')
        table = soup.find('table')
        if not table:
            raise ValueError("No table found in HTML")

        # 🔴 HARD FILTER: remove hardcoded Viettel AI Race header block (2 rows)
        # Build raw HTML string of the entire table for direct pattern matching
        table_html = str(table)
        
        # Pattern: 2 consecutive <tr> with the exact structure (flexible whitespace, &nbsp;)
        pattern = r'''
            <tr\s*>[^<]*(?:<td[^>]*>&nbsp;</td>\s*){3}
            <td[^>]*>VIETTEL\s+AI\s+RACE</td>
            (?:\s*<td[^>]*>&nbsp;</td>){4}
            <td[^>]*>TD441</td>
            (?:\s*<td[^>]*>&nbsp;</td>){3}\s*</tr>\s*
            <tr\s*>[^<]*(?:<td[^>]*>&nbsp;</td>\s*){3}
            <td[^>]*>BỘ\s+CHỈ\s+TIÊU\s+KỸ\s+THUẬT\s+CHO\s+HỆ\s+THỐNG\s+vCOC</td>
            (?:\s*<td[^>]*>&nbsp;</td>){4}
            <td[^>]*>Lần\s+ban\s+hành:\s*1</td>
            (?:\s*<td[^>]*>&nbsp;</td>){3}\s*</tr>
        '''
        new_table_html = re.sub(pattern, '', table_html, flags=re.IGNORECASE | re.DOTALL | re.VERBOSE)
        
        # Parse the cleaned table
        new_soup = BeautifulSoup(new_table_html, 'html.parser')
        clean_table = new_soup.find('table')
        if not clean_table:
            clean_table = soup.new_tag('table')  # empty table if all removed

        # Now parse rows normally (without the hardcoded block)
        for tr in clean_table.find_all('tr'):
            cells = tr.find_all(['td', 'th'])
            # Skip empty rows
            if all(not td.get_text(strip=True).replace('\xa0', '').strip() for td in cells):
                continue
            row = []
            for td in cells:
                text = td.get_text(strip=True).replace('\xa0', ' ').strip()
                if not text:
                    text = '&nbsp;'
                is_bold = bool(td.find('strong') or td.find('b'))
                has_br = bool(td.find('br'))
                rowspan = int(td.get('rowspan', 1))
                colspan = int(td.get('colspan', 1))
                row.append({
                    'text': text,
                    'is_bold': is_bold,
                    'has_br': has_br,
                    'rowspan': rowspan,
                    'colspan': colspan
                })
            self.raw_matrix.append(row)
        return self
    
    def detect_complex_header(self):
        if not self.raw_matrix:
            return 0
        if len(self.raw_matrix) > 0 and any(
            "YÊU CẦU" in cell['text'] or "STT" in cell['text'].upper()
            for cell in self.raw_matrix[0]
        ):
            return 1
        return 0
    
    def clean_and_merge_complex(self):
        if not self.raw_matrix:
            raise ValueError("Run parse_raw_html() first")
        self.cleaned_matrix = self.raw_matrix
        return self
    
    def generate_clean_html(self):
        if not self.cleaned_matrix:
            raise ValueError("Run clean_and_merge_complex() first")
        html_parts = ['<table>']
        html_parts.append('<tbody>')
        for row in self.cleaned_matrix:
            html_parts.append('<tr>')
            for cell in row:
                if cell.get('rowspan', 1) == 0 or cell.get('colspan', 1) == 0:
                    continue
                attrs = []
                if cell.get('rowspan', 1) > 1:
                    attrs.append(f'rowspan="{cell["rowspan"]}"')
                if cell.get('colspan', 1) > 1:
                    attrs.append(f'colspan="{cell["colspan"]}"')
                attr_str = ' ' + ' '.join(attrs) if attrs else ''
                content = cell['text']
                if cell['is_bold']:
                    content = f'<strong>{content}</strong>'
                html_parts.append(f'<td{attr_str}>{content}</td>')
            html_parts.append('</tr>')
        html_parts.append('</tbody>')
        html_parts.append('</table>')
        return '\n'.join(html_parts)


def is_empty(cell):
    if cell is None:
        return True
    text = cell.get('text', '') if isinstance(cell, dict) else str(cell)
    return not text or not text.strip() or text.strip() == '&nbsp;'


def shift_left_compress_header(matrix, verbose=False):
    if not matrix or not matrix[0]:
        return matrix
    num_rows = len(matrix)
    num_cols = len(matrix[0])
    iteration = 0
    while True:
        changed = False
        iteration += 1
        if verbose:
            print(f"\n{'='*70}\nITERATION {iteration}\n{'='*70}")
        for j in range(num_cols - 1):
            header_current = matrix[0][j]
            header_next = matrix[0][j + 1]
            if is_empty(header_current) and not is_empty(header_next):
                if verbose:
                    print(f"\n📍 [HEADER] Column {j}→{j+1}: empty → value")
                for i in range(num_rows):
                    if is_empty(matrix[i][j]) and not is_empty(matrix[i][j + 1]):
                        val = matrix[i][j + 1].get('text', '') if isinstance(matrix[i][j + 1], dict) else str(matrix[i][j + 1])
                        matrix[i][j] = matrix[i][j + 1]
                        matrix[i][j + 1] = {'text': '&nbsp;', 'is_bold': False, 'has_br': False, 'rowspan': 1, 'colspan': 1}
                        changed = True
                        if verbose:
                            print(f"  ✓ Row {i}: '{val}' ({i},{j+1}) → ({i},{j})")
            elif is_empty(header_next):
                data_moved = False
                for i in range(1, num_rows):
                    if is_empty(matrix[i][j]) and not is_empty(matrix[i][j + 1]):
                        if verbose and not data_moved:
                            print(f"\n📍 [DATA] Column {j}→{j+1}: source header empty")
                            data_moved = True
                        val = matrix[i][j + 1].get('text', '') if isinstance(matrix[i][j + 1], dict) else str(matrix[i][j + 1])
                        matrix[i][j] = matrix[i][j + 1]
                        matrix[i][j + 1] = {'text': '&nbsp;', 'is_bold': False, 'has_br': False, 'rowspan': 1, 'colspan': 1}
                        changed = True
                        if verbose:
                            print(f"  ✓ Row {i}: '{val}' ({i},{j+1}) → ({i},{j})")
        if not changed:
            if verbose:
                print(f"\n✅ No changes. Stopping.")
            break
    last_col = num_cols - 1
    while last_col >= 0:
        all_empty = True
        for i in range(num_rows):
            if not is_empty(matrix[i][last_col]):
                all_empty = False
                break
        if all_empty:
            last_col -= 1
        else:
            break
    if last_col >= 0:
        for i in range(num_rows):
            matrix[i] = matrix[i][:last_col + 1]
    if verbose:
        print(f"\n✂️ Trimmed to {last_col + 1} columns")
    return matrix


def merge_and_pad_tables(html_content, verbose=True):
    soup = BeautifulSoup(html_content, 'html.parser')
    tables = soup.find_all('table')
    if verbose:
        print(f"\n📊 Found {len(tables)} tables")
    parsed_tables = []
    for i, table in enumerate(tables):
        proc = AdvancedTableProcessor(str(table), verbose=False)
        proc.parse_raw_html()
        proc.clean_and_merge_complex()
        parsed_tables.append({
            'index': i,
            'processor': proc,
            'html': str(table)
        })
    all_col_counts = []
    has_stt_list = []
    for tbl in parsed_tables:
        proc = tbl['processor']
        header_rows = proc.detect_complex_header()
        data = proc.cleaned_matrix[header_rows:]
        for row in data:
            if row:
                all_col_counts.append(len(row))
        first_row = proc.cleaned_matrix[0] if proc.cleaned_matrix else []
        has_stt_list.append(first_row and first_row[0]['text'].strip().isdigit())
    if all_col_counts:
        counter = Counter(all_col_counts)
        standard_cols = counter.most_common()[0][0]
        if verbose:
            print(f"📐 Column distribution: {dict(counter)}")
            print(f"📊 Standard columns: {standard_cols}")
    else:
        standard_cols = 5
        if verbose:
            print(f"📐 Using fallback: {standard_cols} cols")
    master_has_stt = any(has_stt_list)
    if parsed_tables:
        first_proc = parsed_tables[0]['processor']
        first_cols = len(first_proc.cleaned_matrix[0]) if first_proc.cleaned_matrix else 0
        if first_cols != standard_cols:
            if has_special_technical_header(first_proc.cleaned_matrix):
                if verbose:
                    print(f"\n⚠️ [SKIP] First table has special technical header — skip shift_left_compress_header")
            else:
                if verbose:
                    print(f"\n🔧 [NORMALIZE 1] First table has {first_cols} cols != standard {standard_cols}")
                    print(f"   → Applying shift_left_compress_header...")
                first_proc.cleaned_matrix = shift_left_compress_header(first_proc.cleaned_matrix, verbose=verbose)
            if verbose:
                new_cols = len(first_proc.cleaned_matrix[0]) if first_proc.cleaned_matrix else 0
                print(f"   ✅ Normalized to {new_cols} cols")
    current_stt = 1
    for i, tbl in enumerate(parsed_tables):
        proc = tbl['processor']
        curr_has_stt = has_stt_list[i]
        if i == 0:
            for row in reversed(proc.cleaned_matrix):
                if row and row[0]['text'].strip().isdigit():
                    current_stt = int(row[0]['text'].strip()) + 1
                    break
            continue
        new_matrix = []
        for row in proc.cleaned_matrix:
            if not row:
                continue
            original_data = [cell.copy() for cell in row]
            original_col_count = len(original_data)
            stt_added = 1 if (master_has_stt and not curr_has_stt) else 0
            cols_after_stt = original_col_count + stt_added
            padding_needed = max(0, standard_cols - cols_after_stt)
            new_row = []
            if master_has_stt and not curr_has_stt:
                new_row.append({
                    'text': str(current_stt),
                    'is_bold': False,
                    'has_br': False,
                    'rowspan': 1,
                    'colspan': 1
                })
                current_stt += 1
            for _ in range(padding_needed):
                new_row.append({
                    'text': '&nbsp;',
                    'is_bold': False,
                    'has_br': False,
                    'rowspan': 1,
                    'colspan': 1
                })
            new_row.extend(original_data)
            new_matrix.append(new_row)
        proc.cleaned_matrix = new_matrix
        if verbose:
            print(f"✅ Table {i}: Padded to {standard_cols} cols")
    result_parts = []
    for tbl in parsed_tables:
        result_parts.append(tbl['processor'].generate_clean_html())
    result_html = '\n\n'.join(result_parts)
    result_html = clean_redundant_table_tags(result_html)
    return result_html


def clean_redundant_table_tags(html_content):
    def should_remove_gap(gap_content):
        if not gap_content.strip():
            return True
        cleaned = re.sub(r'<!--.*?-->', '', gap_content, flags=re.DOTALL)
        cleaned = re.sub(r'\s*\|<image_\d+>\|\s*', '', cleaned)
        cleaned = cleaned.strip()
        if not cleaned:
            return True
        return bool(re.fullmatch(r'[\s\-_=*#+\n]{1,50}', cleaned))
    def replace_pair(match):
        full_match = match.group(0)
        gap_content = match.group(2)
        if should_remove_gap(gap_content):
            return ''
        return full_match
    pattern_table = r'(</table>)([^<]*?)(<table[^>]*>)'
    html_content = re.sub(pattern_table, replace_pair, html_content, flags=re.DOTALL)
    pattern_tbody = r'(</tbody>)(\s*)(<tbody>)'
    html_content = re.sub(
        pattern_tbody,
        lambda m: '' if not m.group(2).strip() or should_remove_gap(m.group(2)) else m.group(0),
        html_content,
        flags=re.DOTALL
    )
    return html_content


def parse_html_to_matrix(html_string):
    proc = AdvancedTableProcessor(html_string, verbose=False)
    proc.parse_raw_html()
    proc.clean_and_merge_complex()
    return proc.cleaned_matrix


def matrix_to_html(matrix):
    html_parts = ['<table>']
    html_parts.append('<tbody>')
    for row in matrix:
        html_parts.append('<tr>')
        for cell in row:
            attrs = []
            if cell.get('rowspan', 1) > 1:
                attrs.append(f'rowspan="{cell["rowspan"]}"')
            if cell.get('colspan', 1) > 1:
                attrs.append(f'colspan="{cell["colspan"]}"')
            attr_str = ' ' + ' '.join(attrs) if attrs else ''
            content = cell['text']
            if cell.get('is_bold', False):
                content = f'<strong>{content}</strong>'
            html_parts.append(f'<td{attr_str}>{content}</td>')
        html_parts.append('</tr>')
    html_parts.append('</tbody>')
    html_parts.append('</table>')
    return '\n'.join(html_parts)


def merge_row_with_previous(matrix, stt_col=0, join_with='\n', verbose=False):
    def is_empty(cell):
        if cell is None:
            return True
        text = cell.get('text', '') if isinstance(cell, dict) else str(cell)
        return not text or not text.strip() or text.strip() == '&nbsp;'
    def is_number(cell):
        try:
            text = cell.get('text', '') if isinstance(cell, dict) else str(cell)
            return text.isdigit()
        except:
            return False
    merged_matrix = []
    i = 0
    while i < len(matrix):
        if i > 0 and is_empty(matrix[i][stt_col]) and is_number(matrix[i-1][stt_col]):
            next_is_number = (i + 1 < len(matrix) and is_number(matrix[i+1][stt_col]))
            prev_number = int(matrix[i-1][stt_col].get('text', '') if isinstance(matrix[i-1][stt_col], dict) else str(matrix[i-1][stt_col]))
            next_number = int(matrix[i+1][stt_col].get('text', '') if isinstance(matrix[i+1][stt_col], dict) else str(matrix[i+1][stt_col])) if next_is_number else None
            if next_is_number and next_number == prev_number + 1:
                if verbose:
                    print(f"🟧 Merging row {i} into row {i-1} (STT: {prev_number})")
                for j in range(1, len(matrix[i])):
                    c_prev = matrix[i-1][j]
                    c_cur = matrix[i][j]
                    if not is_empty(c_cur):
                        if isinstance(c_prev, dict):
                            c_prev['text'] += join_with + (c_cur.get('text', '') if isinstance(c_cur, dict) else str(c_cur))
                i += 1
                continue
        merged_matrix.append(matrix[i])
        i += 1
    return merged_matrix
    
def has_special_technical_header(matrix):
    if not matrix or len(matrix) < 1:
        return False
    first_row = matrix[0]
    if len(first_row) < 2:
        return False
    texts = [cell.get('text', '').strip().upper() for cell in first_row]
    if texts[0] == 'STT':
        for t in texts[1:]:
            if 'CẤU HÌNH' in t and 'THÔNG SỐ' in t and 'KỸ THUẬT' in t:
                return True
    return False

def compress_tables_in_file(input_file, output_file=None, verbose=True):
    if output_file is None:
        input_path = Path(input_file)
        output_file = input_path.parent / f"{input_path.stem}_compressed{input_path.suffix}"
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    if verbose:
        print(f"\n📖 Reading: {input_file}")
    soup = BeautifulSoup(content, 'html.parser')
    tables = soup.find_all('table')
    if verbose:
        print(f"📊 Found {len(tables)} tables")
        print(f"\n🔧 [NORMALIZE 2] Post-merge normalization...")
    processed_tables = []
    for i, table in enumerate(tables):
        if verbose:
            print(f"\n{'='*70}\nTABLE {i+1}/{len(tables)}\n{'='*70}")
        try:
            # Trong compress_tables_in_file, trong vòng for xử lý từng table:
            matrix = parse_html_to_matrix(str(table))
            if verbose:
                print(f"📐 Original: {len(matrix)} rows × {len(matrix[0]) if matrix else 0} cols")

            matrix = merge_row_with_previous(matrix, verbose=verbose)

            # → Sửa ở đây:
            if has_special_technical_header(matrix):
                if verbose:
                    print("⚠️ Skip shift_left_compress_header (special technical header)")
                compressed_matrix = matrix
            else:
                compressed_matrix = shift_left_compress_header(matrix, verbose=verbose)
            compressed_html = matrix_to_html(compressed_matrix)
            processed_tables.append(compressed_html)
            if verbose:
                print(f"✅ Final: {len(compressed_matrix)} rows × {len(compressed_matrix[0]) if compressed_matrix else 0} cols")
        except Exception as e:
            if verbose:
                print(f"❌ Error: {e}")
            processed_tables.append(str(table))
    pattern = r'<table[^>]*>.*?</table>'
    sections = []
    last_end = 0
    for match in re.finditer(pattern, content, re.DOTALL):
        if match.start() > last_end:
            sections.append(('text', content[last_end:match.start()]))
        sections.append(('table', None))
        last_end = match.end()
    if last_end < len(content):
        sections.append(('text', content[last_end:]))
    table_idx = 0
    result_parts = []
    for section_type, section_content in sections:
        if section_type == 'text':
            result_parts.append(section_content)
        else:
            result_parts.append(processed_tables[table_idx])
            table_idx += 1
    result = ''.join(result_parts)
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(result)
    if verbose:
        print(f"\n{'='*70}\n✅ DONE\n📁 Output: {output_file}\n{'='*70}")
    return result


def process_markdown_file_complete(input_file_path, output_file_path=None, verbose=True):
    if output_file_path is None:
        input_path = Path(input_file_path)
        output_file_path = input_path.parent / f"{input_path.stem}_final{input_path.suffix}"
    temp_file = Path(input_file_path).parent / "temp_merged.md"
    
    # BƯỚC 1: Merge & Pad (normalize lần 1)
    with open(input_file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if verbose:
        print(f"📖 Reading: {input_file_path}\n")
    
    pattern = r'(<table[^>]*>.*?</table>)'
    sections = []
    last_end = 0
    for match in re.finditer(pattern, content, re.DOTALL):
        if match.start() > last_end:
            sections.append(('text', content[last_end:match.start()]))
        sections.append(('table', match.group(1)))
        last_end = match.end()
    if last_end < len(content):
        sections.append(('text', content[last_end:]))
    processed = []
    i = 0
    while i < len(sections):
        if sections[i][0] == 'text':
            processed.append(sections[i][1])
            i += 1
        else:
            table_group = [sections[i][1]]
            j = i + 1
            while j < len(sections):
                if sections[j][0] == 'table':
                    table_group.append(sections[j][1])
                    j += 1
                elif sections[j][0] == 'text':
                    if sections[j][1].strip():
                        break
                    j += 1
                else:
                    break
            combined = '\n\n'.join(table_group)
            merged = merge_and_pad_tables(combined, verbose=verbose)
            processed.append(merged)
            i = j
    temp_content = ''.join(processed)
    with open(temp_file, 'w', encoding='utf-8') as f:
        f.write(temp_content)
    if verbose:
        print(f"\n💾 Temp saved: {temp_file}")
    
    compress_tables_in_file(temp_file, output_file_path, verbose=verbose)
    
    temp_file.unlink()
    return output_file_path
import os
from pathlib import Path

def process_folder(base_dir: str, pattern: str = "Public_*/main.md", verbose: bool = True):
    base_path = Path(base_dir)
    md_files = list(base_path.glob(pattern))
    
    if not md_files:
        return

    for i, md_file in enumerate(md_files, 1):
        try:
            if verbose:
                print(f"[{i}/{len(md_files)}] {md_file.relative_to(base_path)}")
            process_markdown_file_complete(str(md_file), str(md_file), verbose=verbose)
        except Exception as e:
            print(f"❌ {md_file}: {e}")

if __name__ == "__main__":
    process_folder(r"working\output_mineru_test", verbose=False)
