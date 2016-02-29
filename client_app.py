import sys
from PyQt4 import QtGui, QtCore


class Example(QtGui.QWidget):
    
    def __init__(self):
        super(Example, self).__init__()
        
        self.initUI()
        
    def initUI(self):               
        
        qbtn1 = QtGui.QPushButton('Button 1', self)
        # qbtn1.clicked.connect(btnaction.btntwo)
        qbtn1.resize(qbtn1.sizeHint())
        qbtn1.move(10, 50)

        qbtn2 = QtGui.QPushButton('Button 2', self)
        # qbtn2.clicked.connect(btnaction.btnone)
        qbtn2.resize(qbtn2.sizeHint())
        qbtn2.move(100, 50)       
        
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Telemetry Demo')    
        self.show()
        
def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
