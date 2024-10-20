def book_list(books, func):
    for book in books:
        print(func(book))

books = ['System Design', 'Python и DevOps', 'Git. Практическое Руководство']

book_list(books, lambda book: book.upper() + ' - прочитано')
