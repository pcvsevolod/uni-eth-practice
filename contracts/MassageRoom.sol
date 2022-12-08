pragma solidity ^0.8.13;

contract WorkerManager {
    struct Request {
        string name;
        bool isHere;
    }

    struct Worker {
        string name;
        bool isHere;
    }

    mapping(address => Request) requests;
    mapping(address => Worker) workers;

    function putRequestToRegister(address addr, string memory name) external {
        requests[addr] = Request(name, true);
    }

    function approveRequest(address addr) external {
        requests[addr].isHere = false;
        workers[addr] = Worker(requests[addr].name, true);
    }

    function isRequestHere(address addr) external view returns (bool) {
        return requests[addr].isHere;
    }

    function isWorkerHere(address addr) external view returns (bool) {
        return workers[addr].isHere;
    }
}

contract MassageRoom {
    address deployer;

    WorkerManager workerManager;

    constructor() {
        deployer = msg.sender;

        workerManager = new WorkerManager();
    }

    modifier _canApproveWorkerRegistrationRequests() {
        require(
            msg.sender == deployer,
            "Only deployer can approve worker registration requests"
        );
        _;
    }

    function getTestValue() external pure returns (uint256) {
        return 3;
    }

    function askToRegisterAsWorker(string memory name) external {
        workerManager.putRequestToRegister(msg.sender, name);
    }

    function approveWorkerRegistrationRequest(address workerAddr)
        external
        _canApproveWorkerRegistrationRequests
    {
        workerManager.approveRequest(workerAddr);
    }

    function haveIAskedToBeAWorker() external view returns (bool) {
        return workerManager.isRequestHere(msg.sender);
    }

    function amIAWorker() external view returns (bool) {
        return workerManager.isWorkerHere(msg.sender);
    }
}
