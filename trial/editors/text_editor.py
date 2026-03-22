from PyQt6.QtWidgets import QTextEdit
from PyQt6.QtGui import QFont

class TextEditor(QTextEdit):

    def __init__(self):
        super().__init__()
        self.path=None
        self.setFont(QFont("Segoe UI",11))