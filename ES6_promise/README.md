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

Create a function named getResponseFromAPI that returns a Promise. This simple Promise does not resolve or reject, it remains in the pending state indefinitely. This task is important for understanding the instantiation and basic structure of a Promise.

### Task 1

Create a function getFullResponseFromAPI that returns a promise based on a boolean input. If true, the promise resolves with an object containing status and body attributes. If false, it rejects with an error message indicating that the API is not working.

### Task 2


### Task 3


### Task 4


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


### Task 3


### Task 4


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

![image](https://github.com/ThatsVie/atlas-web_back_end/assets/143755961/e218ed05-db9e-4439-8459-ee75a353d7db)

The ellipsis (...) represents truncated parts of the output, which will contain error stack traces and additional messages. This abbreviation helps focus on the key result without the excessive detail.

### Task 2


### Task 3



### Task 4


### Task 5


### Task 6


### Task 7


### Task 8


### Task 9


### Task 10
