'''
Program Name:   SGM2 Assignment - Home Page UI of Erasmus Page
Author:         Jonathan Noble - C15487922 (DT282/2)
'''
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class Slides(QWidget):
    def __init__(self, image_files, parent=None):
        #super(Slides, self).__init__()
        QWidget.__init__(self, parent)

        self.image_files = image_files
        self.label = QLabel("", self)
        self.label.setGeometry(50, 150, 450, 350)

        #button
        self.button = QPushButton(". . .", self)
        self.button.setGeometry(200, 100, 140, 30)
        self.button.clicked.connect(self.timerEvent)
        #self.w(self.timerEvent)
        self.timer = QBasicTimer()
        self.step = 0
        self.delay = 3000 #ms
        sTitle = "DIT Erasmus Page : {} seconds"
        self.setWindowTitle(sTitle.format(self.delay/1000.0))

        #self.initUI()


    def initUI(self):
        self.win = QWidget()
        self.win.resize(500,500)
        #window
        # sTitle = "DIT Erasmus Page : {} seconds"
        # self.setWindowTitle(sTitle.format(self.delay/1000.0))
        #self.defineLayout()
        #self.defineComponents()
        #self.defineDetailWin()
        #self.win.setLayout(self.mainLayout)

        self.win.show()

    def defineLayout(self):
        self.mainLayout = QGridLayout()
        self.formLayout = QFormLayout()
        self.btnLayout = QHBoxLayout()


    #timer slideshow
    def timerEvent(self, e=None):
        if self.step >= len(self.image_files):
            self.timer.start(self.delay, self)
            self.step = 0
            return
        self.timer.start(self.delay, self)
        file = self.image_files[self.step]
        image = QPixmap(file)
        self.label.setPixmap(image)
        self.setWindowTitle("{} --> {}".format(str(self.step), file))
        self.step += 1

image_files = ["slide1.jpg", "slide2.jpg", "slide3.jpg", "slide4.jpg"]

def main():
    app = QApplication(sys.argv)
    appform = Slides(image_files)
    appform.setGeometry(200, 80, 1000, 650)
    appform.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
