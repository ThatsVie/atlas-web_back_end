<p align="center">
  <img src="https://github.com/user-attachments/assets/569d07df-06c9-4ca2-afa0-4896363330a7" alt="pugsclassroom"/>
</p>

<div align="center">

# Unittests in JS

This project focuses on unit and integration testing in Node.js using Mocha, Chai, and Sinon. It covers testing various endpoints of an Express API, including GET and POST requests, while validating response status codes, messages, and deep equality of objects. The project also introduces testing techniques like spies, stubs, and hooks to ensure reliable and efficient test coverage for server functionality.

</div>


## Learning Objectives
<details>
  <summary><strong>How to use Mocha to write a test suite</strong></summary>
  
  Mocha is used to write test suites in **Task 0 (Basic Test with Mocha)** and in every subsequent task. We set up `mocha` in our `package.json` and use `describe()` to group related tests and `it()` to write individual test cases.

  Example from Task 0:
  ```javascript
  describe('calculateNumber', () => {
    it('returns 4 when a = 1 and b = 3', () => {
      assert.strictEqual(calculateNumber(1, 3), 4);
    });
  });
  ```
</details>

<details>
  <summary><strong>How to use different assertion libraries (Node or Chai)</strong></summary>
  
  In **Task 0**, we use the Node `assert` library to test functions. From **Task 2 onward**, we begin using the Chai assertion library, which provides a more expressive syntax using `expect()` and `should()`.
  
  Example from Task 2:
  ```javascript
  const { expect } = require('chai');
  expect(calculateNumber('SUM', 1.4, 4.5)).to.equal(6);
  ```
</details>

<details>
  <summary><strong>How to present long test suites</strong></summary>
  
  Mocha's `describe()` and `it()` allow us to structure tests clearly, even for long test suites. Grouping tests in **Task 0** through **Task 10** ensures that the suite remains easy to read and maintain. 
  In **Task 9 (Regex Integration Testing)**, we see longer suites with multiple endpoints and different sets of tests for each.

  Example of grouping:
  ```javascript
  describe('Index page', () => {
    it('should return status code 200', (done) => {
      request('http://localhost:7865/', (error, response) => {
        expect(response.statusCode).to.equal(200);
        done();
      });
    });
  });
  ```
</details>

<details>
  <summary><strong>When and how to use spies</strong></summary>
  
  Spies are introduced in **Task 3 (Spies)**. We use Sinon to create a spy to wrap the `calculateNumber` function. Spies allow us to check if a function was called, with what arguments, and how many times.

  Example from Task 3:
  ```javascript
  const spy = sinon.spy(Utils, 'calculateNumber');
  expect(spy.calledOnceWithExactly('SUM', 100, 20)).to.be.true;
  ```
</details>

<details>
  <summary><strong>When and how to use stubs</strong></summary>
  
  Stubs are introduced in **Task 4 (Stubs)**. A stub replaces a function and allows us to control its behavior (e.g., making it return a specific value). This is useful for testing functions that depend on external data or expensive operations.

  Example from Task 4:
  ```javascript
  const stub = sinon.stub(Utils, 'calculateNumber').returns(10);
  expect(stub.calledOnceWithExactly('SUM', 100, 20)).to.be.true;
  ```
</details>

<details>
  <summary><strong>What are hooks and when to use them</strong></summary>
  
  Hooks, such as `beforeEach()` and `afterEach()`, are introduced in **Task 5 (Hooks)**. Hooks allow us to set up conditions before running tests or clean up after each test.

  Example from Task 5:
  ```javascript
  beforeEach(() => {
    spy = sinon.spy(console, 'log');
  });

  afterEach(() => {
    spy.restore();
  });
  ```
</details>

<details>
  <summary><strong>Unit testing with Async functions</strong></summary>
  
  **Task 6 (Async Tests with Done)** covers unit testing with asynchronous functions. We learn to use Mocha’s `done()` callback to test functions that return promises or perform async operations.

  Example from Task 6:
  ```javascript
  it('returns a resolved promise with correct data', (done) => {
    getPaymentTokenFromAPI(true).then((response) => {
      expect(response.data).to.equal('Successful response from the API');
      done();
    });
  });
  ```
</details>

