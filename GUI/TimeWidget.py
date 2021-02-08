from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from GUI.EntryLabel import entry_label
from Objects.TimeStatistics import AnnualStatistics
from GUI.Stylesheets import *


class TimeWidget(QFrame):
    def __init__(self, parent, year: AnnualStatistics):
        super().__init__(parent)
        self._parent = parent
        self._year = year
        self.setStyleSheet(WIDGET_STYLESHEET)

        vert_layout = QVBoxLayout(self)
        vert_layout.setAlignment(Qt.AlignVCenter)

        entry_label(self, vert_layout, "<b>" + str(year.year) + "</b> - Books: " + str(year.number_of_books) + " - Avg. Price: $" + "{:.2f}".format(round(year.avg_price, 2)), "font-size:15px;")
        for k, v in year.months.items():
            entry_label(self, vert_layout, "<b>" + str(v.month) + "</b> - Books: " + str(v.number_of_books) + " - Avg. Price: $" + "{:.2f}".format(round(v.avg_price, 2)))

    @property
    def widgetId(self):
        return self._year.widgetId