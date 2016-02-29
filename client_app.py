from PyQt4.QtCore import *
from PyQt4.QtGui  import *
from PyQt4 import QtGui
import requests
import sys

class MyMainWindow(QMainWindow):

    def __init__(self, parent=None):

        super(MyMainWindow, self).__init__(parent)

        func_one = QtGui.QAction('&Function One', self)
        func_one.triggered.connect(lambda: self.on_menu_press(1))

        func_two = QtGui.QAction('&Function Two', self)
        func_two.triggered.connect(lambda: self.on_menu_press(2))

        func_three = QtGui.QAction('&Function Three', self)
        func_three.triggered.connect(lambda: self.on_menu_press(3))

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(func_one)
        fileMenu.addAction(func_two)
        fileMenu.addAction(func_three)

        self.form_widget = FormWidget(self) 
        self.setCentralWidget(self.form_widget)

        self.setFixedSize(300, 300)

    def on_menu_press(self, menuval):
        print (menuval)
        r = requests.post("http://127.0.0.1:5000/data", data={'item': menuval, 'type': 'menu'})
        if r.status_code != 200:
            #log this telemetry data and send it later
            pass
        #carry on with normal functioning of app


class FormWidget(QWidget):

    def __init__(self, parent):
        super(FormWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)

        self.button1 = QPushButton("Button 1")
        self.button1.clicked.connect(lambda: self.on_button_press(1))
        self.layout.addWidget(self.button1)

        self.button2 = QPushButton("Button 2")
        self.button2.clicked.connect(lambda: self.on_button_press(2))
        self.layout.addWidget(self.button2)

        self.button3 = QPushButton("Button 3")
        self.button3.clicked.connect(lambda: self.on_button_press(3))
        self.layout.addWidget(self.button3)

        self.button4 = QPushButton("Button 4")
        self.button4.clicked.connect(lambda: self.on_button_press(4))
        self.layout.addWidget(self.button4)

        self.setLayout(self.layout)

    def on_button_press(self, buttonval):
        print (buttonval)
        r = requests.post("http://127.0.0.1:5000/data", data={'item': buttonval, 'type': 'button'})
        if r.status_code != 200:
            #log this telemetry data and send it later
            print("Logging data for later send")
        #carry on with normal functioning of app

if __name__ == '__main__':
    app = QApplication([])
    foo = MyMainWindow()
    foo.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    app = QApplication([])
    foo = MyMainWindow()
    foo.show()

    retcode = -1
    try:
        retcode = app.exec_()
    except Exception as e:
        # create github issue
        pass
    sys.exit(retcode)
