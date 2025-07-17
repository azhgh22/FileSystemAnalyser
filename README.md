# 🗂️ File System Analyzer

A command-line tool written in **Python** that analyzes the structure and usage of a file system on **Linux**.

## 🚀 Features

- 🔁 Recursive directory traversal (Parallel traversal in case of large files)
- 🗂️ File type categorization (text, image, executable, video)
- 📊 Size report per file type
- 🔐 File permission report for unusual settings (group-writable,world-executable, world-writable)
- 📦 Identification of large files above a given threshold

---

## 🧰 Requirements

- Python **3.13+**
- Works on **Linux** (not fully tested on Windows/macOS)

### Dependencies

Installed via `pip`: pip3 install -r requirements.txt

## 🛠️ Usage

```bash
cd FileSystemAnalyser/
python3.13 -m src.main

🧪 Running Tests
pytest ./tests/

👤 Author
Archil Zhghenti
Email: azhgh22@freeuni.edu.ge
