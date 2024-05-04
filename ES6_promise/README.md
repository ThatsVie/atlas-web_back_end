# ES6 Promises

### Learning Objectives

### Promises (how, why, and what)

### How to use the then, resolve, catch methods

### How to use every method of the Promise object

### Throw / Try

### The await operator

### How to use an async function


## Task Overview

### Task 0

Create a function named `getResponseFromAPI` that returns a Promise. This simple Promise does not resolve or reject, it remains in the pending state indefinitely. This task is important for understanding the instantiation and basic structure of a Promise.

### Task 1

Create a function `getFullResponseFromAPI` that returns a promise based on a boolean input. If true, the promise resolves with an object containing status and body attributes. If false, it rejects with an error message indicating that the API is not working.

### Task 2

Utilize the `handleResponseFromAPI` function to manage promise resolutions and rejections. The function appends handlers to a promise to process its outcome—either resolved or rejected.
- Resolved Promise: Returns an object { status: 200, body: 'success' } and logs "Got a response from the API."
- Rejected Promise: Returns a new Error object indicating a failure.

### Task 3

Implement the `handleProfileSignup` function to manage the signup process using promises. This function coordinates the execution of two asynchronous operations: uploading a photo and creating a user profile. Both operations return promises, and their results are handled collectively.

### Task 4

Implement the `signUpUser` function that returns a promise which resolves immediately with an object containing the user's first and last names. This task demonstrates the creation of a promise that resolves immediately, useful for simulating asynchronous operations that complete successfully without any delay.

### Task 5

Write and export a function named uploadPhoto that rejects a Promise with an error message stating that a specified file cannot be processed.

### Task 6

Integrate functionality from previous tasks. The task involves creating a function `handleProfileSignup` that takes three arguments: `firstName`, `lastName`, and `fileName`. It uses these to call `signUpUser` and `uploadPhoto`, which return promises. `handleProfileSignup` must handle these promises and return their results in a structured array format, indicating whether each promise was fulfilled or rejected and their corresponding values or error messages.

### Task 7

Implement the `loadBalancer` function which accepts two arguments, both of which are Promises (`chinaDownload` and `USDownload`).

### Task 8

Create a function `divideFunction` that divides a numerator by a denominator. If the denominator is zero, it throws an error to avoid division by zero, otherwise, it returns the result of the division.

### Task 9


### Task 10

## File Overview

### Task 0
`0-promise.js`: Contains the `getResponseFromAPI` function which returns a new, unresolved Promise.

`0-main.js`: A test script that imports `getResponseFromAPI` and checks if the returned object is an instance of a Promise, confirming the correct implementation.

### Task 1
`1-promise.js`: Contains the `getFullResponseFromAPI` function which returns a promise that either resolves or rejects based on the provided boolean argument.

`1-main.js`: Testing script that validates the function `getFullResponseFromAPI` with both true and false conditions, demonstrating promise resolution and rejection.

### Task 2
`2-then.js`: Contains the `handleResponseFromAPI` function which manages the response from a promise by implementing handlers using the .then() and .catch() methods.

`2-main.js`: A testing script for the `handleResponseFromAPI` function. This script imports the function and applies it to a resolved Promise to check how the function handles resolved and possibly rejected states. 

### Task 3
`3-all.js`: Contains the `handleProfileSignup` function which utilizes Promise.all to handle the promises returned by `uploadPhoto` and `createUser`.

`3-main.js`: A script that imports and executes the `handleProfileSignup` function, demonstrating the aggregation of promises and error handling.

### Task 4
`4-user-promise.js`: Contains the implementation of the `signUpUser` function which returns a resolved promise containing user details.

`4-main.js`: A testing script that imports and utilizes the `signUpUser` function to demonstrate promise resolution.

### Task 5
`5-photo-reject.js`: Contains the `uploadPhoto` function that returns a Promise. This Promise always rejects with an Error, stating that the file cannot be processed.

`5-main.js`: Tests the `uploadPhoto` function by attempting to process a file and logging the result.
### Task 6
`6-final-user.js`: Implements the `handleProfileSignup` function which calls `signUpUser` and `uploadPhoto`, handling their completion with Promise.allSettled.

`6-main.js`: A script to test the `handleProfileSignup` function, demonstrating how it handles multiple asynchronous operations.

### Task 7
`7-load_balancer.js`: Contains the `loadBalancer` function which uses Promise.race() to return the result of the first resolved promise between two download operations.

`7-main.js`: A testing script to demonstrate the usage of the `loadBalancer` function with simulated download promises.

### Task 8
`8-try.js`: Contains the `divideFunction` which performs division and handles division by zero with error handling.

`8-main.js`: A testing script for `divideFunction` which tests dividing a number by another and by zero to demonstrate error handling.

### Task 9


### Task 10


## Installation
Clone this repository and navigate to the project directory.

```
git clone https://github.com/ThatsVie/atlas-web_back_end.git
```

```
cd ES6_promise
```

