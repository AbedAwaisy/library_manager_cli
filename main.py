import argparse
import sys
from library import Library
from book import Book
from error_handler import BookNotFoundError, DuplicateBookError
from file_handler import save_library, load_library

def handle_edit(library, edit_args):
    """Manually handle edit commands."""
    if len(edit_args) < 3:
        print("Insufficient arguments for edit command.")
        return

    old_title = edit_args[0]
    i = 1
    new_values = {}
    allowed_edits = {'--title', '--author', '--year', '--genre'}

    while i < len(edit_args):
        if edit_args[i] in allowed_edits:
            if i + 1 < len(edit_args):
                new_values[edit_args[i][2:]] = edit_args[i + 1]  # Convert '--title' to 'title'
                i += 2
            else:
                print(f"Value for {edit_args[i]} not provided")
                return
        else:
            print(f"Invalid edit option: {edit_args[i]}")
            return

    try:
        library.edit_book(old_title, **new_values)
        print(f"Book '{old_title}' edited successfully.")
        save_library(library)
    except BookNotFoundError as e:
        print(e)

def main():
    parser = argparse.ArgumentParser(
        description="Library Management System",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )

    # Register other commands as usual
    parser.add_argument('--add', nargs=4, metavar=('TITLE', 'AUTHOR', 'YEAR', 'GENRE'))
    parser.add_argument('--remove', metavar='TITLE')
    parser.add_argument('--find', metavar='TITLE')
    parser.add_argument('--list', action='store_true')

    # Parse known args, assuming anything after '--edit' is part of the edit command
    args, unknown = parser.parse_known_args()

    library = load_library()

    # Handle known commands
    if args.add:
        title, author, year, genre = args.add
        try:
            library.add_book(Book(title, author, year, genre))
            print(f"Book '{title}' added successfully.")
            save_library(library)
        except DuplicateBookError as e:
            print(e)

    if args.remove:
        try:
            library.remove_book(args.remove)
            print(f"Book '{args.remove}' removed successfully.")
            save_library(library)
        except BookNotFoundError as e:
            print(e)

    if args.find:
        try:
            book = library.find_book(args.find)
            print(f"Found book: {book}")
        except BookNotFoundError as e:
            print(e)

    if args.list:
        print("Listing all books:")
        print(library.list_books())

    # Handle edit manually if '--edit' is in the command line
    if '--edit' in sys.argv:
        edit_index = sys.argv.index('--edit') + 1
        handle_edit(library, sys.argv[edit_index:])

if __name__ == "__main__":
    main()
