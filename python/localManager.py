import utils


class LocalManager:
    address = ""

    def tryLogin(self, address, private_key):
        if [address, private_key] in utils.accounts:
            self.address = address

    def isLoggedIn(self):
        return self.address != ""
