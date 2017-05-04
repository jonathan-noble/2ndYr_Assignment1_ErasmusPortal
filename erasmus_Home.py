'''
Program Name:   SGM2 Assignment - Home Page with Log-in UI of Erasmus Portal
Author:         Jonathan Noble - C15487922 (DT282/2)
'''

#kits and libraries are stored here
from PyQt4 import QtCore, QtGui
from PyQt4.QtWebKit import QWebView
import sys
import gettext
import locale
import icons_rc
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

#-----------------------------------------------------------------------------------------------------#

#MainWindow is implemented here
class MainWindow(QtGui.QMainWindow):
    def __init__(self, image_files, parent=None):
        super(MainWindow, self).__init__()
        #Calling the Slides Widget class and the MainWindow setup
        self.slides_widget = Slides(image_files, self)
        self.setupUi(self)

    def setupUi(self, MainWindow):
        self.defineLayout()

        menubar = self.menuBar()
        homeMenu = menubar.addAction("HOME")
        viewMenu = menubar.addAction("VIEW")
        helpMenu = menubar.addAction("HELP")

        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1269, 688)
        MainWindow.setMinimumSize(QtCore.QSize(1269, 688))          #size of window is fixed to the defined size above only
        MainWindow.setMaximumSize(QtCore.QSize(1269, 688))
        MainWindow.setStyleSheet(_fromUtf8(""))

        #All the Qt Designer widget implementations are separated by functions
        self.loginWid()
        self.signUpWid()
        self.menuWid()
        self.slideFrame()
        self.toolWid()
        self.mottoWid()
        self.slidesWid()

        self.widget_signUp.raise_()
        self.logInWidget.raise_()
        self.groupBox.raise_()
        self.slideFrameget.raise_()
        self.toolbar_widget.raise_()
        self.motto_wid.raise_()
        self.label_welcomeSlide.raise_()


        self.enTranslate(self.slides_widget)        #default language when the window starts
        self.setCentralWidget(self.slides_widget)   #main layout would be based on the slides_widget
        self.retranslateUi(MainWindow)

        #initializing the windows that are opened here
        self.descWin = DescWindow(self)
        self.testWin = TestWindow(self)
        self.instructWin = InstructWindow(self)


    def defineLayout(self): #define the layout of the main window and apply stylesheet
        #read css file
        self.styledata=' '
        file=open('blurange.css','r')
        self.styledata=file.read()
        file.close()

    def loginWid(self):
        self.logInWidget = QtGui.QTabWidget(self.slides_widget)
        self.logInWidget.setGeometry(QtCore.QRect(690, 190, 531, 371))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.logInWidget.setFont(font)
        self.logInWidget.setStyleSheet(_fromUtf8(self.styledata))
        self.logInWidget.setObjectName(_fromUtf8("logInWidget"))

        self.tab_login = QtGui.QWidget()
        self.tab_login.setObjectName(_fromUtf8("tab_login"))

        self.textBrowser_userN = QtGui.QTextEdit(self.tab_login)
        self.textBrowser_userN.setGeometry(QtCore.QRect(140, 90, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textBrowser_userN.setFont(font)
        self.textBrowser_userN.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.textBrowser_userN.setStyleSheet(_fromUtf8(self.styledata))
        self.textBrowser_userN.setObjectName(_fromUtf8("textBrowser_userN"))

        self.pushButton_Instruct = QtGui.QPushButton(self.tab_login)
        self.pushButton_Instruct.setGeometry(QtCore.QRect(380, 10, 51, 51))
        self.pushButton_Instruct.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.pushButton_Instruct.setStyleSheet(_fromUtf8(self.styledata))
        self.pushButton_Instruct.setText(_fromUtf8(""))
        self.pushButton_Instruct.setObjectName(_fromUtf8("pushButton_Instruct"))
        self.pushButton_Instruct.clicked.connect(partial(self.openInstructWin))

        self.textBrowser_pw = QtGui.QTextEdit(self.tab_login)
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
        self.pushButton_login.clicked.connect(self.handleLogin)


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

        self.label_timer = QtGui.QLabel('DATE TODAY', self.tab_calendar)
        self.label_timer.setGeometry(210, 20, 100, 20)
        self.timer = QtCore.QTimer(self.tab_calendar)
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.displayTime)
        self.timer.start()

        self.nextWin = NextWindow(self)

    def signUpWid(self):
        self.widget_signUp = QtGui.QWidget(self.slides_widget)
        self.widget_signUp.setGeometry(QtCore.QRect(690, 577, 531, 71))
        self.widget_signUp.setStyleSheet(_fromUtf8(self.styledata))
        self.widget_signUp.setObjectName(_fromUtf8("widget_signUp"))

        self.label_Account = QtGui.QLabel(self.widget_signUp)
        self.label_Account.setGeometry(QtCore.QRect(110, 30, 191, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lucida Sans"))
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)

        self.label_Account.setFont(font)
        self.label_Account.setStyleSheet(_fromUtf8(self.styledata))
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

    def menuWid(self):
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

        self.pushButton_Test = QtGui.QPushButton(self.groupBox)
        self.pushButton_Test.setGeometry(QtCore.QRect(20, 160, 71, 61))
        self.pushButton_Test.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.pushButton_Test.setStyleSheet(_fromUtf8(self.styledata))
        self.pushButton_Test.setText(_fromUtf8(""))
        self.pushButton_Test.setObjectName(_fromUtf8("pushButton_Test"))
        self.pushButton_Test.clicked.connect(partial(self.openTestWin))

        self.pushButton_Contact = QtGui.QPushButton(self.groupBox)
        self.pushButton_Contact.setGeometry(QtCore.QRect(30, 290, 61, 61))
        self.pushButton_Contact.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.pushButton_Contact.setStyleSheet(_fromUtf8(self.styledata))
        self.pushButton_Contact.setText(_fromUtf8(""))
        self.pushButton_Contact.setObjectName(_fromUtf8("pushButton_Contact"))
        self.pushButton_Contact.clicked.connect(self.openBrowserWin)

    def slideFrame(self):
        self.slideFrameget = QtGui.QListWidget(self.slides_widget)
        self.slideFrameget.setGeometry(QtCore.QRect(70, 190, 421, 361))
        self.slideFrameget.setAutoFillBackground(True)
        self.slideFrameget.setStyleSheet(_fromUtf8(self.styledata))
        self.slideFrameget.setFrameShape(QtGui.QFrame.Box)
        self.slideFrameget.setFrameShadow(QtGui.QFrame.Raised)
        self.slideFrameget.setLineWidth(3)
        self.slideFrameget.setObjectName(_fromUtf8("slideFrameget"))

    def toolWid(self):
        self.toolbar_widget = QtGui.QWidget(self.slides_widget)
        self.toolbar_widget.setGeometry(QtCore.QRect(10, 0, 1241, 71))
        self.toolbar_widget.setStyleSheet(_fromUtf8(self.styledata))
        self.toolbar_widget.setObjectName(_fromUtf8("toolbar_widget")
        )
        self.search_bar = QtGui.QTextEdit(self.toolbar_widget)
        self.search_bar.setGeometry(QtCore.QRect(150, 10, 271, 41))
        self.search_bar.setStyleSheet(_fromUtf8("border-color: rgb(170, 0, 0);"))
        self.search_bar.setObjectName(_fromUtf8("search_bar"))
        self.searchButton = QtGui.QPushButton(self.toolbar_widget)
        self.searchButton.setGeometry(QtCore.QRect(430, 10, 41, 41))
        self.searchButton.setStyleSheet(_fromUtf8(self.styledata))
        self.searchButton.setText(_fromUtf8(""))
        self.searchButton.setObjectName(_fromUtf8("searchButton"))

        self.logo_label = QtGui.QLabel(self.toolbar_widget)
        self.logo_label.setGeometry(QtCore.QRect(0, -5, 121, 81))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.logo_label.setFont(font)
        self.logo_label.setStyleSheet(_fromUtf8(self.styledata))
        self.logo_label.setText(_fromUtf8(""))
        self.logo_label.setObjectName(_fromUtf8("logo_label"))

        self.pushButton_EN = QtGui.QPushButton(self.toolbar_widget)
        self.pushButton_EN.setGeometry(QtCore.QRect(600, 10, 100, 25))
        self.pushButton_EN.setObjectName(_fromUtf8("pushButton_EN"))
        self.pushButton_EN.setStyleSheet(_fromUtf8(self.styledata))
       	self.pushButton_EN.clicked.connect(lambda: self.enTranslate(self.slides_widget))

        self.pushButton_IE = QtGui.QPushButton(self.toolbar_widget)
        self.pushButton_IE.setGeometry(QtCore.QRect(600, 40, 100, 25))
        self.pushButton_IE.setObjectName(_fromUtf8("pushButton_IE"))
        self.pushButton_IE.setStyleSheet(_fromUtf8(self.styledata))
        self.pushButton_IE.clicked.connect(lambda: self.ieTranslate(self.slides_widget))

        # Input
        self.le = QtGui.QLineEdit(self.toolbar_widget)
        self.le.setGeometry(820, 5, 300, 30)
        # enter button
        self.enter_btn = QtGui.QPushButton( self.toolbar_widget)
        self.enter_btn.setGeometry(1150, 7, 80, 30)
        self.enter_btn.setStyleSheet(_fromUtf8(self.styledata))
        self.enter_btn.clicked.connect(self.feedb)
        # display
        self.ans = QtGui.QLabel(self.toolbar_widget)
        self.ans.setGeometry(825, 40, 300, 30)


    def mottoWid(self):
        self.motto_wid = QtGui.QWidget(self.slides_widget)
        self.motto_wid.setGeometry(QtCore.QRect(60, 90, 551, 91))
        self.motto_wid.setStyleSheet(_fromUtf8(""))
        self.motto_wid.setObjectName(_fromUtf8("motto_wid"))
        self.label_motto = QtGui.QLabel(self.motto_wid)
        self.label_motto.setGeometry(QtCore.QRect(0, 0, 551, 91))
        self.label_motto.setStyleSheet(_fromUtf8(self.styledata))
        self.label_motto.setObjectName(_fromUtf8("label_motto"))

    def slidesWid(self):
        self.label_welcomeSlide = QtGui.QLabel(self.slides_widget)
        self.label_welcomeSlide.setGeometry(QtCore.QRect(70, 190, 421, 401))
        self.label_welcomeSlide.setStyleSheet(_fromUtf8(""))
        self.label_welcomeSlide.setObjectName(_fromUtf8("label_welcomeSlide"))

        self.label_wel = QtGui.QLabel(self)
        self.label_wel.setGeometry(QtCore.QRect(80, 170, 241, 381))
        self.label_wel.setStyleSheet(_fromUtf8("background:transparent;"))
        self.label_wel.setObjectName(_fromUtf8("label_wel"))
        self.label_slidenav = QtGui.QLabel(self)
        self.label_slidenav.setGeometry(QtCore.QRect(315, 245, 201, 81))
        self.label_slidenav.setStyleSheet(_fromUtf8("background:transparent;"))
        self.label_slidenav.setObjectName(_fromUtf8("label_slidenav"))


        Slides.button_slide.clicked.connect(self.welcomePop)


#---------------------------------------------------------------------------------------------------------------------#
#               FUNCTIONALITIES ARE SET here

    def displayTime(self):      # real-time display
        self.label_timer.setText(QtCore.QDateTime.currentDateTime().toString())

    def feedb(self):     # feedback submitted is echoed back in the ans label
        input = self.le.text()
        self.ans.setText(input)


    def handleLogin(self):      #the log-in user authentication with error-handling
        if (self.textBrowser_userN.toPlainText() == 'noble' and
            self.textBrowser_pw.toPlainText() == 'lad1234'):
            self.nextWin.resize(300, 200)
            self.nextWin.show()
        else:
            QtGui.QMessageBox.warning(self, 'Error', 'Username or password is wrong! Try again.')

    def welcomePop(self):       #the function to release the labels when the slideshow button is clicked
        self.label_wel.setGeometry(QtCore.QRect(70, 1000, 421, 401))
        self.label_slidenav.setGeometry(QtCore.QRect(315, 1000, 201, 81))

    def openDescWin(self):      #Opens relevant windows
        self.descWin.resize(500,500)
        self.descWin.show();

    def openTestWin(self):
        self.testWin.resize(500,500)
        self.testWin.show();

    def openInstructWin(self):
        self.instructWin.resize(300, 200)
        self.instructWin.show();


    def openBrowserWin(self):       # Opens up the webcourses  browser through a link
        self.feedBack = WebBrowser()
        self.feedBack.loadURL()

    # .po and .mo files are read and goes through strings with underscore(_)
    # functions to translate the following texts
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
        self.search_bar.setHtml(_translate("MainWindow", _("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
    "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
    "p, li { white-space: pre-wrap; }\n"
    "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Type here to search. . .</span></p></body></html>"), None))
        self.pushButton_EN.setText(_translate("MainWindow", _("ENGLISH"), None))
        self.pushButton_IE.setText(_translate("MainWindow", _("IRISH"), None))
        self.label_motto.setText(_translate("MainWindow", _("<html><head/><body><p align=\"center\"><span style=\" font-family:\'verdana,Arial,Tahoma,sans-serif\'; font-size:14pt; font-weight:600; color:#000000;\">EXCHANGE isn\'t a year in your life, </span></p><p align=\"center\"><span style=\" font-family:\'verdana,Arial,Tahoma,sans-serif\'; font-size:14pt; font-weight:600; color:#000000;\">it\'s a LIFE in a year.</span></p></body></html>"), None))
        self.label_wel.setText(_translate("MainWindow", _("<html><head/><body><p><span style=\" font-size:28pt;\">WELCOME</span></p><p><span style=\" font-size:28pt;\">TO</span></p><p><span style=\" font-size:28pt;\">ERASMUS</span></p><p><span style=\" font-size:28pt;\">HOME</span></p><p><span style=\" font-size:28pt;\">PAGE.</span></p></body></html>"), None))
        self.label_slidenav.setText(_translate("MainWindow", _("<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">To navigate the slideshow,</span></p><p><span style=\" font-size:12pt; font-weight:600;\">press the button</span></p><p><span style=\" font-size:14pt; font-weight:600;\">BELOW!</span></p></body></html>"), None))
        self.le.setText(_("Feedback: Great interface!"))
        self.enter_btn.setText(_("Submit"))

#-------------------------------------------------------------------------------------------------------------
#                                     ADDED WINDOWS

class DescWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(DescWindow, self).__init__(parent)

        self.setWindowTitle("Erasmus Description")

        self.buttonBox = QtGui.QDialogButtonBox(self)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel | QtGui.QDialogButtonBox.Ok)

        self.textBrowser_slide = QtGui.QTextBrowser(self)
        self.textBrowser_slide.append(_("The Erasmus Programme (European Region Action Scheme for the Mobility of University Students is a European Union(EU) student exchange programme established in 1987. Erasmus+, or Erasmus Plus, is the new programme combining all the EU's current schemes for education, training, youth and sport, which was started in January 2014. "))
        self.textBrowser_slide.resize(500,500)


#Description Window
class TestWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(TestWindow, self).__init__(parent)

        self.setWindowTitle("Testimonials")

        self.buttonBox = QtGui.QDialogButtonBox(self)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel | QtGui.QDialogButtonBox.Ok)

        self.textBrowser_slide = QtGui.QTextBrowser(self)
        self.textBrowser_slide.append(_("Testimonials by Siobhain: It was an awesome experience! I recommend students to branch out and create more memories through Erasmus."))
        self.textBrowser_slide.resize(500,500)

class NextWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(NextWindow, self).__init__(parent)

        self.setWindowTitle("Country Selection")

        self.buttonBox = QtGui.QDialogButtonBox(self)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel | QtGui.QDialogButtonBox.Ok)

        self.textBrowser_slide = QtGui.QTextBrowser(self)
        self.textBrowser_slide.append("Login Successful! Please wait as the next page loads for you.")
        self.textBrowser_slide.resize(300,200)

class InstructWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(InstructWindow, self).__init__(parent)

        self.setWindowTitle("Instruction")

        self.buttonBox = QtGui.QDialogButtonBox(self)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel | QtGui.QDialogButtonBox.Ok)

        self.textBrowser_slide = QtGui.QTextBrowser(self)
        self.textBrowser_slide.append(_("1. Log-in with your registered username. 2. Enter your password. 3. Press enter. 4. If you have no account, registering is very easy! - Just press the button below"))
        self.textBrowser_slide.resize(300,200)

class WebBrowser(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        QWebView.__init__(self)
        self.setObjectName(_fromUtf8("Dialog"))
        self.resize(1024, 768)
        self.qwebview = QWebView(self)
        self.qwebview.setGeometry(QtCore.QRect(0, 50, 1020, 711))
        self.qwebview.setObjectName(_fromUtf8("qwebview"))
        self.lineEdit = QtGui.QLineEdit(self)
        self.lineEdit.setGeometry(QtCore.QRect(10, 20, 1000, 25))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.lineEdit.returnPressed.connect(self.loadURL)
        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, Dialog):
        self.setWindowTitle(_translate("Contact Us", "Contact Us", None))

    def loadURL(self):
        url = self.lineEdit.text()
        self.qwebview.load(QtCore.QUrl('http://www.dit.ie/lttc/webcourseslogin/'))
        self.show()


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
            self.step = 0       #The pictures will reset from the start after the length of the image array has been finished
            return
        self.timer.start(self.delay, self)
        file = self.image_files[self.step]
        image = QtGui.QPixmap(file)
        self.label.setPixmap(image)
        self.step += 1

#Array of images being stored here
image_files = ["images\slide1.jpg", "images\slide2.jpg", "images\slide3.jpg",
 "images\slide4.jpg", "images\slide5.jpg"]


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon("icons\dit_crest_2010.gif"))
    Main = MainWindow(image_files)
    Main.show()
    sys.exit(app.exec_())
