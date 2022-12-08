import web3, json
import utils


class MassageRoom:
    url = "http://127.0.0.1:9545"
    w3 = web3.Web3(web3.HTTPProvider(str(url)))

    contract_address = web3.Web3.toChecksumAddress(utils.contractAddress)

    with open("python/abi.json", "r") as file:
        abi = json.load(file)

    contract = w3.eth.contract(address=contract_address, abi=abi)

    def getTestValue(self):
        return self.contract.functions.getTestValue().call()

    def askToRegisterAsWorker(self, name):
        pass

    def approveWorkerRegistrationRequest(self, workerAddr):
        pass

    def haveIAskedToBeAWorker(self):
        pass

    def isAWorker(self, addr):
        pass

    def isWorkerAvailable(self, workerAddr):
        pass

    def setWorkerAsUnavailable(self, workerAddr):
        pass

    def setWorkerAsAvailable(self, workerAddr):
        pass

    def registerAsClient(self, name):
        pass

    def isAClient(self, addr):
        pass

    def createService(self, name, price):
        pass

    def getServicesLength(self):
        pass

    def getServiceName(self, i):
        pass

    def getServicePrice(self, i):
        pass

    def setServiceAsUnavailable(self, i):
        pass

    def setServiceAsAvailable(self, i):
        pass

    def isServiceAvailable(self, i):
        pass

    def requestAppointment(self, serviceI, time):
        pass

    def isAppointmentApproved(self, i):
        pass

    def approveAppointment(self, i):
        pass

    def getClientAppointments(self, client):
        pass

    def getAppointmentService(self, i):
        pass

    def getAppointmentTime(self, i):
        pass