## Setup
Ensure you have Node.js installed on your system. [ Visit this site for details about which version may be appropriate for you ](https://github.com/nodejs/Release)

**Install Jest**

Jest is used for running tests. Install Jest using npm by running:
```
npm install --save-dev jest
```

**Install Babel**

Babel is used for compiling ES6+ JavaScript to backwards-compatible versions. Install Babel along with necessary presets:
```
npm install --save-dev babel-jest @babel/core @babel/preset-env
```

**Install ESLint**

ESLint is used to ensure code quality and consistency. Install ESLint with:
```
npm install --save-dev eslint
```

## Usage

### Task 0
To verify that the function returns a Promise, run the following command:
```
npm run dev 0-main.js
```
This executes the script 0-main.js, which imports the function and logs whether the result is an instance of Promise, which outputs true, indicating that the function correctly returns a Promise.

![image](https://github.com/ThatsVie/atlas-web_back_end/assets/143755961/53e531a8-087d-4328-a517-ee4d8ebb4c57)


### Task 1
To test promise resolution and rejection, run:
```
npm run dev 1-main.js
```
This command executes the 1-main.js script

When getFullResponseFromAPI(true) is called, it returns a Promise that resolves to { status: 200, body: 'Success' }.

When getFullResponseFromAPI(false) is called, it returns a Promise that rejects with an error "The fake API is not working currently".

The actual output on the console will be abbreviated to show only the most relevant parts:

![image](https://github.com/ThatsVie/atlas-web_back_end/assets/143755961/cbe45f19-858f-4eff-b314-3e8265b2e155)


The ellipsis (...) represents truncated parts of the output, which will contain error stack traces and additional messages. This abbreviation helps focus on the key result without the excessive detail.

### Task 2
To test the functionality of `handleResponseFromAPI`, execute the following command:
```
npm run dev 2-main.js
```

This runs the 2-main.js script, which imports and uses the handleResponseFromAPI function with a resolved promise. The function logs "Got a response from the API" to the console, indicating that the promise was successfully handled. The function demonstrates handling both resolved and rejected states, showing how to  use promises for asynchronous operations.

![image](https://github.com/ThatsVie/atlas-web_back_end/assets/143755961/de0df3f7-d42b-47fb-845e-73d706f63cd0)


### Task 3
To execute the `handleProfileSignup` function and observe the output:
```
npm run dev 3-main.js
```

![image](https://github.com/ThatsVie/atlas-web_back_end/assets/143755961/9d8c34e9-d124-4efb-806f-ea3ea7702eb2)

Both promises resolve successfully. Console logs a concatenated string of the photo body, user's first name, and last name to the console.

### Task 4
To run the 4-main.js script and test the `signUpUser` function, use the following command:
```
npm run dev 4-main.js
```
When you execute the command, it runs the 4-main.js script which calls signUpUser with the arguments "Bob" and "Dylan". The output should be a promise that resolves to an object displaying the names provided:

![image](https://github.com/ThatsVie/atlas-web_back_end/assets/143755961/7988ecab-e399-4537-9c28-7a5661bb995e)

This confirms that the signUpUser function correctly returns a promise which resolves with the expected user details.

### Task 5
To test the `uploadPhoto` function, run the 5-main.js script using the following command:
```
npm run dev 5-main.js
```
This command executes the script, which imports and calls `uploadPhoto` with a filename argument. If the Promise is rejected, it logs the Error message:

![image](https://github.com/ThatsVie/atlas-web_back_end/assets/143755961/26e59062-6d5b-4cde-b6da-82b8479343fd)

The ellipsis (...) in the output represents truncated error stack trace details, which are omitted for brevity.

### Task 6
To use the `handleProfileSignup` function, run the 6-main.js script using the following command:
```
npm run dev 6-main.js
```

![image](https://github.com/ThatsVie/atlas-web_back_end/assets/143755961/14256683-dd69-453c-ab0a-76d3b565a901)


This output indicates that the promise is still in the process of settling. Once settled, it will provide an array of results for each promise, formatted to show the status and outcome (value or error) of each operation.

**Note:**

The console output Promise { <pending> } is due to the asynchronous nature of promises. If we were to attach .then() or use async/await to handle these promises, we would see the resolved values.

### Task 7
To test the loadBalancer function, run the following command:
```
npm run dev 7-main.js
```

The script in `7-main.js` includes two promise scenarios simulating file downloads from different servers with varied response times. The output demonstrates the effectiveness of `loadBalancer` in selecting the faster response:

![image](https://github.com/ThatsVie/atlas-web_back_end/assets/143755961/0330028c-63e3-46be-8d21-722a84a5b94c)

### Task 8
To run the `8-main.js` script and test the `divideFunction`, use the following command:
```
npm run dev 8-main.js
```

This command executes the script, which attempts to divide 10 by 2 and then 10 by 0. The expected outputs are:

5 when dividing 10 by 2.

An error message when attempting to divide by zero. 

![image](https://github.com/ThatsVie/atlas-web_back_end/assets/143755961/affddf65-b80b-406d-8345-15a2305536e9)

The ellipsis (...) in the output represents truncated stack trace details. These details are typically long error messages and paths which have been shortened here for clarity and brevity

### Task 9


### Task 10
