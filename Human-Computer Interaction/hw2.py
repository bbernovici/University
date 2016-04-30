import sys
from PyQt4 import QtGui, QtCore

# Bogdan Bernovici - 1232

class Homework2(QtGui.QWidget):
    def __init__(self):
        super(self.__class__, self).__init__()

        self.initUI()

    def initUI(self):

        startButton = QtGui.QPushButton("Start", self)
        startButton.setGeometry(100, 200, 100, 30)
        startButton.clicked.connect(self.startClicked)

        exitButton = QtGui.QPushButton("Exit", self)
        exitButton.setGeometry(600, 200, 100, 30)
        exitButton.clicked.connect(self.exitClicked)

        self.setGeometry(0, 0, 800, 300)
        self.setWindowTitle('Homework 2 - Bogdan Bernovici')
        self.show()

    def paintEvent(self, e):
        qp = QtGui.QPainter()
        qp.begin(self)
        self.drawDot(qp)

    dotX = 50
    dir = 5

    def drawDot(self, qp):
        qp.setBrush(QtGui.QColor(0, 0, 255))
        qp.drawEllipse(self.dotX, 50, 50, 50)

    def startClicked(self):
        if (self.dotX > 700):
            self.dir = -5
            self.dotX += self.dir
        elif (self.dotX < 50):
            self.dir = 5
            self.dotX += self.dir
        else:
            self.dotX += self.dir
        self.repaint()
        QtCore.QTimer.singleShot(1, lambda: self.startClicked())

    def exitClicked(self):
        QtGui.QApplication.quit()


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    ex = Homework2()
    sys.exit(app.exec_())
