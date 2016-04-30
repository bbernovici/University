import sys
import pyaudio
import math
from PyQt4 import QtGui, QtCore


# Bogdan Bernovici - 1232

class Homework3(QtGui.QWidget):
    PyAudio = pyaudio.PyAudio
    bitRate = 16000
    frequency = 50
    length = 2
    combo = ''

    def playSound(self):
        numberOfFrames = int(self.bitRate * self.length)
        restFrames = numberOfFrames % self.bitRate
        waveData = ''
        for x in xrange(numberOfFrames):
            waveData = waveData + chr(int(math.sin(x / ((self.bitRate / self.frequency) / (2 * math.pi))) * 127 + 128))
        for x in xrange(restFrames):
            waveData = waveData + chr(128)
        p = self.PyAudio()
        stream = p.open(format=p.get_format_from_width(1),
                        channels=1,
                        rate=self.bitRate,
                        output=True)
        stream.write(waveData)
        stream.stop_stream()
        stream.close()
        p.terminate()

    def __init__(self):
        super(self.__class__, self).__init__()

        self.initUI()

    def initUI(self):
        playButton = QtGui.QPushButton("Play", self)
        playButton.setGeometry(100, 200, 100, 30)
        playButton.clicked.connect(self.playClicked)

        exitButton = QtGui.QPushButton("Exit", self)
        exitButton.setGeometry(600, 200, 100, 30)
        exitButton.clicked.connect(self.exitClicked)

        labelOne = QtGui.QLabel(self)
        labelOne.setGeometry(100, 50, 200, 30)
        labelOne.setText("Set frequency (Hz):")
        self.combo = QtGui.QComboBox(self)
        self.combo.setFocusPolicy(QtCore.Qt.NoFocus)
        self.combo.setGeometry(100, 100, 200, 30)
        frequencies = ['50', '100', '200', '500', '1000', '2000', '5000', '8000', '10000']
        self.combo.addItems(frequencies)
        self.combo.currentIndexChanged.connect(self.changeFrequency)

        labelTwo = QtGui.QLabel(self)
        labelTwo.setGeometry(400, 50, 300, 30)
        labelTwo.setText("Vol. controlled at system level:")
        slider = QtGui.QSlider(QtCore.Qt.Horizontal, self)
        slider.setFocusPolicy(QtCore.Qt.NoFocus)
        slider.setEnabled(False)
        slider.setGeometry(400, 100, 200, 30)
        slider.valueChanged[int].connect(self.changeVolume)

        self.setGeometry(0, 0, 800, 300)
        self.setWindowTitle('Homework 3 - Bogdan Bernovici')
        self.show()

    def changeFrequency(self):
        self.frequency = int(self.combo.currentText())

    def changeVolume(self):
        print "hello"

    def playClicked(self):
        self.playSound()

    def exitClicked(self):
        QtGui.QApplication.quit()


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    ex = Homework3()
    sys.exit(app.exec_())
