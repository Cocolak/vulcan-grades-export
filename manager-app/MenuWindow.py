from PyQt5 import QtCore, QtGui, QtWidgets
import res

class Ui_MenuWindow(object):
    def setupUi(self, MenuWindow):
        self.MenuWindow = MenuWindow
        MenuWindow.setObjectName("MenuWindow")
        MenuWindow.resize(450, 500)
        MenuWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        MenuWindow.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        
        self.widget = QtWidgets.QWidget(MenuWindow)
        self.widget.setGeometry(QtCore.QRect(30, 30, 400, 450))
        self.widget.setStyleSheet("QPushButton {\n"
                                "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(230, 80, 100, 230), stop:1 rgba(180, 0, 110, 230));\n"
                                "color:rgba(255,255,255,210);\n"
                                "border:1px solid rgba(150,0,85,255);\n"
                                "border-radius:5px;\n"
                                "}\n"
                                "QPushButton:hover {\n"
                                "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(250, 100, 120, 230), stop:1 rgba(200, 20, 130, 230));\n"
                                "}\n"
                                "QPushButton:pressed {\n"
                                "padding-left:5px;\n"
                                "padding-top:5px;\n"
                                "}")
        self.widget.setObjectName("widget")

        self.loginpanelLabel = QtWidgets.QLabel(self.widget)
        self.loginpanelLabel.setGeometry(QtCore.QRect(25, 25, 350, 400))
        self.loginpanelLabel.setStyleSheet("border-image: url(:/images/Assets/background.jpg);\n"
                                            "border-radius:20px;")
        self.loginpanelLabel.setText("")
        self.loginpanelLabel.setObjectName("loginpanelLabel")

        self.registerLabel = QtWidgets.QLabel(self.widget)
        self.registerLabel.setGeometry(QtCore.QRect(133, 80, 135, 35))
        font = QtGui.QFont()
        font.setPointSize(23)
        font.setBold(True)
        font.setWeight(75)
        self.registerLabel.setFont(font)
        self.registerLabel.setObjectName("registerLabel")
        
        self.regButton = QtWidgets.QPushButton(self.widget)
        self.regButton.setGeometry(QtCore.QRect(100, 250, 200, 50))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.regButton.sizePolicy().hasHeightForWidth())
        self.regButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.regButton.setFont(font)
        self.regButton.clicked.connect(self.registerClicked)
        self.regButton.setObjectName("regButton")

        self.logButton = QtWidgets.QPushButton(self.widget)
        self.logButton.setGeometry(QtCore.QRect(100, 190, 200, 50))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.logButton.sizePolicy().hasHeightForWidth())
        self.logButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.logButton.setFont(font)
        self.logButton.clicked.connect(self.loginClicked)
        self.logButton.setObjectName("logButton")

        self.githubButton = QtWidgets.QPushButton(self.widget)
        self.githubButton.setGeometry(QtCore.QRect(310, 360, 40, 40))
        self.githubButton.setStyleSheet("border-image: url(:/images/github-mark-white.png);\n"
                                        "background-color:rgba(0,0,0,0);\n"
                                        "border:none;")
        self.githubButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/Assets/github-mark-white.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.githubButton.setIcon(icon)
        self.githubButton.setIconSize(QtCore.QSize(32, 32))
        self.githubButton.setObjectName("githubButton")
        self.githubButton.clicked.connect(self.githubClicked)

        # Add window shadow
        self.registerLabel.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=0, color=QtGui.QColor(185, 30, 90, 100)))
        self.logButton.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=3, yOffset=3, color=QtGui.QColor(185, 30, 90, 100)))
        self.regButton.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=3, yOffset=3, color=QtGui.QColor(185, 30, 90, 100)))

        self.retranslateUi(MenuWindow)
        QtCore.QMetaObject.connectSlotsByName(MenuWindow)

    def retranslateUi(self, MenuWindow):
        _translate = QtCore.QCoreApplication.translate
        MenuWindow.setWindowTitle(_translate("MenuWindow", "Form"))
        self.registerLabel.setText(_translate("MenuWindow", "Welcome"))
        self.regButton.setText(_translate("MenuWindow", "Register"))
        self.logButton.setText(_translate("MenuWindow", "Login"))

    def loginClicked(self):
        from LoginWindow import Ui_LoginWindow

        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_LoginWindow()
        self.ui.setupUi(self.window)
        qr = self.window.frameGeometry()
        cp = QtWidgets.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.window.move(qr.topLeft())

        self.MenuWindow.close()
        self.window.show()

    def registerClicked(self):
        from RegisterWindow import Ui_RegisterWindow

        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_RegisterWindow()
        self.ui.setupUi(self.window)
        qr = self.window.frameGeometry()
        cp = QtWidgets.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.window.move(qr.topLeft())
        
        self.MenuWindow.close()
        self.window.show()

    def githubClicked(self):
        import webbrowser
        webbrowser.open('https://github.com/Cocolak')