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
