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
        accountAddress = web3.Web3.toChecksumAddress(self.localManager.address)
        transaction = self.contract.functions.isAdmin().buildTransaction(
            {
                "gas": 70000,
                # "gasPrice": web3.toWei("1", "gwei"),
                "from": accountAddress,
                "nonce": self.w3.eth.getTransactionCount(accountAddress),
            }
        )
        private_key = LocalManager.pr_key
        signed_txn = web3.Account.signTransaction(transaction, private_key=private_key)
        return self.w3.eth.sendRawTransaction(signed_txn.rawTransaction)
        # return self.contract.functions.isAdmin().call()

    def askToRegisterAsWorker(self, name):
        self.contract.functions.askToRegisterAsWorker().call(name)

    def approveWorkerRegistrationRequest(self, workerAddr):
        self.contract.functions.askToRegisterAsWorker().call(workerAddr)

    def haveIAskedToBeAWorker(self):
        return self.contract.functions.haveIAskedToBeAWorker().call()

    def isAWorker(self, addr):
        return self.contract.functions.isAWorker().call(addr)

    def isWorkerAvailable(self, workerAddr):
        return self.contract.functions.isWorkerAvailable().call(workerAddr)

    def setWorkerAsUnavailable(self, workerAddr):
        return self.contract.functions.setWorkerAsUnavailable().call(workerAddr)

    def setWorkerAsAvailable(self, workerAddr):
        return self.contract.functions.setWorkerAsAvailable().call(workerAddr)

    def registerAsClient(self, name):
        self.contract.functions.registerAsClient().call(name)

    def isAClient(self, addr):
        return self.contract.functions.isAClient().call(addr)

    def createService(self, name, price):
        self.contract.functions.createService().call(name, price)

    def getServicesLength(self):
        return self.contract.functions.getServicesLength().call()

    def getServiceName(self, i):
        return self.contract.functions.getServicesLength().call(i)

    def getServicePrice(self, i):
        return self.contract.functions.getServicePrice().call(i)

    def setServiceAsUnavailable(self, i):
        self.contract.functions.setServiceAsUnavailable().call(i)

    def setServiceAsAvailable(self, i):
        self.contract.functions.setServiceAsAvailable().call(i)

    def isServiceAvailable(self, i):
        return self.contract.functions.isServiceAvailable().call(i)

    def requestAppointment(self, serviceI, time):
        self.contract.functions.requestAppointment().call(serviceI, time)

    def isAppointmentApproved(self, i):
        return self.contract.functions.isAppointmentApproved().call(i)

    def approveAppointment(self, i):
        self.contract.functions.approveAppointment().call(i)

    def getClientAppointments(self, client):
        return self.contract.functions.getClientAppointments().call(client)

    def getAppointmentService(self, i):
        return self.contract.functions.getAppointmentService().call(i)

    def getAppointmentTime(self, i):
        return self.contract.functions.getAppointmentTime().call(i)
