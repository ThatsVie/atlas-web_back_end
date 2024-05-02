# ES6 Data Manipulation

## Learning Objectives

### How to use map, filter and reduce on arrays

### Typed arrays

### The Set, Map, and Weak link data structures

## Task Overview

### Task 0: getListStudents Function
Create a function named `getListStudents` that returns an array of student objects. Each object includes three attributes: `id` (a number), `firstName` (a string), and `location` (a string). The function must return details for students named Guillaume, James, and Serena with specific IDs and locations as described.

### Task 1: getListStudentIds Function
Create a function named `getListStudentIds` that processes an array of student objects and returns an array of their IDs. The function checks if the input is an array and uses the `map` function to extract IDs, returning an empty array for invalid inputs.

### Task 2: getStudentsByLocation Function
Create a function named `getStudentsByLocation` that filters an array of student objects to return only those located in a specified city. This function accepts a list of students and a city as parameters and utilizes the `filter` function to produce the desired subset based on location.


### Task 3: getStudentIdsSum Function
Create a function named `getStudentIdsSum` that computes the sum of all student IDs from a given list of students. This function employs the `reduce` method to aggregate ID values from an array of student objects, demonstrating a fundamental array reduction operation in JavaScript.


### Task 4


### Task 5


### Task 6


### Task 7


### Task 8


### Task 9


### Task 10

## File Overview

### Task 0
- `0-get_list_students.js`: This file contains the `getListStudents` function that returns an array of objects, each representing a student with `id`, `firstName`, and `location` attributes. This setup demonstrates the creation and use of basic data structures in JavaScript.
- `0-main.js`: A testing script that imports and executes the `getListStudents` function from `0-get_list_students.js`. It is used to validate the functionality by logging the returned array of student objects to the console, ensuring that the data is correctly structured and populated as specified.

### Task 1
- `1-get_list_student_ids.js`: Implements the `getListStudentIds` function that extracts and returns an array of IDs from the student objects provided to it. This function validates the input to ensure it is an array before proceeding with the `map` method.
- `1-main.js`: A script to test the `getListStudentIds` function by providing both valid and invalid inputs to verify the function's response to different types of data.

### Task 2
- `2-get_students_by_loc.js`: Implements the `getStudentsByLocation` function that filters students by their location using the `filter` method, ensuring that only students from a specific city are returned.
- `2-main.js`: A script to test the `getStudentsByLocation` function by filtering students for a specific location and displaying the results.

### Task 3
- `3-get_ids_sum.js`: Implements the `getStudentIdsSum` function which calculates the sum of student IDs using the `reduce` method.
- `3-main.js`: Script to test the summing capabilities of the `getStudentIdsSum` function.

### Task 4

## Installation
Clone this repository and navigate to the project directory.

```
git clone https://github.com/ThatsVie/atlas-web_back_end.git
```

```
cd ES6_data_manipulation
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
To run the `0-main.js` script and test the implementation of the `getListStudents` function, use the following command:
```
npm run dev 0-main.js
```

This command executes the `0-main.js` script, which imports the `getListStudents` function from `0-get_list_students.js` and logs the array of student objects to the console. The output confirms that the function correctly creates and returns a structured array of student data with their respective IDs, names, and locations.

![image](https://github.com/ThatsVie/atlas-web_back_end/assets/143755961/c6f1f0cf-12d7-49cf-944d-48358584817f)


### Task 1
To test the `getListStudentIds` function and its handling of different inputs, run the script using the following command:
```
npm run dev 1-main.js
```
This command executes the `1-main.js` script, which:
- Attempts to use `getListStudentIds` with an incorrect input (`"hello"`), expecting to receive an empty array as the function checks for the input type.
- Uses `getListStudentIds` with a valid input (an array of student objects from `getListStudents`), and logs the output array of IDs.

![image](https://github.com/ThatsVie/atlas-web_back_end/assets/143755961/01798e79-64af-4bb6-91d2-833d2ca0070c)

- The first console.log should output an empty array `[]` because the input is a string, not an array.
- The second console.log should output the array `[1, 2, 5]` indicating the successful extraction of student IDs from the provided array.

These tests confirm the functionality of the `getListStudentIds` function, demonstrating its ability to handle both correct and incorrect inputs appropriately.


### Task 2
To test the `getStudentsByLocation` function and its ability to filter students based on location, run the script using the following command:
```
npm run dev 2-main.js
```

This command executes the `2-main.js` script, which:
- Imports and calls the `getListStudents` to retrieve an array of students.
- Uses `getStudentsByLocation` with the student array and the city 'San Francisco' to filter the students.
- Logs the filtered student list to the console.

![image](https://github.com/ThatsVie/atlas-web_back_end/assets/143755961/4d357029-20ac-4863-9642-05e15a905541)

The console outputs an array of student objects who are located in 'San Francisco', confirming that the function correctly filters the students based on the specified location criteria.


### Task 3
To test the `getStudentIdsSum` function for summing student IDs, use the following command:
```
npm run dev 3-main.js
```
This command runs the `3-main.js` script, which performs the following actions:
- Imports the list of students from `getListStudents`.
- Calls the `getStudentIdsSum` function with the list of students as an argument.
- Logs the resulting value to the console, which represents the sum of all student IDs.

![image](https://github.com/ThatsVie/atlas-web_back_end/assets/143755961/8f273b1d-aaa8-454d-8549-11ed75621043)

The console will output `8`, indicating that the IDs of the provided students have been successfully summed. This confirms that the `reduce` method is correctly implemented to accumulate values across the student list.


### Task 4


### Task 5


### Task 6


### Task 7


### Task 8


### Task 9


### Task 10
