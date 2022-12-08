const WorkerManager = artifacts.require('WorkerManager');
const ClientManager = artifacts.require('ClientManager');
const ServiceManager = artifacts.require('ServiceManager');
const AppointmentManager = artifacts.require('AppointmentManager');
const MassageRoom = artifacts.require('MassageRoom');

module.exports = function (deployer, network, accounts) {
  deployer.deploy(WorkerManager, { from: accounts[0] });
  deployer.link(WorkerManager, MassageRoom);
  deployer.deploy(ClientManager, { from: accounts[0] });
  deployer.link(ClientManager, MassageRoom);
  deployer.deploy(ServiceManager, { from: accounts[0] });
  deployer.link(ServiceManager, MassageRoom);
  deployer.deploy(AppointmentManager, { from: accounts[0] });
  deployer.link(AppointmentManager, MassageRoom);
  deployer.deploy(MassageRoom, { from: accounts[0] });
};