<details>
  <summary><strong>How to write integration tests with a small node server</strong></summary>
  
  **Task 8 (Basic Integration Testing)** and **Task 9 (Regex Integration Testing)** focus on writing integration tests for a small Node.js server using Express. We test server responses, status codes, and routes using `request()` and `expect()` for deep equality checks.

  Example from Task 9:
  ```javascript
  it('should return 200 and correct message when :id is a number', (done) => {
    request('http://localhost:7865/cart/12', (error, response, body) => {
      expect(response.statusCode).to.equal(200);
      expect(body).to.equal('Payment methods for cart 12');
      done();
    });
  });
  ```
</details>



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

### Task 3: Spies with Sinon

This task involves using Sinon to create a spy for testing whether the `Utils.calculateNumber` function is called correctly when `sendPaymentRequestToApi` is invoked.

<details>
  <summary><strong>Curriculum Instruction</strong></summary>

- Install Sinon using npm to create spies.
- Create a new module `Utils` in `utils.js` that contains the `calculateNumber` function from the previous tasks.
- Create a new function `sendPaymentRequestToApi` in `3-payment.js` that calls `Utils.calculateNumber` with the type `SUM` and logs the result.
- Write tests for `sendPaymentRequestToApi` in `3-payment.test.js` using Sinon to spy on `Utils.calculateNumber`, ensuring it’s called with the correct arguments.
- Remember to restore the spy after each test to avoid unexpected behavior in future tests.

</details>

<details>
  <summary><strong>Steps and Code Implementation</strong></summary>

1. **Install Sinon:**

   First, install Sinon using npm:

   ```bash
   npm install sinon --save-dev
   ```

2. **Create `utils.js`:**

   Define the `Utils` module with the `calculateNumber` function:

   ```javascript
   const Utils = {
     calculateNumber: function (type, a, b) {
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
   };

   module.exports = Utils;
   ```

3. **Create `3-payment.js`:**

   Write the `sendPaymentRequestToApi` function that calls `Utils.calculateNumber`:

   ```javascript
   const Utils = require('./utils');

   function sendPaymentRequestToApi(totalAmount, totalShipping) {
     const total = Utils.calculateNumber('SUM', totalAmount, totalShipping);
     console.log(`The total is: ${total}`);
   }

   module.exports = sendPaymentRequestToApi;
   ```

4. **Create `3-payment.test.js`:**

   Write the test for `sendPaymentRequestToApi` using Sinon to spy on `Utils.calculateNumber`:

   ```javascript
   const sinon = require('sinon');
   const Utils = require('./utils');
   const sendPaymentRequestToApi = require('./3-payment');
   const { expect } = require('chai');

   describe('sendPaymentRequestToApi', () => {
     let spy;

     beforeEach(() => {
       spy = sinon.spy(Utils, 'calculateNumber');
     });

     afterEach(() => {
       spy.restore(); // Always restore the spy after the test
     });

     it('validates that Utils.calculateNumber was called with the correct arguments', () => {
       sendPaymentRequestToApi(100, 20);

       expect(spy.calledOnceWithExactly('SUM', 100, 20)).to.be.true;
     });
   });
   ```

5. **Run the Test:**

   To run the test suite, use:

   ```bash
   npm test 3-payment.test.js
   ```

   **Expected Output:**

   ```bash
   sendPaymentRequestToApi
     ✔ validates that Utils.calculateNumber was called with the correct arguments

   1 passing (5ms)
   ```

</details>

<details>
  <summary><strong>Explanation: Who, What, Where, When, Why, How</strong></summary>

- **What:** This task introduces Sinon spies, which help verify whether certain functions are called and with what arguments. We use a spy to track calls to `Utils.calculateNumber`.
- **Where:** The function `sendPaymentRequestToApi` is defined in `3-payment.js` and calls `Utils.calculateNumber` from `utils.js`. The tests are written in `3-payment.test.js`.
- **Why:** Spies are useful in testing to validate function interactions without directly testing the function itself.
- **How:** Sinon’s `spy` method is used to monitor calls to `Utils.calculateNumber`. After the function is called, we assert that the spy was called with the correct arguments.
- **Who:** This task is for developers who want to learn how to implement and use spies in their testing process.
- **When:** This test should run whenever `npm test 3-payment.test.js` is executed.

</details>

### Task 4: Stubs with Sinon

This task involves using Sinon stubs to replace the behavior of `Utils.calculateNumber` in order to control the return value for testing purposes. A spy is also used to verify that `console.log` outputs the correct message.

<details>
  <summary><strong>Curriculum Instruction</strong></summary>

