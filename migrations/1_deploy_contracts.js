const MassageRoom = artifacts.require('MassageRoom');

module.exports = function (deployer, network, accounts) {
  deployer.deploy(MassageRoom, { from: accounts[0] });
};
