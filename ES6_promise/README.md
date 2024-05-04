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


### Task 6


### Task 7


### Task 8


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


### Task 6


### Task 7


### Task 8


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
To test the functionality of handleResponseFromAPI, execute the following command:
```
npm run dev 2-main.js
```

This runs the 2-main.js script, which imports and uses the handleResponseFromAPI function with a resolved promise. The function logs "Got a response from the API" to the console, indicating that the promise was successfully handled. The function demonstrates handling both resolved and rejected states, showing how to  use promises for asynchronous operations.

![image](https://github.com/ThatsVie/atlas-web_back_end/assets/143755961/de0df3f7-d42b-47fb-845e-73d706f63cd0)


### Task 3
To execute the handleProfileSignup function and observe the output:
```
npm run dev 3-main.js
```

![image](https://github.com/ThatsVie/atlas-web_back_end/assets/143755961/9d8c34e9-d124-4efb-806f-ea3ea7702eb2)

Both promises resolve successfully. Console logs a concatenated string of the photo body, user's first name, and last name to the console.

### Task 4
To run the 4-main.js script and test the signUpUser function, use the following command:
```
npm run dev 4-main.js
```
When you execute the command, it runs the 4-main.js script which calls signUpUser with the arguments "Bob" and "Dylan". The output should be a promise that resolves to an object displaying the names provided:

![image](https://github.com/ThatsVie/atlas-web_back_end/assets/143755961/7988ecab-e399-4537-9c28-7a5661bb995e)

This confirms that the signUpUser function correctly returns a promise which resolves with the expected user details.

### Task 5


### Task 6


### Task 7


### Task 8


### Task 9


### Task 10
