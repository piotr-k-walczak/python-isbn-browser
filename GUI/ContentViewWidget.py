from PyQt5.QtCore import QSize, Qt, QRect
from PyQt5.QtWidgets import *
from Controller import Controller


class ContentViewWidget(QWidget):
    def __init__(self, parent_layout, parent_widget, controller: Controller):
        super().__init__()

        self._controller = controller
        self._widgets_in_main = []

        layout = QVBoxLayout()

        search_bar = QLineEdit(parent_widget)
        search_bar.setText("Search")
        search_bar.textChanged.connect(self._controller.update_search_phrase)
        layout.addWidget(search_bar)

        scroll_area = QScrollArea(parent_widget)
        scroll_area.setMinimumSize(QSize(620, 496))
        scroll_area.setWidgetResizable(True)
        scroll_area.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)
        scroll_area_widget_contents = QWidget()
        scroll_area_widget_contents.setGeometry(QRect(0, 0, 622, 494))
        self.scrollAreaWidgetContents = scroll_area_widget_contents

        self.widget_container = QVBoxLayout(scroll_area_widget_contents)
        scroll_area.setWidget(scroll_area_widget_contents)

        layout.addWidget(scroll_area, 0, Qt.AlignTop)
        parent_layout.addLayout(layout)

        self._controller.on_search_update_content = self.populate

    def populate(self, data, widget_function):

        for widget in self._widgets_in_main:
            widget.hide()

        for d in data:

            found = False
            for widget in self._widgets_in_main:
                if widget.widgetId == d.widgetId:
                    widget.show()
                    found = True

            if not found:
                widget = widget_function(self.scrollAreaWidgetContents, d)
                self._widgets_in_main.append(widget)
                self.widget_container.addWidget(widget)