from rag import load_books
from memory import init_db
from session import session_data

print("\nLoading books...")

book_chunks = load_books()

print(f"\nLoaded {len(book_chunks)} chunks.")

init_db()

print("\n=== Offline Study Buddy ===")

while True:

    print("\nCommands:")
    print("/ask")
    print("/quiz")
    print("/answer")
    print("/flashcards")
    print("/reveal")
    print("/study")
    print("/recommend")
    print("/books")
    print("/subject")
    print("/difficulty")
    print("/language")
    print("/bilingual")
    print("/exit")

    cmd = input("\nYou: ")

    if cmd == "/ask":

        from modes.ask import ask_mode

        ask_mode(
            session_data["subject"],
            session_data["difficulty"],
            session_data["language"],
            session_data["bilingual"],
            book_chunks
        )

    elif cmd == "/quiz":

        from modes.quiz import quiz_mode

        quiz_mode(
            session_data["subject"],
            session_data["difficulty"],
            session_data["language"],
            session_data["bilingual"],
            book_chunks
        )

    elif cmd == "/answer":

        from modes.quiz import answer_mode

        answer_mode(
            session_data["subject"]
        )

    elif cmd == "/flashcards":

        from modes.flashcards import flashcard_mode

        flashcard_mode(
            session_data["subject"],
            session_data["language"],
            session_data["bilingual"],
            book_chunks
        )

    elif cmd == "/reveal":

        from modes.flashcards import reveal_mode

        reveal_mode()

    elif cmd == "/study":

        from modes.study import study_mode

        study_mode(
            session_data["subject"],
            session_data["difficulty"],
            session_data["language"],
            session_data["bilingual"],
            book_chunks
        )

    elif cmd == "/recommend":

        from modes.recommend import recommend_mode

        recommend_mode()

    elif cmd == "/books":

        from modes.books import books_mode

        books_mode(book_chunks)

    elif cmd == "/subject":

        session_data["subject"] = input(
            "\nChoose subject: "
        ).lower()

    elif cmd == "/difficulty":

        session_data["difficulty"] = input(
            "\nChoose difficulty: "
        ).lower()

    elif cmd == "/language":

        session_data["language"] = input(
            "\nChoose language: "
        ).lower()

    elif cmd == "/bilingual":

        session_data["bilingual"] = (
            not session_data["bilingual"]
        )

        print(
            f"\nBilingual mode: "
            f"{session_data['bilingual']}"
        )

    elif cmd == "/exit":

        break

    else:

        print("\nUnknown command")
