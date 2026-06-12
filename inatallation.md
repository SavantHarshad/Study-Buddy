# Offline Study Buddy Installation Guide

This guide explains installation for:

1. Android (Termux)
2. Windows/Linux/macOS (Anaconda Prompt)

---

# PART 1 — TERMUX INSTALLATION

---

# Step 1 — Install Termux

Install from F-Droid:

https://f-droid.org/packages/com.termux/

DO NOT use Play Store version.

---

# Step 2 — Install Termux API

Install:

https://f-droid.org/packages/com.termux.api/

---

# Step 3 — Update Packages

Open Termux and run:

pkg update -y
pkg upgrade -y

---

# Step 4 — Install Required Packages

pkg install python -y
pkg install nodejs -y
pkg install git -y
pkg install termux-api -y

---

# Step 5 — Install Ollama

Run:

curl -fsSL https://ollama.com/install.sh | sh

---

# Step 6 — Start Ollama

ollama serve

Keep this terminal open.

---

# Step 7 — Pull AI Model

Open another terminal session:

ollama pull qwen2.5:1.5b

Optional larger models:

ollama pull qwen2.5:3b
ollama pull qwen2.5:7b

---

# Step 8 — Clone Project

cd ~

git clone YOUR_GITHUB_REPO_URL

cd study_buddy

---

# Step 9 — Install Python Packages

cd backend

pip install requests
pip install pypdf

---

# Step 10 — Install Node Packages

cd ../frontend

npm install

---

# Step 11 — Create Book Folders

cd ../backend

mkdir -p books/biology
mkdir -p books/physics
mkdir -p books/history
mkdir -p books/business

---

# Step 12 — Add PDF Books

Place PDFs inside subject folders.

Example:

books/biology/ncert_biology.pdf

---

# Step 13 — Start Frontend

cd ../frontend

node server.js

---

# Step 14 — Open Browser

Visit:

http://localhost:3000

OR

http://127.0.0.1:3000

---

# PART 2 — ANACONDA INSTALLATION

---

# Step 1 — Install Anaconda

Download:

https://www.anaconda.com/download

Install Anaconda.

---

# Step 2 — Install Ollama

Download:

https://ollama.com/download

Install Ollama.

---

# Step 3 — Open Anaconda Prompt

---

# Step 4 — Create Environment

conda create -n studybuddy python=3.11 -y

---

# Step 5 — Activate Environment

conda activate studybuddy

---

# Step 6 — Install Node.js

conda install -c conda-forge nodejs -y

---

# Step 7 — Install Git

conda install git -y

---

# Step 8 — Start Ollama

Open separate terminal:

ollama serve

---

# Step 9 — Pull Model

ollama pull qwen2.5:1.5b

---

# Step 10 — Clone Repository

git clone YOUR_GITHUB_REPO_URL

cd study_buddy

---

# Step 11 — Install Python Dependencies

cd backend

pip install requests
pip install pypdf

---

# Step 12 — Install Node Dependencies

cd ../frontend

npm install

---

# Step 13 — Create Book Folders

cd ../backend

mkdir books
mkdir books\biology
mkdir books\physics
mkdir books\history
mkdir books\business

---

# Step 14 — Add PDF Books

Place PDF books into subject folders.

Example:

books\biology\ncert_biology.pdf

---

# Step 15 — Start Frontend

cd ../frontend

node server.js

---

# Step 16 — Open Browser

Visit:

http://localhost:3000

---

# Troubleshooting

---

## Ollama Not Running

Check:

ollama ps

---

## Port Already In Use

Kill previous Node.js server.

---

## No Books Loaded

Ensure:
- PDFs exist
- books folder structure is correct

---

## Voice Not Working In Termux

Ensure:
- Termux API app installed
- termux-api package installed

Test:

termux-tts-speak "Hello"

---

# Recommended Setup

## Android

- qwen2.5:1.5b
- Voice enabled
- Multilingual enabled

---

## PC

- qwen2.5:3b or 7b
- Larger PDFs
- Multiple subjects

---

# Performance Tips

- Keep PDFs under 50MB
- Use smaller models on phones
- Avoid too many simultaneous books
- Restart Ollama occasionally on Android

---

# Running Backend Only

cd backend

python app.py

---

# Running Full UI

Terminal 1:

ollama serve

Terminal 2:

cd frontend
node server.js

Browser:

http://localhost:3000
