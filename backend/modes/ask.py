from ai import ask_ai
from rag import search_books


def ask_mode(
    subject,
    difficulty,
    language,
    bilingual,
    book_chunks
):

    question = input("\nQuestion: ")

    context = ""

    relevant = search_books(
        question,
        book_chunks,
        subject if subject != "general" else None
    )

    for chunk in relevant:

        context += chunk["text"] + "\n"

    context = context[:1200]

    language_rules = f"""
Respond in {language}.
"""

    if bilingual:

        language_rules += """
Include important English terms.
"""

    prompt = f"""
You are a tutor.

SUBJECT:
{subject}

DIFFICULTY:
{difficulty}

TEXTBOOK:
{context}

QUESTION:
{question}

LANGUAGE RULES:
{language_rules}

Rules:
- concise
- easy explanation
"""

    print("\nTutor:\n")

    print(ask_ai(prompt))
