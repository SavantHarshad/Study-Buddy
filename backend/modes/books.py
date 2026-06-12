def books_mode(book_chunks):

    if len(book_chunks) == 0:

        print("\nNo books loaded.")
        return

    books = set()

    for chunk in book_chunks:

        books.add(
            f"{chunk['subject']} → {chunk['source']}"
        )

    print("\nBooks:\n")

    for book in sorted(books):

        print("-", book)
