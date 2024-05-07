import json
from library import Library
from book import Book


def save_library(library):
    with open('library_data.json', 'w') as file:
        json.dump({title: {'title': book.title, 'author': book.author, 'publication_year': book.publication_year, 'genre': book.genre} for title, book in library.books.items()}, file)

def load_library():
    library = Library()
    try:
        with open('library_data.json', 'r') as file:
            books_dict = json.load(file)
            for title, book_data in books_dict.items():
                book = Book(title=book_data['title'], author=book_data['author'], publication_year=book_data['publication_year'], genre=book_data['genre'])
                library.add_book(book)
    except FileNotFoundError:
        print("No data file found, starting with an empty library.")
    except KeyError as e:
        print(f"Key error: {e} - check your data file format.")
    return library
