# ES6 Basic

This project covers ES6 (ECMAScript 2015) features and best practices in modern JavaScript development. It covers topics such as variable declaration with let and const, block-scoped variables, arrow functions, template literals, spread/rest operators, object creation, and iterators. 

## Learning Objectives
**What ES6 is**

ES6, also known as ECMAScript 2015, is the sixth edition of the ECMAScript standard, which defines the scripting language JavaScript.

**New features introduced in ES6**

ES6 introduced several new features to JavaScript, including let and const for variable declaration, arrow functions for concise function syntax, template literals for enhanced string formatting, and the spread and rest operators for working with arrays and function parameters.

**The difference between a constant and a variable**

Constants, declared using the const keyword, are immutable and cannot be reassigned, while variables, declared using let, can be reassigned within their scope.

**Block-scoped variables**

Block-scoped variables, declared using let and const, are scoped to the nearest enclosing block, allowing for more precise variable scoping compared to var, which is function-scoped


**Arrow functions and function parameters default to them**

Arrow functions provide a concise syntax for writing functions, and they automatically bind the this value to the enclosing lexical context, making them particularly useful for callback functions and event handlers.


**Rest and spread function parameters**

Rest parameters, denoted by three dots (...), allow functions to accept an indefinite number of arguments as an array, while spread syntax, also denoted by three dots (...), allows for the expansion of arrays and objects into individual elements or properties.

**String templating in ES6**

String templating in ES6, also known as template literals, allows for embedding expressions and variables directly within strings using the ${} syntax, enabling more readable and maintainable string construction.

**Object creation and their properties in ES6**

Object creation in ES6 supports concise syntax for defining object literals, as well as features such as computed property names, method shorthand notation, and property value shorthand notation, enhancing object-oriented programming in JavaScript.

**Iterators and for-of loops**

ES6 introduces iterators and the for-of loop, providing a more convenient and readable way to iterate over iterable objects such as arrays, strings, and collections, compared to traditional for loops and forEach methods.

## Tasks Overview

### Task 0
Modify two JavaScript functions to use const and let instead of var. This task focuses on understanding the appropriate usage of these ES6 features to manage variable immutability and block scope.

### Task 1
Modify the function to use block-scoped variables (`let` or `const`) instead of `var` to prevent variables from being overwritten inside the conditional block. This task is a practical application of understanding variable hoisting and scope control introduced with ES6.

### Task 2
Rewrite a standard function to utilize ES6 arrow syntax, which helps to maintain the context of `this` without the need for manual binding, such as through a `self` variable.

### Task 3
Refactor a function to make its body more concise by utilizing default parameters, which simplify the handling of unspecified arguments.

### Task 4
Modify a function to use the rest parameter syntax for counting and returning the number of arguments it receives. This functionality allows the function to handle a variable number of input arguments without specifying them individually.

### Task 5
Use the spread syntax to concatenate two arrays and each character of a string into one array, showcasing the versatility of spread operators in handling multiple data types.

### Task 6
Enhance string construction using ES6 template literals to cleanly integrate variables into text, improving readability and maintainability.

### Task 7
Simplify object creation using enhanced object literal syntax, reducing redundancy by utilizing property value shorthand.

### Task 8
Demonstrate the use of computed property names in objects to dynamically construct property keys based on runtime values, showcasing further flexibility in object creation.

### Task 9
Implement ES6 method properties in object definitions to simplify and enhance the readability of method declarations within objects.

### Task 10
Refactor the `appendToEachArrayValue` function to use ES6 `for...of` loop and `const` for iterating through arrays, for more efficient code.

### Task 11
Create a function that dynamically generates objects with department names as keys and lists of employees as values, demonstrating the use of computed property names for object keys.

### Task 12 
Enhance the `createReportObject` function to use internal state with `this` for method operations, promoting better encapsulation and leveraging ES6 features for method definition.

## File Overview

### Task 0
`0-main.js`: Imports and tests functions from `0-constants.js` by executing them and displaying their combined outputs.

