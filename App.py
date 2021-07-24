import sys

from MainWindow import MainWindow
from PySide6 import QtWidgets

if __name__ == "__main__":
    app = QtWidgets.QApplication()

    widget = MainWindow()
    widget.resize(1280, 720)
    widget.show()

    sys.exit(app.exec())
