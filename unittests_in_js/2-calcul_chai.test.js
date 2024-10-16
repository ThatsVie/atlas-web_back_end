const { expect } = require('chai');
const calculateNumber = require('./2-calcul_chai');

describe('calculateNumber with Chai', () => {
  it('returns 6 when type is SUM and a = 1.4, b = 4.5', () => {
    expect(calculateNumber('SUM', 1.4, 4.5)).to.equal(6);
  });

  it('returns -4 when type is SUBTRACT and a = 1.4, b = 4.5', () => {
    expect(calculateNumber('SUBTRACT', 1.4, 4.5)).to.equal(-4);
  });

  it('returns 0.2 when type is DIVIDE and a = 1.4, b = 4.5', () => {
    expect(calculateNumber('DIVIDE', 1.4, 4.5)).to.equal(0.2);
  });

  it('returns "Error" when type is DIVIDE and b = 0', () => {
    expect(calculateNumber('DIVIDE', 1.4, 0)).to.equal('Error');
  });
});
