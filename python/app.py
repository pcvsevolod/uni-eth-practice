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
from w3_helper import accounts
from massage_room import MassageRoom


class MainWindow(QMainWindow, Ui_MainWindow):
    m: MassageRoom

    def __init__(self, massage_room: MassageRoom, w3: W3, parent=None):
        super().__init__(parent)
        self.m = massage_room
        self.w3 = w3
        self.setupUi(self)
        self.custom_setup()

        if False:  # Prod
            self.cheat1.setVisible(False)
            self.cheat2.setVisible(False)
            self.cheat3.setVisible(False)
            self.cheat4.setVisible(False)
            self.cheat5.setVisible(False)
        else:  # Debug

            def set_cheat_login(i: int):
                print(f"set_cheat_login {i=}")
                account = accounts[i]
                self.textAddress.setText(account.address)
                self.textPrivateKey.setText(account.pr_key)

            def cheat1():
                set_cheat_login(0)

            def cheat2():
                set_cheat_login(1)

            def cheat3():
                set_cheat_login(2)

            def cheat4():
                set_cheat_login(3)

            def cheat5():
                set_cheat_login(4)

            self.cheat1.clicked.connect(cheat1)
            self.cheat2.clicked.connect(cheat2)
            self.cheat3.clicked.connect(cheat3)
            self.cheat4.clicked.connect(cheat4)
            self.cheat5.clicked.connect(cheat5)

    def custom_setup(self):
        self.tabWidget.setCurrentIndex(0)
        self.setup_buttons()
        self.refresh()

    def refresh(self):
        self.m.refresh()
        self.update_name()
        self.update_buttons()
        self.update_tabs()
        self.update_services_table()

    def setup_buttons(self):
        self.buttonLogin.clicked.connect(self.on_login)
        self.buttonRefresh.clicked.connect(self.on_refresh)
        self.buttonRegisterAsClient.clicked.connect(self.on_register_as_client)
        self.buttonRegisterAsWorker.clicked.connect(self.on_register_as_worker)
        self.buttonApproveRequest.clicked.connect(self.on_approve_request)
        self.buttonGetWorkerName.clicked.connect(self.on_get_worker_name)
        self.buttonGetRequestName.clicked.connect(self.on_get_request_name)
        self.buttonGetClientName.clicked.connect(self.on_get_client_name)
        self.buttonAdminAddService.clicked.connect(self.on_add_service)

    def update_name(self):
        name = m.get_name()
        print(f"{name=}")
        self.textName.setEnabled(name == "")
        self.textName.setText(name)

    def update_buttons(self):
        logged_in = w3.is_logged_in()
        self.buttonRegisterAsClient.setEnabled(logged_in and not m.is_client())
        self.buttonRegisterAsWorker.setEnabled(
            logged_in and not m.is_worker() and not m.have_asked_to_be_worker()
        )

    def update_tabs(self):
        def enable_tab(i: int):
            self.tabWidget.setTabEnabled(i, True)

        def disable_tab(i: int):
            self.tabWidget.setTabEnabled(i, False)
            if self.tabWidget.currentIndex() == i:
                self.tabWidget.setCurrentIndex(0)

        if self.m.is_admin():
            enable_tab(1)
        else:
            disable_tab(1)

        if self.m.is_worker():
            self.update_worker_table()
            enable_tab(2)
        else:
            disable_tab(2)

        if self.m.is_client():
            enable_tab(3)
        else:
            disable_tab(3)

    def update_services_table(self):
        self.tableServices.clear()
        services = self.m.get_services()
        self.tableServices.setRowCount(len(services))
        self.tableServices.setColumnCount(2)
        for i, s in enumerate(services):
            print(f"{i=}, {s.name=} for {s.price=}")
            self.tableServices.setItem(i, 0, QTableWidgetItem(str(s.name)))
            self.tableServices.setItem(i, 1, QTableWidgetItem(str(s.price)))

    def update_worker_table(self):
        self.tableServices.clear()
        services = self.m.get_services()
        self.tableServices.setRowCount(len(services))
        self.tableServices.setColumnCount(2)
        for i, s in enumerate(services):
            print(f"{i=}, {s.name=} for {s.price=}")
            self.tableServices.setItem(i, 0, QTableWidgetItem(str(s.name)))
            self.tableServices.setItem(i, 1, QTableWidgetItem(str(s.price)))

    def on_login(self):
        address = self.textAddress.text()
        pr_key = self.textPrivateKey.text()

        if self.w3.is_private_key_correct(address, pr_key):
            self.w3.change_default_account(address)
            self.refresh()
            self.labelLogin.setText("Logged in!")
        else:
            self.labelLogin.setText("Incorrect address or password")

    def on_refresh(self):
        self.refresh()

    def on_register_as_client(self):
        self.m.register_as_client(self.textName.text())
        self.refresh()

    def on_register_as_worker(self):
        self.m.register_as_worker(self.textName.text())
        self.refresh()

    def on_get_worker_name(self):
        try:
            addr = self.textRequestAddress.text()
            name = self.m.call_get_worker_name(addr)
            self.textAdminGName.setText(name)
        except Exception as e:
            print(f"{e=}")
            self.textAdminGName.setText("Not a worker")

    def on_get_request_name(self):
        try:
            addr = self.textRequestAddress.text()
            name = self.m.call_get_request_name(addr)
            self.textAdminGName.setText(name)
        except Exception as e:
            print(f"{e=}")
            self.textAdminGName.setText("Has no request")

    def on_get_client_name(self):
        try:
            addr = self.textRequestAddress.text()
            name = self.m.call_get_client_name(addr)
            self.textAdminGName.setText(name)
        except Exception as e:
            print(f"{e=}")
            self.textAdminGName.setText("Not a client")

    def on_approve_request(self):
        try:
            addr = self.textRequestAddress.text()
            self.m.transact_approve_request(addr)
        except Exception as e:
            print(f"{e=}")
            self.textAdminGName.setText("Has no request")

    def on_add_service(self):
        try:
            name = self.textAdminServiceName.text()
            price = int(self.textAdminServicePrice.text())
            self.m.transact_add_service(name, price)
            self.refresh()
        except Exception as e:
            print(f"{e=}")
            self.textAdminGName.setText("ERROR")


if __name__ == "__main__":
    app = QApplication(sys.argv)

    w3 = W3("http://25.64.154.247:9545", "python/abi.json")

    m = MassageRoom(w3)

    mainWin = MainWindow(m, w3)
    mainWin.show()

    sys.exit(app.exec())
