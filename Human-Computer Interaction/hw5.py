import sys
import os
from PyQt4 import QtGui, QtCore
from random import shuffle
from functools import partial


# Bogdan Bernovici - 1232

class Homework5(QtGui.QWidget):
    def __init__(self):
        super(self.__class__, self).__init__()

        self.initUI()

    images = ["/images/1.jpg", "/images/2.jpg", "/images/3.jpg", "/images/4.jpg", "/images/5.jpg", "/images/6.jpg"]
    solutions = []
    duration = 5
    durationEdit = ''
    chooseLabel = ''
    numImgs = 3
    numberEdit = ''
    img1 = ''
    img2 = ''
    img3 = ''
    img4 = ''
    img5 = ''
    img6 = ''

    def initUI(self):
        self.img1 = QtGui.QLabel()
        self.img1.mousePressEvent = partial(self.checkSolution, theImg='0')
        self.img2 = QtGui.QLabel()
        self.img2.mousePressEvent = partial(self.checkSolution, theImg='1')
        self.img3 = QtGui.QLabel()
        self.img3.mousePressEvent = partial(self.checkSolution, theImg='2')
        self.img4 = QtGui.QLabel()
        self.img4.mousePressEvent = partial(self.checkSolution, theImg='3')
        self.img5 = QtGui.QLabel()
        self.img5.mousePressEvent = partial(self.checkSolution, theImg='4')
        self.img6 = QtGui.QLabel()
        self.img6.mousePressEvent = partial(self.checkSolution, theImg='5')

        images_layout = QtGui.QGridLayout()
        images_layout.addWidget(self.img1, 1, 0)
        images_layout.addWidget(self.img2, 2, 0)
        images_layout.addWidget(self.img3, 1, 1)
        images_layout.addWidget(self.img4, 2, 1)
        images_layout.addWidget(self.img5, 1, 2)
        images_layout.addWidget(self.img6, 2, 2)

        images_widget = QtGui.QWidget(self)
        images_widget.setLayout(images_layout)
        images_widget.setGeometry(250, 50, 300, 400)

        self.chooseLabel = QtGui.QLabel(self)
        self.chooseLabel.setGeometry(250, 50, 310, 50)

        labelOne = QtGui.QLabel(self)
        labelOne.setGeometry(250, 470, 100, 30)
        labelOne.setText("Duration:")

        self.durationEdit = QtGui.QLineEdit(self)
        self.durationEdit.setGeometry(250, 500, 100, 30)
        self.durationEdit.setText("5")
        self.durationEdit.textEdited.connect(self.changeDuration)

        labelTwo = QtGui.QLabel(self)
        labelTwo.setGeometry(400, 470, 150, 30)
        labelTwo.setText("No. of images (max 6):")

        self.numberEdit = QtGui.QLineEdit(self)
        self.numberEdit.setGeometry(400, 500, 100, 30)
        self.numberEdit.setText("3")
        self.numberEdit.textEdited.connect(self.changeNumberOfImgs)

        startButton = QtGui.QPushButton("Start", self)
        startButton.setGeometry(100, 500, 100, 30)
        startButton.clicked.connect(self.startClicked)

        exitButton = QtGui.QPushButton("Exit", self)
        exitButton.setGeometry(600, 500, 100, 30)
        exitButton.clicked.connect(self.exitClicked)
        self.setGeometry(0, 0, 800, 600)
        self.setWindowTitle('Homework 5 - Bogdan Bernovici')
        self.show()

    def changeNumberOfImgs(self):
        self.numImgs = int(self.numberEdit.displayText())

    def changeDuration(self):
        self.duration = int(self.durationEdit.displayText())

    def checkSolution(self, event, theImg):
        if self.images[int(theImg)] in self.solutions:
            self.showDialog("Correct!")
        else:
            self.showDialog("Wrong!")

    def showDialog(self, text):
        d = QtGui.QDialog()
        l1 = QtGui.QLabel(text, d)
        b1 = QtGui.QPushButton("Ok", d)
        b1.move(50, 50)
        b1.clicked.connect(d.close)
        l1.move(50, 20)
        d.setWindowTitle("Dialog")
        d.setWindowModality(QtCore.Qt.ApplicationModal)
        d.exec_()

    def randomizeImages(self):
        shuffle(self.images)

    def putImagesForShow(self):
        self.chooseLabel.setText("Try to memorize the images from below")
        self.solutions = []
        if self.numImgs > 0:
            self.img1.setPixmap(QtGui.QPixmap(os.getcwd() + self.images[0]))
            self.solutions.append(self.images[0])
        else:
            self.img1.setPixmap(QtGui.QPixmap(""))
        if self.numImgs > 1:
            self.img2.setPixmap(QtGui.QPixmap(os.getcwd() + self.images[1]))
            self.solutions.append(self.images[1])
        else:
            self.img2.setPixmap(QtGui.QPixmap(""))
        if self.numImgs > 2:
            self.img3.setPixmap(QtGui.QPixmap(os.getcwd() + self.images[2]))
            self.solutions.append(self.images[2])
        else:
            self.img3.setPixmap(QtGui.QPixmap(""))
        if self.numImgs > 3:
            self.img4.setPixmap(QtGui.QPixmap(os.getcwd() + self.images[3]))
            self.solutions.append(self.images[3])
        else:
            self.img4.setPixmap(QtGui.QPixmap(""))
        if self.numImgs > 4:
            self.img5.setPixmap(QtGui.QPixmap(os.getcwd() + self.images[4]))
            self.solutions.append(self.images[4])
        else:
            self.img5.setPixmap(QtGui.QPixmap(""))
        if self.numImgs > 5:
            self.img6.setPixmap(QtGui.QPixmap(os.getcwd() + self.images[5]))
            self.solutions.append(self.images[5])
        else:
            self.img6.setPixmap(QtGui.QPixmap(""))

    def putImagesForPick(self):
        self.chooseLabel.setText("Click on images below to see if correct or not")
        self.randomizeImages()
        self.img1.setPixmap(QtGui.QPixmap(os.getcwd() + self.images[0]))
        self.img2.setPixmap(QtGui.QPixmap(os.getcwd() + self.images[1]))
        self.img3.setPixmap(QtGui.QPixmap(os.getcwd() + self.images[2]))
        self.img4.setPixmap(QtGui.QPixmap(os.getcwd() + self.images[3]))
        self.img5.setPixmap(QtGui.QPixmap(os.getcwd() + self.images[4]))
        self.img6.setPixmap(QtGui.QPixmap(os.getcwd() + self.images[5]))

    def startClicked(self):
        self.randomizeImages()
        self.putImagesForShow()
        QtCore.QTimer.singleShot(self.duration * 1000, lambda: self.putImagesForPick())

    def exitClicked(self):
        QtGui.QApplication.quit()


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    ex = Homework5()
    sys.exit(app.exec_())
