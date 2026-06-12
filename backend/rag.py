from pypdf import PdfReader
import os

BOOKS_PATH = "books"


def read_pdf(pdf_path):

    text = ""

    try:

        reader = PdfReader(pdf_path)

        for page in reader.pages:

            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

    except Exception as e:

        print(f"Error reading {pdf_path}: {e}")

    return text


def chunk_text(text, chunk_size=300):

    words = text.split()

    chunks = []

    for i in range(0, len(words), chunk_size):

        chunk = " ".join(
            words[i:i + chunk_size]
        )

        chunks.append(chunk)

    return chunks


def load_books():

    all_chunks = []

    for root, dirs, files in os.walk(BOOKS_PATH):

        subject = os.path.basename(root)

        for file in files:

            if file.endswith(".pdf"):

                path = os.path.join(root, file)

                print(f"Loading: {file}")

                text = read_pdf(path)

                chunks = chunk_text(text)

                for chunk in chunks:

                    all_chunks.append({
                        "subject": subject,
                        "source": file,
                        "text": chunk
                    })

    return all_chunks


def search_books(query, book_chunks, subject=None):

    results = []

    query_words = query.lower().split()

    for chunk in book_chunks:

        if subject and chunk["subject"] != subject:
            continue

        score = 0

        text = chunk["text"].lower()

        for word in query_words:

            if word in text:
                score += 1

        if score > 0:

            results.append((score, chunk))

    results.sort(
        reverse=True,
        key=lambda x: x[0]
    )

    return [r[1] for r in results[:3]]
