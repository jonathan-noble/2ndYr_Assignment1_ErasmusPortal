'''
Program Name:   SGM2 Assignment - Home Page with Log-in UI of Erasmus Portal
Author:         Jonathan Noble - C15487922 (DT282/2)
'''

from PyQt4 import QtCore, QtGui
import sys
import gettext
import locale
from functools import partial


#Utf-8 Encoding generated from Qt Designer
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
        #Calling the Slides Widget class and the MainWindow setup
        self.slides_widget = Slides(image_files, self)
        self.setupUi(self)

    def setupUi(self, MainWindow):
        #read Css file
        self.styledata=' '
        file=open('blurange.css','r')
        self.styledata=file.read()
        file.close()

        menubar = self.menuBar()
        fileMenu = menubar.addAction("HOME")


        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1269, 688)
        MainWindow.setMinimumSize(QtCore.QSize(1269, 688))          #size of window is fixed to the defined size above only
        MainWindow.setMaximumSize(QtCore.QSize(1269, 688))
        MainWindow.setStyleSheet(_fromUtf8(""))
        self.logInWidget = QtGui.QTabWidget(self.slides_widget)
        self.logInWidget.setGeometry(QtCore.QRect(690, 190, 531, 371))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.logInWidget.setFont(font)
        self.logInWidget.setStyleSheet(_fromUtf8("background-color: rgb(247, 247, 247);\n"
    "border: 1px solid #1e1e1e;\n"
    "border-color: rgb(170, 85, 0);\n"
    "border-radius: 4;"))
        self.logInWidget.setObjectName(_fromUtf8("logInWidget"))
        self.tab_login = QtGui.QWidget()
        self.tab_login.setObjectName(_fromUtf8("tab_login"))
        self.textBrowser_userN = QtGui.QTextBrowser(self.tab_login)
        self.textBrowser_userN.setGeometry(QtCore.QRect(140, 90, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.textBrowser_userN.setFont(font)
        self.textBrowser_userN.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.textBrowser_userN.setStyleSheet(_fromUtf8("border-color: rgb(0, 0, 0);"))
        self.textBrowser_userN.setObjectName(_fromUtf8("textBrowser_userN"))
        self.pushButton_Info = QtGui.QPushButton(self.tab_login)
        self.pushButton_Info.setGeometry(QtCore.QRect(380, 10, 51, 51))
        self.pushButton_Info.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.pushButton_Info.setStyleSheet(_fromUtf8("border-image:url(:/icons/info.png);\n"
    "background: none;\n"
    "background-color: transparent;\n"
    "border: none;"))
        self.pushButton_Info.setText(_fromUtf8(""))
        self.pushButton_Info.setObjectName(_fromUtf8("pushButton_Info"))
        self.textBrowser_pw = QtGui.QTextBrowser(self.tab_login)
        self.textBrowser_pw.setGeometry(QtCore.QRect(140, 180, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.textBrowser_pw.setFont(font)
        self.textBrowser_pw.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.textBrowser_pw.setStyleSheet(_fromUtf8("border-color: rgb(0, 0, 0);"))
        self.textBrowser_pw.setObjectName(_fromUtf8("textBrowser_pw"))
        self.pushButton_login = QtGui.QPushButton(self.tab_login)
        self.pushButton_login.setGeometry(QtCore.QRect(210, 250, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_login.setFont(font)
        self.pushButton_login.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.pushButton_login.setStyleSheet(_fromUtf8("border-color: rgb(0, 0, 0);\n"
    "background-color: rgb(85, 170, 255);"))
        self.pushButton_login.setObjectName(_fromUtf8("pushButton_login"))
        self.label_Erasmus = QtGui.QLabel(self.tab_login)
        self.label_Erasmus.setGeometry(QtCore.QRect(170, 20, 161, 41))
        self.label_Erasmus.setStyleSheet(_fromUtf8("border-color: rgb(0, 0, 0);"))
        self.label_Erasmus.setObjectName(_fromUtf8("label_Erasmus"))
        self.logInWidget.addTab(self.tab_login, _fromUtf8(""))
        self.tab_calendar = QtGui.QWidget()
        self.tab_calendar.setObjectName(_fromUtf8("tab_calendar"))
        self.calendarWidget = QtGui.QCalendarWidget(self.tab_calendar)
        self.calendarWidget.setGeometry(QtCore.QRect(30, 60, 461, 231))
        self.calendarWidget.setObjectName(_fromUtf8("calendarWidget"))
        self.logInWidget.addTab(self.tab_calendar, _fromUtf8(""))
        self.widget_signUp = QtGui.QWidget(self.slides_widget)
        self.widget_signUp.setGeometry(QtCore.QRect(690, 577, 531, 71))
        self.widget_signUp.setStyleSheet(_fromUtf8("background-color: rgb(247, 247, 247);\n"
    "border: 1px solid #1e1e1e;\n"
    "border-color: rgb(170, 85, 0);\n"
    "border-radius: 4;"))
        self.widget_signUp.setObjectName(_fromUtf8("widget_signUp"))
        self.label_Account = QtGui.QLabel(self.widget_signUp)
        self.label_Account.setGeometry(QtCore.QRect(110, 30, 191, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lucida Sans"))
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_Account.setFont(font)
        self.label_Account.setStyleSheet(_fromUtf8("border: transparent;"))
        self.label_Account.setObjectName(_fromUtf8("label_Account"))
        self.pushButton_signUp = QtGui.QPushButton(self.widget_signUp)
        self.pushButton_signUp.setGeometry(QtCore.QRect(310, 30, 61, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lucida Sans"))
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_signUp.setFont(font)
        self.pushButton_signUp.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.pushButton_signUp.setStyleSheet(_fromUtf8("border-color: rgb(0, 0, 0);\n"
    "background-color: rgb(85, 170, 255);"))
        self.pushButton_signUp.setObjectName(_fromUtf8("pushButton_signUp"))
        self.groupBox = QtGui.QGroupBox(self.slides_widget)
        self.groupBox.setGeometry(QtCore.QRect(490, 190, 120, 361))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet(_fromUtf8("background-color: rgb(247, 247, 247);\n"
    "border: 1px solid #1e1e1e;\n"
    "border-color: rgb(170, 85, 0);\n"
    "border-radius: 4;"))
        self.groupBox.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.groupBox.setFlat(False)
        self.groupBox.setCheckable(False)
        self.groupBox.setObjectName(_fromUtf8("groupBox_Slides"))


        self.pushButton_Desc = QtGui.QPushButton(self.groupBox)
        self.pushButton_Desc.setGeometry(QtCore.QRect(20, 30, 71, 61))
        self.pushButton_Desc.setStyleSheet(_fromUtf8(self.styledata))
        self.pushButton_Desc.setText(_fromUtf8(""))
        self.pushButton_Desc.setObjectName(_fromUtf8("pushButton_Desc"))
        self.pushButton_Desc.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.pushButton_Desc.clicked.connect(partial(self.openDescWin))


        self.pushButton_Contact = QtGui.QPushButton(self.groupBox)
        self.pushButton_Contact.setGeometry(QtCore.QRect(30, 290, 61, 61))
        self.pushButton_Contact.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.pushButton_Contact.setStyleSheet(_fromUtf8("border-image:url(:/icons/contact_phone.png);\n"
"background: none;\n"
"background-color: transparent;\n"
"border: none;\n"
""))
        self.pushButton_Contact.setText(_fromUtf8(""))
        self.pushButton_Contact.setObjectName(_fromUtf8("pushButton_Contact"))

        self.pushButton_Test = QtGui.QPushButton(self.groupBox)
        self.pushButton_Test.setGeometry(QtCore.QRect(20, 160, 71, 61))
        self.pushButton_Test.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.pushButton_Test.setStyleSheet(_fromUtf8("border-image:url(:/icons/testimonials.png);\n"
"background: none;\n"
"background-color: transparent;\n"
"border: none;\n"
""))
        self.pushButton_Test.setText(_fromUtf8(""))
        self.pushButton_Test.setObjectName(_fromUtf8("pushButton_Test"))

        self.SlidesWidget = QtGui.QListWidget(self.slides_widget)
        self.SlidesWidget.setGeometry(QtCore.QRect(70, 190, 421, 361))
        self.SlidesWidget.setAutoFillBackground(True)
        self.SlidesWidget.setStyleSheet(_fromUtf8("background-color:transparent;\n"
"border: 1px solid #1e1e1e;\n"
"border-color: rgb(170, 85, 0);\n"
"border-radius: 4;"))
        self.SlidesWidget.setFrameShape(QtGui.QFrame.Box)
        self.SlidesWidget.setFrameShadow(QtGui.QFrame.Raised)
        self.SlidesWidget.setLineWidth(3)
        self.SlidesWidget.setObjectName(_fromUtf8("SlidesWidget"))

        self.toolbar_widget = QtGui.QWidget(self.slides_widget)
        self.toolbar_widget.setGeometry(QtCore.QRect(10, 0, 1241, 71))
        self.toolbar_widget.setStyleSheet(_fromUtf8(self.styledata))
        self.toolbar_widget.setObjectName(_fromUtf8("toolbar_widget")
        )
        self.search_bar_2 = QtGui.QTextEdit(self.toolbar_widget)
        self.search_bar_2.setGeometry(QtCore.QRect(150, 10, 271, 41))
        self.search_bar_2.setStyleSheet(_fromUtf8("border-color: rgb(170, 0, 0);"))
        self.search_bar_2.setObjectName(_fromUtf8("search_bar_2"))
        self.searchButton_2 = QtGui.QPushButton(self.toolbar_widget)
        self.searchButton_2.setGeometry(QtCore.QRect(430, 10, 41, 41))
        self.searchButton_2.setStyleSheet(_fromUtf8("background-color: transparent;\n"
"border-image:url(:/icons/search.png);\n"
"background:none;\n"
"border:none;\n"
"background-repeat:none;\n"
""))
        self.searchButton_2.setText(_fromUtf8(""))
        self.searchButton_2.setObjectName(_fromUtf8("searchButton_2"))

        self.logo_label = QtGui.QLabel(self.toolbar_widget)
        self.logo_label.setGeometry(QtCore.QRect(0, -5, 121, 81))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.logo_label.setFont(font)
        self.logo_label.setStyleSheet(_fromUtf8("background-color: transparent;\n"
"border-image:url(:/icons/small_logo.png);\n"
"background:none;\n"
"border:none;\n"
"background-repeat:none;\n"
""))
        self.logo_label.setText(_fromUtf8(""))
        self.logo_label.setObjectName(_fromUtf8("logo_label"))

        self.pushButton_EN = QtGui.QPushButton(self.toolbar_widget)
        self.pushButton_EN.setGeometry(QtCore.QRect(930, 30, 75, 23))
        self.pushButton_EN.setObjectName(_fromUtf8("pushButton_EN"))
       	self.pushButton_EN.clicked.connect(lambda: self.enTranslate(self.slides_widget))

        self.pushButton_IE = QtGui.QPushButton(self.toolbar_widget)
        self.pushButton_IE.setGeometry(QtCore.QRect(1070, 30, 75, 23))
        self.pushButton_IE.setObjectName(_fromUtf8("pushButton_IE"))
        self.pushButton_IE.clicked.connect(lambda: self.ieTranslate(self.slides_widget))

        self.tleft_wid = QtGui.QWidget(self.slides_widget)
        self.tleft_wid.setGeometry(QtCore.QRect(60, 90, 551, 91))
        self.tleft_wid.setStyleSheet(_fromUtf8(""))
        self.tleft_wid.setObjectName(_fromUtf8("tleft_wid"))
        self.label_motto = QtGui.QLabel(self.tleft_wid)
        self.label_motto.setGeometry(QtCore.QRect(0, 0, 551, 91))
        self.label_motto.setStyleSheet(_fromUtf8("background-color: rgb(247, 247, 247);\n"
"border: 1px solid #1e1e1e;\n"
"border-color: rgb(170, 85, 0);\n"
"border-radius: 4;"))
        self.label_motto.setObjectName(_fromUtf8("label_motto"))

        self.label_welcomeSlide = QtGui.QLabel(self.slides_widget)
        self.label_welcomeSlide.setGeometry(QtCore.QRect(70, 190, 421, 401))
        self.label_welcomeSlide.setStyleSheet(_fromUtf8(""))
        self.label_welcomeSlide.setObjectName(_fromUtf8("label_welcomeSlide"))

        self.label_wel = QtGui.QLabel(self)
        self.label_wel.setGeometry(QtCore.QRect(90, 210, 241, 381))
        self.label_wel.setStyleSheet(_fromUtf8("background:transparent;"))
        self.label_wel.setObjectName(_fromUtf8("label_wel"))
        self.label_slidenav = QtGui.QLabel(self)
        self.label_slidenav.setGeometry(QtCore.QRect(315, 275, 201, 81))
        self.label_slidenav.setStyleSheet(_fromUtf8("background:transparent;"))
        self.label_slidenav.setObjectName(_fromUtf8("label_slidenav"))

        Slides.button_slide.clicked.connect(self.welcomePop)

        self.label_welcomeSlide.setGeometry(QtCore.QRect(70, 190, 421, 401))
        self.label_slidenav.setGeometry(QtCore.QRect(315, 275, 201, 81))

        self.widget_signUp.raise_()
        self.logInWidget.raise_()
        self.groupBox.raise_()
        self.SlidesWidget.raise_()
        self.toolbar_widget.raise_()
        self.tleft_wid.raise_()
        self.label_welcomeSlide.raise_()

        self.enTranslate(self.slides_widget)
        self.setCentralWidget(self.slides_widget)
        self.retranslateUi(MainWindow)

        self.NewWindow = DescWindow(self)

    def welcomePop(self):
        self.label_wel.setGeometry(QtCore.QRect(70, 1000, 421, 401))
        self.label_slidenav.setGeometry(QtCore.QRect(315, 1000, 201, 81))

    def openDescWin(self):
        self.NewWindow.resize(500,500)
        self.NewWindow.show();

    def onActivated(self, text):
        self.lbl.setText(text)
        self.lbl.adjustSize()

    # .po and .mo files are read and goes through strings with underscore(_)
    def enTranslate(self, MainWindow):
    	self.translate('en', MainWindow)

    def ieTranslate(self, MainWindow):
    	self.translate('ie', MainWindow)


    def translate(self, lang, MainWindow):
    	self.messages = gettext.translation('messages', localedir='locale', languages=[lang])
    	self.messages.install()
    	self.retranslateUi(MainWindow)


    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Erasmus", None))
        self.textBrowser_userN.setHtml(_translate("MainWindow", _("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
        "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
        "p, li { white-space: pre-wrap; }\n"
        "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
        "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Username</span></p></body></html>"), None))
        self.textBrowser_pw.setHtml(_translate("MainWindow", _("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
        "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
        "p, li { white-space: pre-wrap; }\n"
        "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
        "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Password</span></p></body></html>"), None))
        self.pushButton_login.setText(_translate("MainWindow", _("Log-In"), None))
        self.label_Erasmus.setText(_translate("MainWindow", _("<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">ERASMUS</span></p></body></html>"), None))
        self.logInWidget.setTabText(self.logInWidget.indexOf(self.tab_login), _translate("MainWindow", _("Log-In"), None))
        self.logInWidget.setTabText(self.logInWidget.indexOf(self.tab_calendar), _translate("MainWindow", _("Calendar"), None))
        self.label_Account.setText(_translate("MainWindow", _("Don\'t have an account?"), None))
        self.pushButton_signUp.setText(_translate("MainWindow", _("Sign up"), None))
        self.groupBox.setTitle(_translate("MainWindow", _("MENU"), None))
        self.search_bar_2.setHtml(_translate("MainWindow", _("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
    "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
    "p, li { white-space: pre-wrap; }\n"
    "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Type here to search. . .</span></p></body></html>"), None))
        self.pushButton_EN.setText(_translate("MainWindow", _("ENGLISH"), None))
        self.pushButton_IE.setText(_translate("MainWindow", _("IRISH"), None))
        self.label_motto.setText(_translate("MainWindow", _("<html><head/><body><p align=\"center\"><span style=\" font-family:\'verdana,Arial,Tahoma,sans-serif\'; font-size:14pt; font-weight:600; color:#000000;\">EXCHANGE isn\'t a year in your life, </span></p><p align=\"center\"><span style=\" font-family:\'verdana,Arial,Tahoma,sans-serif\'; font-size:14pt; font-weight:600; color:#000000;\">it\'s a LIFE in a year.</span></p></body></html>"), None))
        self.label_wel.setText(_translate("MainWindow", _("<html><head/><body><p><span style=\" font-size:28pt;\">WELCOME</span></p><p><span style=\" font-size:28pt;\">TO</span></p><p><span style=\" font-size:28pt;\">ERASMUS</span></p><p><span style=\" font-size:28pt;\">HOME</span></p><p><span style=\" font-size:28pt;\">PAGE.</span></p></body></html>"), None))
        self.label_slidenav.setText(_translate("MainWindow", _("<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">To navigate the slideshow,</span></p><p><span style=\" font-size:12pt; font-weight:600;\">press the button</span></p><p><span style=\" font-size:14pt; font-weight:600;\">BELOW!</span></p></body></html>"), None))

class DescWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(DescWindow, self).__init__(parent)

        self.buttonBox = QtGui.QDialogButtonBox(self)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel | QtGui.QDialogButtonBox.Ok)

        self.textBrowser_slide = QtGui.QTextBrowser(self)
        self.textBrowser_slide.append(_("Testimonials by Siobhain: It was an awesome experience! I recommend students to branch out and create more memories through Erasmus."))
        self.textBrowser_slide.resize(500,500)

        self.verticalLayout = QtGui.QVBoxLayout(self)
        self.verticalLayout.addWidget(self.textBrowser_slide)
        self.verticalLayout.addWidget(self.buttonBox)


class Slides(QtGui.QWidget):
    def __init__(self, image_files, parent=None):
        super(Slides, self).__init__(parent)

        self.image_files = image_files
        self.label = QtGui.QLabel("", self)
        self.label.setGeometry(70, 190, 423, 360)

        #buttons to rewind and forward
        Slides.button_slide = QtGui.QPushButton(". . .", self)
        Slides.button_slide.setGeometry(200, 600, 140, 30)
        Slides.button_slide.clicked.connect(self.timerEvent)

        self.label.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/icons/welcome.png\"/></p></body></html>", None))
        self.timer = QtCore.QBasicTimer()
        self.step = 0
        self.delay = 3000 #ms

    def timerEvent(self, e=None):
        if self.step >= len(self.image_files):
            self.timer.start(self.delay, self)
            self.step = 0
            return
        self.timer.start(self.delay, self)
        file = self.image_files[self.step]
        image = QtGui.QPixmap(file)
        self.label.setPixmap(image)
        self.step += 1


image_files = ["images\slide1.jpg", "images\slide2.jpg", "images\slide3.jpg",
 "images\slide4.jpg", "images\slide5.jpg"]

import icons_rc

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon("icons\dit_crest_2010.gif"))
    Form = MainWindow(image_files)
    Form.show()
    sys.exit(app.exec_())
