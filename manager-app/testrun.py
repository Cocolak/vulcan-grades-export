import vulcan_chandle as vc
import asyncio, sys
from PyQt5 import QtWidgets
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
