# ES6 Data Manipulation

This project focuses on array methods, typed arrays, and complex data structures like `Set` and `Map`. The tasks cover how to manipulate data efficiently, applying methods such as `map`, `filter`, `reduce`, and exploring how `Sets` and `Maps` can be used to handle unique data and key-value storage.

## Learning Objectives

### How to use map, filter and reduce on arrays

Throughout the project, several tasks cover the effective use of array methods such as `map`, `filter`, and `reduce`. In Task 1, the `map` function was used to transform an array of student objects into an array containing only their IDs, demonstrating how to extract specific properties from an array of objects. Task 2 utilized the filter method to generate a new array of students located in a specific city, showcasing the method's ability to select elements based on a criterion. Task 3 featured the `reduce` method to sum all student IDs, providing a clear example of accumulating values from an array into a single output.

### Typed arrays

Task 5 focused on demonstrating typed arrays through the creation and manipulation of an ArrayBuffer using a DataView. This task involved setting an Int8 value at a specific position within the buffer, showing how JavaScript can handle binary data in a structured way. The use of DataView here exemplifies accessing and manipulating binary data efficiently.

### The Set, Map, and Weak link data structures

The manipulation of advanced data structures like `Set` and `Map` was also covered in these tasks. Task 6 demonstrated the use of `Set` by converting an array into a set, ensuring all elements were unique and showing the automatic duplication property of sets. In Tasks 9 and 10, `Map` was extensively used; Task 9 created a `Map` to store and retrieve grocery items along with their quantities, while Task 10 updated the quantities in a `Map` based on certain conditions. These tasks show the utility of `Map` for efficient key-value storage and manipulation, showcasing how real-world applications like inventory management can benefit from such data structures.

Task 11 covered WeakMap, using it to track the number of API calls for each endpoint. By storing endpoints as keys and their call counts as values, WeakMap manages memory by allowing garbage collection of keys when no longer referenced elsewhere, which prevents potential memory leaks in applications where control over memory usage is crucial.

## Task Overview

### Task 0: getListStudents Function
Create a function named `getListStudents` that returns an array of student objects. Each object includes three attributes: `id` (a number), `firstName` (a string), and `location` (a string). The function must return details for students named Guillaume, James, and Serena with specific IDs and locations as described.

### Task 1: getListStudentIds Function
Create a function named `getListStudentIds` that processes an array of student objects and returns an array of their IDs. The function checks if the input is an array and uses the `map` function to extract IDs, returning an empty array for invalid inputs.

### Task 2: getStudentsByLocation Function
Create a function named `getStudentsByLocation` that filters an array of student objects to return only those located in a specified city. This function accepts a list of students and a city as parameters and utilizes the `filter` function to produce the desired subset based on location.

### Task 3: getStudentIdsSum Function
Create a function named `getStudentIdsSum` that computes the sum of all student IDs from a given list of students. This function employs the `reduce` method to aggregate ID values from an array of student objects, demonstrating a fundamental array reduction operation in JavaScript.

### Task 4: updateStudentGradeByCity Function
Create a function named `updateStudentGradeByCity` that retrieves an array of students for a specific city and updates their grades based on provided data. The function accepts a list of students, a city, and an array of new grade objects. It uses filter to select students from the specified city and map combined with find to assign new grades or 'N/A' if a student does not have an updated grade provided.

### Task 5: createInt8TypedArray Function
Create a function named `createInt8TypedArray` that initializes a new ArrayBuffer and sets an Int8 value at a specific position. The function takes three arguments: the buffer's length, the position for the value, and the value itself. It throws an error if the position is outside the permissible range, ensuring error handling in data manipulation scenarios.

### Task 6: setFromArray Function
Create a function named `setFromArray` that transforms an array into a Set. This function accepts an array as an argument and utilizes the JavaScript Set object to automatically remove duplicate elements, returning a collection of unique elements.

### Task 7: hasValuesFromArray Function
Create a function named `hasValuesFromArray` that checks if all elements specified in an array exist within a given set. The function takes a set and an array as parameters and returns a boolean indicating whether every array element is present in the set. It uses the `Set.prototype.has()` method for efficient look-up, ensuring optimal performance even with large datasets.

### Task 8: cleanSet Function
Create a function named `cleanSet` that formats and concatenates elements of a set that start with a specified string (`startString`). This function takes two parameters: a set of strings and a starting string. It filters the set to find elements that begin with `startString`, then removes the `startString` portion from each, and concatenates them with a dash ('-'). If `startString` is empty or not provided, the function returns an empty string.

### Task 9: groceriesList Function
Create a function named `groceriesList` that constructs a `Map` of grocery items with specified quantities. The function simplifies the management of grocery items, ensuring each item's quantity is uniquely stored and easily accessible.

