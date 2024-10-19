const sinon = require('sinon');
const sendPaymentRequestToApi = require('./5-payment');
const { expect } = require('chai');

describe('sendPaymentRequestToApi with hooks', () => {
  let consoleSpy;

  beforeEach(() => {
    consoleSpy = sinon.spy(console, 'log');
  });

  afterEach(() => {
    consoleSpy.restore();
  });

  it('logs the correct total for 100 and 20', () => {
    sendPaymentRequestToApi(100, 20);

    // Verify the console output
    expect(consoleSpy.calledOnceWithExactly('The total is: 120')).to.be.true;
    // Verify console.log was called only once
    expect(consoleSpy.calledOnce).to.be.true;
  });

  it('logs the correct total for 10 and 10', () => {
    sendPaymentRequestToApi(10, 10);

    // Verify the console output
    expect(consoleSpy.calledOnceWithExactly('The total is: 20')).to.be.true;
    // Verify console.log was called only once
    expect(consoleSpy.calledOnce).to.be.true;
  });
});
