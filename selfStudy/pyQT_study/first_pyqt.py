import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

app = QGuiApplication(sys.argv)
label = QLabel("Hello World")
label.show()
app.exec_()

