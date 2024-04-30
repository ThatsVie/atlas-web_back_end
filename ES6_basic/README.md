# ES6 Basic

## Learning Objectives

## Tasks Overview

**Task 0:** Refactor JavaScript functions to utilize ES6 `const` and `let` for improved scoping and maintainability, demonstrating best practices in variable declaration.

**Task 1:** Modify `taskBlock` to prevent variable hoisting issues by using `const` within conditional blocks, showcasing block-level scoping with ES6.

**Task 2:** Refactor an object method to use ES6 arrow syntax, illustrating how arrow functions maintain the lexical scope of `this`, improving method definitions within object constructors.

**Task 3:** Simplify the function `getSumOfHoods` by using default parameters to condense its internals into one line, demonstrating efficient function setup and parameter handling.

**Task 4:** Modify a function to utilize ES6 rest parameters for dynamically counting and returning the number of arguments passed to it.

**Task 5:** Use the spread syntax to concatenate two arrays and each character of a string into one array, showcasing the versatility of spread operators in handling multiple data types.

**Task 6:** Enhance string construction using ES6 template literals to cleanly integrate variables into text, improving readability and maintainability.

**Task 7:** Simplify object creation using enhanced object literal syntax, reducing redundancy by utilizing property value shorthand.

**Task 8:** Demonstrate the use of computed property names in objects to dynamically construct property keys based on runtime values, showcasing further flexibility in object creation.

## File Overview

**0-main.js:** Imports and tests functions from 0-constants.js by executing them and displaying their combined outputs.

**0-constants.js:** 
- `taskFirst`: Demonstrates the immutable variable declaration with `const`.
- `getLast`: Provides a reusable component for string manipulation.
- `taskNext`: Illustrates mutable variable management with `let` in a dynamic context.

**1-main.js:** Tests the taskBlock function by executing it with different boolean values and displays the results to demonstrate the effect of the conditional logic.

**1-block-scoped.js:** 
- Demonstrates the use of `const` to maintain block-level scope and prevent hoisting issues within conditional blocks.

**2-main.js:** Executes the `getNeighborhoodsList` constructor and its method `addNeighborhood` to demonstrate the application of arrow functions in methods.

**2-arrow.js:** 
- `getNeighborhoodsList`: A constructor function that initializes an object with a list of neighborhoods and includes a method to add new items.
- `addNeighborhood`: An arrow function method added to `getNeighborhoodsList` to demonstrate the lexical scoping of `this`.

**3-main.js:** Executes `getSumOfHoods` demonstrating the use of default parameters in function condensation.

**3-default-parameter.js:** 
- `getSumOfHoods`: Simplifies parameter handling by using default values, demonstrating a streamlined approach to function design.

**4-main.js:** Demonstrates the use of the rest parameter syntax by executing `returnHowManyArguments` with various sets of arguments.

**4-rest-parameter.js:** 
- `returnHowManyArguments`: Uses rest parameters to dynamically handle an arbitrary number of arguments and returns their count.

**5-main.js:** Executes `concatArrays` function demonstrating the use of spread syntax to merge arrays and string characters.

**5-spread-operator.js:** 
- `concatArrays`: Combines two arrays and the characters of a string into a single array using the spread syntax.

**6-main.js:** Executes `getSanFranciscoDescription` showcasing the use of template literals for string interpolation.

**6-string-interpolation.js:** 
- `getSanFranciscoDescription`: Uses template literals to incorporate variables and create a descriptive text about San Francisco's economic figures, demonstrating clear and concise string formatting.

**7-main.js:** Demonstrates the functionality of `getBudgetObject`, showcasing the use of ES6 property shorthand in object literals.

**7-getBudgetObject.js:** 
- `getBudgetObject`: Creates and returns a budget object using property shorthand to streamline the assignment of properties when the variable names and property names are identical.

**8-main.js:** Executes `getBudgetForCurrentYear`, showcasing how to dynamically construct object properties using computed names based on current year data.

**8-getBudgetCurrentYear.js:** 
- `getBudgetForCurrentYear`: Illustrates the dynamic construction of object properties using computed property names, integrating runtime values into object keys.


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

Executes functions from `0-constants.js` to showcase variable management with `const` and `let`.

```
npm run dev 0-main.js
```
When npm run dev 0-main.js is run, it uses npx babel-node to execute the 0-main.js script. Babel-node is a part of Babel, which compiles ES6+ JavaScript to backward-compatible JavaScript. This ensures that even if newer syntax features are used (like const and let), the code runs smoothly on environments that might only support older JavaScript versions.
![image](https://github.com/ThatsVie/atlas-web_back_end/assets/143755961/c234e973-5148-467c-b22a-47791cc5c822)


**Output:** "I prefer const when I can. But sometimes let is okay" illustrates how the functions taskFirst and taskNext handle string values and return them in a combined format.

### Task 1

Test block scoping with const to validate how conditional blocks isolate variable scope.
```
npm run dev 1-main.js
```
![image](https://github.com/ThatsVie/atlas-web_back_end/assets/143755961/9dc7228b-4109-4177-8475-a9a0f8de576e)


**Output:**
When true is passed it outputs "true false" from within the block, then [false, true] from the function return.
When false is passed it directly outputs [false, true] as the block does not execute, showing the initial values are unchanged.

### Task 2
Demonstrates the use of ES6 arrow functions within object methods to maintain the lexical context of this.
```
npm run dev 2-main.js
```
![image](https://github.com/ThatsVie/atlas-web_back_end/assets/143755961/cf9df8d0-000a-4e77-aa3d-10b44f23e948)

Outputs "[ 'SOMA', 'Union Square', 'Noe Valley' ]", indicating that the arrow function retains the this context correctly.

### Task 3
Illustrates the use of default parameters to simplify function logic in getSumOfHoods
```
npm run dev 3-main.js
```

![image](https://github.com/ThatsVie/atlas-web_back_end/assets/143755961/77f641fc-3c39-462a-999b-a115772fb099)

Prints "142", "56", and "41" for different function calls, showing how default parameters handle missing arguments.

### Task 4
Shows how the rest parameter can be used to handle any number of input arguments dynamically.

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

### Task 10

### Task 11

### Task 12
