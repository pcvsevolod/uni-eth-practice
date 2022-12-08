const MassageRoom = artifacts.require('MassageRoom');

contract('MassageRoom', (accounts) => {
  let contract;

  const admin = {
    addr: accounts[0],
  };

  const worker = {
    addr: accounts[1],
    name: 'Worker Zero',
  };

  const guest = {
    addr: accounts[9],
    name: 'Guest',
  };

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
      const amIAWorker = await contract.amIAWorker.call({ from: worker.addr });
      assert.equal(requestPut, true, 'Request was not put');
      assert.equal(amIAWorker, false, 'Worker without admin permission');

      await contract.approveWorkerRegistrationRequest(worker.addr, { from: admin.addr });

      const requestPutAfter = await contract.haveIAskedToBeAWorker.call({ from: worker.addr });
      const amIAWorkerAfter = await contract.amIAWorker.call({ from: worker.addr });
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
});
