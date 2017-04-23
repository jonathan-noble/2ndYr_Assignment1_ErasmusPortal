'''
Program Name:   SGM2 Assignment - Home Page UI of Erasmus Page
Author:         Jonathan Noble - C15487922 (DT282/2)
'''

from PyQt4 import QtCore, QtGui
import sys

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class MainWindow(QtGui.QMainWindow):
    def __init__(self, image_files, parent=None):
        super(MainWindow, self).__init__()
        #QtGui.QWidget.__init__(self, parent)

        self.setupUi(self)
        self.styledata=' '
        file=open('blurange.css','r')
        self.styledata=file.read()
        file.close()
        self.slides_widget = Slides(image_files, self)
        self.setCentralWidget(self.slides_widget)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1278, 688)
        self.logInWidget = QtGui.QTabWidget(MainWindow)
        self.logInWidget.setGeometry(QtCore.QRect(690, 220, 531, 371))
        self.logInWidget.setObjectName(_fromUtf8("logInWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.textBrowser_4 = QtGui.QTextBrowser(self.tab)
        self.textBrowser_4.setGeometry(QtCore.QRect(180, 80, 211, 41))
        self.textBrowser_4.setObjectName(_fromUtf8("textBrowser_4"))
        self.label_2 = QtGui.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(40, 160, 81, 21))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label = QtGui.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(40, 70, 81, 21))
        self.label.setObjectName(_fromUtf8("label"))
        self.pushButton_Info = QtGui.QPushButton(self.tab)
        self.pushButton_Info.setGeometry(QtCore.QRect(390, 20, 51, 51))
        self.pushButton_Info.setStyleSheet(_fromUtf8("border-image:url(:/icons/info.png);\n"
"background: none;\n"
"background-color: transparent;\n"
"border: none;"))
        self.pushButton_Info.setText(_fromUtf8(""))
        self.pushButton_Info.setObjectName(_fromUtf8("pushButton_Info"))
        self.textBrowser_2 = QtGui.QTextBrowser(self.tab)
        self.textBrowser_2.setGeometry(QtCore.QRect(180, 150, 211, 41))
        self.textBrowser_2.setObjectName(_fromUtf8("textBrowser_2"))
        self.Submit = QtGui.QPushButton(self.tab)
        self.Submit.setGeometry(QtCore.QRect(240, 230, 75, 23))
        self.Submit.setObjectName(_fromUtf8("Submit"))
        self.label_3 = QtGui.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(230, 20, 51, 31))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.logInWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.calendarWidget = QtGui.QCalendarWidget(self.tab_2)
        self.calendarWidget.setGeometry(QtCore.QRect(30, 60, 461, 231))
        self.calendarWidget.setObjectName(_fromUtf8("calendarWidget"))
        self.widget_2 = QtGui.QWidget(self.tab_2)
        self.widget_2.setGeometry(QtCore.QRect(-10, 260, 531, 78))
        self.widget_2.setObjectName(_fromUtf8("widget_2"))
        self.logInWidget.addTab(self.tab_2, _fromUtf8(""))
        self.widget = QtGui.QWidget(MainWindow)
        self.widget.setGeometry(QtCore.QRect(690, 600, 531, 78))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.label_4 = QtGui.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(170, 30, 111, 21))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.pushButton_2 = QtGui.QPushButton(self.widget)
        self.pushButton_2.setGeometry(QtCore.QRect(270, 30, 75, 23))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.groupBox = QtGui.QGroupBox(MainWindow)
        self.groupBox.setGeometry(QtCore.QRect(490, 220, 120, 371))
        self.groupBox.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.groupBox.setFlat(False)
        self.groupBox.setCheckable(False)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.pushButton_Desc = QtGui.QPushButton(self.groupBox)
        self.pushButton_Desc.setGeometry(QtCore.QRect(20, 30, 71, 61))
        self.pushButton_Desc.setStyleSheet(_fromUtf8("border-image:url(:/icons/description.png);\n"
"background: none;\n"
"background-color: transparent;\n"
"border: none;\n"
""))
        self.pushButton_Desc.setText(_fromUtf8(""))
        self.pushButton_Desc.setObjectName(_fromUtf8("pushButton_Desc"))
        self.pushButton_Contact = QtGui.QPushButton(self.groupBox)
        self.pushButton_Contact.setGeometry(QtCore.QRect(30, 290, 61, 61))
        self.pushButton_Contact.setStyleSheet(_fromUtf8("border-image:url(:/icons/contact_phone.png);\n"
"background: none;\n"
"background-color: transparent;\n"
"border: none;\n"
""))
        self.pushButton_Contact.setText(_fromUtf8(""))
        self.pushButton_Contact.setObjectName(_fromUtf8("pushButton_Contact"))
        self.pushButton_Test = QtGui.QPushButton(self.groupBox)
        self.pushButton_Test.setGeometry(QtCore.QRect(20, 160, 71, 61))
        self.pushButton_Test.setStyleSheet(_fromUtf8("border-image:url(:/icons/testimonials.png);\n"
"background: none;\n"
"background-color: transparent;\n"
"border: none;\n"
""))
        self.pushButton_Test.setText(_fromUtf8(""))
        self.pushButton_Test.setObjectName(_fromUtf8("pushButton_Test"))
        self.SlidesWidget = QtGui.QListWidget(MainWindow)
        self.SlidesWidget.setGeometry(QtCore.QRect(60, 220, 431, 371))
        self.SlidesWidget.setStyleSheet(_fromUtf8("background-color:rgb(193, 193, 193);"))
        self.SlidesWidget.setFrameShape(QtGui.QFrame.Box)
        self.SlidesWidget.setFrameShadow(QtGui.QFrame.Raised)
        self.SlidesWidget.setLineWidth(3)
        self.SlidesWidget.setObjectName(_fromUtf8("SlidesWidget"))
        self.widget.raise_()
        self.logInWidget.raise_()
        self.groupBox.raise_()
        self.SlidesWidget.raise_()

        self.retranslateUi(MainWindow)
        self.logInWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Erasmus", None))
        self.label_2.setText(_translate("MainWindow", "PASSWORD:", None))
        self.label.setText(_translate("MainWindow", "USERNAME:", None))
        self.Submit.setText(_translate("MainWindow", "SUBMIT", None))
        self.label_3.setText(_translate("MainWindow", "Register", None))
        self.logInWidget.setTabText(self.logInWidget.indexOf(self.tab), _translate("MainWindow", "Tab 1", None))
        self.logInWidget.setTabText(self.logInWidget.indexOf(self.tab_2), _translate("MainWindow", "Tab 2", None))
        self.label_4.setText(_translate("MainWindow", "Have an account?", None))
        self.pushButton_2.setText(_translate("MainWindow", "Log-in here!", None))
        self.groupBox.setTitle(_translate("MainWindow", "MENU", None))

