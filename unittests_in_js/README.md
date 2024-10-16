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

*(We'll expand this section with answers once we've completed all tasks.)*

## Resources
- [Mocha Documentation](https://mochajs.org/)
- [Chai API](https://www.chaijs.com/api/)
- [Sinon](https://sinonjs.org/#get-started)
- [Express - Routing](https://expressjs.com/en/guide/routing.html)
- [Request](https://www.npmjs.com/package/request)
- [Testing NodeJS Apps with Mocha, Chai, and SinonJS](https://www.digitalocean.com/community)

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
   "scripts": {
     "test": "mocha"
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
   });
   ```

6. **Run the Test:**

   To run the test suite, use the following command:

   ```bash
   npm test 0-calcul.test.js
   ```

   **Expected Output:**

   ```bash
   calculateNumber
     ✔ should return 4 when a = 1 and b = 3
     ✔ should return 5 when a = 1 and b = 3.7
     ✔ should return 5 when a = 1.2 and b = 3.7
     ✔ should return 6 when a = 1.5 and b = 3.7

   4 passing (6ms)
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
