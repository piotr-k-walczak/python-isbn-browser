from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from Objects.Book import Book
from GUI.EntryLabel import entry_label
from GUI.Stylesheets import *


class BookWidget(QFrame):
    def __init__(self, parent, book):
        super().__init__(parent)
        self._parent = parent
        self._book = book

        self.setStyleSheet(WIDGET_STYLESHEET)

        vert_layout = QVBoxLayout(self)
        vert_layout.setAlignment(Qt.AlignVCenter)

        entry_label(self, vert_layout, "<b>" + str(book.title) + "</b>", "font-size:15px; font-weight:500")
        entry_label(self, vert_layout, "<b>Author</b>: " + str(book.author))
        entry_label(self, vert_layout, "<b>Publisher</b>: " + str(book.publisher))
        entry_label(self, vert_layout, "<b>ISBN10</b>: " + str(book.isbn10))
        entry_label(self, vert_layout, "<b>ISBN13</b>: " + str(book.isbn13))
        entry_label(self, vert_layout, "<b>Price</b>: $" + str(round(book.price, 2)))

        if len(book.assigned_subjects) > 0:
            entry_label(self, vert_layout, "<b>Subjects</b>: " + str(book.assigned_subjects_as_string))

        if book.overview != "nan":
            entry_label(self, vert_layout, "<b>Overview</b>: " + str(book.overview))

    @property
    def widgetId(self):
        return self._book.widgetId