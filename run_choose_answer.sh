pip install -q torch==2.4.1 torchvision==0.19.1 torchaudio==2.4.1 --index-url https://download.pytorch.org/whl/cu124

pip install faiss-cpu

python src/qa_task.py

python src/combie.py

python src/create_late_file.py

python src/zip