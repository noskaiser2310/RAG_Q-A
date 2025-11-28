import os
import sys
import zipfile
from pathlib import Path

def merge_python_files():
    """Merge all Python files from src/ (recursively) into main.py"""
    SRC_DIR = Path("src")

    if not SRC_DIR.exists():
        print("✗ src/ directory not found")
        return False

    print("\n--- Merging Python source files ---")

    python_files = sorted([
        f for f in SRC_DIR.rglob("*.py")
        if f.is_file() and "__pycache__" not in f.parts
    ])

    if not python_files:
        print("✗ No Python files found in src/")
        return False

    main_py_content = [
        '"""',
        "RAG-based QA System - Merged Source Code",
        "Generated automatically from multiple modules in src/",
        '"""',
        "",
    ]

    for file_path in python_files:
        rel_path = file_path.relative_to(SRC_DIR)
        print(f"  ✓ Adding {rel_path}")

        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        main_py_content.append(f"# {'='*60}")
        main_py_content.append(f"# {rel_path.as_posix()}")
        main_py_content.append(f"# {'='*60}")
        main_py_content.append("")
        main_py_content.append(content)
        main_py_content.append("")

    output_path = Path("main.py")
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(main_py_content))

    print(f"\n✓ Created main.py ({output_path.stat().st_size / 1024:.2f} KB)")
    return True


def package_submission():
    WORKING_DIR = Path.cwd()
    OUTPUT_DIR = Path(os.getenv('OUTPUT_DIR', 'working/output_mineru_test'))
    ANSWER_FILE = Path("working/answer.md")

    if not OUTPUT_DIR.exists():
        print(f"✗ Output directory not found: {OUTPUT_DIR}")
        print("  Run Task 1 and Task 2 first!")
        return False

    print("\n" + "="*50)
    print("PACKAGING SUBMISSION")
    print("="*50)

    output_zip = WORKING_DIR / 'submission_output.zip'

    print(f"\nPacking files from: {OUTPUT_DIR}")
    print(f"Creating ZIP: {output_zip}")

    with zipfile.ZipFile(output_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
        file_count = 0
        skipped_count = 0

        for file_path in OUTPUT_DIR.rglob('*'):
            if file_path.is_file():
                if file_path.suffix == '.pkl':
                    skipped_count += 1
                    continue
                if '__pycache__' in file_path.parts:
                    continue
                arcname = file_path.relative_to(OUTPUT_DIR)
                zipf.write(file_path, arcname)
                file_count += 1

        # ====================================================
        # FIX: place answer.md directly in root of ZIP
        # ====================================================
        if ANSWER_FILE.exists():
            zipf.write(ANSWER_FILE, "answer.md")  # <-- FIXED
            file_count += 1
            print(f"  ✓ Added answer.md to ZIP root")
        else:
            print("  ⚠ Missing working/answer.md — please ensure it exists before submission!")

        # Add merged main.py
        main_py = Path("main.py")
        if main_py.exists():
            zipf.write(main_py, "main.py")
            file_count += 1
            print(f"  ✓ Added main.py")

        print(f"\n  Added: {file_count} files")
        print(f"  Skipped: {skipped_count} .pkl files")

    print(f"\n✓ Created: {output_zip}")
    print(f"  Size: {output_zip.stat().st_size / 1024 / 1024:.2f} MB")

    # Validation
    print("\n--- Validation ---")
    with zipfile.ZipFile(output_zip, 'r') as zipf:
        files = zipf.namelist()

        has_main = 'main.py' in files
        has_answer = 'answer.md' in files  # MUST be root
        has_pkl = any(f.endswith('.pkl') for f in files)

        print(f"{'✓' if has_main else '✗'} main.py")
        print(f"{'✓' if has_answer else '✗'} answer.md (root)")
        print(f"{'✓' if not has_pkl else '✗'} No .pkl files (correct)")

    return True


def main():
    print("="*50)
    print("SUBMISSION PACKAGING TOOL")
    print("="*50)

    if not merge_python_files():
        sys.exit(1)

    if not package_submission():
        sys.exit(1)


if __name__ == "__main__":
    main()
