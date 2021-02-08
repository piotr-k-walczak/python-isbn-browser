from CsvLoader import CsvLoader


class DataStore:
    def __init__(self, data_sources):
        self._csv_loader = CsvLoader(data_sources)
        self._books = []
        self._authors = []
        self._subjects = []
        self._sub_subjects = []
        self._sub_sub_subjects = []
        self.load()

    def load(self):
        self.load_authors()
        self.load_books()
        self.load_subjects()
        self.load_sub_subjects()
        self.load_sub_sub_subjects()
        self.load_subject_assignments()
        self.assign_authors_to_books()

    @property
    def books(self):
        return self._books

    @property
    def authors(self):
        return self._authors

    @property
    def subjects(self):
        return self._subjects

    @property
    def sub_subjects(self):
        return self._sub_subjects

    @property
    def sub_sub_subjects(self):
        return self._sub_sub_subjects

    @property
    def all_subjects(self):
        return self._subjects + self._sub_subjects + self._sub_sub_subjects

    def load_authors(self):
        self._csv_loader.load_authors(self._authors)

    def load_books(self):
        self._csv_loader.load_books(self._books)

    def load_subjects(self):
        self._csv_loader.load_subjects(self._subjects)

    def load_sub_subjects(self):
        self._csv_loader.load_sub_subjects(self._subjects, self._sub_subjects)

    def load_sub_sub_subjects(self):
        self._csv_loader.load_sub_sub_subjects(self._sub_subjects, self._sub_sub_subjects)

    def load_subject_assignments(self):
        self._csv_loader.load_subject_assignments(self._books, self._sub_subjects, self._sub_sub_subjects)

    def print(self):
        print("Loaded data")
        print("Books:")
        for book in self._books:
            print(book)
        print("Authors:")
        for author in self._authors:
            print(author)
        print("Subjects:")
        for subjects in self._subjects:
            print(subjects)
        print("SubSubjects:")
        for subjects in self._sub_subjects:
            print(subjects)
        print("SubSubSubjects:")
        for subjects in self._sub_sub_subjects:
            print(subjects)

    def assign_authors_to_books(self):
        for book in self._books:
            found_author = next((x for x in self._authors if x.author_id == book.author_id), None)
            if found_author is not None:
                book.assign_author(found_author)
            elif book.author_id != 0:
                raise ValueError("SubSubject with id: " + str(book.author_id) + " has not been found.")