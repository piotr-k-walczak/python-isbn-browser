from Search.SearchBy import SearchBy


class SearchableObject:
    def matches_search(self, searched_phrase, search_by=SearchBy.ALL):
        raise NotImplementedError()
