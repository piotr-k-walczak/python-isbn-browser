from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from Controller import Controller, DataType
from GUI.Stylesheets import *


class Toolbar(QWidget):
    def __init__(self, parent, controller: Controller):
        super().__init__(parent)

        self._controller = controller
        self.setGeometry(QRect(20, 10, 781, 41))
        self.setObjectName("toolbarWidget")

        horizontal_layout = QHBoxLayout(self)
        horizontal_layout.setContentsMargins(0, 0, 0, 0)
        horizontal_layout.setSpacing(10)
        horizontal_layout.setAlignment(Qt.AlignLeft)

        self.browse_books_button = toolbar_button(self, "Browse Books", lambda _: self._controller.update_data_type(DataType.BOOK))
        horizontal_layout.addWidget(self.browse_books_button)

        self.books_stats_button = toolbar_button(self, "Books Stats", lambda _: self._controller.update_data_type(DataType.OTHER))
        horizontal_layout.addWidget(self.books_stats_button)

        self.author_stats_button = toolbar_button(self, "Authors Stats", lambda _: self._controller.update_data_type(DataType.AUTHOR))
        horizontal_layout.addWidget(self.author_stats_button)

        self.subject_stats_button = toolbar_button(self, "Subjects Stats", lambda _: self._controller.update_data_type(DataType.SUBJECT))
        horizontal_layout.addWidget(self.subject_stats_button)

        self.time_stats_button = toolbar_button(self, "Books in Time", lambda _: self._controller.update_data_type(DataType.TIME))
        horizontal_layout.addWidget(self.time_stats_button)


def toolbar_button(parent, text, callback):
    button = QToolButton(parent)
    button.setText(text)
    button.setStyleSheet(TOP_BUTTON_STYLESHEET)
    button.clicked.connect(callback)
    return button
