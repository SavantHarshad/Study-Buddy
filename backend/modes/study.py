from ai import ask_ai
from rag import search_books


def study_mode(
    subject,
    difficulty,
    language,
    bilingual,
    book_chunks
):

    chapter = input("\nChapter: ")

    context = ""

    relevant = search_books(
        chapter,
        book_chunks,
        subject if subject != "general" else None
    )

    for chunk in relevant:

        context += chunk["text"] + "\n"

    context = context[:1500]

    language_rules = f"""
Respond in {language}.
"""

    if bilingual:

        language_rules += """
Use important English terms too.
"""

    prompt = f"""
Teach this chapter.

SUBJECT:
{subject}

DIFFICULTY:
{difficulty}

CHAPTER:
{chapter}

TEXTBOOK:
{context}

LANGUAGE:
{language_rules}

Rules:
- concise lesson
- simple explanation
- important concepts only
"""

    print("\nStudy Session:\n")

    print(ask_ai(prompt))
