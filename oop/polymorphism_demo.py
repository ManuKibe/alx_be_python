# library_system.py

class Book:
    """
    Base class representing a generic book.
    Attributes:
        title (str): The title of the book.
        author (str): The author of the book.
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

    def __str__(self):
        """
        Returns a user-friendly string representation of the Book object.
        """
        return f"Book: {self.title} by {self.author}"


class EBook(Book):
    """
    Derived class representing an electronic book, inheriting from Book.
    Additional Attributes:
        file_size (int): The size of the e-book file in KB.
    """
    def __init__(self, title: str, author: str, file_size: int):
        """
        Initializes a new EBook instance.
        Calls the base class (Book) constructor and initializes file_size.
        Args:
            title (str): The title of the e-book.
            author (str): The author of the e-book.
            file_size (int): The size of the e-book file in KB.
        """
        super().__init__(title, author)  # Call the constructor of the base class (Book)
        self.file_size = file_size

    def __str__(self):
        """
        Returns a user-friendly string representation of the EBook object,
        including its file size.
        """
        # Reuse the __str__ from the base class for common attributes
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"


class PrintBook(Book):
    """
    Derived class representing a physical print book, inheriting from Book.
    Additional Attributes:
        page_count (int): The number of pages in the print book.
    """
    def __init__(self, title: str, author: str, page_count: int):
        """
        Initializes a new PrintBook instance.
        Calls the base class (Book) constructor and initializes page_count.
        Args:
            title (str): The title of the print book.
            author (str): The author of the print book.
            page_count (int): The number of pages in the print book.
        """
        super().__init__(title, author)  # Call the constructor of the base class (Book)
        self.page_count = page_count

    def __str__(self):
        """
        Returns a user-friendly string representation of the PrintBook object,
        including its page count.
        """
        # Reuse the __str__ from the base class for common attributes
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


class Library:
    """
    Represents a library that manages a collection of various types of books.
    This class demonstrates composition, as it 'has-a' list of books.
    Attributes:
        books (list): A list to store instances of Book, EBook, and PrintBook.
    """
    def __init__(self):
        """
        Initializes a new Library instance with an empty list of books.
        """
        self.books = []

    def add_book(self, book):
        """
        Adds a book (Book, EBook, or PrintBook instance) to the library's collection.
        Args:
            book: An instance of Book, EBook, or PrintBook.
        """
        # Basic type checking to ensure only book-like objects are added
        if isinstance(book, (Book, EBook, PrintBook)):
            self.books.append(book)
            # print(f"Added '{book.title}' to the library.") # Optional: for debugging
        else:
            print(f"Error: Cannot add an unsupported type to the library.")

    def list_books(self):
        """
        Prints the details of each book currently in the library.
        Polymorphism is demonstrated here as the __str__ method of each
        book object (Book, EBook, or PrintBook) is called appropriately.
        """
        if not self.books:
            print("The library is empty.")
            return

        for book in self.books:
            print(book) # This will automatically call the __str__ method of the respective book object

