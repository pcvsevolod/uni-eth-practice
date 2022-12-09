import json
from web3 import Web3, HTTPProvider

import w3_helper as Helper


class W3:
    def __init__(
        self,
        url: str,
        abi_file_path: str,
    ) -> None:
        self.w3 = Web3(HTTPProvider(url))
        with open(abi_file_path, "r") as file:
            abi = json.load(file)
            self.contract = self.w3.eth.contract(
                address=Helper.contract_address, abi=abi
            )

    def get_contract_functions(self):
        return self.contract.functions

    def is_logged_in(self):
        return Web3.isChecksumAddress(self.w3.eth.default_account)

    def get_account(self):
        return self.w3.eth.default_account

    def change_default_account(self, account):
        if not Web3.isChecksumAddress(account):
            account = Web3.toChecksumAddress(account)
        self.w3.eth.default_account = account

    def is_private_key_correct(self, address, pr_key) -> bool:
        account = Helper.Account(Web3.toChecksumAddress(address), pr_key)
        return account in Helper.accounts
