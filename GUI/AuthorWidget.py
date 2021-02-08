from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from Objects.AuthorStatistics import AuthorStatistics
from GUI.EntryLabel import entry_label
from GUI.Stylesheets import *


class AuthorWidget(QFrame):
    def __init__(self, parent, author: AuthorStatistics):
        super().__init__(parent)
        self._parent = parent
        self._author = author

        self.setStyleSheet(WIDGET_STYLESHEET)

        vert_layout = QVBoxLayout(self)
        vert_layout.setAlignment(Qt.AlignVCenter)

        entry_label(self, vert_layout, "<b>" + str(author.name) + "</b>", "font-size:15px; font-weight:500")
        entry_label(self, vert_layout, "<b>Number of Books</b>: " + str(author.number_of_books))
        entry_label(self, vert_layout, "<b>Bio</b>: " + str(author.bio))
        entry_label(self, vert_layout, "<b>Books</b>: " + str(author.books_as_string))

    @property
    def widgetId(self):
        return self._author.widgetId