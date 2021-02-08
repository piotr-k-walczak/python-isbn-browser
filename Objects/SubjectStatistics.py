from Objects.Subject import Subject

class SubjectsStatistics:
    def __init__(self):
        self._all_books = 0
        self._subjects = {}

    @property
    def subjects(self):
        return self._subjects

    @property
    def subjects_as_list(self):
        return list(self._subjects.values())

    def add_subject(self, subject):
        if subject.subject_name not in self._subjects.keys():
            self._subjects[subject.subject_name] = SubjectStatistics.create_with_data(subject.subject_id, subject.subject_name, subject.parent_id, subject.sub_subjects)

    def add_book(self, book):
        self._all_books += 1
        for subject in book.assigned_subjects:
            found_subject = next((sub for sub in self._subjects.values() if sub.subject_name == subject.subject_name), None)
            if found_subject is not None:
                self._subjects[found_subject.subject_name].add_book(book)

    def confirm(self):
        for val in self._subjects.values():
            val.set_market_share(val.number_of_books / self._all_books)

    def __str__(self):
        return "Subjects stats:\n" + "\n".join(str(val) for val in self._subjects.values())


class SubjectStatistics(Subject):
    def __init__(self):
        super(SubjectStatistics, self).__init__()
        self._books = []
        self._market_share = 0

    @classmethod
    def create_with_data(cls, subject_id, name, parent_id=None, sub_subjects=None):
        subject = SubjectStatistics()
        subject._subject_id = subject_id
        subject._name = name
        subject._parent_id = parent_id
        subject._sub_subjects = sub_subjects
        return subject

    @property
    def books(self):
        return self._books

    @property
    def books_as_string(self):
        return "None" if len(self._books) == 0 else ";\n".join([b.title for b in self._books])

    @property
    def number_of_books(self):
        return len(self._books)

    @property
    def market_share(self):
        return self._market_share

    @property
    def avg_price(self):
        return 0 if self.number_of_books == 0 else sum([book.price for book in self._books]) / self.number_of_books

    @property
    def widgetId(self):
        prefix = "S_" if self._parent_id is None else ("S_S_" if self._sub_subjects is not None else "S_S_S_")
        return prefix + str(self._subject_id)

    def add_book(self, book):
        self._books.append(book)

    def set_market_share(self, share):
        self._market_share = share

    def __str__(self):
        return super().__str__() + ", Total: " + str(self.number_of_books) + ", Avg. Price ($): " + str(self.avg_price)