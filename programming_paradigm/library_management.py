# programming_paradigm/library_management.py

class Book:
    def __init__(self, title, author):
        self.title = title           # public attribute
        self.author = author         # public attribute
        self._is_checked_out = False # private attribute

    def check_out(self):
        """Marks the book as checked out."""
        if not self._is_checked_out:
            self._is_checked_out = True
        else:
            print(f"'{self.title}' is already checked out.")

    def return_book(self):
        """Marks the book as available."""
        if self._is_checked_out:
            self._is_checked_out = False
        else:
            print(f"'{self.title}' is not currently checked out.")

    def is_available(self):
        """Returns True if book is not checked out."""
        return not self._is_checked_out


class Library:
    def __init__(self):
        self._books = []  # private list of all books

    def add_book(self, book):
        """Adds a Book instance to the library."""
        self._books.append(book)

    def check_out_book(self, title):
        """Checks out a book by title if available."""
        for book in self._books:
            if book.title == title:
                if book.is_available():
                    book.check_out()
                    return
                else:
                    print(f"'{title}' is already checked out.")
                    return
        print(f"Book titled '{title}' not found in the library.")

    def return_book(self, title):
        """Returns a book by title."""
        for book in self._books:
            if book.title == title:
                if not book.is_available():
                    book.return_book()
                    return
                else:
                    print(f"'{title}' was not checked out.")
                    return
        print(f"Book titled '{title}' not found in the library.")

    def list_available_books(self):
        """Prints all available books."""
        for book in self._books:
            if book.is_available():
                print(f"{book.title} by {book.author}")
