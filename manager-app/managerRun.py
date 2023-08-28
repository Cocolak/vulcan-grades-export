from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QPushButton
import sys, res

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('ui/managerWindow.ui', self) 
        self.show()

        self.menuButton = self.findChild(QPushButton, "menuButton")
        self.icon_sidebar = self.find()

        self.menuButton.setChecked(True)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    app.exec_()