from Search.SearchBy import SearchBy
from Objects.SearchableObject import SearchableObject


class Author(SearchableObject):
    def __init__(self):
        self._id = None
        self._name = None
        self._bio = None

    @classmethod
    def create_with_data(cls, author_id, name, bio):
        author = Author()
        author._id = author_id
        author._name = name
        author._bio = author.prep_bio(bio)
        return author

    @property
    def author_id(self):
        return self._id

    @property
    def name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    @property
    def bio(self):
        return self._bio

    def set_bio(self, bio):
        self._bio = bio

    def prep_bio(self, bio):
        return bio.replace("<p>", "", 1).replace("</p>", "", 1).replace("<P>", "", 1).replace("</P>", "", 1)

    def matches_search(self, searched_phrase, search_by=SearchBy.ALL):
        return (False if self._name is None else searched_phrase.lower() in self._name.lower()) or \
               (False if self._id is None else searched_phrase.lower() in str(self._id).lower())

    def __str__(self):
        return str(self._id) + ". " + self._name
