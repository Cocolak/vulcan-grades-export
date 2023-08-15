from PyQt5 import QtWidgets
import sys
from RegisterWindow import Ui_RegisterWindow

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