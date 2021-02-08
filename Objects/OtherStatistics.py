class OtherStatistics:
    def __init__(self, books):
        self._books = books

    @property
    def papercover(self):
        filtered = len([book for book in self._books if book.cover == "Paperback"])
        return [filtered, filtered / len(self._books)]

    @property
    def hardcover(self):
        filtered = len([book for book in self._books if book.cover == "Hardcover"])
        return [filtered, filtered / len(self._books)]

    @property
    def avg_price(self):
        return sum([book.price for book in self._books]) / len(self._books)

    @property
    def most_expensive(self):
        return max(self._books, key=lambda book: book.price)

    @property
    def mass_market_papercover(self):
        filtered = len([book for book in self._books if book.cover == "Mass Market Paperback"])
        return [filtered, filtered / len(self._books)]

    @property
    def below15(self):
        filtered = len([book for book in self._books if book.price < 15])
        return [filtered, filtered / len(self._books)]

    @property
    def from15to30(self):
        filtered = len([book for book in self._books if 15 <= book.price <= 30])
        return [filtered, filtered / len(self._books)]

    @property
    def above30(self):
        filtered = len([book for book in self._books if book.price > 30])
        return [filtered, filtered / len(self._books)]

    @property
    def widgetId(self):
        return "OTHER"