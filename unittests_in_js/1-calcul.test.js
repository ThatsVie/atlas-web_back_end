const assert = require('assert');
const calculateNumber = require('./1-calcul');

describe('calculateNumber', () => {
  it('return 6 when type is SUM and a = 1.4, b = 4.5', () => {
    assert.strictEqual(calculateNumber('SUM', 1.4, 4.5), 6);
  });

  it('return -4 when type is SUBTRACT and a = 1.4, b = 4.5', () => {
    assert.strictEqual(calculateNumber('SUBTRACT', 1.4, 4.5), -4);
  });

  it('return 0.2 when type is DIVIDE and a = 1.4, b = 4.5', () => {
    assert.strictEqual(calculateNumber('DIVIDE', 1.4, 4.5), 0.2);
  });

  it('return "Error" when type is DIVIDE and b = 0', () => {
    assert.strictEqual(calculateNumber('DIVIDE', 1.4, 0), 'Error');
  });
});
