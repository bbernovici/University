import sys
from PyQt4 import QtGui, QtCore

#Bogdan Bernovici - 1232

class Homework1(QtGui.QWidget):

    def __init__(self):
        super(self.__class__, self).__init__()

        self.initUI()


    def initUI(self):

        labelOne = QtGui.QLabel(self)
        labelOne.setGeometry(100, 350, 200, 30)
        labelOne.setText("Set distance:")
        sliderOne = QtGui.QSlider(QtCore.Qt.Horizontal, self)
        sliderOne.setFocusPolicy(QtCore.Qt.NoFocus)
        sliderOne.setGeometry(100, 400, 200, 30)
        sliderOne.valueChanged[int].connect(self.changeDistance)

        labelTwo = QtGui.QLabel(self)
        labelTwo.setGeometry(400, 350, 200, 30)
        labelTwo.setText("Set line width:")
        sliderTwo = QtGui.QSlider(QtCore.Qt.Horizontal, self)
        sliderTwo.setFocusPolicy(QtCore.Qt.NoFocus)
        sliderTwo.setGeometry(400, 400, 200, 30)
        sliderTwo.valueChanged[int].connect(self.changeLineWidth)

        exitButton = QtGui.QPushButton("Exit", self)
        exitButton.setGeometry(650, 400, 50, 30)
        exitButton.clicked.connect(self.exitClicked)

        self.setGeometry(0, 0, 800, 600)
        self.setWindowTitle('Homework 1 - Bogdan Bernovici')
        self.show()


    def paintEvent(self, e):
        qp = QtGui.QPainter()
        qp.begin(self)
        self.drawLines(qp)
        qp.end()

    y1 = 0;
    y2 = 0;
    lineWidth = 1;
    def drawLines(self, qp):
        pen = QtGui.QPen(QtCore.Qt.black, self.lineWidth, QtCore.Qt.SolidLine)
        qp.setPen(pen)
        qp.drawLine(100, 100+self.y1, 700, 100+self.y1)
        qp.drawLine(100, 200+self.y2, 700, 200+self.y2)

    def changeDistance(self, value):
            self.y1 = value
            self.y2 = -value
            self.repaint()

    def changeLineWidth(self, value):
        self.lineWidth = value;
        self.repaint()

    def exitClicked(self):
        QtGui.QApplication.quit()

if __name__ == '__main__':

    app = QtGui.QApplication(sys.argv)
    ex = Homework1()
    sys.exit(app.exec_())