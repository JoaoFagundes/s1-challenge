import json


class Storage():
    """
        Handles and store all the books in memory. Contains methods and
        routines to load and manipulate the books set.
    """
    def __init__(self):
        self._books = []

    @property
    def books(self):
        return self._books

    def set_books(self, books_list):
        self._books = books_list

    def load_json(self, filename):
        with open(filename, 'r') as file:
            data = json.load(file)
        self._books = data['books']
