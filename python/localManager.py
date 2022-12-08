import utils


class LocalManager:
    address = "0x547a87b51b9d776d4a8e7063a966acafae7a3854"
    pr_key = "905f13dc50da1d564de44fff15549cb5f0018653bd355a89e8222d775106ab70"

    def tryLogin(self, address, pr_key):
        account = utils.Account(address, pr_key)
        account1 = utils.Account(address, pr_key)
        print(f"{account==account1=}")
        if account in utils.accounts:
            self.address = address
            self.pr_key = pr_key
        else:
            self.address = ""
            self.pr_key = ""

    def isLoggedIn(self):
        return self.address != ""
