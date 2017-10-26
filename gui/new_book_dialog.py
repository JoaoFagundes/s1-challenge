import sys
from gui.book_dialog import Ui_new_book
from PyQt5.QtWidgets import QDialog


class NewBookDialog(QDialog, Ui_new_book):

    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)

        self.insert_button.clicked.connect(self._insert_book)
        self._book = {}
        self._valid = False

    def _insert_book(self):
        self._book['id'] = self.id_entry.text()
        self._book['title'] = self.title_entry.text()
        self._book['author'] = self.author_entry.text()
        self._book['year'] = self.year_entry.text()
        self._valid = "" not in self._book.values()
        self.close()

    def get_book(self):
        return self._book, self._valid
