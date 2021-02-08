from enum import Enum

from PyQt5.QtWidgets import QMessageBox

from ChartsReports.Charts import create_cover_stats_bar_chart, create_time_distribution_bar_chart, create_price_bar_chart
from GUI.AuthorWidget import AuthorWidget
from GUI.BookWidget import BookWidget
from GUI.OtherWidgets import OtherWidget
from GUI.SubjectWidget import SubjectWidget
from GUI.TimeWidget import TimeWidget
from Search.Search import Search
from Search.SearchParameters import SearchParameters
from StatisticsGenerator import StatisticsGenerator


class DataType(Enum):
    BOOK = 1
    AUTHOR = 2
    SUBJECT = 3
    TIME = 4
    OTHER = 5


class Controller:
    def __init__(self, dataStore, excel):
        self._excel = excel
        self._data_store = dataStore

        self._stat_generator = StatisticsGenerator.create_with_data(self._data_store)
        self._authors_stats = self._stat_generator.get_author_statistics().authors_as_list
        self._time_stats = self._stat_generator.get_time_statistics().years_as_list
        self._subject_stats = self._stat_generator.get_subject_statistics().subjects_as_list
        self._other_stats = [self._stat_generator.get_other_statistics()]

        self._data_type = DataType.BOOK
        self._search_parameters = SearchParameters()
        self.on_search_update_content = None
        self.on_search_update_sidebar = None

        self._full_sidemenu = True

    @property
    def data_store(self):
        return self._data_store

    @property
    def excel(self):
        return self._excel

    @property
    def search_parameters(self):
        return self._search_parameters

    @property
    def matching_books(self):
        return Search(self._data_store.books, self._search_parameters.search_phrase, self._search_parameters.search_by)

    @property
    def matching_authors(self):
        return Search(self._authors_stats, self._search_parameters.search_phrase, self._search_parameters.search_by)

    @property
    def matching_subjects(self):
        return Search(self._subject_stats, self._search_parameters.search_phrase, self._search_parameters.search_by)

    @property
    def matching_others(self):
        return self._other_stats

    @property
    def matching_time(self):
        return Search(self._time_stats, self._search_parameters.search_phrase, self._search_parameters.search_by)

    def show_book_cover_chart(self):
        self._chart = create_cover_stats_bar_chart(self._stat_generator.get_other_statistics())
        self._chart.show()

    def show_book_price_chart(self):
        self._chart = create_price_bar_chart(self._stat_generator.get_other_statistics())
        self._chart.show()

    def show_books_per_year_chart(self):
        self._chart = create_time_distribution_bar_chart(self._stat_generator.get_time_statistics())
        self._chart.show()

    def update_search(self):
        if self.on_search_update_content:
            if self._data_type == DataType.BOOK:
                self.on_search_update_content(self.matching_books, lambda p, d: BookWidget(p, d))
            elif self._data_type == DataType.AUTHOR:
                self.on_search_update_content(self.matching_authors, lambda p, d: AuthorWidget(p, d))
            elif self._data_type == DataType.SUBJECT:
                self.on_search_update_content(self.matching_subjects, lambda p, d: SubjectWidget(p, d))
            elif self._data_type == DataType.TIME:
                self.on_search_update_content(self.matching_time, lambda p, d: TimeWidget(p, d))
            else:
                self.on_search_update_content(self.matching_others, lambda p, d: OtherWidget(p, d))

        if self.on_search_update_sidebar:
            full = self._data_type == DataType.BOOK
            if full != self._full_sidemenu:
                self.on_search_update_sidebar(full)
                self._full_sidemenu = full

    def update_search_params(self, phrase, searchBy):
        self._search_parameters.search_phrase = phrase
        self._search_parameters.search_by = searchBy
        self.update_search()

    def update_search_by(self, searchBy):
        self._search_parameters.search_by = searchBy
        self.update_search()

    def update_search_phrase(self, phrase):
        self._search_parameters.search_phrase = phrase
        self.update_search()

    def update_data_type(self, dataType):
        self._data_type = dataType
        self.update_search()

    def generate_report(self):
        self._excel.generate()
