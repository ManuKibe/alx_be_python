# book_class.py

class Book:
    """
    Represents a book with a title, author, and publication year.
    This class demonstrates the use of Python's magic methods:
    __init__ (constructor), __del__ (destructor),
    __str__ (informal string representation), and
    __repr__ (official string representation).
    """

    def __init__(self, title: str, author: str, year: int):
        """
        Initializes a new Book instance.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
            year (int): The publication year of the book.
        """
        self.title = title
        self.author = author
        self.year = year
        # print(f"Book '{self.title}' created.") # Optional: for debugging creation

    def __del__(self):
        """
        Destructor method.
        This method is called when the object is about to be destroyed (deleted).
        It prints a message indicating which book is being deleted.
        """
        print(f"Deleting {self.title}")

    def __str__(self):
        """
        Returns the informal, user-friendly string representation of the Book object.
        This is what gets printed when you use `print(book_instance)`.
        """
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """
        Returns the official string representation of the Book object.
        This string should ideally be unambiguous and, if possible,
        a valid Python expression that could be used to recreate the object.
        This is what gets printed when you use `repr(book_instance)`.
        """
        return f"Book('{self.title}', '{self.author}', {self.year})"

