# library_management.py

class Book:
    """A class representing a book in the library."""

    def __init__(self, title, author):
        """Initialize a Book with a title, author, and checked-out status."""
        self.title = title
        self.author = author
        self._is_checked_out = False  # Private attribute

    def check_out(self):
        """Mark the book as checked out if it’s available."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        """Mark the book as returned (available)."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        """Return True if the book is available (not checked out)."""
        return not self._is_checked_out


class Library:
    """A class that manages a collection of books."""

    def __init__(self):
        """Initialize the library with an empty private list of books."""
        self._books = []

    def add_book(self, book):
        """Add a Book instance to the library."""
        self._books.append(book)

    def check_out_book(self, title):
        """Check out a book by title if it’s available."""
        for book in self._books:
            if book.title == title:
                if book.check_out():
                    print(f"'{title}' has been checked out.")
                else:
                    print(f"'{title}' is already checked out.")
                return
        print(f"Book titled '{title}' not found in library.")

    def return_book(self, title):
        """Return a book by title."""
        for book in self._books:
            if book.title == title:
                if book.return_book():
                    print(f"'{title}' has been returned.")
                else:
                    print(f"'{title}' was not checked out.")
                return
        print(f"Book titled '{title}' not found in library.")

    def list_available_books(self):
        """Print a list of all available (not checked out) books."""
        available_books = [book for book in self._books if book.is_available()]
        if not available_books:
