import pandas
from Objects.Author import Author
from Objects.Book import Book
from Objects.Subject import Subject


class CsvLoader:
    def __init__(self, data_sources):
        self._data_sources = data_sources

    def load_rows(self, source, predicate):
        try:
            df = pandas.read_csv(source)
            for index, row in df.iterrows():
                predicate(row)
        except:
            print("Nie udało się wczytać danych.")

    def load_books(self, books):
        self.load_rows(
            self._data_sources.books,
            lambda row: books.append(Book.createWithData(
                row['id'], row['title'], row['author'], row['author_id'], row['isbn10'], row['isbn13'], row['format'],
                row['pages'],
                row['price'], row['pubdate'], row['overview'], row['synopsis'], row['publisher']
            ))
        )

    def load_authors(self, authors):
        self.load_rows(
            self._data_sources.authors,
            lambda row: authors.append(Author.create_with_data(row['id'], row['title'], row['biography']))
        )

    def load_subjects(self, subjects):
        self.load_rows(
            self._data_sources.subjects,
            lambda row: subjects.append(Subject.create_with_data(
                row['id'], row['title']
            ))
        )

    def load_sub_subjects(self, subjects, sub_subjects):
        self.load_rows(self._data_sources.sub_subjects, lambda row: self.append_and_asign(subjects, sub_subjects, row))

    def load_sub_sub_subjects(self, sub_subjects, sub_sub_subjects):
        self.load_rows(self._data_sources.sub_sub_subjects,
                       lambda row: self.append_and_asign(sub_subjects, sub_sub_subjects, row, 'sub_subject'))

    def append_and_asign(self, subjects, sub_subjects, row, subject_tag='subject'):
        sub_subject = Subject.create_with_data(row['id'], row['title'], row[subject_tag])
        sub_subjects.append(sub_subject)
        parent = list(filter(lambda sub: sub.subject_id == row[subject_tag], subjects))[0]
        if parent is not None:
            parent.add_sub_subject(sub_subject)

    def load_subject_assignments(self, books, sub_subjects, sub_sub_subjects):

        self.load_rows(
            self._data_sources.books_to_subjects,
            lambda row: self.assign_subjects_to_books(books, row['book'],
                                                      sub_subjects, row['sub_subject'],
                                                      sub_sub_subjects, row['sub_sub_subject'])
        )

    def assign_subjects_to_books(self, books, book_id, sub_subjects, sub_subject_id, sub_sub_subjects,
                                 sub_sub_subject_id):
        found_book = next((x for x in books if x.book_id == book_id), None)
        if found_book is not None:
            found_sub_subject = next((x for x in sub_subjects if x.subject_id == sub_subject_id), None)
            if found_sub_subject is not None:
                found_book.assign_subject(found_sub_subject)
            elif sub_subject_id != 0:
                raise ValueError("SubSubject with id: " + str(sub_subject_id) + " has not been found.")

            found_sub_sub_subject = next((x for x in sub_sub_subjects if x.subject_id == sub_sub_subject_id), None)
            if found_sub_sub_subject is not None:
                found_book.assign_subject(found_sub_sub_subject)
            elif sub_sub_subject_id != 0:
                raise ValueError("SubSubSubject with id: " + str(sub_sub_subject_id) + " has not been found.")
        else:
            raise ValueError("Book with id: " + str(book_id) + " has not been found.")
