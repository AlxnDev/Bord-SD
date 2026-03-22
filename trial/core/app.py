import sys
from PyQt6.QtWidgets import QApplication
from ui.main_window import MainWindow

def run():
    app=QApplication(sys.argv)
    win=MainWindow()
    win.show()
    sys.exit(app.exec())