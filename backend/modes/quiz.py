from ai import ask_ai
from rag import search_books
from memory import save_score

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


def quiz_mode(
    subject,
    difficulty,
    language,
    bilingual,
    book_chunks
):

    global current_question
    global current_answer

    topic = input("\nQuiz topic: ")

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
Create ONE quiz question.

SUBJECT:
{subject}

TOPIC:
{topic}

TEXTBOOK:
{context}

LANGUAGE:
{language_rules}

RULES:
- only about topic
- no unrelated trivia
- concise answer

FORMAT:
QUESTION: question here
ANSWER: answer here
"""

    result = ask_ai(prompt)

    question, answer = safe_parse(result)

    if not question or not answer:

        print("\nFailed to create quiz.")
        return

    current_question = question
    current_answer = answer

    print("\nQuiz Question:\n")

    print(current_question)

    print("\nUse /answer")


def answer_mode(subject):

    global current_question
    global current_answer

    if current_question is None:

        print("\nNo active quiz.")
        return

    user_answer = input("\nYour answer: ")

    prompt = f"""
QUESTION:
{current_question}

CORRECT ANSWER:
{current_answer}

STUDENT ANSWER:
{user_answer}

FORMAT:
RESULT: Correct/Partially Correct/Wrong
EXPLANATION: short explanation
CORRECT_ANSWER: short answer
SCORE: x/10
"""

    evaluation = ask_ai(prompt)

    print("\nEvaluation:\n")

    print(evaluation)

    score_value = 0

    for i in range(10, 0, -1):

        if f"{i}/10" in evaluation:

            score_value = i
            break

    save_score(
        current_question,
        subject,
        score_value
    )

    current_question = None
    current_answer = None
