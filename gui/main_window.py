# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_main_window(object):
    def setupUi(self, main_window):
        main_window.setObjectName("main_window")
        main_window.resize(810, 410)
        main_window.setMaximumSize(QtCore.QSize(810, 410))
        main_window.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(main_window)
        self.centralwidget.setObjectName("centralwidget")
        self.books_table = QtWidgets.QTableWidget(self.centralwidget)
        self.books_table.setGeometry(QtCore.QRect(160, 10, 641, 191))
        self.books_table.setObjectName("books_table")
        self.books_table.setColumnCount(4)
        self.books_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.books_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.books_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.books_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.books_table.setHorizontalHeaderItem(3, item)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 141, 110))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.new_book_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.new_book_button.setObjectName("new_book_button")
        self.verticalLayout.addWidget(self.new_book_button)
        self.clear_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.clear_button.setObjectName("clear_button")
        self.verticalLayout.addWidget(self.clear_button)
        self.sort_books_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.sort_books_button.setObjectName("sort_books_button")
        self.verticalLayout.addWidget(self.sort_books_button)
        self.listView = QtWidgets.QListView(self.centralwidget)
        self.listView.setGeometry(QtCore.QRect(160, 230, 641, 151))
        self.listView.setObjectName("listView")
        self.ordened_label = QtWidgets.QLabel(self.centralwidget)
        self.ordened_label.setGeometry(QtCore.QRect(10, 230, 141, 20))
        self.ordened_label.setObjectName("ordened_label")
        main_window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(main_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 810, 26))
        self.menubar.setObjectName("menubar")
        self.menuLoad_Books = QtWidgets.QMenu(self.menubar)
        self.menuLoad_Books.setObjectName("menuLoad_Books")
        main_window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(main_window)
        self.statusbar.setObjectName("statusbar")
        main_window.setStatusBar(self.statusbar)
        self.load_books = QtWidgets.QAction(main_window)
        self.load_books.setObjectName("load_books")
        self.menuLoad_Books.addAction(self.load_books)
        self.menubar.addAction(self.menuLoad_Books.menuAction())

        self.retranslateUi(main_window)
        QtCore.QMetaObject.connectSlotsByName(main_window)

    def retranslateUi(self, main_window):
        _translate = QtCore.QCoreApplication.translate
        main_window.setWindowTitle(_translate("main_window", "MainWindow"))
        item = self.books_table.horizontalHeaderItem(0)
        item.setText(_translate("main_window", "ID"))
        item = self.books_table.horizontalHeaderItem(1)
        item.setText(_translate("main_window", "Title"))
        item = self.books_table.horizontalHeaderItem(2)
        item.setText(_translate("main_window", "Author"))
        item = self.books_table.horizontalHeaderItem(3)
        item.setText(_translate("main_window", "Year"))
        self.new_book_button.setText(_translate("main_window", "Insert Book"))
        self.clear_button.setText(_translate("main_window", "Clear Books List"))
        self.sort_books_button.setText(_translate("main_window", "Sort Books"))
        self.ordened_label.setText(_translate("main_window", "Sorted list of Books:"))
        self.menuLoad_Books.setTitle(_translate("main_window", "File"))
        self.load_books.setText(_translate("main_window", "Load Books"))
        self.load_books.setShortcut(_translate("main_window", "Ctrl+O"))

