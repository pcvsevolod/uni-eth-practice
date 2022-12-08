pragma solidity ^0.8.13;

contract ClientManager {
    struct Client {
        string name;
        bool isHere;
    }

    mapping(address => Client) clients;

    function registerClient(address addr, string memory name) external {
        clients[addr] = Client(name, true);
    }

    function isClientHere(address addr) external view returns (bool) {
        return clients[addr].isHere;
    }
}
