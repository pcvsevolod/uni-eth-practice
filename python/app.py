from massageRoom import MassageRoom
import sys

from PyQt5.QtWidgets import (
    QApplication,
    QDialog,
    QMainWindow,
    QMessageBox,
    QTableWidgetItem,
)

from localManager import LocalManager


from PyQt5.QtWidgets import (
    QApplication,
    QDialog,
    QMainWindow,
    QMessageBox,
    QTableWidgetItem,
)
from PyQt5.uic import loadUi

from ui.mainWindow import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    localManager: LocalManager
    massageRoom: MassageRoom

    def __init__(self, localManager, massageRoom, parent=None):
        super().__init__(parent)
        self.localManager = localManager
        self.massageRoom = massageRoom
        self.setupUi(self)
        self.customSetup()

    def customSetup(self):
        self.tabWidget.setTabEnabled(1, False)
        self.tabWidget.setTabEnabled(2, False)
        self.tabWidget.setTabEnabled(3, False)
        self.buttonLogin.clicked.connect(self.onLogin)
        self.buttonRefresh.clicked.connect(self.onRefresh)
        self.buttonRegisterAsClient.clicked.connect(self.onRegisterAsClient)
        self.buttonRegisterAsWorker.clicked.connect(self.onRegisterAsWorker)
        self.refresh()

    def onLogin(self):
        address = self.textAddress.text()
        private_key = self.textPrivateKey.text()
        self.localManager.tryLogin(address, private_key)
        if self.localManager.isLoggedIn():
            self.labelLogin.setText("Logged in!")
        else:
            self.labelLogin.setText("Incorrect address or password")

    def onRefresh(self):
        self.refresh()

    def onRegisterAsClient(self):
        self.massageRoom.registerAsClient(localManager.address)

    def onRegisterAsWorker(self):
        self.massageRoom.askToRegisterAsWorker(localManager.address)

    def refresh(self):
        self.updateTabs()
        self.updateServicesTable()
        self.updateButtons()

    def updateServicesTable(self):
        self.tableServices.clear()
        servicesLength = self.massageRoom.getServicesLength()
        print(f"{servicesLength=}")
        for i in range(servicesLength):
            self.tableServices.setItem(
                i, 0, QTableWidgetItem(str(self.massageRoom.getServiceName(i)))
            )
            self.tableServices.setItem(
                i, 1, QTableWidgetItem(str(self.massageRoom.getServicePrice(i)))
            )

    def updateTabs(self):
        if self.massageRoom.isAdmin():
            self.tabWidget.setTabEnabled(1, True)
            print(f"is Admin")
        else:
            self.tabWidget.setTabEnabled(1, False)
            print(f"not Admin")
            if self.tabWidget.currentIndex() == 1:
                self.tabWidget.setCurrentIndex(0)

        if self.massageRoom.isAWorker(localManager.address):
            self.tabWidget.setTabEnabled(2, True)
            print(f"is Admin")
        else:
            self.tabWidget.setTabEnabled(2, False)
            print(f"not Admin")
            if self.tabWidget.currentIndex() == 2:
                self.tabWidget.setCurrentIndex(0)

        if self.massageRoom.isAClient(localManager.address):
            self.tabWidget.setTabEnabled(3, True)
            print(f"is Admin")
        else:
            self.tabWidget.setTabEnabled(3, False)
            print(f"not Admin")
            if self.tabWidget.currentIndex() == 3:
                self.tabWidget.setCurrentIndex(0)

    def updateButtons(self):
        loggedIn = localManager.isLoggedIn()
        self.buttonRegisterAsClient.setEnabled(loggedIn)
        self.buttonRegisterAsWorker.setEnabled(loggedIn)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    localManager = LocalManager()

    m = MassageRoom(localManager)
    print(f"{m.getTestValue()}")

    mainWin = MainWindow(localManager, m)
    mainWin.show()

    sys.exit(app.exec())