- Copy the file `3-payment.js` to `4-payment.js` (same content and behavior).
- Copy the test suite from `3-payment.test.js` to `4-payment.test.js`.
- Stub the function `Utils.calculateNumber` to always return the number `10`.
- Verify that the stub is called with the correct arguments (`type = SUM`, `a = 100`, `b = 20`).
- Use a spy to verify that `console.log` logs the correct message: `The total is: 10`.
- Ensure all tests pass and restore the spy and stub after each test to avoid unintended side effects.

</details>

<details>
  <summary><strong>Steps and Code Implementation</strong></summary>

1. **Copy `4-payment.js`:**

   Copy the contents of `3-payment.js` to `4-payment.js`. No changes are required for the logic:

   ```javascript
   const Utils = require('./utils');

   function sendPaymentRequestToApi(totalAmount, totalShipping) {
     const total = Utils.calculateNumber('SUM', totalAmount, totalShipping);
     console.log(`The total is: ${total}`);
   }

   module.exports = sendPaymentRequestToApi;
   ```

2. **Write `4-payment.test.js`:**

   In `4-payment.test.js`, we replace the actual implementation of `Utils.calculateNumber` with a stub that always returns `10`. We also add a spy on `console.log` to verify the correct output.

   ```javascript
   const sinon = require('sinon');
   const Utils = require('./utils');
   const sendPaymentRequestToApi = require('./4-payment');
   const { expect } = require('chai');

   describe('sendPaymentRequestToApi with stubs', () => {
     let calculateNumberStub;
     let consoleSpy;

     beforeEach(() => {
       // Stub the Utils.calculateNumber method to return 10
       calculateNumberStub = sinon.stub(Utils, 'calculateNumber').returns(10);
       // Spy on console.log
       consoleSpy = sinon.spy(console, 'log');
     });

     afterEach(() => {
       // Restore the original methods
       calculateNumberStub.restore();
       consoleSpy.restore();
     });

     it('validates that Utils.calculateNumber was called with the correct arguments and console.log logs the correct message', () => {
       sendPaymentRequestToApi(100, 20);

       // Verify that the stub was called with the correct arguments
       expect(calculateNumberStub.calledOnceWithExactly('SUM', 100, 20)).to.be.true;

       // Verify that console.log was called with the correct message
       expect(consoleSpy.calledOnceWithExactly('The total is: 10')).to.be.true;
     });
   });
   ```

3. **Run the Test:**

   To run the test suite, use:

   ```bash
   npm test 4-payment.test.js
   ```

   **Expected Output:**

   ```bash
   sendPaymentRequestToApi with stubs
     ✔ validates that Utils.calculateNumber was called with the correct arguments and console.log logs the correct message

   1 passing (6ms)
   ```

</details>

<details>
  <summary><strong>Explanation: Who, What, Where, When, Why, How</strong></summary>

- **What:** This task involves using Sinon stubs to replace the behavior of a function for testing purposes, ensuring that the function returns a specific result without executing the actual implementation.
- **Where:** The function `sendPaymentRequestToApi` is located in `4-payment.js`, and the tests are in `4-payment.test.js`.
- **Why:** Stubbing is useful when testing code that depends on functions with side effects (e.g., API calls, expensive calculations) to control the results and focus only on the behavior of the code under test.
- **How:** We use `sinon.stub()` to make `Utils.calculateNumber` always return `10` and `sinon.spy()` to ensure `console.log` logs the correct message. After each test, we restore the stub and spy to avoid affecting other tests.
- **Who:** This task is for developers learning how to use stubs in unit testing to improve test speed and control function behavior.
- **When:** Run the tests using `npm test 4-payment.test.js`.

</details>

### Task 5: Hooks with Mocha

This task involves using Mocha hooks (`beforeEach` and `afterEach`) to set up a spy for `console.log`, ensuring that the spy is initialized before each test and restored afterward. The tests validate that `sendPaymentRequestToApi` logs the correct total and that the console is only called once per test.

<details>
  <summary><strong>Curriculum Instruction</strong></summary>

- Copy the contents of `4-payment.js` into a new file `5-payment.js` (same content and behavior).
- In `5-payment.test.js`, use `beforeEach` and `afterEach` hooks to set up a spy on `console.log`.
- Create two tests:
  1. Call `sendPaymentRequestToApi(100, 20)` and verify that the console logs `The total is: 120` and that it’s only called once.
  2. Call `sendPaymentRequestToApi(10, 10)` and verify that the console logs `The total is: 20` and that it’s only called once.
