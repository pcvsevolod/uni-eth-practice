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

    function getClientName(address addr) external view returns (string memory) {
        return clients[addr].name;
    }

    address testV;

    function putTest(address v) external {
        testV = v;
    }

    function getTest() external view returns (address) {
        return testV;
    }
}
