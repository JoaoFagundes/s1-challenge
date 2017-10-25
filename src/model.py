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

    def load_json(self, filename):
        with open(filename, 'r') as file:
            data = json.load(file)
        self._books = data['books']

    def load_config(self, filename='.config'):
        """
            Opens the configuration file and loads the sorting settings
            (priority and direction).
        """
        try:
            self._parser.read(filename)
            priorities = self._parser.get('sort', 'order').split(", ")
        except configparser.NoOptionError:
            raise OrderingError 

        self._sort_priority = []
        for item in priorities:
            attribute, direction = item.split(' ')
            self._sort_priority.append((attribute.lower(), direction.lower()))
