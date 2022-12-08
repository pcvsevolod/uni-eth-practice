from massageRoom import MassageRoom
import sys

from PyQt5.QtWidgets import (
    QApplication,
    QDialog,
    QMainWindow,
    QMessageBox,
    QTableWidgetItem,
)
from PyQt5.uic import loadUi

from ui.loginWindow import Ui_LoginWindow
from localManager import LocalManager


class LoginWindow(QMainWindow, Ui_LoginWindow):
    localManager = None

    def __init__(self, localManager, parent=None):
        super().__init__(parent)
        self.localManager = localManager
        self.setupUi(self)
        self.custom_setup()

    def custom_setup(self):
        self.buttonLogin.clicked.connect(self.on_login)

    def on_login(self):
        address = self.textAddress.text()
        private_key = self.textPrivateKey.text()
        localManager.tryLogin(address, private_key)
        if localManager.isLoggedIn():
            self.close()
        else:
            self.label.setText("Incorrect address or password")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    localManager = LocalManager()
    loginWindow = LoginWindow(localManager)
    loginWindow.show()
    sys.exit(app.exec())
