pragma solidity ^0.8.13;

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
