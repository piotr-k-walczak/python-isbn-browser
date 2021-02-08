from PyQt5.QtWidgets import QDialog, QVBoxLayout
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

from Objects.OtherStatistics import OtherStatistics
from Objects.TimeStatistics import TimeStatistics


def create_cover_stats_bar_chart(books_stats: OtherStatistics):
    title = "Number of books with certain cover"
    xlabel = "Type of cover"
    ylabel = "Number of books"
    labels = ["Paperback", "Hardcover", "Mass Market Paperback"]
    values = [books_stats.papercover[0], books_stats.hardcover[0], books_stats.mass_market_papercover[0]]
    return StandaloneChart(title, labels, values, xlabel, ylabel)


def create_price_bar_chart(books_stats: OtherStatistics):
    title = "Number of books at certain price points"
    xlabel = "Price point"
    ylabel = "Number of books"
    labels = ["Below $15", "From \$15 to \$30", "Above $30"]
    values = [books_stats.below15[0], books_stats.from15to30[0], books_stats.above30[0]]
    return StandaloneChart(title, labels, values, xlabel, ylabel)


def create_time_distribution_bar_chart(time_stats: TimeStatistics):
    title = "Books Released Per Year"
    xlabel = "Year"
    ylabel = "Number of books"
    labels = [int(y) for y in time_stats.years.keys() if int(y) >= 1980]
    values = [y.number_of_books for y in time_stats.years.values() if int(y.year) >= 1980]
    return StandaloneChart(title, labels, values, xlabel, ylabel)


class StandaloneChart(QDialog):

    def __init__(self, title, xdata, ydata, xlabel, ylabel, *args, **kwargs):
        super(StandaloneChart, self).__init__(*args, **kwargs)

        self._figure = Figure()
        self._canvas = FigureCanvas(self._figure)
        self._toolbar = NavigationToolbar(self._canvas, self)

        layout = QVBoxLayout()
        layout.addWidget(self._toolbar)
        layout.addWidget(self._canvas)
        self.setLayout(layout)

        self.plot(title, xdata, ydata, xlabel, ylabel)

    def plot(self, title, xdata, ydata, xlabel, ylabel):
        ax = self._figure.add_subplot(111)
        ax.set_title(title)
        ax.set_xlabel(xlabel)
        ax.set_ylabel(ylabel)
        ax.bar(xdata, ydata)
        self._canvas.draw()