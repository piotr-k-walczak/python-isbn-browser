from Search.SearchBy import SearchBy
from Objects.SearchableObject import SearchableObject


class Subject(SearchableObject):
    def __init__(self):
        self._subject_id = None
        self._name = None
        self._parent_id = None
        self._sub_subjects = None

    @classmethod
    def create_with_data(cls, subject_id, name, parent_id=None, sub_subjects=None):
        subject = Subject()
        subject._subject_id = subject_id
        subject._name = name
        subject._parent_id = parent_id
        subject._sub_subjects = sub_subjects
        return subject

    @property
    def subject_id(self):
        return self._subject_id

    @property
    def subject_name(self):
        return self._name

    @property
    def parent_id(self):
        return self._parent_id

    @property
    def sub_subjects(self):
        return self._sub_subjects

    def add_sub_subject(self, sub_subject):
        if isinstance(sub_subject, Subject):
            if self._sub_subjects is None:
                self._sub_subjects = [sub_subject]
            else:
                self._sub_subjects.append(sub_subject)
        else:
            raise TypeError

    def matches_search(self, searched_phrase, search_by=SearchBy.ALL):
        return (False if self._name is None else searched_phrase.lower() in self._name.lower()) or \
               (False if self._subject_id is None else searched_phrase.lower() in str(self._subject_id).lower())

    def __str__(self):
        return str(self._subject_id) + ". " + self._name + ", children: " + str(
            0 if self._sub_subjects is None else len(self._sub_subjects))
