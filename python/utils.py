class Account:
    def __init__(self, address, pr_key):
        self.address = address
        self.pr_key = pr_key

    def __repr__(self) -> str:
        return f"[{self.address}, {self.pr_key}]"

    def __str__(self) -> str:
        return self.__repr__()


accounts = [
    Account(
        "0x547a87b51b9d776d4a8e7063a966acafae7a3854",
        "905f13dc50da1d564de44fff15549cb5f0018653bd355a89e8222d775106ab70",
    ),
    Account(
        "0xca54e16cf9e8cfbd999eb4663d603538727b5d92",
        "5d9e668e9986127343ca00c0a8c54d4355f534f6c2e8f37230fb918f1de93df4",
    ),
    Account(
        "0x46154aba31327ca00bb672da0d4d699fb6d911a0",
        "3062b37494e7a5d3ff2918dd82288fd0439bd93c53dafa3a7c3a40d9ebb3e423",
    ),
    Account(
        "0xbecf16bbfd29a01a25d765b7ffeead78315cfd92",
        "75a30fbeb4a5392a6af609c5c375486dbbe175394c2f9ec37ca47ebe33d0c1d7",
    ),
    Account(
        "0x90e8e653d47173ef9c3c192fd3ea43207d7a8a80",
        "17578bc5109253f1c9c4f66197b4ad5c15ad419870010cb107e4810d34c7598b",
    ),
    Account(
        "0xace24046d17841ad2ee826c04e1006d3aa10ada1",
        "2dd50723e8e10f12c89a0058ed82f714701962a8ec123328e03bfabd17f7dda4",
    ),
    Account(
        "0xba1d4bccc3910f5ad79690fc267f5e789f45cf74",
        "a21ca38a86cd0690efb11dccae1940d617043cf2dc8c90f1b60c64ab0740ff6c",
    ),
    Account(
        "0xd5b5552beeaf5d4d7202a4f2833e8b9d0e8e32bf",
        "b8254ea40ba5e704514a0678dee78a14b92b5f1e8bc8f3a73debcb1b0aec19c9",
    ),
    Account(
        "0x0c01203589604f798107d9f0cf1fd4e1b41334ae",
        "ae2db280b4d4a544455b598491eeaee2dc5c155c936f93e8e392d72d1213a1f8",
    ),
    Account(
        "0xf6b1848265ea4559b7d426916eb557ea7b8ce39f",
        "cce0edcb3363d5d65b7a858b55c7b4a0c294405d8222adbd4562b8842c33c8d3",
    ),
]

contractAddress = "0x6d313e4E565dF9d8f8Af62CB5E7F677df6410427"
