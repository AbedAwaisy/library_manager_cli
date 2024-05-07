class Error(Exception):
    """Base class for other exceptions"""
    pass

class BookNotFoundError(Error):
    """Raised when a book is not found in the library"""
    def __init__(self, title):
        self.message = f"No book found with the title: {title}"
        super().__init__(self.message)

class DuplicateBookError(Error):
    """Raised when trying to add a book that already exists in the library"""
    def __init__(self, title):
        self.message = f"A book with the title '{title}' already exists."
        super().__init__(self.message)

class InvalidBookError(Error):
    """Raised when a book has invalid attributes"""
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
