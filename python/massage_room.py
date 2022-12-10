from w3_manager import W3
from typing import List


class Service:
    name: str
    price: int
    available: bool

    def __init__(self, name, price, available) -> None:
        self.name = name
        self.price = price
        self.available = available


class WorkerAppointment:
    service: int
    time: int

    def __init__(self, service, time) -> None:
        self.service = service
        self.time = time


class MassageRoom:
    def __init__(self, w3: W3) -> None:
        self.functions = w3.get_contract_functions()
        self.w3 = w3

    cached_is_admin = False
    cached_is_client = False
    cached_is_worker = False
    cached_have_asked_to_be_worker = False
    cached_name = ""
    cached_services = []
    cached_worker_appointments = []

    def get_name(self) -> str:
        return self.cached_name

    def is_admin(self) -> bool:
        return self.cached_is_admin

    def is_client(self) -> bool:
        print("\n *** is_client ***")
        print(f"{self.cached_is_client=}")
        return self.cached_is_client

    def have_asked_to_be_worker(self) -> bool:
        return self.cached_have_asked_to_be_worker

    def is_worker(self) -> bool:
        return self.cached_is_worker

    def get_services(self) -> List[Service]:
        return self.cached_services

    def refresh(self):
        print(f"{self.w3.get_account()=}")
        if self.w3.is_logged_in():
            print("logged in")
            addr = self.w3.get_account()
            print(f"{addr=}")

            self.cached_is_admin = self.functions.isAdmin().call()
            self.cached_is_client = self.functions.isAClient(addr).call()
            self.cached_is_worker = self.functions.isAWorker(addr).call()
            self.cached_have_asked_to_be_worker = self.functions.isWorkerRequestHere(
                addr
            ).call()

            if self.cached_is_client:
                self.cached_name = self.call_get_client_name(addr)
            elif self.cached_is_worker:
                self.cached_name = self.call_get_worker_name(addr)
            elif self.cached_have_asked_to_be_worker:
                self.cached_name = self.call_get_request_name(addr)
            else:
                self.cached_name = ""

        else:
            print("logged out")
            self.cached_is_admin = False
            self.cached_is_client = False
            self.cached_is_worker = False
            self.cached_have_asked_to_be_worker = False
            self.cached_name = ""

        self.cached_services = []
        services_l = self.functions.getServicesLength().call()
        for i in range(services_l):
            name = self.functions.getServiceName(i).call()
            price = self.functions.getServicePrice(i).call()
            available = self.functions.isServiceAvailable(i).call()
            self.cached_services.append(Service(name, price, available))

        if self.is_worker:
            self.cached_worker_appointments = []
            app_is = self.functions.getUnapprovedAppointments().call()
            for i in app_is:
                if i >= 0:
                    time = self.functions.getAppointmentTime(i).call()
                    service = self.functions.getAppointmentService(i).call()
                    self.cached_worker_appointments.append(
                        WorkerAppointment(time, service)
                    )

        print(f"{self.cached_is_admin=}")
        print(f"{self.cached_is_client=}")
        print(f"{self.cached_is_worker=}")
        print(f"{self.cached_have_asked_to_be_worker=}")
        print(f"{self.cached_name=}")
        print(f"{self.cached_services=}")

    def register_as_client(self, name):
        print("\n *** register_as_client ***")
        print(f"{name=}")
        self.functions.registerAsClient(name).transact()

    def register_as_worker(self, name):
        print("\n *** register_as_worker ***")
        print(f"{name=}")
        self.functions.askToRegisterAsWorker(name).transact()

    def getTestValue(self):
        return self.functions.getTestValue().call()

    def call_get_worker_name(self, addr) -> str:
        print("\n *** call_get_worker_name ***")
        addr = self.w3.to_addr(addr)
        print(f"{addr=}")
        return self.functions.getWorkerName(addr).call()

    def call_get_request_name(self, addr) -> str:
        print("\n *** call_get_request_name ***")
        addr = self.w3.to_addr(addr)
        print(f"{addr=}")
        return self.functions.getWorkerRequestName(addr).call()

    def call_get_client_name(self, addr) -> str:
        print("\n *** call_get_client_name ***")
        addr = self.w3.to_addr(addr)
        print(f"{addr=}")
        return self.functions.getClientName(addr).call()

    def transact_approve_request(self, addr):
        print("\n *** transact_approve_request ***")
        addr = self.w3.to_addr(addr)
        print(f"{addr=}")
        self.functions.approveWorkerRegistrationRequest(addr).transact()

    def transact_add_service(self, name: str, price: int):
        print("\n *** transact_add_service ***")
        print(f"{name=}")
        print(f"{price=}")
        self.functions.createService(name, price).transact()
