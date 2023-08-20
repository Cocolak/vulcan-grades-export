from PyQt5 import QtWidgets
import sys
import asyncio
import vulcan_chandle as vc

isLogin, client = asyncio.run(vc.login())

if isLogin:
    from ManagerWindow import Ui_ManagerWindow

    app = QtWidgets.QApplication(sys.argv)

    window = QtWidgets.QMainWindow()
    ui = Ui_ManagerWindow()
    ui.setupUi(window, client)
    qr = window.frameGeometry()
    cp = QtWidgets.QDesktopWidget().availableGeometry().center()
    qr.moveCenter(cp)
    window.move(qr.topLeft())
    window.show()
    sys.exit(app.exec_())

else:
    from MenuWindow import Ui_MenuWindow

    app = QtWidgets.QApplication(sys.argv)

    window = QtWidgets.QMainWindow()
    ui = Ui_MenuWindow()
    ui.setupUi(window)
    qr = window.frameGeometry()
    cp = QtWidgets.QDesktopWidget().availableGeometry().center()
    qr.moveCenter(cp)
    window.move(qr.topLeft())
    window.show()
    sys.exit(app.exec_())