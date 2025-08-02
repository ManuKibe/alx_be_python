# library_management.py

class Book:
    """
    Represents a book in the library.

    Attributes:
        title (str): The title of the book.
        author (str): The author of the book.
        _is_checked_out (bool): A private attribute indicating if the book is currently checked out.
                                 Defaults to False (available).
    """
    def __init__(self, title: str, author: str):
        """
        Initializes a new Book instance.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
        """
        self.title = title
        self.author = author
        self._is_checked_out = False  # Book is available by default

    def check_out(self):
        """
        Marks the book as checked out.
        """
        self._is_checked_out = True

    def return_book(self):
        """
        Marks the book as returned (available).
        """
        self._is_checked_out = False

    def is_available(self) -> bool:
        """
        Checks if the book is currently available.

        Returns:
            bool: True if the book is not checked out, False otherwise.
        """
        return not self._is_checked_out

    def __str__(self):
        """
        Returns a string representation of the Book object.
        """
        return f"{self.title} by {self.author}"


class Library:
    """
    Manages a collection of books.

    Attributes:
        _books (list): A private list to store Book instances.
    """
    def __init__(self):
        """
        Initializes a new Library instance with an empty list of books.
        """
        self._books = []

    def add_book(self, book: Book):
        """
        Adds a Book object to the library's collection.

        Args:
            book (Book): The Book object to add.
        """
        if isinstance(book, Book):
            self._books.append(book)
            # print(f"Added '{book.title}' to the library.")
        else:
            print("Error: Only Book objects can be added to the library.")

    def check_out_book(self, title: str):
        """
        Finds a book by its title and marks it as checked out if available.

        Args:
            title (str): The title of the book to check out.
        """
        found = False
        for book in self._books:
            if book.title == title:
                if book.is_available():
                    book.check_out()
                    print(f"'{title}' has been checked out.")
                else:
                    print(f"'{title}' is already checked out.")
                found = True
                break
        if not found:
            print(f"'{title}' not found in the library.")

    def return_book(self, title: str):
        """
        Finds a book by its title and marks it as returned (available).

        Args:
            title (str): The title of the book to return.
        """
        found = False
        for book in self._books:
            if book.title == title:
                if not book.is_available():
                    book.return_book()
                    print(f"'{title}' has been returned.")
                else:
                    print(f"'{title}' was not checked out.")
                found = True
                break
        if not found:
            print(f"'{title}' not found in the library.")

    def list_available_books(self):
        """
        Prints the title and author of all books currently available in the library.
        """
        available_count = 0
        for book in self._books:
            if book.is_available():
                print(f"{book.title} by {book.author}")
                available_count += 1
        if available_count == 0:
            print("No books currently available.")

