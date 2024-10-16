const assert = require('assert');
const calculateNumber = require('./0-calcul');

describe('calculateNumber', () => {
  it('return 4 when a = 1 and b = 3', () => {
    assert.strictEqual(calculateNumber(1, 3), 4);
  });

  it('return 5 when a = 1 and b = 3.7', () => {
    assert.strictEqual(calculateNumber(1, 3.7), 5);
  });

  it('return 5 when a = 1.2 and b = 3.7', () => {
    assert.strictEqual(calculateNumber(1.2, 3.7), 5);
  });

  it('return 6 when a = 1.5 and b = 3.7', () => {
    assert.strictEqual(calculateNumber(1.5, 3.7), 6);
  });

  it('round only the second number when necessary', () => {
    assert.strictEqual(calculateNumber(2, 3.2), 5); // b = 3.2 rounds to 3, 2 + 3 = 5
  });
});