class Slides(QtGui.QWidget):
    def __init__(self, image_files, parent=None):
        super(Slides, self).__init__(parent)
        #QWidget.__init__(self, parent)

        self.image_files = image_files
        self.label = QtGui.QLabel("", self)
        self.label.setGeometry(65, 225, 423, 363)

        #buttons to rewind and forward
        self.button = QtGui.QPushButton(". . .", self)
        self.button.setGeometry(200, 100, 140, 30)
        self.button.clicked.connect(self.timerEvent)

        self.timer = QtCore.QBasicTimer()
        self.step = 0
        self.delay = 3000 #ms
        sTitle = "DIT Erasmus Page : {} seconds"
        self.setWindowTitle(sTitle.format(self.delay/1000.0))


    def timerEvent(self, e=None):
        if self.step >= len(self.image_files):
            self.timer.start(self.delay, self)
            self.step = 0
            return
        self.timer.start(self.delay, self)
        file = self.image_files[self.step]
        image = QtGui.QPixmap(file)
        self.label.setPixmap(image)
        #self.setWindowTitle("{} --> {}".format(str(self.step), file))
        self.step += 1


image_files = ["images\slide1.jpg", "images\slide2.jpg", "images\slide3.jpg",
 "images\slide4.jpg", "images\slide5.jpg"]

import icons_rc

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    Form = MainWindow(image_files)
    Form.show()
    sys.exit(app.exec_())
