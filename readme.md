# Offline Study Buddy

Offline Study Buddy is a lightweight AI-powered educational platform that runs completely offline on Android phones, laptops, and low-resource systems.

It combines:

- Local LLMs via Ollama
- PDF textbook RAG
- Adaptive learning
- Quiz generation
- Flashcards
- Multilingual tutoring
- Voice support
- Lightweight web UI

The system is designed especially for:

- Students
- Self-learners
- Rural/offline education
- Low-end devices
- Android + Termux users

---

# Features

## AI Tutor

Ask questions from textbooks using local AI.

- Offline operation
- Subject-aware responses
- Difficulty levels
- Multilingual explanations

---

## PDF RAG (Retrieval-Augmented Generation)

Place PDF books into subject folders.

Example:

books/
├── biology/
├── physics/
├── business/

The AI automatically:
- reads books
- chunks text
- searches relevant sections
- answers from textbooks

---

## Quiz Mode

Generate quizzes from:
- textbooks
- subjects
- custom topics

Features:
- answer evaluation
- scoring
- adaptive recommendations

---

## Flashcards

Generate active recall flashcards.

Flow:

Question
↓
Think
↓
Reveal Answer

---

## Study Sessions

Generate chapter summaries and guided learning sessions.

---

## Adaptive Learning

Tracks:
- quiz performance
- weak topics
- revision recommendations

---

## Multilingual Support

Supports:
- English
- Hindi
- Marathi
- Tamil

Can operate in:
- single-language mode
- bilingual mode

---

## Voice Tutor

Uses Android TTS through Termux API.

Can:
- speak answers
- read quizzes
- narrate lessons

---

## Lightweight Frontend

Simple dashboard UI using:
- Node.js
- Express
- HTML/CSS/JS

Works in mobile browser.

---

# Architecture

Frontend:
- Node.js
- Express
- HTML/CSS/JS

Backend:
- Python
- Ollama
- SQLite

AI:
- Qwen2.5 via Ollama

---

# Directory Structure

study_buddy/
│
├── backend/
│   ├── app.py
│   ├── ai.py
│   ├── rag.py
│   ├── memory.py
│   ├── session.py
│   ├── adaptive.py
│   ├── voice.py
│   ├── web_api.py
│   │
│   ├── books/
│   │   ├── biology/
│   │   ├── physics/
│   │   ├── history/
│   │   └── business/
│   │
│   └── modes/
│       ├── ask.py
│       ├── quiz.py
│       ├── flashcards.py
│       ├── study.py
│       ├── recommend.py
│       └── books.py
│
└── frontend/
    ├── server.js
    ├── package.json
    │
    └── public/
        ├── index.html
        ├── style.css
        └── app.js

---

# Supported Platforms

- Android (Termux)
- Linux
- Windows
- macOS

---

# Minimum Requirements

## Android

Recommended:
- 6GB+ RAM
- Android 11+

Minimum:
- 4GB RAM

---

## PC

Recommended:
- 8GB RAM
- SSD storage

---

# Recommended Models

## Low-end Devices

- qwen2.5:1.5b

## Mid-range Devices

- qwen2.5:3b

## High-end Systems

- qwen2.5:7b

---

# Future Roadmap

- OCR support
- Voice input
- Classroom mode
- Android APK
- Spaced repetition
- Teacher dashboard
- Multi-user support

---
