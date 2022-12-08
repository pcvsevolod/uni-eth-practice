pragma solidity ^0.8.13;

contract WorkerManager {
    struct Request {
        string name;
        bool isHere;
    }

    enum WorkerStatus {
        Unknown,
        Available,
        Unavailable
    }

    struct Worker {
        string name;
        bool isHere;
        WorkerStatus status;
    }

    mapping(address => Request) requests;
    mapping(address => Worker) workers;

    function putRequestToRegister(address addr, string memory name) external {
        requests[addr] = Request(name, true);
    }

    function approveRequest(address addr) external {
        requests[addr].isHere = false;
        workers[addr] = Worker(
            requests[addr].name,
            true,
            WorkerStatus.Available
        );
    }

    function isRequestHere(address addr) external view returns (bool) {
        return requests[addr].isHere;
    }

    function isWorkerHere(address addr) external view returns (bool) {
        return workers[addr].isHere;
    }

    function isWorkerAvailable(address addr) external view returns (bool) {
        return
            workers[addr].isHere &&
            workers[addr].status == WorkerStatus.Available;
    }

    function setWorkerAsUnavailable(address addr) external {
        workers[addr].status = WorkerStatus.Unavailable;
    }

    function setWorkerAsAvailable(address addr) external {
        workers[addr].status = WorkerStatus.Available;
    }
}

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

contract MassageRoom {
    address deployer;

    WorkerManager workerManager;
    ClientManager clientManager;

    constructor() {
        deployer = msg.sender;

        workerManager = new WorkerManager();
        clientManager = new ClientManager();
    }

    modifier _canApproveWorkerRegistrationRequests() {
        require(
            msg.sender == deployer,
            "Only deployer can approve worker registration requests"
        );
        _;
    }

    modifier _canChangeWorkerStatus(address targetWorker) {
        require(
            msg.sender == deployer || msg.sender == targetWorker,
            "Only deployer can approve worker registration requests"
        );
        _;
    }

    modifier _hasWorker(address targetWorker) {
        require(workerManager.isWorkerHere(targetWorker), "Worker isn't here");
        _;
    }

    modifier _hasWorkerRequest(address targetWorker) {
        require(
            workerManager.isRequestHere(targetWorker),
            "Request isn't here"
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

    function isAWorker(address addr) external view returns (bool) {
        return workerManager.isWorkerHere(addr);
    }

    function isWorkerAvailable(address workerAddr)
        external
        view
        returns (bool)
    {
        return workerManager.isWorkerAvailable(workerAddr);
    }

    function setWorkerAsUnavailable(address workerAddr)
        external
        _canChangeWorkerStatus(workerAddr)
        _hasWorker(workerAddr)
    {
        workerManager.setWorkerAsUnavailable(workerAddr);
    }

    function setWorkerAsAvailable(address workerAddr)
        external
        _canChangeWorkerStatus(workerAddr)
        _hasWorker(workerAddr)
    {
        workerManager.setWorkerAsAvailable(workerAddr);
    }

    function registerAsClient(string memory name) external {
        clientManager.registerClient(msg.sender, name);
    }

    function isAClient(address addr) external view returns (bool) {
        return clientManager.isClientHere(addr);
    }
}
