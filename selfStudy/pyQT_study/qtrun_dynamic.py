import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.uic import *
from PyQt5.QtCore import *

form_class = loadUiType('mainwindow.ui')[0]


class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        print(self.objectName())
        self.btn1.clicked.connect(self.btn1_clicked)
        self.lnEdit1.setText("Please click button")

    def btn1_clicked(self):
        self.label1.setText("Button clicked")
        QMessageBox.about(self, "message", "clicked")
        self.lnEdit1.setText("Thank you for your click")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    app.exec_()