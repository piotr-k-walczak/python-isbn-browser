from PyQt5.QtWidgets import *


def entry_label(parent, layout, text, stylesheet=None):
    overview_label = QLabel(parent)
    overview_label.setWordWrap(True)
    overview_label.setText(text)
    overview_label.setStyleSheet("border: none;" if stylesheet is None else stylesheet + "; border:none")
    layout.addWidget(overview_label)
