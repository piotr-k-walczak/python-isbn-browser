import collections

from Search.SearchBy import SearchBy
from Objects.SearchableObject import SearchableObject

months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]


class TimeStatistics:
    def __init__(self):
        self._years = collections.OrderedDict(sorted({}.items()))

    @property
    def years(self):
        return self._years

    @property
    def years_as_list(self):
        return list(self._years.values())

    def add_book(self, book):
        [_, year] = book.release_date.split()
        if year not in self._years.keys():
            self._years[year] = AnnualStatistics(year)
            self._years = collections.OrderedDict(sorted(self._years.items()))
        self._years[year].add_book(book)

    def __str__(self):
        return "Time stats:\n" + "\n".join(str(val) for val in self._years.values())


class AnnualStatistics(SearchableObject):
    def __init__(self, year):
        self._year = year
        self._months = {
            "January": MonthlyStatistics("January"),
            "February": MonthlyStatistics("February"),
            "March": MonthlyStatistics("March"),
            "April": MonthlyStatistics("April"),
            "May": MonthlyStatistics("May"),
            "June": MonthlyStatistics("June"),
            "July": MonthlyStatistics("July"),
            "August": MonthlyStatistics("August"),
            "September": MonthlyStatistics("September"),
            "October": MonthlyStatistics("October"),
            "November": MonthlyStatistics("November"),
            "December": MonthlyStatistics("December")
        }

    @property
    def year(self):
        return self._year

    @property
    def months(self):
        return self._months

    @property
    def months_as_list(self):
        return list(self._months.values())

    @property
    def books(self):
        sum = []
        for m in self._months.values():
            sum += m.books
        return sum

    @property
    def widgetId(self):
        return "T_" + str(self._year)

    @property
    def number_of_books(self):
        return sum([month.number_of_books for month in self._months.values()])

    @property
    def avg_price(self):
        return 0 if self.number_of_books == 0 else sum([book.price for book in self.books]) / self.number_of_books

    def add_book(self, book):
        [month, _] = book.release_date.split()
        if month not in self._months.keys():
            self._months[month] = MonthlyStatistics(month)
        self._months[month].add_book(book)

    def matches_search(self, searched_phrase, search_by=SearchBy.ALL):
        return searched_phrase.lower() in str(self._year).lower()

    def __str__(self):
        return self._year + ": \n" + "\n".join([str(v) for v in self._months.values()])


class MonthlyStatistics:
    def __init__(self, month):
        self._month = month
        self._books = []

    @property
    def month(self):
        return self._month

    @property
    def books(self):
        return self._books

    @property
    def number_of_books(self):
        return len(self._books)

    @property
    def avg_price(self):
        return 0 if len(self._books) == 0 else sum([book.price for book in self._books]) / len(self._books)

    def add_book(self, book):
        self._books.append(book)

    def __str__(self):
        return self._month + ", Total: " + str(self.number_of_books) + ", Avg. Price ($): " + str(self.avg_price)
