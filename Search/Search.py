from Search.SearchBy import SearchBy


def Search(data, phrase, searchBy=SearchBy.ALL):
    return [x for x in data if x.matches_search(phrase, searchBy)]


class Searcher:
    def __init__(self):
        self._data_store = None

    @classmethod
    def create_with_data(cls, data_store):
        search = Searcher()
        search._data_store = data_store
        return search

    def search_actors(self, phrase, searchBy=SearchBy.ALL):
        return Search(self._data_store.actors, phrase, searchBy)

    def search_books(self, phrase, searchBy=SearchBy.ALL):
        return Search(self._data_store.books, phrase, searchBy)

    def search_subjects(self, phrase, searchBy=SearchBy.ALL):
        return Search(self._data_store.subjects, phrase, searchBy)

    def search_sub_subjects(self, phrase, searchBy=SearchBy.ALL):
        return Search(self._data_store.sub_subjects, phrase, searchBy)

    def search_sub_sub_subjects(self, phrase, searchBy=SearchBy.ALL):
        return Search(self._data_store.sub_sub_subjects, phrase, searchBy)