from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from Objects.OtherStatistics import OtherStatistics
from GUI.EntryLabel import entry_label
from GUI.Stylesheets import *


class OtherWidget(QFrame):
    def __init__(self, parent, bookStat: OtherStatistics):
        super().__init__(parent)
        self._parent= parent
        self._bookStat = bookStat
        self.setStyleSheet(WIDGET_STYLESHEET)

        vert_layout = QVBoxLayout(self)
        vert_layout.setAlignment(Qt.AlignVCenter)

        entry_label(self, vert_layout, "<b>Books by Cover</b>")
        entry_label(self, vert_layout, "<b>Paperback</b>: " + str(bookStat.papercover[0]) + " (" + str(bookStat.papercover[1] * 100) + "%)")
        entry_label(self, vert_layout, "<b>Hardcover</b>: " + str(bookStat.hardcover[0]) + " (" + str(bookStat.hardcover[1] * 100) + "%)")
        entry_label(self, vert_layout, "<b>Mass Market Paperback</b>: " + str(bookStat.mass_market_papercover[0]) + " (" + str(bookStat.mass_market_papercover[1] * 100) + "%)")
        entry_label(self, vert_layout, "")
        entry_label(self, vert_layout, "<b>Books by Price</b>")
        entry_label(self, vert_layout, "<b>Below $15</b>: " + str(bookStat.below15[0]) + " (" + str(bookStat.below15[1] * 100) + "%)")
        entry_label(self, vert_layout, "<b>From $15 to $30</b>: " + str(bookStat.from15to30[0]) + " (" + str(bookStat.from15to30[1] * 100) + "%)")
        entry_label(self, vert_layout, "<b>Above $30</b>: " + str(bookStat.above30[0]) + " (" + str(bookStat.above30[1] * 100) + "%)")
        entry_label(self, vert_layout, "")
        entry_label(self, vert_layout, "<b>Avg. Price</b>: $" + "{:.2f}".format(round(bookStat.avg_price, 2)))
        entry_label(self, vert_layout, "<b>Most expensive book: $" + str(bookStat.most_expensive.price) + "</b> " + str(bookStat.most_expensive.title) + " by " + str(bookStat.most_expensive.author))

    @property
    def widgetId(self):
        return self._bookStat.widgetId