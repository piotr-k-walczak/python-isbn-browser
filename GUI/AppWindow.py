import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from GUI.Stylesheets import *
from Controller import Controller
from GUI.MainWindow import MainWindow
from GUI.Toolbar import Toolbar


class AppWindow:
    def __init__(self, controller: Controller):
        super().__init__()

        self._controller = controller

        self._app = QApplication([])

        self._window = QWidget()
        self._window.setWindowTitle(QCoreApplication.translate("Project - ISBN Analysis", "Project - ISBN Analysis"))
        self._window.setFixedSize(930, 600)

        self._toolbar = Toolbar(self._window, self._controller)
        self._main = MainWindow(self._window, self._controller)
        self._window.show()

        sys.exit(self._app.exec())