- Ensure all tests pass and that the spy is correctly restored after each test.

</details>

<details>
  <summary><strong>Steps and Code Implementation</strong></summary>

1. **Copy `5-payment.js`:**

   Copy the contents of `4-payment.js` to `5-payment.js`:

   ```javascript
   const Utils = require('./utils');

   function sendPaymentRequestToApi(totalAmount, totalShipping) {
     const total = Utils.calculateNumber('SUM', totalAmount, totalShipping);
     console.log(`The total is: ${total}`);
   }

   module.exports = sendPaymentRequestToApi;
   ```

2. **Write `5-payment.test.js`:**

   In this test file, Mocha’s hooks are used to set up a spy on `console.log` and verify that it logs the correct totals for each test case.

   ```javascript
   const sinon = require('sinon');
   const sendPaymentRequestToApi = require('./5-payment');
   const { expect } = require('chai');

   describe('sendPaymentRequestToApi with hooks', () => {
     let consoleSpy;

     beforeEach(() => {
       // Set up a spy on console.log before each test
       consoleSpy = sinon.spy(console, 'log');
     });

     afterEach(() => {
       // Restore the spy after each test
       consoleSpy.restore();
     });

     it('logs the correct total for 100 and 20', () => {
       sendPaymentRequestToApi(100, 20);

       // Check that the correct message was logged
       expect(consoleSpy.calledOnceWithExactly('The total is: 120')).to.be.true;
       // Ensure console.log was only called once
       expect(consoleSpy.calledOnce).to.be.true;
     });

     it('logs the correct total for 10 and 10', () => {
       sendPaymentRequestToApi(10, 10);

       // Check that the correct message was logged
       expect(consoleSpy.calledOnceWithExactly('The total is: 20')).to.be.true;
       // Ensure console.log was only called once
       expect(consoleSpy.calledOnce).to.be.true;
     });
   });
   ```

3. **Run the Test:**

   To run the test suite, use:

   ```bash
   npm test 5-payment.test.js
   ```

   **Expected Output:**

   ```bash
   sendPaymentRequestToApi with hooks
     ✔ logs the correct total for 100 and 20
     ✔ logs the correct total for 10 and 10

   2 passing (7ms)
   ```

</details>

<details>
  <summary><strong>Explanation: Who, What, Where, When, Why, How</strong></summary>

- **What:** This task focuses on using Mocha’s hooks (`beforeEach` and `afterEach`) to set up and restore spies, ensuring that each test starts with a fresh spy instance.
- **Where:** The `sendPaymentRequestToApi` function is in `5-payment.js`, and the test suite is in `5-payment.test.js`.
- **Why:** Hooks allow us to initialize spies before each test and restore them afterward, preventing side effects across tests.
- **How:** Mocha’s `beforeEach` hook sets up a spy on `console.log`, and the `afterEach` hook restores it after each test. This ensures that we can accurately test the console output without interference from previous tests.
- **Who:** This task is for developers learning how to use Mocha hooks to manage test setup and teardown for repetitive tasks like spying, stubbing, or setting up a database.
- **When:** The test suite runs using `npm test 5-payment.test.js` to verify the behavior.

</details>

### Task 6: Async Tests with `done`

This task involves testing an asynchronous function `getPaymentTokenFromAPI` that returns a promise. We use Mocha’s `done` callback to handle the asynchronous nature of the test.

<details>
  <summary><strong>Curriculum Instruction</strong></summary>

- Create the `getPaymentTokenFromAPI` function in `6-payment_token.js` that accepts a `success` argument (boolean).
- If `success` is `true`, return a resolved promise with the object `{ data: 'Successful response from the API' }`.
- Write tests in `6-payment_token.test.js` using Mocha’s `done` callback to verify the promise resolves correctly.
- Ensure all tests pass and handle async properly using `done`.

</details>

<details>
  <summary><strong>Steps and Code Implementation</strong></summary>

1. **Create `6-payment_token.js`:**

   Define the `getPaymentTokenFromAPI` function that returns a resolved promise when `success` is true:

   ```javascript
   function getPaymentTokenFromAPI(success) {
     if (success) {
       return Promise.resolve({ data: 'Successful response from the API' });
     }
   }

   module.exports = getPaymentTokenFromAPI;
   ```

