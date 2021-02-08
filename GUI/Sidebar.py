from PyQt5.QtWidgets import *
from Search.SearchBy import SearchBy


class Sidebar(QWidget):
    def __init__(self, parent, controller):
        super().__init__()

        self._parent = parent
        self._controller = controller

        self._sidebar_label = None
        self._all_toggle = None
        self._title_toggle = None
        self._author_toggle = None
        self._subject_toggle = None
        self._publisher_toggle = None
        self._spacer = None
        self._chart_book_price_button = None
        self._chart_book_time_button = None
        self._chart_book_cover_button = None
        self._generate_report_button = None

        self._vertical_layout = QVBoxLayout()
        self._vertical_layout.setSpacing(10)
        self._parent.addLayout(self._vertical_layout)

        self._all_toggle = None
        self._controller.on_search_update_sidebar = self.update_side_menu
        self.setup_side_menu()

    def update_search_by(self):
        if self._author_toggle.isChecked():
            self._controller.update_search_by(SearchBy.AUTHOR)
        elif self._subject_toggle.isChecked():
            self._controller.update_search_by(SearchBy.SUBJECTS)
        elif self._title_toggle.isChecked():
            self._controller.update_search_by(SearchBy.TITLE)
        elif self._publisher_toggle.isChecked():
            self._controller.update_search_by(SearchBy.PUBLISHER)
        else:
            self._controller.update_search_by(SearchBy.ALL)

    def update_side_menu(self, is_full):
        self.clear_side_menu()

        self._vertical_layout = QVBoxLayout()
        self._vertical_layout.setSpacing(10)
        self._parent.insertLayout(0, self._vertical_layout)

        if is_full:
            self.show_side_menu()

    def setup_side_menu(self):
        self.setup_toggle_buttons()
        self.setup_other_buttons()

    def setup_toggle_buttons(self):
        self._sidebar_label = QLabel(self)
        self._sidebar_label.setText("Search by")
        self._vertical_layout.addWidget(self._sidebar_label)

        self._all_toggle = QRadioButton(self)
        self._all_toggle.setText("All")
        self._all_toggle.setChecked(True)
        self._vertical_layout.addWidget(self._all_toggle)

        self._author_toggle = QRadioButton(self)
        self._author_toggle.setText("Author")
        self._vertical_layout.addWidget(self._author_toggle)

        self._title_toggle = QRadioButton(self)
        self._title_toggle.setText("Title")
        self._vertical_layout.addWidget(self._title_toggle)

        self._subject_toggle = QRadioButton(self)
        self._subject_toggle.setText("Subject")
        self._vertical_layout.addWidget(self._subject_toggle)

        self._publisher_toggle = QRadioButton(self)
        self._publisher_toggle.setText("Publisher")
        self._publisher_toggle.toggled.connect(self.update_search_by)
        self._vertical_layout.addWidget(self._publisher_toggle)

        self._author_toggle.toggled.connect(self.update_search_by)
        self._title_toggle.toggled.connect(self.update_search_by)
        self._subject_toggle.toggled.connect(self.update_search_by)
        self._all_toggle.toggled.connect(self.update_search_by)

    def setup_other_buttons(self):
        self._spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self._vertical_layout.addItem(self._spacer)

        self._chart_book_cover_button = sidebutton(self, "Chart - Books by Cover", self._controller.show_book_cover_chart)
        self._vertical_layout.addWidget(self._chart_book_cover_button)

        self._chart_book_price_button = sidebutton(self, "Chart - Books Price Distribution", self._controller.show_book_price_chart)
        self._vertical_layout.addWidget(self._chart_book_price_button)

        self._chart_book_time_button = sidebutton(self, "Chart - Books Time Distribution", self._controller.show_books_per_year_chart)
        self._vertical_layout.addWidget(self._chart_book_time_button)

        self._generate_report_button = sidebutton(self, "Generate XLSX Report", self._controller.generate_report)
        self._vertical_layout.addWidget(self._generate_report_button)

    def clear_side_menu(self):
        self._sidebar_label.hide()
        self._all_toggle.hide()
        self._title_toggle.hide()
        self._subject_toggle.hide()
        self._author_toggle.hide()
        self._publisher_toggle.hide()

    def show_side_menu(self):
        self._sidebar_label.show()
        self._all_toggle.show()
        self._title_toggle.show()
        self._subject_toggle.show()
        self._author_toggle.show()
        self._publisher_toggle.show()

def sidebutton(parent, text, function):
    button = QPushButton(parent)
    button.setText(text)
    button.pressed.connect(function)
    return button
