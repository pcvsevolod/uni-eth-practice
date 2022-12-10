from w3_manager import W3


class Service:
    name: str
    price: int
    available: bool

    def __init__(self, name, price, available) -> None:
        self.name = name
        self.price = price
        self.available = available


class MassageRoom:
    def __init__(self, w3: W3) -> None:
        self.functions = w3.get_contract_functions()
        self.w3 = w3

    cached_is_admin = False
    cached_is_client = False
    cached_is_worker = False
    cached_have_asked_to_be_worker = False
    cached_services = []

    def is_admin(self) -> bool:
        return self.cached_is_admin

    def is_client(self) -> bool:
        return self.cached_is_client

    def have_asked_to_be_worker(self) -> bool:
        return self.cached_have_asked_to_be_worker

    def is_worker(self) -> bool:
        return self.cached_is_worker

    def get_services_length(self) -> int:
        return len(self.cached_services)

    def get_service(self, i) -> Service:
        return self.cached_services[i]

    def refresh(self):
        # Fetching for cached
        print(f"{self.w3.get_account()=}")
        if self.w3.is_logged_in():
            self.cached_is_admin = self.functions.isAdmin().call()
            self.cached_is_client = self.functions.isAClient(
                self.w3.get_account()
            ).call()
            self.cached_is_worker = self.functions.isAWorker(
                self.w3.get_account()
            ).call()
            self.cached_is_worker = self.functions.isAWorker(
                self.w3.get_account()
            ).call()
        else:
            self.cached_is_admin = False
        self.cached_is_client = False
        self.cached_is_worker = False

        self.cached_services = []
        services_l = self.functions.getServicesLength().call()
        for i in range(services_l):
            name = function.getServiceName().call(i)
            price = function.getServicePrice().call(i)
            available = function.isServiceAvailable().call(i)
            self.cached_services.append(Service(name, price, available))

        print(f"{self.cached_is_admin=}")
        print(f"{self.cached_is_client=}")
        print(f"{self.cached_is_worker=}")
        print(f"{self.cached_services=}")

    def register_as_client(self, addr):
        self.functions.registerAsClient(addr).call()

    def register_as_worker(self, addr):
        self.functions.askToRegisterAsWorker(addr).call()

    def getTestValue(self):
        return self.functions.getTestValue().call()
