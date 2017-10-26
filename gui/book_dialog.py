# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'new_book_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_new_book(object):
    def setupUi(self, new_book):
        new_book.setObjectName("new_book")
        new_book.resize(387, 235)
        self.id_dialog = QtWidgets.QLabel(new_book)
        self.id_dialog.setGeometry(QtCore.QRect(10, 20, 141, 30))
        self.id_dialog.setObjectName("id_dialog")
        self.title_dialog = QtWidgets.QLabel(new_book)
        self.title_dialog.setGeometry(QtCore.QRect(10, 60, 141, 30))
        self.title_dialog.setObjectName("title_dialog")
        self.author_dialog = QtWidgets.QLabel(new_book)
        self.author_dialog.setGeometry(QtCore.QRect(10, 100, 141, 30))
        self.author_dialog.setObjectName("author_dialog")
        self.year_dialog = QtWidgets.QLabel(new_book)
        self.year_dialog.setGeometry(QtCore.QRect(10, 140, 141, 30))
        self.year_dialog.setObjectName("year_dialog")
        self.id_entry = QtWidgets.QLineEdit(new_book)
        self.id_entry.setGeometry(QtCore.QRect(100, 20, 261, 32))
        self.id_entry.setObjectName("id_entry")
        self.title_entry = QtWidgets.QLineEdit(new_book)
        self.title_entry.setGeometry(QtCore.QRect(100, 60, 261, 32))
        self.title_entry.setObjectName("title_entry")
        self.author_entry = QtWidgets.QLineEdit(new_book)
        self.author_entry.setGeometry(QtCore.QRect(100, 100, 261, 32))
        self.author_entry.setObjectName("author_entry")
        self.year_entry = QtWidgets.QLineEdit(new_book)
        self.year_entry.setGeometry(QtCore.QRect(100, 140, 261, 32))
        self.year_entry.setObjectName("year_entry")
        self.insert_button = QtWidgets.QPushButton(new_book)
        self.insert_button.setGeometry(QtCore.QRect(270, 190, 94, 32))
        self.insert_button.setObjectName("insert_button")

        self.retranslateUi(new_book)
        QtCore.QMetaObject.connectSlotsByName(new_book)

    def retranslateUi(self, new_book):
        _translate = QtCore.QCoreApplication.translate
        new_book.setWindowTitle(_translate("new_book", "Dialog"))
        self.id_dialog.setText(_translate("new_book", "ID: "))
        self.title_dialog.setText(_translate("new_book", "Title:"))
        self.author_dialog.setText(_translate("new_book", "Author:"))
        self.year_dialog.setText(_translate("new_book", "Year:"))
        self.insert_button.setText(_translate("new_book", "Insert"))

