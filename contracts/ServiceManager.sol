pragma solidity ^0.8.13;

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
