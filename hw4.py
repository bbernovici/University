import sys
from PyQt4 import QtGui, QtCore
import re

# Bogdan Bernovici - 1232

class Homework4(QtGui.QWidget):
    def __init__(self):
        super(self.__class__, self).__init__()

        self.initUI()

    labelOne = ''
    def initUI(self):

        self.labelOne = QtGui.QLabel(self)
        self.labelOne.setWordWrap(True)
        self.labelOne.setGeometry(50, 50, 500, 100)
        self.labelOne.setText("Please open a file in order to show stats about it.")

        openButton = QtGui.QPushButton("Open Text", self)
        openButton.setGeometry(100, 200, 100, 30)
        openButton.clicked.connect(self.showDialog)

        exitButton = QtGui.QPushButton("Exit", self)
        exitButton.setGeometry(400, 200, 100, 30)
        exitButton.clicked.connect(self.exitClicked)

        self.setGeometry(0, 0, 600, 300)
        self.setWindowTitle('Homework 4 - Bogdan Bernovici')
        self.show()

    def showDialog(self):
        fileName = QtGui.QFileDialog.getOpenFileName(self, 'Open file', '/home')
        f = open(fileName, 'r')
        self.createStats(f.read())

    def createStats(self, theText):
        textStats = "In the file you have opened, there are " + str(self.countWords(theText)) + " words. " \
                "The total number of syllables found is " + str(self.countAllSyllables(theText)) + ". " \
                "The average number of syllables per word is " + str(self.countAllSyllables(theText)/self.countWords(theText)) + "" \
                ". Finally, the total number of paragraphs found is " + str(self.getNumberOfParagraphs(theText)) + "."
        self.labelOne.setText(textStats)

    # This function returns an array with all words from the text using regex
    def getWordsFromText(self, theText):
        return re.compile('\w+').findall(theText)

    def countWords(self, theText):
        words = self.getWordsFromText(theText)
        return len(words)

    # I have observed that the number of syllables is strongly related to the number of vowels
    # The following function is based on this observation in order to compute the no. of syllables
    def countSyllables(self, theWord):
        vowels = ['a', 'e', 'i', 'o', 'u', 'y']
        currWord = theWord
        numOfVowels = 0
        wasLastVowel = False

        for wordChar in currWord:
            foundVowel = False
            for vow in vowels:
                if (vow == wordChar and wasLastVowel):
                    foundVowel = True
                    wasLastVowel = True
                    break
                elif (vow == wordChar and not wasLastVowel):
                    numOfVowels += 1
                    foundVowel = True
                    wasLastVowel = True
                    break
            if (not foundVowel):
                wasLastVowel = False
        if(len(currWord) > 2 and currWord[-2:] == "es"):
            numOfVowels -= 1
        elif (len(currWord) > 1 and currWord[-1:] == "e"):
            numOfVowels -= 1
        return numOfVowels

    def countAllSyllables(self, theText):
        words = self.getWordsFromText(theText)
        sumSyll = 0
        for w in words:
            syll = self.countSyllables(w)
            sumSyll += syll
        return sumSyll

    def getNumberOfParagraphs(self, theText):
        paragraphs = theText.split("\n\n")
        return len(paragraphs)

    def exitClicked(self):
        QtGui.QApplication.quit()


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    ex = Homework4()
    sys.exit(app.exec_())