2. **Write `6-payment_token.test.js`:**

   In the test file, we test the resolved value of `getPaymentTokenFromAPI(true)` using the `done` callback to ensure the test waits for the promise to resolve.

   ```javascript
   const getPaymentTokenFromAPI = require('./6-payment_token');
   const { expect } = require('chai');

   describe('getPaymentTokenFromAPI', () => {
     it('returns a resolved promise with correct data when success is true', (done) => {
       getPaymentTokenFromAPI(true)
         .then((response) => {
           expect(response).to.have.property('data', 'Successful response from the API');
           done(); // Call done when the test finishes successfully
         })
         .catch((error) => done(error)); // Call done with error if the promise rejects
     });
   });
   ```

3. **Run the Test:**

   Run the test suite using:

   ```bash
   npm test 6-payment_token.test.js
   ```

   **Expected Output:**

   ```bash
   getPaymentTokenFromAPI
     ✔ returns a resolved promise with correct data when success is true

   1 passing (4ms)
   ```

</details>

<details>
  <summary><strong>Explanation: Who, What, Where, When, Why, How</strong></summary>

- **What:** This task involves testing a function that returns a promise and verifying the result using Mocha’s `done` callback to handle asynchronous tests.
- **Where:** The function `getPaymentTokenFromAPI` is located in `6-payment_token.js`, and the tests are in `6-payment_token.test.js`.
- **Why:** The `done` callback is used to properly manage asynchronous tests, ensuring that Mocha waits for the test to complete before moving on.
- **How:** The promise returned by `getPaymentTokenFromAPI` is tested by chaining a `.then()` method, and the `done()` callback is called after the promise resolves. If the promise rejects, `done(error)` is used to fail the test.
- **Who:** This task is for developers learning how to handle async testing, especially when testing promises or other asynchronous behavior.
- **When:** Run the tests using `npm test 6-payment_token.test.js` to verify the behavior.

</details>


### Task 7: Skipping a Test with Mocha

This task involves skipping a failing test in a test suite without removing or commenting it out. Mocha’s `it.skip` is used to skip the test, allowing the rest of the test suite to pass.

<details>
  <summary><strong>Curriculum Instruction</strong></summary>

- In `7-skip.test.js`, skip the failing test `'1 is equal to 3'` using `it.skip` without removing or modifying the test description.
- Ensure that the rest of the test suite passes and the skipped test is marked as pending.

</details>

<details>
  <summary><strong>Steps and Code Implementation</strong></summary>

1. **Create `7-skip.test.js`:**

   Here’s the code with the failing test skipped:

   ```javascript
   const { expect } = require('chai');

   describe('Testing numbers', () => {
     it('1 is equal to 1', () => {
       expect(1 === 1).to.be.true;
     });

     it('2 is equal to 2', () => {
       expect(2 === 2).to.be.true;
     });

     it.skip('1 is equal to 3', () => {
       expect(1 === 3).to.be.true; // This test will be skipped
     });

     it('3 is equal to 3', () => {
       expect(3 === 3).to.be.true;
     });

     it('4 is equal to 4', () => {
       expect(4 === 4).to.be.true;
     });

     it('5 is equal to 5', () => {
       expect(5 === 5).to.be.true;
     });

     it('6 is equal to 6', () => {
       expect(6 === 6).to.be.true;
     });

     it('7 is equal to 7', () => {
       expect(7 === 7).to.be.true;
     });
   });
   ```

2. **Run the Test:**

   Run the test suite using:

   ```bash
   npm test 7-skip.test.js
   ```

   **Expected Output:**

   ```bash
   Testing numbers
     ✔ 1 is equal to 1
     ✔ 2 is equal to 2
     - 1 is equal to 3 (skipped)
     ✔ 3 is equal to 3
     ✔ 4 is equal to 4
     ✔ 5 is equal to 5
     ✔ 6 is equal to 6
     ✔ 7 is equal to 7

   7 passing (4ms)
   1 pending
   ```

</details>

<details>
  <summary><strong>Explanation: Who, What, Where, When, Why, How</strong></summary>

