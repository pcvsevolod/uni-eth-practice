import web3, json
import utils
from localManager import LocalManager


class MassageRoom:
    url = "http://25.64.154.247:9545"
    w3 = web3.Web3(web3.HTTPProvider(str(url)))

    contract_address = web3.Web3.toChecksumAddress(utils.contractAddress)

    with open("python/abi.json", "r") as file:
        abi = json.load(file)

    contract = w3.eth.contract(address=contract_address, abi=abi)

    localManager: LocalManager

    def __init__(self, localManager) -> None:
        self.localManager = localManager

    def getTestValue(self):
        return self.contract.functions.getTestValue().call()

    def isAdmin(self):
        if self.localManager.isLoggedIn():
            accountAddress = web3.Web3.toChecksumAddress(self.localManager.address)
            transaction = self.contract.functions.isAdmin().buildTransaction(
                {
                    "gas": 70000,
                    "from": accountAddress,
                    "nonce": self.w3.eth.getTransactionCount(accountAddress),
                }
            )
            private_key = LocalManager.pr_key
            signed_txn = web3.Account.signTransaction(
                transaction, private_key=private_key
            )
            return self.w3.eth.sendRawTransaction(signed_txn.rawTransaction)
        else:
            return self.contract.functions.isAdmin().call()

    def askToRegisterAsWorker(self, name):
        if self.localManager.isLoggedIn():
            accountAddress = web3.Web3.toChecksumAddress(self.localManager.address)
            transaction = self.contract.functions.isAdmin().buildTransaction(
                {
                    "gas": 70000,
                    "from": accountAddress,
                    "nonce": self.w3.eth.getTransactionCount(accountAddress),
                }
            )
            private_key = LocalManager.pr_key
            signed_txn = web3.Account.signTransaction(
                transaction, private_key=private_key
            )
            self.w3.eth.sendRawTransaction(signed_txn.rawTransaction)
        else:
            self.contract.functions.isAdmin().call()

    def approveWorkerRegistrationRequest(self, workerAddr):
        if self.localManager.isLoggedIn():
            accountAddress = web3.Web3.toChecksumAddress(self.localManager.address)
            transaction = self.contract.functions.approveWorkerRegistrationRequest(
                workerAddr
            ).buildTransaction(
                {
                    "gas": 70000,
                    "from": accountAddress,
                    "nonce": self.w3.eth.getTransactionCount(accountAddress),
                }
            )
            private_key = LocalManager.pr_key
            signed_txn = web3.Account.signTransaction(
                transaction, private_key=private_key
            )
            self.w3.eth.sendRawTransaction(signed_txn.rawTransaction)
        else:
            self.contract.functions.approveWorkerRegistrationRequest(workerAddr).call()

    def isWorkerRequestHere(self, addr):
        if self.localManager.isLoggedIn():
            accountAddress = web3.Web3.toChecksumAddress(self.localManager.address)
            transaction = self.contract.functions.isWorkerRequestHere(
                addr
            ).buildTransaction(
                {
                    "gas": 70000,
                    "from": accountAddress,
                    "nonce": self.w3.eth.getTransactionCount(accountAddress),
                }
            )
            private_key = LocalManager.pr_key
            signed_txn = web3.Account.signTransaction(
                transaction, private_key=private_key
            )
            return self.w3.eth.sendRawTransaction(signed_txn.rawTransaction)
        else:
            return self.contract.functions.isWorkerRequestHere(addr).call()

    def isAWorker(self, addr):
        if self.localManager.isLoggedIn():
            accountAddress = web3.Web3.toChecksumAddress(self.localManager.address)
            transaction = self.contract.functions.isAWorker(addr).buildTransaction(
                {
                    "gas": 70000,
                    "from": accountAddress,
                    "nonce": self.w3.eth.getTransactionCount(accountAddress),
                }
            )
            private_key = LocalManager.pr_key
            signed_txn = web3.Account.signTransaction(
                transaction, private_key=private_key
            )
            return self.w3.eth.sendRawTransaction(signed_txn.rawTransaction)
        else:
            return self.contract.functions.isAWorker(addr).call()

    def getWorkerName(self, addr):
        if self.localManager.isLoggedIn():
            accountAddress = web3.Web3.toChecksumAddress(self.localManager.address)
            transaction = self.contract.functions.getWorkerName(addr).buildTransaction(
                {
                    "gas": 70000,
                    "from": accountAddress,
                    "nonce": self.w3.eth.getTransactionCount(accountAddress),
                }
            )
            private_key = LocalManager.pr_key
            signed_txn = web3.Account.signTransaction(
                transaction, private_key=private_key
            )
            return self.w3.eth.sendRawTransaction(signed_txn.rawTransaction)
        else:
            return self.contract.functions.getWorkerName(addr).call()

    def isWorkerAvailable(self, workerAddr):
        if self.localManager.isLoggedIn():
            accountAddress = web3.Web3.toChecksumAddress(self.localManager.address)
            transaction = self.contract.functions.isWorkerAvailable(
                workerAddr
            ).buildTransaction(
                {
                    "gas": 70000,
                    "from": accountAddress,
                    "nonce": self.w3.eth.getTransactionCount(accountAddress),
                }
            )
            private_key = LocalManager.pr_key
            signed_txn = web3.Account.signTransaction(
                transaction, private_key=private_key
            )
            return self.w3.eth.sendRawTransaction(signed_txn.rawTransaction)
        else:
            return self.contract.functions.isWorkerAvailable(workerAddr).call()

    def setWorkerAsUnavailable(self, workerAddr):
        if self.localManager.isLoggedIn():
            accountAddress = web3.Web3.toChecksumAddress(self.localManager.address)
            transaction = self.contract.functions.setWorkerAsUnavailable(
                workerAddr
            ).buildTransaction(
                {
                    "gas": 70000,
                    "from": accountAddress,
                    "nonce": self.w3.eth.getTransactionCount(accountAddress),
                }
            )
            private_key = LocalManager.pr_key
            signed_txn = web3.Account.signTransaction(
                transaction, private_key=private_key
            )
            self.w3.eth.sendRawTransaction(signed_txn.rawTransaction)
        else:
            self.contract.functions.setWorkerAsUnavailable(workerAddr).call()

    def setWorkerAsAvailable(self, workerAddr):
        if self.localManager.isLoggedIn():
            accountAddress = web3.Web3.toChecksumAddress(self.localManager.address)
            transaction = self.contract.functions.setWorkerAsAvailable(
                workerAddr
            ).buildTransaction(
                {
                    "gas": 70000,
                    "from": accountAddress,
                    "nonce": self.w3.eth.getTransactionCount(accountAddress),
                }
            )
            private_key = LocalManager.pr_key
            signed_txn = web3.Account.signTransaction(
                transaction, private_key=private_key
            )
            self.w3.eth.sendRawTransaction(signed_txn.rawTransaction)
        else:
            self.contract.functions.setWorkerAsAvailable(workerAddr).call()

    def registerAsClient(self, name):
        if self.localManager.isLoggedIn():
            accountAddress = web3.Web3.toChecksumAddress(self.localManager.address)
            transaction = self.contract.functions.registerAsClient(
                name
            ).buildTransaction(
                {
                    "gas": 70000,
                    "from": accountAddress,
                    "nonce": self.w3.eth.getTransactionCount(accountAddress),
                }
            )
            private_key = LocalManager.pr_key
            signed_txn = web3.Account.signTransaction(
                transaction, private_key=private_key
            )
            self.w3.eth.sendRawTransaction(signed_txn.rawTransaction)
        else:
            self.contract.functions.registerAsClient(name).call()

    def isAClient(self, addr):
        if self.localManager.isLoggedIn():
            accountAddress = web3.Web3.toChecksumAddress(self.localManager.address)
            transaction = self.contract.functions.isAClient(addr).buildTransaction(
                {
                    "gas": 70000,
                    "from": accountAddress,
                    "nonce": self.w3.eth.getTransactionCount(accountAddress),
                }
            )
            private_key = LocalManager.pr_key
            signed_txn = web3.Account.signTransaction(
                transaction, private_key=private_key
            )
            return self.w3.eth.sendRawTransaction(signed_txn.rawTransaction)
        else:
            return self.contract.functions.isAClient(addr).call()

    def createService(self, name, price):
        if self.localManager.isLoggedIn():
            accountAddress = web3.Web3.toChecksumAddress(self.localManager.address)
            transaction = self.contract.functions.createService(
                name, price
            ).buildTransaction(
                {
                    "gas": 70000,
                    "from": accountAddress,
                    "nonce": self.w3.eth.getTransactionCount(accountAddress),
                }
            )
            private_key = LocalManager.pr_key
            signed_txn = web3.Account.signTransaction(
                transaction, private_key=private_key
            )
            self.w3.eth.sendRawTransaction(signed_txn.rawTransaction)
        else:
            self.contract.functions.createService(name, price).call()

    def getServicesLength(self):
        if self.localManager.isLoggedIn():
            accountAddress = web3.Web3.toChecksumAddress(self.localManager.address)
            transaction = self.contract.functions.getServicesLength().buildTransaction(
                {
                    "gas": 70000,
                    "from": accountAddress,
                    "nonce": self.w3.eth.getTransactionCount(accountAddress),
                }
            )
            private_key = LocalManager.pr_key
            signed_txn = web3.Account.signTransaction(
                transaction, private_key=private_key
            )
            return self.w3.eth.send_raw_transaction(signed_txn.rawTransaction)
        else:
            return self.contract.functions.getServicesLength().call()

    def getServiceName(self, i):
        if self.localManager.isLoggedIn():
            accountAddress = web3.Web3.toChecksumAddress(self.localManager.address)
            transaction = self.contract.functions.getServiceName(i).buildTransaction(
                {
                    "gas": 70000,
                    "from": accountAddress,
                    "nonce": self.w3.eth.getTransactionCount(accountAddress),
                }
            )
            private_key = LocalManager.pr_key
            signed_txn = web3.Account.signTransaction(
                transaction, private_key=private_key
            )
            return self.w3.eth.sendRawTransaction(signed_txn.rawTransaction)
        else:
            return self.contract.functions.getServiceName(i).call()

    def getServicePrice(self, i):
        if self.localManager.isLoggedIn():
            accountAddress = web3.Web3.toChecksumAddress(self.localManager.address)
            transaction = self.contract.functions.getServicePrice(i).buildTransaction(
                {
                    "gas": 70000,
                    "from": accountAddress,
                    "nonce": self.w3.eth.getTransactionCount(accountAddress),
                }
            )
            private_key = LocalManager.pr_key
            signed_txn = web3.Account.signTransaction(
                transaction, private_key=private_key
            )
            return self.w3.eth.sendRawTransaction(signed_txn.rawTransaction)
        else:
            return self.contract.functions.getServicePrice(i).call()

    def setServiceAsUnavailable(self, i):
        if self.localManager.isLoggedIn():
            accountAddress = web3.Web3.toChecksumAddress(self.localManager.address)
            transaction = self.contract.functions.setServiceAsUnavailable(
                i
            ).buildTransaction(
                {
                    "gas": 70000,
                    "from": accountAddress,
                    "nonce": self.w3.eth.getTransactionCount(accountAddress),
                }
            )
            private_key = LocalManager.pr_key
            signed_txn = web3.Account.signTransaction(
                transaction, private_key=private_key
            )
            self.w3.eth.sendRawTransaction(signed_txn.rawTransaction)
        else:
            self.contract.functions.setServiceAsUnavailable(i).call()

    def setServiceAsAvailable(self, i):
        if self.localManager.isLoggedIn():
            accountAddress = web3.Web3.toChecksumAddress(self.localManager.address)
            transaction = self.contract.functions.setServiceAsAvailable(
                i
            ).buildTransaction(
                {
                    "gas": 70000,
                    "from": accountAddress,
                    "nonce": self.w3.eth.getTransactionCount(accountAddress),
                }
            )
            private_key = LocalManager.pr_key
            signed_txn = web3.Account.signTransaction(
                transaction, private_key=private_key
            )
            self.w3.eth.sendRawTransaction(signed_txn.rawTransaction)
        else:
            self.contract.functions.setServiceAsAvailable(i).call()

    def isServiceAvailable(self, i):
        if self.localManager.isLoggedIn():
            accountAddress = web3.Web3.toChecksumAddress(self.localManager.address)
            transaction = self.contract.functions.isServiceAvailable(
                i
            ).buildTransaction(
                {
                    "gas": 70000,
                    "from": accountAddress,
                    "nonce": self.w3.eth.getTransactionCount(accountAddress),
                }
            )
            private_key = LocalManager.pr_key
            signed_txn = web3.Account.signTransaction(
                transaction, private_key=private_key
            )
            return self.w3.eth.sendRawTransaction(signed_txn.rawTransaction)
        else:
            return self.contract.functions.isServiceAvailable(i).call()

    def requestAppointment(self, serviceI, time):
        if self.localManager.isLoggedIn():
            accountAddress = web3.Web3.toChecksumAddress(self.localManager.address)
            transaction = self.contract.functions.requestAppointment(
                serviceI, time
            ).buildTransaction(
                {
                    "gas": 70000,
                    "from": accountAddress,
                    "nonce": self.w3.eth.getTransactionCount(accountAddress),
                }
            )
            private_key = LocalManager.pr_key
            signed_txn = web3.Account.signTransaction(
                transaction, private_key=private_key
            )
            self.w3.eth.sendRawTransaction(signed_txn.rawTransaction)
        else:
            self.contract.functions.requestAppointment(serviceI, time).call()

    def isAppointmentApproved(self, i):
        if self.localManager.isLoggedIn():
            accountAddress = web3.Web3.toChecksumAddress(self.localManager.address)
            transaction = self.contract.functions.isAppointmentApproved(
                i
            ).buildTransaction(
                {
                    "gas": 70000,
                    "from": accountAddress,
                    "nonce": self.w3.eth.getTransactionCount(accountAddress),
                }
            )
            private_key = LocalManager.pr_key
            signed_txn = web3.Account.signTransaction(
                transaction, private_key=private_key
            )
            return self.w3.eth.sendRawTransaction(signed_txn.rawTransaction)
        else:
            return self.contract.functions.isAppointmentApproved(i).call()

    def approveAppointment(self, i):
        if self.localManager.isLoggedIn():
            accountAddress = web3.Web3.toChecksumAddress(self.localManager.address)
            transaction = self.contract.functions.approveAppointment(
                i
            ).buildTransaction(
                {
                    "gas": 70000,
                    "from": accountAddress,
                    "nonce": self.w3.eth.getTransactionCount(accountAddress),
                }
            )
            private_key = LocalManager.pr_key
            signed_txn = web3.Account.signTransaction(
                transaction, private_key=private_key
            )
            self.w3.eth.sendRawTransaction(signed_txn.rawTransaction)
        else:
            self.contract.functions.approveAppointment(i).call()

    def getClientAppointments(self, client):
        if self.localManager.isLoggedIn():
            accountAddress = web3.Web3.toChecksumAddress(self.localManager.address)
            transaction = self.contract.functions.getClientAppointments(
                client
            ).buildTransaction(
                {
                    "gas": 70000,
                    "from": accountAddress,
                    "nonce": self.w3.eth.getTransactionCount(accountAddress),
                }
            )
            private_key = LocalManager.pr_key
            signed_txn = web3.Account.signTransaction(
                transaction, private_key=private_key
            )
            return self.w3.eth.sendRawTransaction(signed_txn.rawTransaction)
        else:
            return self.contract.functions.getClientAppointments(client).call()

    def getAppointmentService(self, i):
        if self.localManager.isLoggedIn():
            accountAddress = web3.Web3.toChecksumAddress(self.localManager.address)
            transaction = self.contract.functions.getAppointmentService(
                i
            ).buildTransaction(
                {
                    "gas": 70000,
                    "from": accountAddress,
                    "nonce": self.w3.eth.getTransactionCount(accountAddress),
                }
            )
            private_key = LocalManager.pr_key
            signed_txn = web3.Account.signTransaction(
                transaction, private_key=private_key
            )
            return self.w3.eth.sendRawTransaction(signed_txn.rawTransaction)
        else:
            return self.contract.functions.getAppointmentService(i).call()

    def getAppointmentTime(self, i):
        if self.localManager.isLoggedIn():
            accountAddress = web3.Web3.toChecksumAddress(self.localManager.address)
            transaction = self.contract.functions.getAppointmentTime(
                i
            ).buildTransaction(
                {
                    "gas": 70000,
                    "from": accountAddress,
                    "nonce": self.w3.eth.getTransactionCount(accountAddress),
                }
            )
            private_key = LocalManager.pr_key
            signed_txn = web3.Account.signTransaction(
                transaction, private_key=private_key
            )
            return self.w3.eth.sendRawTransaction(signed_txn.rawTransaction)
        else:
            return self.contract.functions.getAppointmentTime(i).call()
