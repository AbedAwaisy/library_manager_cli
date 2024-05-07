from error_handler import BookNotFoundError, DuplicateBookError

class Library:
    def __init__(self):
        self._books = {}

    @property
    def books(self):
        return self._books

    def add_book(self, book):
        if book.title in self._books:
            raise DuplicateBookError(book.title)
        self._books[book.title] = book

    def remove_book(self, title):
        if title not in self._books:
            raise BookNotFoundError(title)
        del self._books[title]

    def find_book(self, title):
        if title not in self._books:
            raise BookNotFoundError(title)
        return self._books[title]

    def list_books(self):
        if not self._books:
            return "No books in the library."
        return '\n'.join(f"{idx + 1}. {book}" for idx, book in enumerate(self._books.values()))

    def edit_book(self, old_title, new_title=None, author=None, publication_year=None, genre=None):
        if old_title not in self._books:
            raise BookNotFoundError(old_title)
        book = self._books[old_title]

        if new_title:
            if new_title != old_title:
                if new_title in self._books:
                    raise DuplicateBookError(new_title)
                book.title = new_title
                self._books[new_title] = self._books.pop(old_title)

        if author:
            book.author = author
        if publication_year:
            book.publication_year = publication_year
        if genre:
            book.genre = genre