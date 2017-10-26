from src.exception import OrderingError
import configparser
import json


class Storage():
    """
        Handles and store all the books in memory. Contains methods and
        routines to load and manipulate the books set.
    """
    def __init__(self):
        self._books = []
        self._sort_priority = []
        self._parser = configparser.SafeConfigParser()

        self.load_config()

    @property
    def books(self):
        return self._books

    def set_books(self, books_list):
        self._books = books_list

    def insert_book(self, book):
        self._books.append(book)
    
    def sort(self):
        """
            Applies the ordenation algorithm to the books stored, basde on
            the priorities defined by 'sort_priority'.
        """
        if(not len(self._sort_priority)):
            return []
    
        for item in reversed(self._sort_priority):
            reverse = True if item[1] == 'descendant' else False
            self._books = sorted(self._books, 
                                 key=lambda k: k[item[0]],
                                 reverse=reverse)
        
        return self._books

    def load_json(self, filename):
        """
            Loads a JSON file with the books of the library. The file has
            the following style:
                {
                    "id" : 1,
                    "title" : "Java How To Program",
                    "author" : "Deitel & Deitel",
                    "year" : 2007
                }
        """
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
            self._books.extend(data['books'])
        except json.decoder.JSONDecodeError:
            pass

    def load_config(self, filename='.config'):
        """
            Opens the configuration file and loads the sorting settings
            (priority and direction).
        """
        priorities = self._read_sort_order(filename)
        self._sort_priority = []

        if '' in priorities:
            return
        
        for item in priorities:
            attribute, direction = item.split(' ')
            self._sort_priority.append((attribute.lower(), direction.lower()))

    def _read_sort_order(self, filename):
        """
            Attempts to read the configuration file, treating the exceptions
            that it may raise properly.
        """
        try:
            self._parser.read(filename)
            priorities = self._parser.get('sort', 'order').split(", ")
            return priorities
        except configparser.NoOptionError:
            raise OrderingError("No option 'order' defined")
        except configparser.DuplicateOptionError:
            raise OrderingError("Multiple definitions of 'order' parameter")
