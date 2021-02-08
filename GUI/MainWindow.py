from PyQt5.QtCore import QRect
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import *

from GUI.ContentViewWidget import ContentViewWidget
from GUI.Sidebar import Sidebar
from Search.SearchBy import SearchBy


class MainWindow(QWidget):
    def __init__(self, parent, controller):
        super().__init__(parent)

        widget = QWidget(parent)
        widget.setGeometry(QRect(20, 60, 881, 531))

        layout = QHBoxLayout(widget)
        layout.setContentsMargins(0, 0, 0, 0)

        self._controller = controller
        self._sidebar = Sidebar(layout, self._controller)
        self._content = ContentViewWidget(layout, widget, self._controller)
        self._controller.update_search_params("", SearchBy.ALL)