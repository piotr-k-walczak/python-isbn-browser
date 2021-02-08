from Objects.SearchableObject import SearchableObject
from Search.SearchBy import SearchBy


class Book(SearchableObject):
    def __init__(self):
        self._id = None
        self._title = None
        self._author = None
        self._author_id = None
        self._isbn10 = None
        self._isbn13 = None
        self._cover = None
        self._pages = None
        self._price = None
        self._release_date = None
        self._overview = None
        self._synopsis = None
        self._publisher = None
        self._assigned_author = None
        self._assigned_subjects = []

    @classmethod
    def createWithData(cls, book_id, title, author, author_id, isbn10, isbn13, cover, pages, price, release_date, overview,
                       synopsis, publisher):
        book = Book()
        book._id = book_id
        book._title = title
        book._author = author
        book._author_id = author_id
        book._isbn10 = isbn10
        book._isbn13 = isbn13
        book._cover = cover
        book._pages = pages
        book._price = float(str(price)[1:]) if str(price)[0] == '$' else 0
        book._release_date = release_date
        book._overview = book.prep_overview(str(overview))
        book._synopsis = synopsis
        book._publisher = publisher
        return book

    @property
    def synopsis(self):
        return self._synopsis

    @property
    def publisher(self):
        return self._publisher

    @property
    def release_date(self):
        return self._release_date

    @property
    def assigned_subjects(self):
        return self._assigned_subjects

    @property
    def assigned_subjects_as_string(self):
        return ", ".join([sub.subject_name for sub in self._assigned_subjects])

    @property
    def assigned_author(self):
        return self._assigned_author

    @property
    def cover(self):
        return self._cover

    @property
    def book_id(self):
        return self._id

    @property
    def author(self):
        return self._author

    @property
    def title(self):
        return self._title

    @property
    def author_id(self):
        return self._author_id

    @property
    def isbn10(self):
        return self._isbn10

    @property
    def isbn13(self):
        return self._isbn13

    @property
    def pages(self):
        return self._pages

    @property
    def overview(self):
        return self._overview

    @property
    def price(self):
        return self._price

    @property
    def widgetId(self):
        return "B_" + str(self._id)

    def prep_overview(self, overview):
        return overview.replace("<p>", "", 1).replace("</p>", "", 1).replace("<P>", "", 1).replace("</P>", "", 1)

    def assign_subject(self, subject):
        self._assigned_subjects.append(subject)

    def assign_author(self, author):
        self._assigned_author = author
        if author:
            self._author = author.name

    def matches_title(self, searched_phrase):
        return False if self._title is None else searched_phrase.lower() in self._title.lower()

    def matches_author(self, searched_phrase):
        return False if self._author is None else searched_phrase.lower() in self._author.lower()

    def matches_publisher(self, searched_phrase):
        return False if self._publisher is None else searched_phrase.lower() in self._publisher.lower()

    def matches_subjects(self, searched_phrase):
        return False if len(self._assigned_subjects) == 0 \
            else len(list(filter(lambda sub: sub.matches_search(searched_phrase), self._assigned_subjects))) > 0

    def matches_search(self, searched_phrase, search_by=SearchBy.ALL):
        if search_by is SearchBy.TITLE:
            return self.matches_title(searched_phrase)
        elif search_by is SearchBy.AUTHOR:
            return self.matches_author(searched_phrase)
        elif search_by is SearchBy.SUBJECTS:
            return self.matches_subjects(searched_phrase)
        elif search_by is SearchBy.PUBLISHER:
            return self.matches_publisher(searched_phrase)
        else:
            return self.matches_publisher(searched_phrase) or self.matches_title(searched_phrase) or \
                   self.matches_subjects(searched_phrase) or self.matches_author(searched_phrase)

    def __str__(self):
        return str(self._id) + ". " + self._title \
               + ",\nAuthor: " + (str(self._assigned_author) if self._assigned_author else str(self._author)) \
               + ",\nPublisher: " + str(self._publisher) \
               + ",\nISBN10: " + str(self._isbn10) \
               + ",\nISBN13: " + str(self._isbn13) \
               + ",\nPrice: " + str(self._price) \
               + ",\nAssigned Subjects:(\n" + "\n".join([str(x) for x in self._assigned_subjects]) + "\n)\n"
