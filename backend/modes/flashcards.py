from ai import ask_ai
from rag import search_books

current_question = None
current_answer = None


def safe_parse(text):

    question = None
    answer = None

    lines = text.splitlines()

    for line in lines:

        line = line.strip()

        line = line.replace("**", "")

        upper = line.upper()

        if upper.startswith("QUESTION:"):

            question = line.split(
                ":",
                1
            )[1].strip()

        elif upper.startswith("ANSWER:"):

            answer = line.split(
                ":",
                1
            )[1].strip()

    return question, answer


def flashcard_mode(
    subject,
    language,
    bilingual,
    book_chunks
):

    global current_question
    global current_answer

    topic = input("\nFlashcard topic: ")

    context = ""

    relevant = search_books(
        topic,
        book_chunks,
        subject if subject != "general" else None
    )

    for chunk in relevant:

        context += chunk["text"] + "\n"

    context = context[:1000]

    language_rules = f"""
Respond in {language}.
"""

    if bilingual:

        language_rules += """
Use important English terms too.
"""

    prompt = f"""
Create ONE flashcard.

SUBJECT:
{subject}

TOPIC:
{topic}

TEXTBOOK:
{context}

LANGUAGE:
{language_rules}

FORMAT:
QUESTION: question here
ANSWER: answer here
"""

    result = ask_ai(prompt)

    question, answer = safe_parse(result)

    if not question or not answer:

        print("\nFailed to create flashcard.")
        return

    current_question = question
    current_answer = answer

    print("\nFlashcard:\n")

    print(current_question)

    print("\nUse /reveal")


def reveal_mode():

    global current_question
    global current_answer

    if current_question is None:

        print("\nNo active flashcard.")
        return

    print("\nAnswer:\n")

    print(current_answer)

    current_question = None
    current_answer = None
