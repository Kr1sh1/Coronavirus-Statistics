from PySide6 import QtWidgets, QtCore

class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QtWidgets.QGridLayout(self)
        self.layout.setAlignment(QtCore.Qt.AlignCenter)
        
        self.label = QtWidgets.QLabel("Hello World")
        
        self.layout.addWidget(self.label)

        #self.label.setAlignment(QtCore.Qt.AlignBottom)