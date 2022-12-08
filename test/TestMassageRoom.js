const MassageRoom = artifacts.require('MassageRoom');

contract('MassageRoom', (accounts) => {
  let contract;

  beforeEach('Clearing contract', async () => {
    contract = await MassageRoom.new({ from: accounts[0] });
  });

  it('Should get test value', async () => {
    const testValue = await contract.getTestValue.call({ from: accounts[1] });
    assert.equal(testValue, 3, 'Wrong test value');
  });
});
