# Unittests in JS

## Project Overview
This project focuses on writing and running unit tests for JavaScript applications using Mocha, Chai, and Sinon. You'll learn how to create test suites, use assertion libraries, and implement spies, stubs, and hooks. By the end of this project, you'll be able to confidently test Node.js apps with both synchronous and asynchronous code.

## Learning Objectives
At the end of this project, you will be able to:
- Use Mocha to write a test suite.
- Implement different assertion libraries (Node or Chai).
- Present long test suites.
- Understand and apply spies and stubs.
- Use hooks effectively.
- Write unit tests for asynchronous functions.
- Write integration tests with a small Node server.


## Resources
- [Mocha Documentation](https://mochajs.org/)
- [Chai API](https://www.chaijs.com/api/)
- [Sinon](https://sinonjs.org/#get-started)
- [Express - Routing](https://expressjs.com/en/guide/routing.html)
- [Request](https://www.npmjs.com/package/request)
- [Testing NodeJS Apps with Mocha, Chai, and SinonJS](https://stackoverflow.com/questions/43878090/how-to-test-nodejs-fs-using-mocha-chai-sinon)

## Requirements
- **Node Version:** Node 20.x.x
- **Operating System:** Ubuntu 20.04
- **Editors:** vi, vim, emacs, Visual Studio Code
- **Mandatory Files:** All code files must end with a new line, use the `.js` extension, and pass all tests without warnings or errors when running `npm run test *.test.js`.


## Tasks and Usage


### Task 0: Basic Test with Mocha and Node Assertion Library

This task involves creating a function that rounds two numbers and returns their sum, then writing test cases using Mocha and the Node.js `assert` library.

<details>
  <summary><strong>Curriculum Instruction</strong></summary>

- Install Mocha using npm.
- Set up a script in your `package.json` to quickly run Mocha using `npm test`.
- You have to use `assert`.
- Create a new file named `0-calcul.js`:
  - Create a function named `calculateNumber` that accepts two arguments (numbers `a` and `b`).
  - The function should round `a` and `b` and return the sum.
- Create a file `0-calcul.test.js` that contains test cases for this function.
  - You can assume `a` and `b` are always numbers.
  - Tests should verify behavior around the “rounded” part.
- You should be able to run the test suite using `npm test 0-calcul.test.js`.
- Every test should pass without any warnings.

</details>

<details>
  <summary><strong>Steps and Code Implementation</strong></summary>

1. **Create `package.json`:**

   Before installing Mocha, initialize the `package.json` file:

   ```bash
   npm init -y
   ```

   This command sets up the `package.json` file, allowing you to install Mocha successfully.

2. **Install Mocha:**

   Once `package.json` is set up, install Mocha as a development dependency:

   ```bash
   npm install mocha --save-dev
   ```

3. **Update `package.json` to Include a Test Script:**

   Add the test script to your `package.json` file:

   ```json
   {
     "scripts": {
       "test": "mocha"
     }
   }
   ```

4. **Create `0-calcul.js`:**
   
   Write the function `calculateNumber` that rounds two numbers and returns their sum:

   ```javascript
   function calculateNumber(a, b) {
     return Math.round(a) + Math.round(b);
   }

   module.exports = calculateNumber;
   ```

5. **Create `0-calcul.test.js`:**

   Write the test cases for the `calculateNumber` function using the Node.js `assert` module:

   ```javascript
   const assert = require('assert');
   const calculateNumber = require('./0-calcul');

   describe('calculateNumber', () => {
     it('should return 4 when a = 1 and b = 3', () => {
       assert.strictEqual(calculateNumber(1, 3), 4);
     });

     it('should return 5 when a = 1 and b = 3.7', () => {
       assert.strictEqual(calculateNumber(1, 3.7), 5);
     });

     it('should return 5 when a = 1.2 and b = 3.7', () => {
       assert.strictEqual(calculateNumber(1.2, 3.7), 5);
     });

     it('should return 6 when a = 1.5 and b = 3.7', () => {
       assert.strictEqual(calculateNumber(1.5, 3.7), 6);
     });

     it('should round only the second number when necessary', () => {
       assert.strictEqual(calculateNumber(2, 3.2), 5); // b = 3.2 rounds to 3, 2 + 3 = 5
     });
   });
   ```

6. **Run the Test:**

   To run the test suite, use the following command:

   ```bash
   npm test 0-calcul.test.js
   ```

   **Expected Output:**

   ```bash
    unittests_in_js@1.0.0 test
    mocha 0-calcul.test.js

    calculateNumber
      ✔ return 4 when a = 1 and b = 3
      ✔ return 5 when a = 1 and b = 3.7
      ✔ return 5 when a = 1.2 and b = 3.7
      ✔ return 6 when a = 1.5 and b = 3.7
      ✔ round only the second number when necessary

    5 passing (3ms)
   ```

</details>

<details>
  <summary><strong>Explanation: Who, What, Where, When, Why, How</strong></summary>

- **What:** This task involves creating a function called `calculateNumber` that rounds two input numbers and returns their sum. We also wrote unit tests using Mocha and Node's `assert` library.
- **Where:** The function is defined in `0-calcul.js`, and the test cases are in `0-calcul.test.js`.
- **Why:** This task demonstrates how to write simple functions, use rounding, and test them using Mocha and `assert`.
- **How:** The numbers are rounded using `Math.round()`, and their sum is returned. The test cases use `assert.strictEqual()` to check if the results are correct.
- **Who:** This task is important for developers learning how to set up and run tests in Node.js using Mocha and assertion libraries.
- **When:** The tests are run every time the test command (`npm test 0-calcul.test.js`) is executed, ensuring that the function behaves correctly in various cases.

</details>

<details>
  <summary><strong>Troubleshooting</strong></summary>

- **Issue:** Tests were passing, but the checker indicated that the test suite was missing a specific test case for rounding only the second number.
  
  - **Solution:** Added a test case to check that when only the second number (`b`) is rounded, the function still behaves as expected. This test case specifically rounds the second number and verifies the result:

    ```javascript
    it('should round only the second number when necessary', () => {
      assert.strictEqual(calculateNumber(2, 3.2), 5); // b = 3.2 rounds to 3, 2 + 3 = 5
    });
    ```

</details>

### Task 1: Combining Descriptions

This task involves upgrading the `calculateNumber` function from Task 0 by adding a `type` argument, which specifies whether the operation is `SUM`, `SUBTRACT`, or `DIVIDE`.

<details>
  <summary><strong>Curriculum Instruction</strong></summary>

- Create a new file named `1-calcul.js` and modify the previous function:
  - Add a new argument `type` which can be `SUM`, `SUBTRACT`, or `DIVIDE`.
  - For `SUM`, round the two numbers and add them.
  - For `SUBTRACT`, round the two numbers and subtract the second from the first.
  - For `DIVIDE`, round the two numbers and divide the first by the second. If the second number is `0` (after rounding), return the string `"Error"`.
  
- Create a file `1-calcul.test.js` with test cases that verify each operation, including edge cases.

- You should be able to run the test suite using `npm test 1-calcul.test.js`, and all tests should pass without any warnings or errors.

</details>

<details>
  <summary><strong>Steps and Code Implementation</strong></summary>

1. **Create `1-calcul.js`:**

   Modify the `calculateNumber` function to handle `SUM`, `SUBTRACT`, and `DIVIDE`:

   ```javascript
   function calculateNumber(type, a, b) {
     const roundedA = Math.round(a);
     const roundedB = Math.round(b);

     if (type === 'SUM') {
       return roundedA + roundedB;
     } else if (type === 'SUBTRACT') {
       return roundedA - roundedB;
     } else if (type === 'DIVIDE') {
       if (roundedB === 0) {
         return 'Error';
       }
       return roundedA / roundedB;
     }
   }

   module.exports = calculateNumber;
   ```

2. **Create `1-calcul.test.js`:**

   Write test cases to verify the behavior of `calculateNumber` for `SUM`, `SUBTRACT`, `DIVIDE`, and edge cases like division by zero:

   ```javascript
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
   ```

3. **Run the Test:**

   Run the test suite using the following command:

   ```bash
   npm test 1-calcul.test.js
   ```

   **Expected Output:**

   ```bash
   calculateNumber
     ✔ return 6 when type is SUM and a = 1.4, b = 4.5
     ✔ return -4 when type is SUBTRACT and a = 1.4, b = 4.5
     ✔ return 0.2 when type is DIVIDE and a = 1.4, b = 4.5
     ✔ return "Error" when type is DIVIDE and b = 0

   4 passing (3ms)
   ```

</details>

<details>
  <summary><strong>Explanation: Who, What, Where, When, Why, How</strong></summary>

- **What:** This task enhances the `calculateNumber` function to perform different operations (`SUM`, `SUBTRACT`, or `DIVIDE`) based on the `type` argument. We also wrote test cases to ensure each operation behaves as expected.
- **Where:** The function is written in `1-calcul.js`, and the test cases are in `1-calcul.test.js`.
- **Why:** This task demonstrates how to extend the functionality of an existing function and test for different behaviors and edge cases.
- **How:** The numbers are rounded using `Math.round()`, and then the appropriate operation is performed based on the `type` argument. The test cases use `assert.strictEqual()` to verify the correct outputs.
- **Who:** This task is relevant for anyone learning how to write and test more complex JavaScript functions.
- **When:** The tests can be run at any time using the command `npm test 1-calcul.test.js`.

</details>

### Task 2: Basic Test Using Chai Assertion Library

This task involves copying the `calculateNumber` function from Task 1 and rewriting the test suite using Chai’s `expect` assertion style, which is more behavior-driven and easier to read.

<details>
  <summary><strong>Curriculum Instruction</strong></summary>

- Copy the file `1-calcul.js` into a new file named `2-calcul_chai.js`.
- Copy the file `1-calcul.test.js` into a new file named `2-calcul_chai.test.js`.
- Rewrite the test suite using Chai’s `expect` style to improve readability.
- The tests should behave exactly as they did in Task 1 but with the Chai assertion library.
- Run the test suite using `npm test 2-calcul_chai.test.js`, and ensure all tests pass without any warnings.

</details>

<details>
  <summary><strong>Steps and Code Implementation</strong></summary>

1. **Copy and Modify the Files:**

   - Copy `1-calcul.js` to `2-calcul_chai.js` and `1-calcul.test.js` to `2-calcul_chai.test.js`.
   - Modify `2-calcul_chai.test.js` to use Chai’s `expect` style.

2. **Install Chai:**

   First, install Chai using npm:

   ```bash
   npm install chai --save-dev
   ```

3. **Update `2-calcul_chai.js`:**

   No changes are required for the `calculateNumber` function, but here's a reminder of how it looks:

   ```javascript
   function calculateNumber(type, a, b) {
     const roundedA = Math.round(a);
     const roundedB = Math.round(b);

     if (type === 'SUM') {
       return roundedA + roundedB;
     } else if (type === 'SUBTRACT') {
       return roundedA - roundedB;
     } else if (type === 'DIVIDE') {
       if (roundedB === 0) {
         return 'Error';
       }
       return roundedA / roundedB;
     }
   }

   module.exports = calculateNumber;
   ```

4. **Rewrite `2-calcul_chai.test.js`:**

   The test file now uses Chai’s `expect` for assertions:

   ```javascript
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
   ```

5. **Run the Test:**

   To run the test suite, use:

   ```bash
   npm test 2-calcul_chai.test.js
   ```

   **Expected Output:**

   ```bash
   calculateNumber with Chai
     ✔ returns 6 when type is SUM and a = 1.4, b = 4.5
     ✔ returns -4 when type is SUBTRACT and a = 1.4, b = 4.5
     ✔ returns 0.2 when type is DIVIDE and a = 1.4, b = 4.5
     ✔ returns "Error" when type is DIVIDE and b = 0

   4 passing (6ms)
   ```

</details>

<details>
  <summary><strong>Explanation: Who, What, Where, When, Why, How</strong></summary>

- **What:** This task involves writing unit tests using the Chai assertion library for behavior-driven development.
- **Where:** The function `calculateNumber` is copied into `2-calcul_chai.js`, and the tests are rewritten using Chai’s `expect` style in `2-calcul_chai.test.js`.
- **Why:** Chai’s syntax offers better readability and ease of understanding, which improves maintainability of the test suite.
- **How:** The `expect` method from Chai is used to perform assertions. The test suite covers `SUM`, `SUBTRACT`, `DIVIDE`, and handles edge cases like division by zero.
- **Who:** This task is useful for developers who want to write more maintainable and readable tests.
- **When:** Run the tests using `npm test 2-calcul_chai.test.js`.

</details>

<details>
  <summary><strong>Troubleshooting</strong></summary>

- **Issue:** After installing the latest version of Chai, we encountered the error: `Error [ERR_REQUIRE_ESM]: require() of ES Module chai.js`.
  
  - **Solution:** This error occurred because newer versions of Chai use ES Modules (ESM), and our project was using CommonJS. To fix this, we downgraded Chai to version `4.3.6`, which still supports CommonJS.

    To install the correct version:
    
    ```bash
    npm install chai@4.3.6 --save-dev
    ```

- **Additional Note:** Ensure that your test files use `require()` for both `chai` and `calculateNumber`. This allows you to continue using CommonJS without switching to ESM.

</details>
