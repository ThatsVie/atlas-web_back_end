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
Use the spread syntax to concatenate two arrays and each character of a string into one array, showing the versatility of spread operators in handling multiple data types.

### Task 6
Modify the function `getSanFranciscoDescription` to use ES6 template literals for more readable string concatenation. The task demonstrates the replacement of traditional string concatenation with template literals, which allows for direct insertion of variables into strings.

### Task 7
Simplify object initialization in JavaScript using ES6's object property value shorthand. The function `getBudgetObject` is modified to utilize this shorthand, making the code more concise and readable when the variable names are the same as the object keys.

### Task 8
Use ES6 computed property names to dynamically construct object keys. This approach enhances flexibility and readability, particularly when keys depend on runtime values.

### Task 9
Implement ES6 method properties in object definitions to simplify and enhance the readability of method declarations within objects.

### Task 10
Refactor the `appendToEachArrayValue` function to use ES6 `for...of` loop and `const` for iterating through arrays, for more efficient code.

### Task 11
Create a function that dynamically generates objects with department names as keys and lists of employees as values, demonstrating the use of computed property names for object keys.

### Task 12 
Enhance the `createReportObject` function to use internal state with `this` for method operations. 

### Task 13
This task involves writing a function named `createIteratorObject` that accepts a report object (produced by the `createReportObject` function).

### Task 14


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

`5-main.js`: Executes `concatArrays` function demonstrating the use of spread syntax to merge arrays and string characters.

`5-spread-operator.js`: Contains the `concatArrays` function that uses spread syntax to merge two arrays and expand each character of a string into a single array.
  
### Task 6

`6-main.js`: Executes `getSanFranciscoDescription` showcasing the use of template literals for string interpolation.

`6-string-interpolation.js`:  Contains the function `getSanFranciscoDescription`, which constructs a description of San Francisco's financial statistics using template literals for string creation.

### Task 7

`7-main.js`: Demonstrates the functionality of `getBudgetObject`, showing the use of ES6 property shorthand in object literals.

`7-getBudgetObject.js`: Features the function `getBudgetObject`, which constructs a budget object using the shorthand syntax, simplifying the assignment of variables to object properties.

### Task 8

`8-main.js`: Executes `getBudgetForCurrentYear`, showing how to dynamically construct object properties using computed names based on current year data.

`8-getBudgetCurrentYear.js`: Implements the `getBudgetForCurrentYear` function, which dynamically constructs an object with keys based on the current year, making use of computed property names.

### Task 9

`9-main.js`:Executes `getFullBudgetObject`, showing how ES6 method properties can be used within object literals for more concise method definitions.

`9-getFullBudget.js`: Enhances a basic budget object with methods to format financial values. 

### Task 10
`10-main.js`: Tests the `appendToEachArrayValue` function by demonstrating its ability to prepend a string to each element of an array.

`10-loops.js`:  Contains the function `appendToEachArrayValue`, which demonstrates the use of ES6's `for...of` loop and enhanced variable scoping with `const` to better manage collections and iterations.

### Task 11
`11-main.js`: Tests the `createEmployeesObject` function by passing department names and employee lists to see if it correctly maps them into an object.

