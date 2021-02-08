from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from GUI.EntryLabel import entry_label
from Objects.SubjectStatistics import SubjectStatistics
from GUI.Stylesheets import *


class SubjectWidget(QFrame):
    def __init__(self, parent, subject: SubjectStatistics):
        super().__init__(parent)
        self._parent = parent
        self._subject = subject
        self.setStyleSheet(WIDGET_STYLESHEET)
    
        vert_layout = QVBoxLayout(self)
        vert_layout.setAlignment(Qt.AlignVCenter)
    
        entry_label(self, vert_layout, "<b>" + str(subject.subject_name) + "</b>", "font-size:15px; font-weight:500")
        entry_label(self, vert_layout, "<b>Number of Books</b>: " + str(subject.number_of_books))
        entry_label(self, vert_layout, "<b>Market share</b>: " + str(round(subject.market_share * 100, 2)) + "%")
        entry_label(self, vert_layout, "<b>Avg. Price</b>: ${:.2f}".format(round(subject.avg_price, 2)))
        entry_label(self, vert_layout, "<b>Books</b>: " + str(subject.books_as_string))

    @property
    def widgetId(self):
        return self._subject.widgetId
