from Objects.AuthorStatistics import AuthorsStatistics
from Objects.SubjectStatistics import  SubjectsStatistics
from Objects.TimeStatistics import TimeStatistics
from Objects.OtherStatistics import OtherStatistics

class StatisticsGenerator:
    def __init__(self):
        self._dataStore = None

    @classmethod
    def create_with_data(cls, dataStore):
        generator = StatisticsGenerator()
        generator._dataStore = dataStore
        return generator

    def get_author_statistics(self) -> AuthorsStatistics:
        statistics = AuthorsStatistics()
        for auth in self._dataStore.authors:
            statistics.add_author(auth)
        for book in self._dataStore.books:
            statistics.add_book(book)
        return statistics

    def get_subject_statistics(self) -> SubjectsStatistics:
        statistics = SubjectsStatistics()
        for sub in self._dataStore.all_subjects:
            statistics.add_subject(sub)
        for book in self._dataStore.books:
            statistics.add_book(book)
        statistics.confirm()
        return  statistics

    def get_time_statistics(self) -> TimeStatistics:
        statistics = TimeStatistics()
        for book in self._dataStore.books:
            statistics.add_book(book)
        return  statistics

    def get_other_statistics(self) -> OtherStatistics:
        return OtherStatistics(self._dataStore.books)

