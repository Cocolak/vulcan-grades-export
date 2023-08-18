from PyQt5 import QtWidgets
import sys, os
from RegisterWindow import Ui_RegisterWindow

if not os.path.exists("!_reg"):
    os.makedirs("!_reg")

    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow()
    ui = Ui_RegisterWindow()
    ui.setupUi(window)
    qr = window.frameGeometry()
    cp = QtWidgets.QDesktopWidget().availableGeometry().center()
    qr.moveCenter(cp)
    window.move(qr.topLeft())
    window.show()
    sys.exit(app.exec_())

else:
    print("Zalogowano")