`0-constants.js`:
- `taskFirst`: Declares a constant string and returns it.
- `getLast`: Returns a string to be appended by another function.
- `taskNext`: Declares a string and modifies it by appending another string from `getLast()` before returning the result.

### Task 1

`1-main.js`: Tests the `taskBlock` function by executing it with different boolean values and displays the results to demonstrate the effect of the conditional logic.

`1-block-scoped.js`: Contains the `taskBlock` function which demonstrates the difference between block scope (`let`, `const`) and function scope (`var`). The function modifies the behavior of variable declaration to prevent unexpected overwrites due to hoisting.

### Task 2

`2-main.js`: Executes the `getNeighborhoodsList` constructor and its method `addNeighborhood` to demonstrate the application of arrow functions in methods.

`2-arrow.js`: 
Contains the `getNeighborhoodsList` constructor function which is adapted to use arrow syntax for its method `addNeighborhood`. This change shows the benefits of arrow functions in handling the `this` context more predictably within JavaScript classes or constructor functions.

### Task 3

`3-main.js`: Executes `getSumOfHoods` demonstrating the use of default parameters in function condensation.

`3-default-parameter.js`: 
This file contains the `getSumOfHoods` function, demonstrating how to effectively use default parameters to simplify function logic. By setting default values for parameters directly in the function signature, it removes the need for conditional checks within the function body.

### Task 4

`4-main.js`: Demonstrates the use of the rest parameter syntax by executing `returnHowManyArguments` with various sets of arguments.

`4-rest-parameter.js`: Contains the `returnHowManyArguments` function which demonstrates the use of rest parameters to count the number of arguments passed to it. This ES6 feature simplifies functions that can take an indefinite number of parameters.

### Task 5

**5-main.js:** Executes `concatArrays` function demonstrating the use of spread syntax to merge arrays and string characters.

**5-spread-operator.js:** 
- `concatArrays`: Combines two arrays and the characters of a string into a single array using the spread syntax.
  
### Task 6

**6-main.js:** Executes `getSanFranciscoDescription` showcasing the use of template literals for string interpolation.

**6-string-interpolation.js:** 
- `getSanFranciscoDescription`: Uses template literals to incorporate variables and create a descriptive text about San Francisco's economic figures, demonstrating clear and concise string formatting.

### Task 7

**7-main.js:** Demonstrates the functionality of `getBudgetObject`, showcasing the use of ES6 property shorthand in object literals.

**7-getBudgetObject.js:** 
- `getBudgetObject`: Creates and returns a budget object using property shorthand to streamline the assignment of properties when the variable names and property names are identical.

### Task 8

**8-main.js:** Executes `getBudgetForCurrentYear`, showcasing how to dynamically construct object properties using computed names based on current year data.

**8-getBudgetCurrentYear.js:** 
- `getBudgetForCurrentYear`: Illustrates the dynamic construction of object properties using computed property names, integrating runtime values into object keys.

### Task 9

**9-main.js:** Executes `getFullBudgetObject`, showcasing how ES6 method properties can be used within object literals for more concise method definitions.

**9-getFullBudget.js:** 
- `getFullBudgetObject`: Demonstrates the use of ES6 method properties in objects, simplifying the definition of methods that format financial figures into different currencies.

### Task 10

**10-main.js:** Tests the `appendToEachArrayValue` function by demonstrating its ability to prepend a string to each element of an array.

**10-loops.js:** 
- `appendToEachArrayValue`: Refactored to utilize the ES6 `for...of` loop and `const` for iterating over array elements. This function modifies each element of the array by appending a specified string, illustrating a more modern and efficient approach to array manipulation.

### Task 11

**11-main.js:** Tests the `createEmployeesObject` function by passing department names and employee lists to see if it correctly maps them into an object.

**11-createEmployeesObject.js:** 
- `createEmployeesObject`: Constructs objects dynamically using computed property names, allowing the department names to be used as keys and the corresponding employee arrays as values. This illustrates a practical use of ES6 features to handle real-world data structuring tasks.

### Task 12

**12-main.js:** Demonstrates the functionality of the `createReportObject` by using it to manage and report on employee department data dynamically.