`11-createEmployeesObject.js:  Contains the function `createEmployeesObject`, which is an example of how to dynamically construct objects with properties determined at runtime. This is particularly useful for handling data structures where keys are determined by external inputs.

### Task 12
`12-main.js`: Demonstrates the functionality of the `createReportObject` by using it to manage and report on employee department data dynamically.

`12-createReportObject.js`:  This file defines `createReportObject`, a function that encapsulates employee data and provides a method to count the number of departments. This exemplifies the use of ES6 features to create more interactive and self-contained modules.

### Task 13
`100-main.js`: This script serves as a test for the functionality provided by the `createIteratorObject` function.

`100-createIteratorObject.js`: This file contains the `createIteratorObject` function, which creates an iterator for iterating through all employees listed under any department. It utilizes ES6 features like the iterator protocol and computed property names.

### Task 14

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
Here's how you can test the concatArrays function to understand how it merges arrays and spreads the characters of a string:
```
npm run dev 5-main.js
```
![image](https://github.com/ThatsVie/atlas-web_back_end/assets/143755961/85e5d40e-94fa-4520-886b-7fe6a561f7c4)

This output demonstrates that the function successfully concatenates two arrays `['a', 'b']` and `['c', 'd']`, and spreads each character of the string 'Hello' into the resulting array. Each element and character is listed as a separate entry, showing the use of spread syntax in array concatenation and string splitting.

### Task 6
To see how template literals enhance readability and maintainability, run the following command:
```
npm run dev 6-main.js
```

This command runs the getSanFranciscoDescription function, which uses template literals to construct a complex string that includes several variables for a clear description.

![image](https://github.com/ThatsVie/atlas-web_back_end/assets/143755961/6606d433-13e0-4d3f-9354-535c8164dca5)

Displays a detailed description, using variables to show income, GDP, and per capita data dynamically integrated into the text.

### Task 7
To demonstrate the functionality of the updated `getBudgetObject` function, execute the following command:
```
npm run dev 7-main.js
```

![image](https://github.com/ThatsVie/atlas-web_back_end/assets/143755961/cc40ba9e-c95a-4241-84e4-d174e6b99739)

Output:

The output will display a budget object, e.g., { income: 400, gdp: 700, capita: 900 }, confirming that the object has been created with the correct properties and values.

This shows how the function returns a budget object with properties directly assigned from the arguments passed to the function. The use of shorthand syntax simplifies the object creation process, enhancing the clarity and brevity of the code.

### Task 8
The `getBudgetForCurrentYear` function demonstrates how it dynamically assigns properties based on the current year:
```
npm run dev 8-main.js
```

This command runs the getBudgetForCurrentYear function, demonstrating the effective use of computed property names to incorporate the current year into property keys dynamically.

![image](https://github.com/ThatsVie/atlas-web_back_end/assets/143755961/ca7b0da6-1139-4778-9498-4bdba4c88065)

Output:

Shows the dynamically generated budget object with properties such as 'income-2021', 'gdp-2021', and 'capita-2021', where '2021' would be replaced by the current year.

This output indicates that the function successfully creates keys that reflect the year at the time of execution, incorporating the values provided to it. This technique is useful in situations where the structure of an object needs to adapt to changing conditions or contexts.

### Task 9
The `getFullBudgetObject` function demonstrates a practical use of ES6 enhancements to object literals by adding methods directly within the object definition:
```
npm run dev 9-main.js
```
This command runs the `getFullBudgetObject` function, showing the effective use of ES6 method properties to define methods that convert income figures into dollars and euros.

![image](https://github.com/ThatsVie/atlas-web_back_end/assets/143755961/c40da33e-41c6-4f37-aea9-917ad5cb71ab)


Outputs the formatted income values, e.g., "$20" and "20 euros". 

This shows how the methods `getIncomeInDollars` and `getIncomeInEuros`, are effectively formatting the income values into respective currencies. 

### Task 10
The function `appendToEachArrayValue` is used to prepend a string to each element in an array, demonstrating the practical use of `for...of` loops for straightforward array manipulations:
```
npm run dev 10-main.js
```
This command runs the appendToEachArrayValue function, showing how each array item is modified by prefixing a string.

![image](https://github.com/ThatsVie/atlas-web_back_end/assets/143755961/318ea3f6-10a4-4e62-ad22-61a814fb6335)

This shows how each element in the initial array is processed to include the prefix "correctly-", showing an efficient way to manipulate and return arrays with enhanced readability and reduced potential for bugs that come with older ES5 code practices.

### Task 11
The function `createEmployeesObject` is used to map department names to employee lists dynamically, showing the flexibility of ES6 in handling data structures:
```
npm run dev 11-main.js
```
This command runs the `createEmployeesObject` function, which creates an object mapping a department to its employees based on inputs.

![image](https://github.com/ThatsVie/atlas-web_back_end/assets/143755961/42adbf8b-1988-4ece-89ee-c76678863c23)

Prints an object like { Software: [ 'Bob', 'Sylvie' ] }.

This output confirms that the function effectively creates an object with a department name as the key and an array of employees as the value, demonstrating a common pattern in organizing and structuring data within applications. This approach is especially useful in applications where data organization and retrieval efficiency are important, such as in human resources or team management software.

### Task 12
This function is used to generate a comprehensive report object from an employee list, featuring dynamic interaction through its embedded methods:

```
npm run dev 12-main.js
```
Runs the `createReportObject` function, showing how the internal methods utilize the object's state (`this`) to perform operations like counting departments.

![image](https://github.com/ThatsVie/atlas-web_back_end/assets/143755961/c184cb4e-5dc5-4494-b4e4-74f4e858ece7)

This output displays the structured grouping of employees by department and the total number of departments, showing the practical use of modern JavaScript techniques to manage and interact with complex data structures effectively.

### Task 13
To execute the function `createIteratorObject` and display each employee's name across different departments, you can use the following command:
```
npm run dev 100-main.js
```
![image](https://github.com/ThatsVie/atlas-web_back_end/assets/143755961/8978aef2-3833-4439-8cba-a3d1fe55299f)


Each name printed to the console represents an employee in various departments processed by the iterator. This output confirms that the iterator successfully traverses all employees in the given structure.

### Task 14