- **What:** This task focuses on skipping failing tests using `it.skip` to allow the rest of the test suite to pass.
- **Where:** The test suite is located in `7-skip.test.js`.
- **Why:** Skipping tests is a best practice for retaining tests that are failing or not currently relevant without removing or commenting them out. This allows developers to revisit the issue later while ensuring the test suite still runs smoothly.
- **How:** Mocha’s `it.skip` is used to mark the test as pending, and the skipped test will show as pending in the test results.
- **Who:** This task is important for developers who want to maintain the integrity of their test suite while dealing with tests that need to be temporarily skipped.
- **When:** Run the tests using `npm test 7-skip.test.js` to verify the behavior.

</details>


### Task 8: Basic Integration Testing

In this task, we set up a basic Express API and wrote integration tests to ensure the API is working as expected. We used Mocha and Chai for the tests, and the `request` module to make HTTP requests during the test.

<details>
  <summary><strong>Curriculum Instruction</strong></summary>

- Create a folder `8-api` at the root of your project directory.
- Inside this folder:
  - Create a `package.json` file with the appropriate dependencies.
  - Create an `api.js` file to implement a basic Express server that listens on port `7865`.
  - Create an `api.test.js` file to test the API using Mocha and Chai.
- The test should:
  - Verify the status code and the returned message for the `/` route.
  
</details>

<details>
  <summary><strong>Steps and Code Implementation</strong></summary>

1. **Create the `package.json` file:**

   Inside the `8-api` folder, create a `package.json` file with the following content:

   ```json
   {
     "name": "8-api",
     "version": "1.0.0",
     "scripts": {
       "test": "./node_modules/mocha/bin/mocha"
     },
     "dependencies": {
       "express": "^4.17.1"
     },
     "devDependencies": {
       "chai": "^4.2.0",
       "mocha": "^6.2.2",
       "request": "^2.88.0"
     }
   }
   ```

   Run `npm install` to install the necessary dependencies:

   ```bash
   npm install
   ```

2. **Create the `api.js` file:**

   Write the following code in `api.js` to create a basic Express server:

   ```javascript
   const express = require('express');
   const app = express();

   app.get('/', (req, res) => {
     res.send('Welcome to the payment system');
   });

   if (require.main === module) {
     app.listen(7865, () => {
       console.log('API available on localhost port 7865');
     });
   }

   module.exports = app;
   ```

3. **Create the `api.test.js` file:**

   Write the test cases in `api.test.js`:

   ```javascript
   const request = require('request');
   const { expect } = require('chai');

   describe('Index page', () => {
     it('should return status code 200', (done) => {
       request('http://localhost:7865/', (error, response, body) => {
         expect(response.statusCode).to.equal(200);
         done();
       });
     });

     it('should return the correct message', (done) => {
       request('http://localhost:7865/', (error, response, body) => {
         expect(body).to.equal('Welcome to the payment system');
         done();
       });
     });
   });
   ```

4. **Start the Server (Terminal 1):**

   To run the server, open **Terminal 1**, navigate to the `8-api` folder, and run:

   ```bash
   node api.js
   ```

   You should see the following output:

   ```bash
   API available on localhost port 7865
   ```

5. **Run the Tests (Terminal 2):**

   In **Terminal 2**, navigate to the `8-api` folder and run the test suite:

   ```bash
   npm test api.test.js
   ```

   **Expected output:**

   ```bash
   Index page
     ✓ should return status code 200
     ✓ should return the correct message

   2 passing (24ms)
   ```

