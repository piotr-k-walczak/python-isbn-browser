from Objects.Author import Author


class AuthorsStatistics:
    def __init__(self):
        self._authors = {}

    @property
    def authors(self):
        return self._authors

    @property
    def authors_as_list(self):
        return list(self._authors.values())

    def add_author(self, author):
        if str(author.author_id) not in self._authors.keys():
            self._authors[str(author.author_id)] = AuthorStatistics.create_with_data(author.author_id, author.name, author.bio)

    def add_book(self, book):
        found_author = next((auth for auth in self._authors.values() if auth.author_id == book.author_id), None)
        if found_author is not None:
            self._authors[str(found_author.author_id)].add_book(book)

    def __str__(self):
        return "Authors stats:\n" + "\n".join(str(val) for val in self._authors.values())


class AuthorStatistics(Author):
    def __init__(self):
        super().__init__()
        self._written_books = []

    @classmethod
    def create_with_data(cls, author_id, name, bio):
        author = AuthorStatistics()
        author._id = author_id
        author._name = name
        author._bio = bio
        return author

    @property
    def widgetId(self):
        return "A_" + str(self._id)

    @property
    def books(self):
        return self._written_books

    @property
    def books_as_string(self):
        return "None" if len(self._written_books) == 0 else ";\n".join([b.title for b in self._written_books])

    @property
    def number_of_books(self):
        return len(self._written_books)

    def add_book(self, book):
        self._written_books.append(book)

    def __str__(self):
        return super().__str__() + ", Total books: " + str(self.number_of_books)

