# make the necessary packages available
import json # json package to read the json file
from datetime import date # date module of datetime package to get current year

# Define Book class
class Book:
    """Book class"""
    language = "English" # class attribute

    def __init__(self, title, author, year):
        """Instantiate 

        Args:
            title (str): Title of the book
            author (str): Author of the book
            year (int): Publication year
        """
        self.title = title
        self.author = author
        self.year = year
        
        this_year = date.today().year # current year
        self.age = this_year - self.year # difference between current year and publication year

        self.characters = set() # starting set for characters
        # this is a set to make sure only unique names are captured

    def get_age(self):
        """Print a text indicating the age of the book.

        Returns:
            _str_: Text with the age of the book.
        """
        if self.age < 0:
            # if the publication date is in the future
            return f"This book will be published in {-self.age} years."
        else:
            # if the publication thate is not in the future
            return f"This book is {self.age} years old."

    def add_character(self, name):
        """Add a character to the list of characters.

        Args:
            name (str): Name of the character to add.
        """
        self.characters.add(name) # add the character name to the set of characters

    def __str__(self):
        """Define `print()` behavior.

        Returns:
            str: Text describing different attributes of the book.
        """
        sent_1 = f"{self.title} was written by {self.author} in {self.language}."
        sent_2 = f"It was published in {self.year}, that is, {self.age} years ago."
        # the if statement considers whether any characters have been added
        if len(self.characters) > 0:
            sent_3 = f"The main characters are: {', '.join(self.characters)}."
        else:
            sent_3 = ""
        # pritn one line per sentence
        return "\n".join([sent_1, sent_2, sent_3])

# define DiscWorldBook class, a child of the Book class
class DiscWorldBook(Book):
    """Subclass of Book for Discworld books."""
    series = "Discworld" # class attribute

    def __init__(self, title, year):
        """Instantiate the DiscWorldBook class.
        
        This is a specification of the Book with an additional class attribute "series"
        and always "Terry Pratchett" as author.

        Args:
            title (str): Title of the book
            year (int): Publication year
        """
        super().__init__(title, "Terry Pratchett", year) # instantiate parent class
        self.subseries = "" # start empty subseries attribute

    def set_subseries(self, subseries):
        """Define the subseries that the book belongs to.

        Args:
            subseries (str): Name of the subseries.
        """
        self.subseries = subseries # change the value of the subseries attribute
    
    def __str__(self):
        """Define behavior of print().

        Returns:
            str: Description of the book, including the subseries.
        """
        parent = super().__str__() # retrieve the parent method output
        # add a sentence if the subseries name has been defined
        if self.subseries:
            return parent + f'\nThis book belongs to the "{self.subseries}" subseries of {self.series}.'
        else:
            return parent

# open the json file
books_file = 'books.json' # assign filename to a string variable
with open(books_file, encoding = 'utf-8') as f:
    # open file and use json to parse it
    books = json.load(f)
    """books is now a list of dictionaries.
    
    Each dictionary has the following keys:
    
    - "title" (a string) indicates the book title
    - "author" (a string) indicates the author of the book
    - "year" (an integer) indicates the publication year
    - "language" (a string) indicates the language of the book
    - "main_characters" (a list of strings) lists the names of the main characters.
    
    In one case, the language is not "English" and there are no characters.
    In addition, Discworld books also have a "subseries" key.
    We can use this information to distinguish which books should be turned
    into instances of `DiscWorldBook` and which into instances of `Book`.
    """

# go through each of the items in the list
for book in books:
    # if there is a 'subseries' key, it is a Discworld book
    if 'subseries' in book:
        # create a DiscWorldBook instance with just the title and publication year
        my_book = DiscWorldBook(book['title'], book['year'])
        # Specify the subseries
        my_book.subseries = book['subseries']
    else:
        # create a Book instance with title, author and year
        my_book = Book(book['title'], book['author'], book['year'])
    
    # if the language is not English (the default, class attribute), change it
    if book['language'] != "English":
        my_book.language = book['language']
        
    # go through each character in the 'main_characters' key and add it to the book
    for character in book['main_characters']:
        my_book.add_character(character)
        
    # print the book contents
    print(my_book)
    
    # print a separating line between books
    print('----')
    