### Task 10: updateUniqueItems Function
Create a function named `updateUniqueItems` that modifies a `Map` by updating all entries with a quantity of 1 to 100. The function demonstrates handling data structures and ensuring type safety by throwing an error if the provided argument is not a `Map`.

### Task 11:  WeakMap and queryAPI
Task 11 introduces the use of a `WeakMap` to track the number of times an API endpoint is queried. The function `queryAPI` increments a count for each call associated with a specific endpoint. If an endpoint is queried five times or more, it throws an error indicating high load.

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
- `4-update_grade_by_city.js`: Implements the `updateStudentGradeByCity` function that updates student grades based on their location and provided grade updates.
- `4-main.js`: Script to test the `updateStudentGradeByCity` function by applying grade updates to students in a specified city.

### Task 5
- `5-typed_arrays.js`: Implements the `createInt8TypedArray` function which creates a new ArrayBuffer and sets an Int8 value at a specific position, using a DataView for manipulation.
- `5-main.js`: Script to test the ArrayBuffer creation and data setting functionality of `createInt8TypedArray`.

### Task 6
- `6-set.js`: Implements the `setFromArray` function that converts an array into a Set, ensuring all elements are unique.
- `6-main.js`: Script to test the `setFromArray` function by converting an array to a Set and demonstrating the removal of duplicates.

### Task 7
- `7-has_array_values.js`: Implements the `hasValuesFromArray` function to verify if all elements of an array are contained in a specific set.
- `7-main.js`: Script to test the functionality of `hasValuesFromArray`.

### Task 8
- `8-clean_set.js`: Implements the `cleanSet` function to extract and format set values based on a start string.
- `8-main.js`: Script to test the `cleanSet` function.

### Task 9
- `9-groceries_list.js`: Contains the `groceriesList` function which initializes a `Map` to store grocery items with their respective quantities.
- `9-main.js`: Script to test the `groceriesList` function, demonstrating the initialization and display of the grocery `Map`.

### Task 10
- `10-update_uniq_items.js`: Contains the `updateUniqueItems` function which updates the quantities in a `Map` based on specific conditions. This function demonstrates manipulation of `Map` objects and error handling when the argument is not as expected.
- `10-main.js`: Script to test the `updateUniqueItems` function by displaying changes in the grocery list `Map`.

### Task 11
- `100-weak.js`: Contains the `queryAPI` function and the `weakMap` instance. The function manages the count of API calls per endpoint using `weakMap` and controls the request load by throwing an error when the count exceeds a threshold.
- `100-main.js`: Demonstrates the usage of `queryAPI` and how it interacts with `weakMap` to track and manage API call limits.

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

