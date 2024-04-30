# ES6 Classes

## Learning Objectives

## Task Overview

### Task 0:
The objective is to implement a class named `ClassRoom` that captures the maximum number of students a room can hold.

### Task 1
The goal is to implement a function named `initializeRooms` that returns an array of three `ClassRoom` objects with specific sizes: 19, 20, and 34.

### Task 2
Implement a class named `HolbertonCourse` with attributes for name, length, and students. Include type validation and implement getters and setters for each attribute.

## File Overview
- `0-classroom.js`: Contains the implementation of the `ClassRoom` class. This class accepts a `maxStudentsSize` parameter in its constructor and assigns it to a private property `_maxStudentsSize`.
- `0-main.js`: A testing script used to validate the functionality of the `ClassRoom` class by creating an instance and logging the `_maxStudentsSize` property.

- `1-make_classrooms.js`: Contains the `initializeRooms` function which creates and returns an array of `ClassRoom` objects with predefined sizes.
- `1-main.js`: A testing script used to validate the functionality of the `initializeRooms` function by logging the array of `ClassRoom` objects.

- `2-hbtn_course.js`: Contains the `HolbertonCourse` class with getters and setters for name, length, and students.
- `2-main.js`: A testing script for `HolbertonCourse`.


## Installation
Clone this repository and navigate to the project directory.

```
git clone https://github.com/ThatsVie/atlas-web_back_end.git
```

```
cd ES6_classes
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

To run the 0-main.js script and test the implementation, use the following command:
```
npm run dev 0-main.js
```
When you run the above command, it executes the script 0-main.js, which imports the ClassRoom class and creates an instance with a maxStudentsSize of 10. The script then logs the value of _maxStudentsSize:

![image](https://github.com/ThatsVie/atlas-web_back_end/assets/143755961/a8770cee-d130-415f-af22-e68b052156ad)


This output confirms that the ClassRoom instance has been successfully created with a maximum student size of 10, and that the _maxStudentsSize property is correctly storing and retrieving this value.

### Task 1

To run the `1-main.js` script and test the implementation, use the following command:
```
npm run dev 1-main.js
```
When you run the above command for Task 1, it executes the script `1-main.js`, which imports and calls the `initializeRooms` function. The output should be an array of `ClassRoom` objects with the specified sizes:

![image](https://github.com/ThatsVie/atlas-web_back_end/assets/143755961/47309aee-92a4-41f9-8cb5-5096e1026528)

This confirms that the `initializeRooms` function correctly creates and returns an array of `ClassRoom` instances with the correct sizes.


### Task 2

To run the `2-main.js` script and test the implementation, use the following command:
```
npm run dev 2-main.js
```
When you run the above command for Task 2, it executes the script `2-main.js`, which tests various functionalities of the `HolbertonCourse` class. The output should look like this:

![image](https://github.com/ThatsVie/atlas-web_back_end/assets/143755961/4ea3e2ae-a8da-4867-b9c4-b87f90ae640b)


**Note on Output Abbreviation:**
The ellipsis (`...`) in the output represents truncated stack trace details. These details are typically long error messages and paths which have been shortened here for clarity and brevity in the README.


### Task 3


### Task 4


### Task 5


### Task 6


### Task 7


### Task 8


### Task 9


### Task 10
