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

contract ServiceManager {
    enum ServiceStatus {
        Unknown,
        Available,
        Unavailable
    }

    struct Service {
        string name;
        uint256 price;
        ServiceStatus status;
    }

    Service[] services;

    function createService(string memory name, uint256 price) external {
        services.push(Service(name, price, ServiceStatus.Available));
    }

    function hasService(uint256 i) external view returns (bool) {
        return i < services.length;
    }

    function getServicesLength() external view returns (uint256) {
        return services.length;
    }

    function getServiceName(uint256 i) external view returns (string memory) {
        return services[i].name;
    }

    function getServicePrice(uint256 i) external view returns (uint256) {
        return services[i].price;
    }

    function setServiceAsUnavailable(uint256 i) external {
        services[i].status = ServiceStatus.Unavailable;
    }

    function setServiceAsAvailable(uint256 i) external {
        services[i].status = ServiceStatus.Available;
    }

    function isServiceAvailable(uint256 i) external view returns (bool) {
        return services[i].status == ServiceStatus.Available;
    }
}

contract AppointmentManager {
    enum AppointmentStatus {
        Unknown,
        Unapproved,
        Approved
    }

    struct Appointment {
        uint256 service;
        uint256 time;
        address client;
        address worker;
        AppointmentStatus status;
    }

    Appointment[] appointments;

    function getAppointmentsLength() external view returns (uint256) {
        return appointments.length;
    }

    function hasAppointment(uint256 i) external view returns (bool) {
        return i < appointments.length;
    }

    function isAppointmentApproved(uint256 i) external view returns (bool) {
        return appointments[i].status == AppointmentStatus.Approved;
    }

    function requestAppointment(
        address client,
        uint256 service,
        uint256 time
    ) external {
        appointments.push(
            Appointment(
                service,
                time,
                client,
                address(0),
                AppointmentStatus.Unapproved
            )
        );
    }

    function approveAppointment(uint256 i) external {
        appointments[i].status = AppointmentStatus.Approved;
    }

    function getServiceIndex(uint256 i) external view returns (uint256) {
        return appointments[i].service;
    }

    function getClientAppointments(address client)
        external
        view
        returns (int256[5] memory)
    {
        uint256 iRet = 0;
        uint256 iA = 0;
        uint256 aL = appointments.length;
        uint256 reqI = 5;

        int256[5] memory result;

        for (; iA < aL && iRet < reqI; ++iA) {
            if (appointments[iA].client == client) {
                result[iRet++] = int256(iA);
            }
        }

        for (; iRet < reqI; ++iRet) {
            result[iRet] = -1;
        }

        return result;
    }

    function getAppointmentService(uint256 i) external view returns (uint256) {
        return appointments[i].service;
    }

    function getAppointmentTime(uint256 i) external view returns (uint256) {
        return appointments[i].time;
    }
}

contract MassageRoom {
    address deployer;

    WorkerManager workerManager;
    ClientManager clientManager;
    ServiceManager serviceManager;
    AppointmentManager appointmentManager;

    constructor() {
        deployer = msg.sender;

        workerManager = new WorkerManager();
        clientManager = new ClientManager();
        serviceManager = new ServiceManager();
        appointmentManager = new AppointmentManager();
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

    modifier _hasClient(address targetClient) {
        require(clientManager.isClientHere(targetClient), "Client isn't here");
        _;
    }

    modifier _canCreateServices() {
        require(msg.sender == deployer, "Only admin can create services");
        _;
    }

    modifier _canChangeServiceStatus() {
        require(msg.sender == deployer, "Only admin can change service status");
        _;
    }

    modifier _hasService(uint256 i) {
        require(serviceManager.hasService(i), "Service doesn't exist");
        _;
    }

    modifier _hasUnapprovedAppointment(uint256 i) {
        require(
            appointmentManager.isAppointmentApproved(i) == false,
            "Don't have an unapproved appointment"
        );
        _;
    }

    modifier _hasAppointment(uint256 i) {
        require(
            appointmentManager.hasAppointment(i),
            "Don't have an appointment"
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

    function createService(string memory name, uint256 price)
        external
        _canCreateServices
    {
        serviceManager.createService(name, price);
    }

    function getServicesLength() external view returns (uint256) {
        return serviceManager.getServicesLength();
    }

    function getServiceName(uint256 i)
        external
        view
        _hasService(i)
        returns (string memory)
    {
        return serviceManager.getServiceName(i);
    }

    function getServicePrice(uint256 i)
        external
        view
        _hasService(i)
        returns (uint256)
    {
        return serviceManager.getServicePrice(i);
    }

    function setServiceAsUnavailable(uint256 i)
        external
        _canChangeServiceStatus
        _hasService(i)
    {
        serviceManager.setServiceAsUnavailable(i);
    }

    function setServiceAsAvailable(uint256 i)
        external
        _canChangeServiceStatus
        _hasService(i)
    {
        serviceManager.setServiceAsAvailable(i);
    }

    function isServiceAvailable(uint256 i)
        external
        view
        _hasService(i)
        returns (bool)
    {
        return serviceManager.isServiceAvailable(i);
    }

    function requestAppointment(uint256 serviceI, uint256 time)
        external
        payable
        _hasClient(msg.sender)
        _hasService(serviceI)
    {
        require(
            msg.value == serviceManager.getServicePrice(serviceI),
            "Wrong value for service"
        );

        require(block.timestamp < time, "Wrong time");

        appointmentManager.requestAppointment(msg.sender, serviceI, time);
    }

    function isAppointmentApproved(uint256 i)
        external
        view
        _hasAppointment(i)
        returns (bool)
    {
        return appointmentManager.isAppointmentApproved(i);
    }

    function approveAppointment(uint256 i)
        external
        payable
        _hasWorker(msg.sender)
        _hasAppointment(i)
        _hasUnapprovedAppointment(i)
    {
        require(
            workerManager.isWorkerAvailable(msg.sender),
            "You are unavailable"
        );
        appointmentManager.approveAppointment(i);
        uint256 serviceI = appointmentManager.getServiceIndex(i);
        uint256 servicePrice = serviceManager.getServicePrice(serviceI);
        payable(msg.sender).transfer(servicePrice);
    }

    function getClientAppointments(address client)
        external
        view
        returns (int256[5] memory)
    {
        return appointmentManager.getClientAppointments(client);
    }

    function getAppointmentService(uint256 i)
        external
        view
        _hasAppointment(i)
        returns (uint256)
    {
        return appointmentManager.getAppointmentService(i);
    }

    function getAppointmentTime(uint256 i)
        external
        view
        _hasAppointment(i)
        returns (uint256)
    {
        return appointmentManager.getAppointmentTime(i);
    }
}