![image](https://github.com/ThatsVie/atlas-web_back_end/assets/143755961/eeb42fcc-a001-42ee-b499-cefd6e1c9a4a)


### Task 1
To test the `getListStudentIds` function and its handling of different inputs, run the script using the following command:
```
npm run dev 1-main.js
```
This command executes the `1-main.js` script, which:
- Attempts to use `getListStudentIds` with an incorrect input (`"hello"`), expecting to receive an empty array as the function checks for the input type.
- Uses `getListStudentIds` with a valid input (an array of student objects from `getListStudents`), and logs the output array of IDs.

![image](https://github.com/ThatsVie/atlas-web_back_end/assets/143755961/b26b05a3-ccd2-43e3-9bf1-a7c9ac458954)

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

![image](https://github.com/ThatsVie/atlas-web_back_end/assets/143755961/04cd55f2-5e67-4fdc-8742-13db816127b3)


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

![image](https://github.com/ThatsVie/atlas-web_back_end/assets/143755961/65390d7e-f9f1-40cf-98d0-1237f58a16fd)


The console will output `8`, indicating that the IDs of the provided students have been successfully summed. This confirms that the `reduce` method is correctly implemented to accumulate values across the student list.


### Task 4
To test the `updateStudentGradeByCity` function for updating student grades based on city and provided grades, use the following command:
```
npm run dev 4-main.js
```
This command executes the `4-main.js` script, which performs the following actions:
- Retrieves a list of students using the `getListStudents` function.
- Calls `updateStudentGradeByCity` with the list of students, specifying 'San Francisco' as the city and providing grade updates.
- Logs the results to the console, showing students with their updated grades or 'N/A' where no specific grade was provided.

![image](https://github.com/ThatsVie/atlas-web_back_end/assets/143755961/e71f0db8-d319-4fb5-a1cd-159123c841a0)

- The first console log shows students in 'San Francisco' with updated grades
- The second console log shows students in 'San Francisco' with one having an updated grade and another with 'N/A':
  
### Task 5
To test the `createInt8TypedArray` function for creating an ArrayBuffer and setting an Int8 value, use the following command:
```
npm run dev 5-main.js
```
This command runs the `5-main.js` script, which performs the following actions:
- Calls `createInt8TypedArray` with a buffer length of 10, position 2, and value 89.
- Logs the resulting DataView to the console, showing the byte configuration of the buffer.

![image](https://github.com/ThatsVie/atlas-web_back_end/assets/143755961/e5206496-a86a-4361-8c29-dbd98e715bc7)

The console output will show a DataView reflecting the ArrayBuffer status. This demonstrates that the `createInt8TypedArray` function correctly initializes an ArrayBuffer and successfully sets an Int8 value at the specified position without overflowing the buffer, verifying both functionality and error handling.

### Task 6
To test the `setFromArray` function for converting an array to a Set, use the following command:
```
npm run dev 6-main.js
```

This command runs the `6-main.js` script, which:
- Calls `setFromArray` with an array that includes duplicates (`[12, 32, 15, 78, 98, 15]`).
- Logs the resulting Set to the console, displaying the unique elements.

![image](https://github.com/ThatsVie/atlas-web_back_end/assets/143755961/8e318c59-cc55-4e6d-82b0-ce52b8bbc42f)


This output confirms that the `setFromArray` function effectively removes duplicates (number 15 in this case) and retains only unique elements, demonstrating the utility of JavaScript's Set object for data manipulation.

### Task 7
To test the `hasValuesFromArray` function for verifying the presence of array elements within a set, use the following command:
```
npm run dev 7-main.js
```
This command runs the `7-main.js` script, which:
- Tests `hasValuesFromArray` by checking multiple arrays against a set containing the numbers 1 through 5.

![image](https://github.com/ThatsVie/atlas-web_back_end/assets/143755961/fdc1d46f-a646-460f-8aba-b311606117d1)

- The first test checks if the element `1` is in the set, return `true`.
- The second test checks if the non-existent element `10` is in the set, returns `false`.
- The third test checks if both `1` and `10` are in the set, returns `false` since `10` is not in the set.

### Task 8
To test the `cleanSet` function, use the following command:
```
npm run dev 8-main.js
```
This command executes the `8-main.js` script, which tests the `cleanSet` function in the following scenarios:
- Filtering and formatting set values that start with "bon", resulting in concatenated values separated by dashes.
- Attempting to filter with an empty start string, which should return an empty string due to the function's validation check.

![image](https://github.com/ThatsVie/atlas-web_back_end/assets/143755961/1ada7f96-4eee-481f-8448-1867b1e7f340)

- When called with "bon" as the start string: `jovi-aparte-appetit`
- When called with an empty start string: (nothing, just an empty line)

This setup demonstrates how `cleanSet` effectively processes sets based on prefix criteria and provides dynamic string construction, which is useful for applications requiring customized data displays or reports.

### Task 9
To test the `groceriesList` function and see the structure of the created `Map`, use the following command:
```
npm run dev 9-main.js
```
This command executes the `9-main.js` script, which uses the `groceriesList` function to create a `Map` with predefined grocery items and their quantities.

![image](https://github.com/ThatsVie/atlas-web_back_end/assets/143755961/bb5b8355-77eb-4e7f-aa5a-8935ef01da85)


The console will display the `Map` object listing the grocery items and their quantities.

This demonstrates the `groceriesList` function's ability to create a structured and easily manipulatable collection of grocery items using the `Map` data structure, which is ideal for scenarios where key uniqueness and order are important.

### Task 10
To test the `updateUniqueItems` function and observe how it modifies a `Map` of groceries, use the following command:
```
npm run dev 10-main.js
```

This command executes the `10-main.js` script, which uses both `groceriesList` to generate a grocery list `Map` and `updateUniqueItems` to update quantities in this map.

![image](https://github.com/ThatsVie/atlas-web_back_end/assets/143755961/98c46694-d7e8-439a-b62d-29555aea9444)


- Before updating, the `Map` shows various grocery items with their initial quantities.
- After invoking `updateUniqueItems`, the quantities of items that were initially 1 are updated to 100.

This output shows that only the items with an initial quantity of 1 (Pasta and Rice) are updated to 100, demonstrating effective map manipulation based on a condition. The map's other entries remain unchanged, showcasing selective updating based on specific criteria.

### Task 11
To test the `queryAPI` function, the `100-main.js` file is used. The script creates an endpoint and attempts to query it multiple times, logging the count of queries until the limit is reached and an error is thrown.
```
npm run dev 100-main.js
```
![image](https://github.com/ThatsVie/atlas-web_back_end/assets/143755961/4285ae07-d302-4765-9047-3d2b93872baf)

This output shows the function in action, successfully counting and limiting the API queries, throwing an error when the maximum allowed queries are exceeded, ensuring the system's stability by preventing overload.

The ellipses (...) are used to indicate that parts of the error traceback and additional command line logs are omitted to simplify the display.
