from PyQt5 import QtCore, QtGui, QtWidgets
import res

class Ui_RegisterWindow(object):
    def setupUi(self, RegisterWindow):
        self.RegisterWindow = RegisterWindow
        RegisterWindow.setObjectName("RegisterWindow")
        RegisterWindow.resize(450, 600)
        RegisterWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        RegisterWindow.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        
        self.widget = QtWidgets.QWidget(RegisterWindow)
        self.widget.setGeometry(QtCore.QRect(30, 30, 400, 550))
        self.widget.setStyleSheet("QPushButton#regButton {\n"
                                "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(230, 80, 100, 230), stop:1 rgba(180, 0, 110, 230));\n"
                                "color:rgba(255,255,255,210);\n"
                                "border:1px solid rgba(150,0,85,255);\n"
                                "border-radius:5px;\n"
                                "}\n"
                                "QPushButton#regButton:hover {\n"
                                "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(250, 100, 120, 230), stop:1 rgba(200, 20, 130, 230));\n"
                                "}\n"
                                "QPushButton#regButton:pressed {\n"
                                "padding-left:5px;\n"
                                "padding-top:5px;\n"
                                "}\n"
                                "QPushButton#tutorialButton:hover {\n"
                                "color:rgba(220,150,160,255);\n"
                                "}\n"
                                "QPushButton#exitButton{\n"
                                "background-color:rgba(150,0, 100, 255);\n"
                                "}")
        self.widget.setObjectName("widget")

        ### Main panel
        self.loginpanelLabel = QtWidgets.QLabel(self.widget)
        self.loginpanelLabel.setGeometry(QtCore.QRect(25, 25, 350, 500))
        self.loginpanelLabel.setStyleSheet("border-image: url(:/images/Assets/background.jpg);\n"
                                        "border-radius:20px;\n"
                                        "")
        self.loginpanelLabel.setObjectName("loginpanelLabel")

        self.registerLabel = QtWidgets.QLabel(self.widget)
        self.registerLabel.setGeometry(QtCore.QRect(107, 80, 185, 50))
        font = QtGui.QFont()
        font.setPointSize(23)
        font.setBold(True)
        self.registerLabel.setFont(font)
        self.registerLabel.setObjectName("registerLabel")

        ### Input section
        self.tokenLineEdit = QtWidgets.QLineEdit(self.widget)
        self.tokenLineEdit.setGeometry(QtCore.QRect(100, 180, 200, 40))
        self.tokenLineEdit.setStyleSheet("background-color:rgba(0,0,0,0);\n"
                                        "border:none;\n"
                                        "border-bottom:2px solid rgba(150,0,85,255);\n"
                                        "color:rgba(255,255,255,240);\n"
                                        "padding-bottom:7px;")
        self.tokenLineEdit.setObjectName("tokenLineEdit")

        self.symbolLineEdit = QtWidgets.QLineEdit(self.widget)
        self.symbolLineEdit.setGeometry(QtCore.QRect(100, 240, 200, 40))
        self.symbolLineEdit.setStyleSheet("background-color:rgba(0,0,0,0);\n"
                                        "border:none;\n"
                                        "border-bottom:2px solid rgba(150,0,85,255);\n"
                                        "color:rgba(255,255,255,240);\n"
                                        "padding-bottom:7px;")
        self.symbolLineEdit.setObjectName("symbolLineEdit")
        
        self.pinLineEdit = QtWidgets.QLineEdit(self.widget)
        self.pinLineEdit.setGeometry(QtCore.QRect(100, 300, 200, 40))
        self.pinLineEdit.setStyleSheet("background-color:rgba(0,0,0,0);\n"
                                        "border:none;\n"
                                        "border-bottom:2px solid rgba(150,0,85,255);\n"
                                        "color:rgba(255,255,255,240);\n"
                                        "padding-bottom:7px;")
        self.pinLineEdit.setObjectName("pinLineEdit")

        self.regButton = QtWidgets.QPushButton(self.widget)
        self.regButton.setGeometry(QtCore.QRect(100, 370, 200, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.regButton.setFont(font)
        self.regButton.setObjectName("regButton")
        self.regButton.clicked.connect(self.registerClicked)

        ## Tutorial
        self.tutorialButton = QtWidgets.QPushButton(self.widget)
        self.tutorialButton.setGeometry(QtCore.QRect(125, 415, 150, 21))
        self.tutorialButton.setMinimumSize(QtCore.QSize(121, 21))
        self.tutorialButton.setStyleSheet("background-color:rgba(0,0,0,0);\n"
                                        "border:none;")
        self.tutorialButton.setObjectName("tutorialButton")
        self.tutorialButton.clicked.connect(self.tutorialClicked)


        self.githubButton = QtWidgets.QPushButton(self.widget)
        self.githubButton.setGeometry(QtCore.QRect(310, 460, 40, 40))
        self.githubButton.setStyleSheet("border-image: url(:/images/Assets/github-mark-white.png);\n"
                                        "border-radius:20px;")
        self.githubButton.setText("")
        self.githubButton.setObjectName("githubButton")
        self.githubButton.clicked.connect(self.githubClicked)

        # Add window shadow
        self.registerLabel.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=0, color=QtGui.QColor(185, 30, 90, 100)))
        self.regButton.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=3, yOffset=3, color=QtGui.QColor(185, 30, 90, 100)))

        self.retranslateUi(RegisterWindow)
        QtCore.QMetaObject.connectSlotsByName(RegisterWindow)

    def retranslateUi(self, RegisterWindow):
        _translate = QtCore.QCoreApplication.translate
        RegisterWindow.setWindowTitle(_translate("RegisterWindow", "Form"))
        self.registerLabel.setText(_translate("RegisterWindow", "Registration"))
        self.tokenLineEdit.setPlaceholderText(_translate("RegisterWindow", "Token"))
        self.symbolLineEdit.setPlaceholderText(_translate("RegisterWindow", "Symbol"))
        self.pinLineEdit.setPlaceholderText(_translate("RegisterWindow", "PIN"))
        self.regButton.setText(_translate("RegisterWindow", "Register"))
        self.tutorialButton.setText(_translate("RegisterWindow", "Where to find this data?"))

    def tutorialClicked(self):
        ## TODO update funcion
        pass

    def githubClicked(self):
        import webbrowser
        webbrowser.open('https://github.com/Cocolak')

    def registerClicked(self):
        from PyQt5.QtWidgets import QMessageBox
        import vulcan_chandle as vc
        import asyncio

        token = self.tokenLineEdit.text().upper().strip()
        symbol = self.symbolLineEdit.text().strip()
        pin = self.pinLineEdit.text().strip()
        
        isRegister = asyncio.run(vc.register(token, symbol, pin))

        if isRegister == True:
            msg = QMessageBox()
            msg.setWindowTitle("Successful register")
            msg.setText("Successful register.")
            msg.setIcon(QMessageBox.Information)
            msg.exec_()

            ## TODO Login

        elif isRegister == False:
            msg = QMessageBox()
            msg.setWindowTitle("Failed register")
            msg.setText("Failed register. Try again.")
            msg.setIcon(QMessageBox.Information)
            msg.exec_()



