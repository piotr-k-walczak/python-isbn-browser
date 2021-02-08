import sys

from PyQt5.QtWidgets import *

from GUI.AppWindow import AppWindow
from Controller import Controller
from DataSources import DataSources
from DataStore import DataStore
from ChartsReports.Excel import ExcelReportGenerator


class App:
    def __init__(self):

        data_sources = DataSources(
            authors="data/author.csv",
            books="data/book.csv",
            books_to_subjects="data/book2subjects.csv",
            subjects="data/subject.csv",
            sub_subjects="data/sub_subject.csv",
            sub_sub_subjects="data/sub_sub_subject.csv"
        )

        self._data_store = DataStore(data_sources)
        self._excel = ExcelReportGenerator(self._data_store)
        self._controller = Controller(self._data_store, self._excel)

        self._window = AppWindow(self._controller)

        sys.exit(self._app.exec_())