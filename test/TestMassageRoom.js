const MassageRoom = artifacts.require('MassageRoom');
const truffleAssert = require('truffle-assertions');

contract('MassageRoom', (accounts) => {
  let contract;

  const admin = {
    addr: accounts[0],
  };

  const worker = {
    addr: accounts[1],
    name: 'Worker Zero',
  };

  const client = {
    addr: accounts[3],
    name: 'Client Zero',
  };

  const guest = {
    addr: accounts[9],
    name: 'Guest',
  };

  const services = [
    { name: 'Service Zero', price: 0 },
    { name: 'Service One', price: 1_000 },
    { name: 'Service Two', price: 2_000 },
  ];

  beforeEach('Clearing contract', async () => {
    contract = await MassageRoom.new({ from: admin.addr });
  });

  it('Should get test value', async () => {
    const testValue = await contract.getTestValue.call({ from: accounts[1] });
    assert.equal(testValue, 3, 'Wrong test value');
  });

  describe('Working with workers', () => {
    it('Should register as worker', async () => {
      await contract.askToRegisterAsWorker(worker.name, { from: worker.addr });
      const requestPut = await contract.haveIAskedToBeAWorker.call({ from: worker.addr });
      const amIAWorker = await contract.isAWorker.call(worker.addr, { from: worker.addr });
      assert.equal(requestPut, true, 'Request was not put');
      assert.equal(amIAWorker, false, 'Worker without admin permission');

      await contract.approveWorkerRegistrationRequest(worker.addr, { from: admin.addr });

      const requestPutAfter = await contract.haveIAskedToBeAWorker.call({ from: worker.addr });
      const amIAWorkerAfter = await contract.isAWorker.call(worker.addr, { from: worker.addr });
      assert.equal(amIAWorkerAfter, true, 'Request was not approved');
      assert.equal(requestPutAfter, false, 'Request is still here');
    });

    it('Should change worker status as same worker', async () => {
      await contract.askToRegisterAsWorker(worker.name, { from: worker.addr });
      await contract.approveWorkerRegistrationRequest(worker.addr, { from: admin.addr });

      let available = await contract.isWorkerAvailable.call(worker.addr, { from: worker.addr });
      assert.equal(available, true, 'Worker is not available after registration');

      await contract.setWorkerAsUnavailable(worker.addr, { from: worker.addr });
      available = await contract.isWorkerAvailable.call(worker.addr, { from: worker.addr });
      assert.equal(available, false, 'Worker should change to unavailable');

      await contract.setWorkerAsAvailable(worker.addr, { from: worker.addr });
      available = await contract.isWorkerAvailable.call(worker.addr, { from: worker.addr });
      assert.equal(available, true, 'Worker should change to available');
    });
  });

  describe('Working with clients', () => {
    it('Should register as client', async () => {
      await contract.registerAsClient(client.name, { from: client.addr });
      const amIAClient = await contract.isAClient.call(client.addr, { from: client.addr });
      assert.equal(amIAClient, true, 'Should be client');
    });
  });

  describe('Working with services', () => {
    it('Should create a service as admin', async () => {
      await contract.createService(services[0].name, services[0].price, { from: admin.addr });
      const serviceName = await contract.getServiceName.call(0, { from: client.addr });
      assert.equal(serviceName, services[0].name, 'Wrong service name');
      const servicePrice = await contract.getServicePrice.call(0, { from: client.addr });
      assert.equal(servicePrice, services[0].price, 'Wrong service price');

      const servicesLength = await contract.getServicesLength.call({ from: guest.addr });
      assert.equal(servicesLength, 1, 'Wrong services length');
    });

    it('Should fail to create a service as non admin', async () => {
      const err = 'Only admin can create services';

      await truffleAssert.reverts(
        contract.createService(services[0].name, services[0].price, { from: guest.addr }),
        err,
      );
    });

    it('Should fail to get non-existent service', async () => {
      const err = "Service doesn't exist";

      await truffleAssert.reverts(
        contract.getServiceName.call(0, { from: client.addr }),
        err,
      );
    });

    it('Should change service status as admin', async () => {
      await contract.createService(services[0].name, services[0].price, { from: admin.addr });
      let available = await contract.isServiceAvailable(0, { from: guest.addr });
      assert.equal(available, true, 'Service should be created available');

      await contract.setServiceAsUnavailable(0, { from: admin.addr });
      available = await contract.isServiceAvailable(0, { from: guest.addr });
      assert.equal(available, false, 'Service should be unavailable');

      await contract.setServiceAsAvailable(0, { from: admin.addr });
      available = await contract.isServiceAvailable(0, { from: guest.addr });
      assert.equal(available, true, 'Service should be available');
    });

    it('Should fail to change service status as non admin', async () => {
      await contract.createService(services[0].name, services[0].price, { from: admin.addr });
      const err = 'Only admin can change service status';

      await truffleAssert.reverts(
        contract.setServiceAsUnavailable(0, { from: guest.addr }),
        err,
      );

      await truffleAssert.reverts(
        contract.setServiceAsAvailable(0, { from: guest.addr }),
        err,
      );
    });
  });
});
