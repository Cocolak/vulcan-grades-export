def get_keystore():
    from vulcan import Keystore
    with open("!_reg/keystore.json") as f: keystore = Keystore.load(f)
    return keystore

def get_account():
    from vulcan import Account
    with open("!_reg/account.json") as f: account = Account.load(f)
    return account

async def register(token, symbol, pin):
    from vulcan import Keystore, Account
    
    keystore = await Keystore.create(device_model="Vulcan Manager")
    with open("!_reg/keystore.json", "w") as f: f.write(keystore.as_json)
    
    try: account = await Account.register(keystore, token, symbol, pin)
    except:
        print("Nieprawidłowe dane") 
        ## TODO Komunikat 
        return

    with open("!_reg/account.json", "w") as f: f.write(account.as_json)

async def login():
    def runRegisterWindow():
        window = QtWidgets.QMainWindow()
        ui = Ui_RegisterWindow()
        ui.setupUi(window)
        qr = window.frameGeometry()
        cp = QtWidgets.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        window.move(qr.topLeft())
        window.show()
        sys.exit(app.exec_())

    import sys
    from vulcan import Vulcan
    from PyQt5 import QtWidgets
    from PyQt5.QtWidgets import QMessageBox
    from RegisterWindow import Ui_RegisterWindow

    try: client = Vulcan(keystore=get_keystore(), account=get_account())
    except:
        ## TODO Sprawdź czy można rozpoznać jaka jest przyczyna błędu w logowaniu

        app = QtWidgets.QApplication(sys.argv)

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
        choice = msg.exec_()
        
        if choice == QMessageBox.Yes:
            runRegisterWindow()
        else: return

    ## Open MangerWindow(client)

