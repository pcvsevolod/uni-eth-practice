import sys

from PyQt5.QtWidgets import (
    QApplication,
    QDialog,
    QMainWindow,
    QMessageBox,
    QTableWidgetItem,
)

from PyQt5.QtWidgets import (
    QApplication,
    QDialog,
    QMainWindow,
    QMessageBox,
    QTableWidgetItem,
)
from PyQt5.uic import loadUi

from ui.mainWindow import Ui_MainWindow


from w3_manager import W3
from massage_room import MassageRoom


class MainWindow(QMainWindow, Ui_MainWindow):
    m: MassageRoom

    def __init__(self, massage_room: MassageRoom, w3: W3, parent=None):
        super().__init__(parent)
        self.m = massage_room
        self.w3 = w3
        self.setupUi(self)
        self.custom_setup()

    def custom_setup(self):
        self.setup_buttons()
        self.refresh()

    def refresh(self):
        self.m.refresh()
        # self.update_buttons()
        # self.updateTabs()
        # self.updateServicesTable()

    def setup_buttons(self):
        self.buttonLogin.clicked.connect(self.on_login)
        # self.buttonRefresh.clicked.connect(self.onRefresh)
        # self.buttonRegisterAsClient.clicked.connect(self.onRegisterAsClient)
        # self.buttonRegisterAsWorker.clicked.connect(self.onRegisterAsWorker)

    def on_login(self):
        address = self.textAddress.text()
        pr_key = self.textPrivateKey.text()

        if self.w3.is_private_key_correct(address, pr_key):
            self.w3.change_default_account(address)
            self.refresh()
            self.labelLogin.setText("Logged in!")
        else:
            self.labelLogin.setText("Incorrect address or password")

    # def onRefresh(self):
    #     self.refresh()

    # def onRegisterAsClient(self):
    #     self.massageRoom.registerAsClient(localManager.address)

    # def onRegisterAsWorker(self):
    #     self.massageRoom.askToRegisterAsWorker(localManager.address)

    # def updateServicesTable(self):
    #     self.tableServices.clear()
    #     servicesLength = self.massageRoom.getServicesLength()
    #     print(f"{servicesLength=}")
    #     for i in range(servicesLength):
    #         self.tableServices.setItem(
    #             i, 0, QTableWidgetItem(str(self.massageRoom.getServiceName(i)))
    #         )
    #         self.tableServices.setItem(
    #             i, 1, QTableWidgetItem(str(self.massageRoom.getServicePrice(i)))
    #         )

    # def updateTabs(self):
    #     if self.massageRoom.isAdmin():
    #         self.tabWidget.setTabEnabled(1, True)
    #         print(f"is Admin")
    #     else:
    #         self.tabWidget.setTabEnabled(1, False)
    #         print(f"not Admin")
    #         if self.tabWidget.currentIndex() == 1:
    #             self.tabWidget.setCurrentIndex(0)

    #     if self.massageRoom.isAWorker(localManager.address):
    #         self.tabWidget.setTabEnabled(2, True)
    #         print(f"is Admin")
    #     else:
    #         self.tabWidget.setTabEnabled(2, False)
    #         print(f"not Admin")
    #         if self.tabWidget.currentIndex() == 2:
    #             self.tabWidget.setCurrentIndex(0)

    #     if self.massageRoom.isAClient(localManager.address):
    #         self.tabWidget.setTabEnabled(3, True)
    #         print(f"is Admin")
    #     else:
    #         self.tabWidget.setTabEnabled(3, False)
    #         print(f"not Admin")
    #         if self.tabWidget.currentIndex() == 3:
    #             self.tabWidget.setCurrentIndex(0)

    # def updateButtons(self):
    #     loggedIn = localManager.isLoggedIn()
    #     self.buttonRegisterAsClient.setEnabled(loggedIn)
    #     self.buttonRegisterAsWorker.setEnabled(loggedIn)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    w3 = W3("http://25.64.154.247:9545", "python/abi.json")

    m = MassageRoom(w3)
    print(f"{m.isAdmin()=}")

    mainWin = MainWindow(m, w3)
    mainWin.show()

    sys.exit(app.exec())