6. **Verify in the Browser:**

   After starting the server, open your browser and visit [http://localhost:7865/](http://localhost:7865/). You should see:

   ```text
   Welcome to the payment system
   ```

</details>


<details>
  <summary><strong>Explanation: Who, What, Where, When, Why, How</strong></summary>

- **What:** This task involves setting up a basic Express server that responds to a `GET` request on the `/` route and writing integration tests to ensure the server behaves correctly.
- **Where:** The API is defined in `api.js`, and the tests are located in `api.test.js`. The API listens on port `7865`.
- **Why:** This task demonstrates how to create a simple API and how to perform integration testing to ensure the API is functioning as expected.
- **How:** The server is set up using Express, and the tests use the `request` module to make HTTP requests and the `chai` library for assertions.
- **Who:** This task is important for developers working on backend APIs to ensure their endpoints function correctly through automated tests.
- **When:** The server can be run anytime by executing `node api.js`, and the tests can be run by executing `npm test api.test.js` from the command line.

</details>


### Task 9: Regex Integration Testing

In this task, you will extend the previous integration tests by adding a new endpoint `/cart/:id` with route validation and additional tests for handling both valid and invalid `:id` values.

<details>
  <summary><strong>Curriculum Instruction</strong></summary>

1. **Modify `api.js`:**
   - Add a new endpoint `GET /cart/:id`.
   - Ensure that `:id` is validated to be a number using a regular expression in the route definition.
   - If `:id` is a number, return the message: `Payment methods for cart :id`.
   - If `:id` is not a number, return a 404 status code.

2. **Modify `api.test.js`:**
   - Add a new test suite for the `/cart/:id` route.
   - Test cases:
     - Check that the correct status code (`200`) and message are returned when `:id` is a number.
     - Check that a `404` status code is returned when `:id` is not a number.

3. **Usage:**
   - Start the server on port 7865 and test the new `/cart/:id` endpoint.
   - Ensure that all tests pass without any warnings.

</details>

<details>
  <summary><strong>Steps and Code Implementation</strong></summary>

1. **Step 1: Create `9-api` folder**

   First, create the `9-api` folder by copying the `8-api` project:
   
   ```bash
   cp -r 8-api 9-api
   ```


2. **Update `api.js`:**

   Modify the `api.js` file to handle the new `/cart/:id` route with regex validation:

   ```javascript
   const express = require('express');
   const app = express();

   app.get('/', (req, res) => {
     res.send('Welcome to the payment system');
   });

   // Add the new route with regex validation for cart ID
   app.get('/cart/:id(\\d+)', (req, res) => {
     const id = req.params.id;
     res.send(`Payment methods for cart ${id}`);
   });

   // Start the server on port 7865
   app.listen(7865, () => {
     console.log('API available on localhost port 7865');
   });

   module.exports = app;
   ```

3. **Update `api.test.js`:**

   Modify the `api.test.js` file to add tests for the `/cart/:id` endpoint:

   ```javascript
   const request = require('request');
   const { expect } = require('chai');

   describe('Index page', () => {
     it('should return status code 200', (done) => {
       request('http://localhost:7865/', (error, response, body) => {
         expect(response.statusCode).to.equal(200);
         done();
       });
     });

     it('should return the correct message', (done) => {
       request('http://localhost:7865/', (error, response, body) => {
         expect(body).to.equal('Welcome to the payment system');
         done();
       });
     });
   });

   describe('Cart page', () => {
     it('should return 200 and correct message when :id is a number', (done) => {
       request('http://localhost:7865/cart/12', (error, response, body) => {
         expect(response.statusCode).to.equal(200);
         expect(body).to.equal('Payment methods for cart 12');
         done();
       });
     });

     it('should return 404 when :id is not a number', (done) => {
       request('http://localhost:7865/cart/hello', (error, response, body) => {
         expect(response.statusCode).to.equal(404);
         done();
       });
     });
   });
   ```

4. **Run the Test Suite:**

   In **Terminal 1**, start the server:

   ```bash
   node api.js
   ```

   In **Terminal 2**, run the tests:

   ```bash
   npm test api.test.js
   ```

   **Expected Output:**

   ```bash
   Index page
     ✔ should return status code 200
     ✔ should return the correct message

   Cart page
     ✔ should return 200 and correct message when :id is a number
     ✔ should return 404 when :id is not a number

   4 passing (25ms)
   ```

</details>

<details>
  <summary><strong>Explanation: Who, What, Where, When, Why, How</strong></summary>

- **What:** This task involves extending the integration tests to include a new `/cart/:id` endpoint with proper validation for `:id` using regex. We then created test cases to verify the behavior for both valid and invalid `:id` values.
- **Where:** The changes were made in the `api.js` and `api.test.js` files within the `9-api/` folder.
- **Why:** This task helps ensure that the `/cart/:id` endpoint properly validates input and returns the correct response for valid and invalid cases.
- **How:** We used regular expressions to validate that `:id` is a number and wrote tests to cover both valid and invalid cases.
- **Who:** This is important for developers working on API integrations and validating route parameters to prevent unexpected behavior in the application.
- **When:** These tests are executed whenever we run `npm test api.test.js` to verify the API behavior.

</details>


### Task 10: Deep Equality & Post Integration Testing

This task involves adding two new endpoints to your API and writing integration tests for them: `GET /available_payments` and `POST /login`.

<details>
  <summary><strong>Curriculum Instruction</strong></summary>

- **Modify the file `api.js`:**
  - Add a new endpoint `GET /available_payments` that returns an object with the structure:
    ```json
    {
      "payment_methods": {
        "credit_cards": true,
        "paypal": false
      }
    }
    ```
  - Add a new endpoint `POST /login` that returns the message `Welcome :username` where `:username` is the value of the body variable `userName`.
  
- **Modify the file `api.test.js`:**
  - Add a test suite for the `/login` endpoint.
  - Add a test suite for the `/available_payments` endpoint.

</details>

<details>
  <summary><strong>Steps and Code Implementation</strong></summary>

1. **Update `api.js` with the new endpoints:**

   - Add the `GET /available_payments` and `POST /login` routes:
   
   ```javascript
   const express = require('express');
   const app = express();
   
   app.use(express.json());
   
   // Existing endpoints
   app.get('/', (req, res) => {
     res.send('Welcome to the payment system');
   });

   app.get('/cart/:id(\\d+)', (req, res) => {
     const cartId = req.params.id;
     res.send(`Payment methods for cart ${cartId}`);
   });

   // New endpoint for available payments
   app.get('/available_payments', (req, res) => {
     res.json({
       payment_methods: {
         credit_cards: true,
         paypal: false
       }
     });
   });

   // New endpoint for login
   app.post('/login', (req, res) => {
     const { userName } = req.body;
     if (!userName) {
       res.status(400).send('Username is required');
     } else {
       res.send(`Welcome ${userName}`);
     }
   });

   app.listen(7865, () => {
     console.log('API available on localhost port 7865');
   });

   module.exports = app;
   ```

2. **Update `api.test.js` with tests for the new endpoints:**

```javascript
const request = require('request');
const { expect } = require('chai');

describe('Index page', () => {
  it('should return status code 200', (done) => {
    request('http://localhost:7865/', (error, response, body) => {
      expect(response.statusCode).to.equal(200);
      done();
    });
  });

  it('should return the correct message', (done) => {
    request('http://localhost:7865/', (error, response, body) => {
      expect(body).to.equal('Welcome to the payment system');
      done();
    });
  });
});

describe('Cart page', () => {
  it('should return 200 and correct message when :id is a number', (done) => {
    request('http://localhost:7865/cart/12', (error, response, body) => {
      expect(response.statusCode).to.equal(200);
      expect(body).to.equal('Payment methods for cart 12');
      done();
    });
  });

  it('should return 404 when :id is not a number', (done) => {
    request('http://localhost:7865/cart/hello', (error, response, body) => {
      expect(response.statusCode).to.equal(404);
      done();
    });
  });
});


describe('GET /available_payments', () => {
  it('should return available payment methods', (done) => {
    request('http://localhost:7865/available_payments', (error, response, body) => {
      expect(response.statusCode).to.equal(200);
      expect(JSON.parse(body)).to.deep.equal({
        payment_methods: {
          credit_cards: true,
          paypal: false,
        },
      });
      done();
    });
  });
});

describe('POST /login', () => {
  it('should return a welcome message with the userName', (done) => {
    const options = {
      url: 'http://localhost:7865/login',
      method: 'POST',
      json: {
        userName: 'Betty',
      },
    };
    request(options, (error, response, body) => {
      expect(response.statusCode).to.equal(200);
      expect(body).to.equal('Welcome Betty');
      done();
    });
  });
});
```

3. **Run the tests:**

   - In **Terminal 1**, start the server:
     ```bash
     node api.js
     ```

   - In **Terminal 2**, run the tests:
     ```bash
     npm test api.test.js
     ```

   **Expected Output:**
   
   ```bash
   Index page
     ✓ should return status code 200
     ✓ should return the correct message
   
   Cart page
     ✓ should return 200 and correct message when :id is a number
     ✓ should return 404 when :id is not a number
   
   GET /available_payments
     ✓ should return available payment methods
   
   POST /login
     ✓ should return a welcome message with the userName
   
   6 passing (45ms)
   ```

</details>

<details>
  <summary><strong>Troubleshooting</strong></summary>

- **Issue:** Failing test for cart when :id is a number.
  - **Solution:** Ensure the route `/cart/:id` is properly set up with `\\d+` to validate the `:id` is a number.
  
- **Issue:** Deep equality test failure for `/available_payments`.
  - **Solution:** Use `expect(JSON.parse(body)).to.deep.equal(expectedResponse)` to compare objects for deep equality in the test.

</details>
