from PyQt5 import QtCore, QtGui, QtWidgets
import res

class Ui_LoginWindow(object):
    def setupUi(self, LoginWindow):
        LoginWindow.setObjectName("LoginWindow")
        LoginWindow.resize(450, 600)
        LoginWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        LoginWindow.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.LoginWindow = LoginWindow
        self.Keystore_path = "path"
        self.Account_path = "path"

        self.widget = QtWidgets.QWidget(LoginWindow)
        self.widget.setGeometry(QtCore.QRect(30, 30, 400, 550))
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
                                "}\n"
                                "QCheckBox#remCheckBox:hover{\n"
                                "background-color:rgba(0,0,0,0);\n"
                                "}")
        self.widget.setObjectName("widget")

        self.loginpanelLabel = QtWidgets.QLabel(self.widget)
        self.loginpanelLabel.setGeometry(QtCore.QRect(25, 25, 350, 500))
        self.loginpanelLabel.setStyleSheet("border-image: url(:/images/Assets/background.jpg);\n"
                                            "border-radius:20px;")
        self.loginpanelLabel.setText("")
        self.loginpanelLabel.setObjectName("loginpanelLabel")

        self.registerLabel = QtWidgets.QLabel(self.widget)
        self.registerLabel.setGeometry(QtCore.QRect(158, 80, 85, 35))
        font = QtGui.QFont()
        font.setPointSize(23)
        font.setBold(True)
        font.setWeight(75)
        self.registerLabel.setFont(font)
        self.registerLabel.setObjectName("registerLabel")

        self.keystoreWidget = QtWidgets.QWidget(self.widget)
        self.keystoreWidget.setGeometry(QtCore.QRect(25, 170, 350, 60))
        self.keystoreWidget.setObjectName("keystoreWidget")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.keystoreWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        self.keystorePath = QtWidgets.QLabel(self.keystoreWidget)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.keystorePath.setFont(font)
        self.keystorePath.setObjectName("keystorePath")
        self.verticalLayout.addWidget(self.keystorePath, 0, QtCore.Qt.AlignHCenter)
        self.keystoreButton = QtWidgets.QPushButton(self.keystoreWidget)
        self.keystoreButton.setMinimumSize(QtCore.QSize(150, 25))
        self.keystoreButton.setMaximumSize(QtCore.QSize(150, 16777215))
        self.keystoreButton.setObjectName("keystoreButton")
        self.keystoreButton.clicked.connect(self.keystoreClicked)

        self.verticalLayout.addWidget(self.keystoreButton, 0, QtCore.Qt.AlignHCenter)
        self.accountWidget = QtWidgets.QWidget(self.widget)
        self.accountWidget.setGeometry(QtCore.QRect(25, 250, 350, 60))
        self.accountWidget.setObjectName("accountWidget")

        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.accountWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.accountPath = QtWidgets.QLabel(self.accountWidget)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.accountPath.setFont(font)
        self.accountPath.setObjectName("accountPath")
        self.verticalLayout_2.addWidget(self.accountPath, 0, QtCore.Qt.AlignHCenter)

        self.accountButton = QtWidgets.QPushButton(self.accountWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.accountButton.sizePolicy().hasHeightForWidth())
        self.accountButton.setSizePolicy(sizePolicy)
        self.accountButton.setMinimumSize(QtCore.QSize(150, 25))
        self.accountButton.setMaximumSize(QtCore.QSize(150, 16777215))
        self.accountButton.setObjectName("accountButton")
        self.accountButton.clicked.connect(self.accountClicked)
        self.verticalLayout_2.addWidget(self.accountButton, 0, QtCore.Qt.AlignHCenter)

        self.logButton = QtWidgets.QPushButton(self.widget)
        self.logButton.setGeometry(QtCore.QRect(100, 350, 200, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.logButton.setFont(font)
        self.logButton.setObjectName("logButton")
        self.logButton.clicked.connect(self.loginClicked)

        self.remCheckBox = QtWidgets.QCheckBox(self.widget)
        self.remCheckBox.setGeometry(QtCore.QRect(100, 400, 116, 21))
        self.remCheckBox.setObjectName("remCheckBox")

        self.githubButton = QtWidgets.QPushButton(self.widget)
        self.githubButton.setGeometry(QtCore.QRect(310, 460, 40, 40))
        self.githubButton.setStyleSheet("border-image: url(:/images/github-mark-white.png);\n"
                                        "border-radius:20px;\n"
                                        "background-color:rgba(0,0,0,0);")
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
        self.keystoreButton.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=3, yOffset=3, color=QtGui.QColor(185, 30, 90, 100)))
        self.accountButton.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=3, yOffset=3, color=QtGui.QColor(185, 30, 90, 100)))

        self.retranslateUi(LoginWindow)
        QtCore.QMetaObject.connectSlotsByName(LoginWindow)

    def retranslateUi(self, LoginWindow):
        _translate = QtCore.QCoreApplication.translate
        LoginWindow.setWindowTitle(_translate("LoginWindow", "Form"))
        self.registerLabel.setText(_translate("LoginWindow", "Login"))
        self.logButton.setText(_translate("LoginWindow", "Login"))
        self.remCheckBox.setText(_translate("LoginWindow", "Remember me"))
        self.keystorePath.setText(_translate("LoginWindow", self.Keystore_path))
        self.keystoreButton.setText(_translate("LoginWindow", "Select Keystore"))
        self.accountPath.setText(_translate("LoginWindow", self.Account_path))
        self.accountButton.setText(_translate("LoginWindow", "Select Account"))

    def keystoreClicked(self):
        self.Keystore_path = QtWidgets.QFileDialog.getOpenFileName(self.LoginWindow, "Open Keystore File", "!_reg", "Keystore File (*.json)", )
        self.keystorePath.setText(self.Keystore_path[0])

    def accountClicked(self):
        self.Account_path = QtWidgets.QFileDialog.getOpenFileName(self.LoginWindow, "Open Account File", "!_reg", "Account File (*.json)", )
        self.accountPath.setText(self.Account_path[0])

    def loginClicked(self):
        from PyQt5.QtWidgets import QMessageBox
        import os, shutil
        import vulcan_chandle as vc
        import asyncio

        isLogin, client = asyncio.run(vc.login(self.Keystore_path[0], self.Account_path[0]))

        if isLogin:
            if self.remCheckBox.isChecked():
                if not os.path.exists("!_reg"):
                    os.makedirs("!_reg")

                try: shutil.copyfile(self.Keystore_path[0], "!_reg/Keystore.json")
                except: pass
                try: shutil.copyfile(self.Account_path[0], "!_reg/Account.json")
                except: pass

            self.runManagerWindow(client)
        else:
            msg = QMessageBox()
            msg.setWindowTitle("Login error")
            msg.setText("Login error. Want to register?")
            msg.setIcon(QMessageBox.Question)
            msg.setStandardButtons(QMessageBox.Yes|QMessageBox.No)
            msg.setDefaultButton(QMessageBox.No)
            msg.setInformativeText("See details for more.")
            msg.setDetailedText("1. First opening of the app.\n"
                                "2. Missing or invalid 'keystore.json' or 'account.json' file in the '!_reg' folder.\n"
                                "3. Expired session in Vulcan application.")
            wantRegister = msg.exec_()

            if wantRegister == QMessageBox.Yes:
                self.runRegisterWindow()
            else:
                self.LoginWindow.close()

    def runRegisterWindow(self):
        from RegisterWindow import Ui_RegisterWindow

        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_RegisterWindow()
        self.ui.setupUi(self.window)
        qr = self.window.frameGeometry()
        cp = QtWidgets.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.window.move(qr.topLeft())
        
        self.LoginWindow.close()
        self.window.show()

    def runManagerWindow(self, client):
        from ManagerWindow import Ui_ManagerWindow

        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_ManagerWindow()
        self.ui.setupUi(self.window, client)
        qr = self.window.frameGeometry()
        cp = QtWidgets.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.window.move(qr.topLeft())
        
        self.LoginWindow.close()
        self.window.show()

    def githubClicked(self):
        import webbrowser
        webbrowser.open('https://github.com/Cocolak')