import subprocess
import shutil
from pathlib import Path
from tqdm import tqdm
import os
import time

INPUT_DIR = Path(r'working/cleaned_pdfs_test')
state = 'test' if 'test' in str(INPUT_DIR).lower() else 'train'
WORKING_DIR = Path(r'working')
OUTPUT_DIR = WORKING_DIR / f'output_mineru_raw_{state}'
os.makedirs(OUTPUT_DIR, exist_ok=True)

def find_pdf_directory(base_dir):
    pdf_dirs = []
    for root, dirs, files in os.walk(base_dir):
        pdf_files = [f for f in files if f.lower().endswith('.pdf')]
        if pdf_files:
            pdf_dirs.append((Path(root), pdf_files))
    
    if pdf_dirs:
        pdf_dirs.sort(key=lambda x: len(x[1]), reverse=True)
        return pdf_dirs[0]
    return None, []


class PDFExtractorBatch:
    
    def __init__(self, batch_size=10):
        """
        Xử lý theo batch thay vì từng file
        - 1 lần init models phục vụ nhiều PDFs
        - Giảm overhead từ 28.7s/PDF xuống 28.7s/batch
        """
        self.batch_size = batch_size
    
    def extract_batch(self, pdf_paths, output_dir):
        """Xử lý 1 batch PDFs"""
        # Tạo temp dir cho batch
        batch_temp_dir = output_dir / f"batch_temp_{int(time.time())}"
        batch_temp_dir.mkdir(parents=True, exist_ok=True)
        
        # Copy PDFs vào temp dir
        temp_pdfs = []
        for pdf_path in pdf_paths:
            temp_pdf = batch_temp_dir / pdf_path.name
            shutil.copy2(pdf_path, temp_pdf)
            temp_pdfs.append(temp_pdf)
        
        # Chạy mineru cho toàn bộ batch
        mineru_output = output_dir / f"batch_output_{int(time.time())}"
        
        env = os.environ.copy()
        env['MINERU_DEVICE_MODE'] = 'cuda'
        # env['MINERU_FORMULA_ENABLE'] = 'false'  # ← Thêm dòng này

        
        cmd = [
            "mineru",
            "-p", str(batch_temp_dir),  # Process entire directory
            "-o", str(mineru_output),
            "--method","txt",
            "--format", "markdown",
        ]
        
        try:
            result = subprocess.run(cmd, capture_output=True, text=True, env=env, timeout=3600)
            
            if result.returncode != 0:
                print(f"Batch failed: {result.stderr[:200]}")
                return {}
            
            # Move results to final locations
            results = {}
            for pdf_path in pdf_paths:
                pdf_name = pdf_path.stem
                
                # Find output for this PDF
                source_dir = mineru_output / pdf_name / "txt"
                if not source_dir.exists():
                    results[pdf_name] = "Failed: No output"
                    continue
                
                # Create final output dir
                final_dir = output_dir / pdf_name
                final_dir.mkdir(parents=True, exist_ok=True)
                
                # Move markdown
                md_file = source_dir / f"{pdf_name}.md"
                if md_file.exists():
                    final_md = final_dir / "main.md"
                    shutil.copy2(md_file, final_md)
                    results[pdf_name] = final_md.read_text(encoding='utf-8')
                else:
                    results[pdf_name] = "Failed: No markdown"
                
                # Move images
                images_source = source_dir / "images"
                if images_source.exists():
                    images_dest = final_dir / "images"
                    if images_dest.exists():
                        shutil.rmtree(images_dest)
                    shutil.copytree(images_source, images_dest)
            
            # Cleanup
            shutil.rmtree(batch_temp_dir, ignore_errors=True)
            shutil.rmtree(mineru_output, ignore_errors=True)
            
            return results
            
        except Exception as e:
            print(f"Batch error: {e}")
            return {}
    
    def extract_all(self, pdf_dir: Path, output_dir: Path) -> dict:
        pdf_files = sorted(Path(pdf_dir).glob("*.pdf"))
        all_results = {}
        
        # Split into batches
        batches = [pdf_files[i:i + self.batch_size] 
                  for i in range(0, len(pdf_files), self.batch_size)]
        
        print(f"\n🚀 Processing {len(pdf_files)} PDFs in {len(batches)} batches")
        print(f"   Batch size: {self.batch_size}")
        print(f"   Expected init overhead: {len(batches)} × 28.7s = {len(batches) * 28.7:.1f}s")
        
        start_time = time.time()
        
        for batch_idx, batch in enumerate(batches, 1):
            print(f"\n📦 Batch {batch_idx}/{len(batches)} ({len(batch)} PDFs)")
            batch_start = time.time()
            
            batch_results = self.extract_batch(batch, output_dir)
            all_results.update(batch_results)
            
            batch_elapsed = time.time() - batch_start
            print(f"   ⏱️  Batch time: {batch_elapsed:.1f}s ({batch_elapsed/len(batch):.1f}s per PDF)")
            
            # Progress
            processed = sum(len(b) for b in batches[:batch_idx])
            remaining_batches = len(batches) - batch_idx
            eta = remaining_batches * batch_elapsed
            print(f"   Progress: {processed}/{len(pdf_files)} | ETA: {eta/60:.1f} min")
        
        total_elapsed = time.time() - start_time
        avg_per_pdf = total_elapsed / len(pdf_files)
        
        print(f"\n⏱️  Total time: {total_elapsed:.1f}s ({total_elapsed/60:.1f} min)")
        print(f"📊 Avg per PDF: {avg_per_pdf:.1f}s")
        print(f"🚀 Speedup vs sequential: {109/avg_per_pdf:.2f}x")
        
        return all_results


# Main execution
pdf_dir, pdf_files = find_pdf_directory(INPUT_DIR)

if pdf_dir:
    print("\n" + "="*50)
    print("TASK 1: PDF EXTRACTION (BATCH MODE)")
    print("="*50)
    
    # Batch size tuning:
    # - Small (5-10): More overhead, better memory control
    # - Medium (10-20): Balance
    # - Large (20-50): Less overhead, risk OOM
    extractor = PDFExtractorBatch(batch_size=20)
    
    extracted_contents = extractor.extract_all(pdf_dir, OUTPUT_DIR)
    
    print("\n=== EXTRACTION SUMMARY ===")
    success = sum(1 for c in extracted_contents.values() if not c.startswith("Failed"))
    failed = len(extracted_contents) - success
    
    print(f"✓ Success: {success}/{len(extracted_contents)}")
    if failed > 0:
        print(f"✗ Failed: {failed}")
else:
    print("\n✗ Cannot proceed without PDF files")