**12-createReportObject.js:** 
- `createReportObject`: Enhances the structure of employee reporting objects by using ES6 method properties and `this` keyword to access and manipulate internal state, demonstrating use of ES6 for object-oriented programming.

## Installation
Clone this repository and navigate to the project directory.

```
git clone https://github.com/ThatsVie/atlas-web_back_end.git
```

```
cd ES6_basic
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
To run the example code from 0-main.js and observe the usage of const and let:
```
npm run dev 0-main.js
```
When npm run dev 0-main.js is run, it uses npx babel-node to execute the 0-main.js script. Babel-node is a part of Babel, which compiles ES6+ JavaScript to backward-compatible JavaScript. This ensures that even if newer syntax features are used (like const and let), the code runs smoothly on environments that might only support older JavaScript versions.

![image](https://github.com/ThatsVie/atlas-web_back_end/assets/143755961/c234e973-5148-467c-b22a-47791cc5c822)

This output demonstrates the usage of `const` and `let` within JavaScript functions. The `const` keyword is shown to enforce immutability, ensuring the variable's value remains unchanged throughout its scope, while `let` allows for reassignment and shows a more flexible variable scope suitable for values that may need to be modified.

### Task 1
To run the code from `1-main.js` and see the effects of proper block scoping:
```
npm run dev 1-main.js
```
![image](https://github.com/ThatsVie/atlas-web_back_end/assets/143755961/9dc7228b-4109-4177-8475-a9a0f8de576e)


**Output:**
When true is passed it outputs "true false" from within the block, then [false, true] from the function return.
When false is passed it directly outputs [false, true] as the block does not execute, showing the initial values are unchanged.

This output demonstrates that the changes to `task` and `task2` within the conditional block do not affect the function scope variables due to the proper use of `const`. The function's return value remains consistent regardless of the input parameter, showing how `const` and `let` can be used to manage variable scopes effectively within blocks, preventing unintended overwrites and ensuring that variables retain their values as expected across different execution contexts.

### Task 2
To run the code from 2-main.js and see the application of arrow syntax in class methods:
```
npm run dev 2-main.js
```
![image](https://github.com/ThatsVie/atlas-web_back_end/assets/143755961/cf9df8d0-000a-4e77-aa3d-10b44f23e948)

Outputs "[ 'SOMA', 'Union Square', 'Noe Valley' ]", indicating that the arrow function retains the this context correctly.

This confirms that the `addNeighborhood` method correctly modifies the object's `sanFranciscoNeighborhoods` property. Arrow functions capture the `this` context from the enclosing context, in this case, the instance of `getNeighborhoodsList`. Unlike traditional functions, there is no need to assign `this` to another variable (`self`) to access it within callbacks, simplifying the code and making it more maintainable.

### Task 3
To test the function from 3-main.js and verify the effectiveness of default parameters:
```
npm run dev 3-main.js
```

![image](https://github.com/ThatsVie/atlas-web_back_end/assets/143755961/77f641fc-3c39-462a-999b-a115772fb099)

Outputs:

142 when called with one argument (34), using default values for the other two parameters.

56 when called with two arguments (34, 3), using the default value for the third parameter.

41 when all parameters are provided (34, 3, 4).

This shows that the `getSumOfHoods` function correctly calculates the sum of its parameters.

### Task 4
To test the `returnHowManyArguments` function

```
npm run dev 4-main.js
```

![image](https://github.com/ThatsVie/atlas-web_back_end/assets/143755961/40074da0-6191-436a-b3ba-9c3076058fcb)

Outputs "1" and "4", demonstrating the function's ability to count how many arguments it receives.

### Task 5
Demonstrates the use of spread syntax to dynamically combine multiple arrays and strings into a single array.
```
npm run dev 5-main.js
```
![image](https://github.com/ThatsVie/atlas-web_back_end/assets/143755961/85e5d40e-94fa-4520-886b-7fe6a561f7c4)


Output:

When calling concatArrays(['a', 'b'], ['c', 'd'], 'Hello'), the output will be: [ 'a', 'b', 'c', 'd', 'H', 'e', 'l', 'l', 'o' ], demonstrating how arrays and string characters are combined.

### Task 6
Demonstrates template literals in creating detailed and formatted strings by integrating variables directly within the text.

```
npm run dev 6-main.js
```

This command runs the getSanFranciscoDescription function, which uses template literals to construct a complex string that includes several variables for a clear description.

![image](https://github.com/ThatsVie/atlas-web_back_end/assets/143755961/6606d433-13e0-4d3f-9354-535c8164dca5)

Displays a detailed description, using variables to show income, GDP, and per capita data dynamically integrated into the text.

### Task 7

Demonstrates the simplification of object creation using ES6 object literal enhancements.

```
npm run dev 7-main.js
```

This command runs the getBudgetObject function, illustrating how ES6 allows for a more concise object definition when property names match the variable names used for their values.

![image](https://github.com/ThatsVie/atlas-web_back_end/assets/143755961/cc40ba9e-c95a-4241-84e4-d174e6b99739)

Output:

The output will display a budget object, e.g., { income: 400, gdp: 700, capita: 900 }, confirming that the object has been created with the correct properties and values.


### Task 8

Illustrates the dynamic generation of object properties using computed property names, based on runtime values such as the current year.
```
npm run dev 8-main.js
```

This command runs the getBudgetForCurrentYear function, demonstrating the effective use of computed property names to incorporate the current year into property keys dynamically.

![image](https://github.com/ThatsVie/atlas-web_back_end/assets/143755961/ca7b0da6-1139-4778-9498-4bdba4c88065)

Output:

Shows the dynamically generated budget object with properties such as 'income-2021', 'gdp-2021', and 'capita-2021', where '2021' would be replaced by the current year, verifying that the properties are created correctly based on the execution year.

### Task 9

Demonstrates the utilization of ES6 method properties to streamline method definition within an object.
```
npm run dev 9-main.js
```
This command runs the getFullBudgetObject function, illustrating the effective use of ES6 method properties to define methods that convert income figures into dollars and euros.

![image](https://github.com/ThatsVie/atlas-web_back_end/assets/143755961/c40da33e-41c6-4f37-aea9-917ad5cb71ab)


Outputs the formatted income values, e.g., "$20" and "20 euros", verifying that the methods are correctly attached to the object and functional.


### Task 10

Demonstrates the refactoring of an array manipulation function to use ES6 `for...of` loop and `const`.
```
npm run dev 10-main.js
```
This command runs the appendToEachArrayValue function, showing how each array item is modified by prefixing a string.

![image](https://github.com/ThatsVie/atlas-web_back_end/assets/143755961/318ea3f6-10a4-4e62-ad22-61a814fb6335)

Shows the modified array, [ 'correctly-appended', 'correctly-fixed', 'correctly-displayed' ], verifying the function’s ability to efficiently prepend text to each array element.

### Task 11

Demonstrates how to dynamically create objects with department names as keys and employee arrays as values, using computed property names.
```
npm run dev 11-main.js
```
This command runs the createEmployeesObject function, which creates an object mapping a department to its employees based on inputs.

![image](https://github.com/ThatsVie/atlas-web_back_end/assets/143755961/42adbf8b-1988-4ece-89ee-c76678863c23)

Prints an object like { Software: [ 'Bob', 'Sylvie' ] }, demonstrating that the function correctly assigns department names as keys and lists employees under them. This output confirms the function's ability to dynamically structure data based on given parameters.

### Task 12
Showcases the use of encapsulated methods within an object to operate on internal state for dynamic data reporting.
```
npm run dev 12-main.js
```
Runs the createReportObject function, illustrating how the internal methods utilize the object's state (this) to perform operations like counting departments.

![image](https://github.com/ThatsVie/atlas-web_back_end/assets/143755961/c184cb4e-5dc5-4494-b4e4-74f4e858ece7)

Displays structured employee data by departments and provides a count of departments, verifying the object’s methods correctly access and manipulate the internal state.


