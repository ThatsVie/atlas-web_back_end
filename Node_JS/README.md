# Node Express

## Project Overview

This project is focused on building a web server using Node.js and Express.js, following modern JavaScript practices. The project also involves setting up a development environment with tools like ESLint, Babel, and Nodemon to enhance development speed and code quality.

## Resources

- [Node JS Getting Started](https://nodejs.org/en/learn/getting-started/introduction-to-nodejs)
- [Process API](https://node.readthedocs.io/en/latest/api/process/)
- [Child Process](https://nodejs.org/api/child_process.html)
- [Express Getting Started](https://expressjs.com/en/starter/installing.html)
- [Mocha Documentation](https://mochajs.org/)
- [Nodemon Documentation](https://github.com/remy/nodemon#nodemon)

## Learning Objectives

- Run JavaScript using NodeJS
- Use NodeJS modules
- Use specific NodeJS modules to read files
- Use process to access command line arguments and the environment
- Create a small HTTP server using NodeJS
- Create a small HTTP server using ExpressJS
- Create advanced routes with ExpressJS
- Use ES6 with NodeJS and Babel-node
- Use Nodemon to develop faster

## Requirements

- Allowed editors: vi, vim, emacs, Visual Studio Code
- All files will be interpreted/compiled on Ubuntu 18.04 LTS using Node (version 12.x.x)
- All files should end with a new line
- A README.md file at the root of the project folder is mandatory
- Your code should use the `.js` extension
- Code will be tested using Jest (`npm run test`)
- Code will be linted using ESLint (`npm run lint`)
- Code needs to pass all tests and linting (`npm run full-test`)
- All functions/classes must be exported using the format: `module.exports = myFunction;`

## Provided Files

<details>
  <summary><strong>database.csv</strong></summary>

```csv
firstname,lastname,age,field
Johann,Kerbrou,30,CS
Guillaume,Salou,30,SWE
Arielle,Salou,20,CS
Jonathan,Benou,30,CS
Emmanuel,Turlou,40,CS
Guillaume,Plessous,35,CS
Joseph,Crisou,34,SWE
Paul,Schneider,60,SWE
Tommy,Schoul,32,SWE
Katie,Shirou,21,CS
```
</details>

<details>
  <summary><strong>package.json</strong></summary>

```json
{
  "name": "node_js_basics",
  "version": "1.0.0",
  "description": "",
  "main": "index.js",
  "scripts": {
    "lint": "./node_modules/.bin/eslint",
    "check-lint": "lint [0-9]*.js",
    "test": "./node_modules/mocha/bin/mocha --require babel-register --exit",
    "dev": "nodemon --exec babel-node --presets babel-preset-env ./server.js ./database.csv"
  },
  "author": "",
  "license": "ISC",
  "dependencies": {
    "chai-http": "^4.3.0",
    "express": "^4.17.1"
  },
  "devDependencies": {
    "babel-cli": "^6.26.0",
    "babel-preset-env": "^1.7.0",
    "nodemon": "^2.0.2",
    "eslint": "^6.4.0",
    "eslint-config-airbnb-base": "^14.0.0",
    "eslint-plugin-import": "^2.18.2",
    "eslint-plugin-jest": "^22.17.0",
    "chai": "^4.2.0",
    "mocha": "^6.2.2",
    "request": "^2.88.0",
    "sinon": "^7.5.0"
  }
}
```
</details>

<details>
  <summary><strong>babel.config.js</strong></summary>

```js
module.exports = {
  presets: [
    [
      '@babel/preset-env',
      {
        targets: {
          node: 'current',
        },
      },
    ],
  ],
};
```
</details>

<details>
  <summary><strong>.eslintrc.js</strong></summary>

```js
module.exports = {
  env: {
    browser: false,
    es6: true,
    jest: true,
  },
  extends: [
    'airbnb-base',
    'plugin:jest/all',
  ],
  globals: {
    Atomics: 'readonly',
    SharedArrayBuffer: 'readonly',
  },
  parserOptions: {
    ecmaVersion: 2018,
    sourceType: 'module',
  },
  plugins: ['jest'],
  rules: {
    'max-classes-per-file': 'off',
    'no-underscore-dangle': 'off',
    'no-console': 'off',
    'no-shadow': 'off',
    'no-restricted-syntax': [
      'error',
      'LabeledStatement',
      'WithStatement',
    ],
  },
  overrides: [
    {
      files: ['*.js'],
      excludedFiles: 'babel.config.js',
    }
  ]
};
```
</details>

## Tasks and Usage

### Task 0: Executing Basic JavaScript with Node JS

This task involves creating a JavaScript function using Node.js that prints a string argument to STDOUT.

<details>
  <summary><strong>Curriculum Instruction</strong></summary>

In the file 0-console.js, create a function named displayMessage that prints in STDOUT the string argument.


</details>

<details>
  <summary><strong>Steps and Code Implementation</strong></summary>

1. **Create the File `0-console.js`**: 
   
```javascript
  // Prints a message to the console
function displayMessage(message) {
    console.log(message);
}


module.exports = displayMessage;



```

2. **Create the `0-main.js` for Testing**:  
   To test the function, create a `0-main.js` file in the same directory:
   
   ```javascript
   // 0-main.js
   const displayMessage = require('./0-console');

   displayMessage("Hello NodeJS!");
   ```

3. **Run the Program**:  
   In your terminal, navigate to the `Node_JS` directory and run:
   ```bash
   node 0-main.js
   ```

   **Expected Output**:
   ```bash
   Hello NodeJS!
   ```

</details>

<details>
  <summary><strong>Explanation: Who, What, Where, When, Why, How</strong></summary>

- **What**: This task involves creating a simple JavaScript function that prints any given string to the console using Node.js.
- **Where**: The function is written in a file called `0-console.js` and is called from another file (`0-main.js`) to test its functionality.
- **Why**: This task demonstrates how to create and export a basic function in Node.js, as well as how to use `console.log()` to print messages to the console.
- **How**: The function is written in JavaScript, using `console.log()` to print the message, and is exported using `module.exports`.
- **Who**: This task is relevant for anyone learning Node.js basics, especially how to work with functions and modules.
- **When**: This function can be executed anytime by running `node 0-main.js` in the terminal.

</details>


### Task 1: Using Process stdin

This task involves creating a Node.js program that takes input from the user via the command line and processes it.

<details>
  <summary><strong>Curriculum Instruction</strong></summary>

- Create a program named `1-stdin.js` that will be executed via the command line.
- It should display the message `Welcome to Holberton School, what is your name?` (followed by a new line).
- The user should input their name on a new line.
- The program should display `Your name is: INPUT`.
- When the user ends the program, it should display `This important software is now closing` (followed by a new line).

</details>

<details>
  <summary><strong>Steps and Code Implementation</strong></summary>

1. **Create the File `1-stdin.js`**:  


   ```javascript
   // Welcomes the user and prompts for their name.
   console.log('Welcome to Holberton School, what is your name?');

   // Listen for readable input from the user
   process.stdin.on('readable', () => {
     const name = process.stdin.read();
     if (name !== null) {
       // Print the user's name
       process.stdout.write(`Your name is: ${name}`);
     }
   });

   // On the end of input (when piped input is used), print the closing message.
   process.stdin.on('end', () => {
     console.log('This important software is now closing');
   });
   ```

2. **Test the Program**:
   - Run the program from the command line and input your name.
   - Alternatively, use `echo` to pipe input into the program.

   **Examples**:
   ```bash
   node 1-stdin.js
   ```

   ```bash
   echo "John" | node 1-stdin.js
   ```

3. **Expected Output**:
   - For manual input:
     ```bash
     Welcome to Holberton School, what is your name?
     Bob
     Your name is: Bob
     ```
   - For piped input:
     ```bash
     Welcome to Holberton School, what is your name?
     Your name is: John
     This important software is now closing
     ```

</details>

<details>
  <summary><strong>Troubleshooting</strong></summary>

**What We Tried**:
1. **Initial Approach**: 
   We initially tried using `process.stdin.on('data')` to handle input and output. While this approach worked, it continued listening for additional input even after the name was entered, causing multiple outputs and unintended behavior.

2. **Why It Didn't Work**:
   - The program kept listening for more input even after the user's name was entered.
   - This resulted in the `Your name is: ...` message being printed repeatedly if the user didn't manually end the program.
   
3. **Final Approach**:
   We switched to using `process.stdin.on('readable')`, which correctly handles input without looping or repeating the output. Additionally, we used `process.stdin.on('end')` to detect when the input stream ends (for piped input) and print the closing message in that case.

4. **Why This Works**:
   - The `readable` event only triggers when there is actual input to be processed, preventing the program from listening indefinitely.
   - The `end` event triggers when piped input ends, ensuring the closing message is only displayed in that case.

</details>

<details>
  <summary><strong>Explanation: Who, What, Where, When, Why, How</strong></summary>

- **What**: This task involves creating a program that accepts user input from the command line and displays it, then gracefully exits with a closing message.
- **Where**: The program is executed from the terminal, and input is provided via the terminal as well.
- **Why**: This task helps you understand how to handle user input and program termination in Node.js.
- **How**: Using `process.stdin.on('readable')`, the program listens for input, processes it, and exits cleanly. The `end` event handles piped input cases to print the closing message.
- **Who**: This is useful for developers working with command-line applications in Node.js.
- **When**: This function can be executed at any time from the command line to accept user input.

</details>


### Task 2: Reading a File Synchronously with Node JS

This task involves creating a function that reads a file synchronously and processes student data from a CSV file.

<details>
  <summary><strong>Curriculum Instruction</strong></summary>

- Create a function `countStudents` that takes a path as an argument and reads a file synchronously.
- If the file does not exist, it should throw an error with the message `Cannot load the database`.
- The function should log the total number of students and the number of students per field, followed by the list of first names in each field.

</details>

<details>
  <summary><strong>Steps and Code Implementation</strong></summary>

1. **Create the File `2-read_file.js`**:  
   
   ```javascript
   /**
    * Defines function countStudents that reads a CSV file,
    * counts the total number of students, and logs the number of students 
    * in each field. If the file cannot be loaded, 
    * it throws an error with the message "Cannot load the database."
    */
   const fs = require('fs');

   // Function to count students from a CSV file
   function countStudents(path) {
     try {
       // Read file synchronously
       const data = fs.readFileSync(path, 'utf-8').trim();
       const lines = data.split('\n');

       // Remove empty lines and the header
       const students = lines.filter((line, index) => line.trim() !== '' && index > 0);

       console.log(`Number of students: ${students.length}`);

       const fields = {};

       // Process each student line
       students.forEach((student) => {
         const [firstname, lastname, age, field] = student.split(',');

         if (!fields[field]) {
           fields[field] = [];
         }
         fields[field].push(firstname);
       });

       // Log the number of students in each field and their names
       for (const [field, names] of Object.entries(fields)) {
         console.log(`Number of students in ${field}: ${names.length}. List: ${names.join(', ')}`);
       }
     } catch (error) {
       // If an error occurs (file not found), throw an error
       throw new Error('Cannot load the database');
     }
   }

   module.exports = countStudents;
   ```

2. **Test the Program**:
   - Test using the `2-main_0.js` and `2-main_1.js` files provided.

   **Content of `2-main_0.js`** (for a non-existent file):
   ```javascript
   const countStudents = require('./2-read_file');

   countStudents('nope.csv');
   ```

   **Content of `2-main_1.js`** (for the valid `database.csv`):
   ```javascript
   const countStudents = require('./2-read_file');

   countStudents('database.csv');
   ```

3. **Expected Output**:
   - For a non-existent file (`nope.csv`):
     ```bash
     Error: Cannot load the database
     ```
   - For a valid file (`database.csv`):
     ```bash
     Number of students: 10
     Number of students in CS: 6. List: Johann, Arielle, Jonathan, Emmanuel, Guillaume, Katie
     Number of students in SWE: 4. List: Guillaume, Joseph, Paul, Tommy
     ```

</details>


<details>
  <summary><strong>Explanation: Who, What, Where, When, Why, How</strong></summary>

- **What**: This task involves reading a CSV file synchronously and counting the number of students, along with the number of students in each field.
- **Where**: The program is executed from the terminal and reads the CSV file from the provided path.
- **Why**: This task helps understand how to handle synchronous file reading and parsing of CSV data in Node.js.
- **How**: The `fs.readFileSync()` method is used to read the file, and the data is processed by splitting the lines and categorizing students by their fields.
- **Who**: This task is relevant for developers working with file systems in Node.js.
- **When**: This function can be executed anytime to read a student database file and log the student data.

</details>

### Task 3: Reading a File Asynchronously with Node JS

This task involves creating a function that reads a file asynchronously and processes student data from a CSV file.

<details>
  <summary><strong>Curriculum Instruction</strong></summary>

- Create a function `countStudents` that takes a path as an argument and reads a file asynchronously.
- If the file does not exist, it should throw an error with the message `Cannot load the database`.
- The function should return a Promise.
- If the file is available, it should log the total number of students and the number of students per field, followed by the list of first names in each field.

</details>

<details>
  <summary><strong>Steps and Code Implementation</strong></summary>

1. **Create the File `3-read_file_async.js`**:  
   Inside the `Node_JS` directory, create the `3-read_file_async.js` file:
   
   ```javascript
   const fs = require('fs').promises;

   // Asynchronous function to count students from a CSV file
   function countStudents(path) {
     return fs.readFile(path, 'utf-8')
       .then((data) => {
         const lines = data.trim().split('\n');

         // Remove empty lines and the header
         const students = lines.filter((line, index) => line.trim() !== '' && index > 0);

         console.log(`Number of students: ${students.length}`);

         const fields = {};

         // Process each student line
         students.forEach((student) => {
           const [firstname, lastname, age, field] = student.split(',');

           if (!fields[field]) {
             fields[field] = [];
           }
           fields[field].push(firstname);
         });

         // Log the number of students in each field and their names
         for (const [field, names] of Object.entries(fields)) {
           console.log(`Number of students in ${field}: ${names.length}. List: ${names.join(', ')}`);
         }
       })
       .catch(() => {
         throw new Error('Cannot load the database');
       });
   }

   module.exports = countStudents;
   ```

2. **Test the Program**:
   - Use the following commands to test the function with the `3-main_0.js` and `3-main_1.js` files.

   **Content of `3-main_0.js`** (for a non-existent file):
   ```javascript
   const countStudents = require('./3-read_file_async');

   countStudents('nope.csv')
     .then(() => {
       console.log('Done!');
     })
     .catch((error) => {
       console.log(error);
     });
   ```

   **Content of `3-main_1.js`** (for the valid `database.csv`):
   ```javascript
   const countStudents = require('./3-read_file_async');

   countStudents('database.csv')
     .then(() => {
       console.log('Done!');
     })
     .catch((error) => {
       console.log(error);
     });
   console.log('After!');
   ```

3. **Run the Program**:
   - For the non-existent file, use this command:
     ```bash
     node 3-main_0.js
     ```
   - For the valid file, use this command:
     ```bash
     node 3-main_1.js
     ```

4. **Expected Output**:
   - For a non-existent file (`nope.csv`):
     ```bash
     vie@ThatsVie:~/atlas-web_back_end/Node_JS$ node 3-main_0.js
     Error: Cannot load the database
         at /home/vie/atlas-web_back_end/Node_JS/3-read_file_async.js:32:13
     vie@ThatsVie:~/atlas-web_back_end/Node_JS$
     ```
   - For a valid file (`database.csv`):
     ```bash
     vie@ThatsVie:~/atlas-web_back_end/Node_JS$ node 3-main_1.js
     After!
     Number of students: 10
     Number of students in CS: 6. List: Johann, Arielle, Jonathan, Emmanuel, Guillaume, Katie
     Number of students in SWE: 4. List: Guillaume, Joseph, Paul, Tommy
     Done!
     vie@ThatsVie:~/atlas-web_back_end/Node_JS$
     ```

</details>


<details>
  <summary><strong>Explanation: Who, What, Where, When, Why, How</strong></summary>

- **What**: This task involves reading a CSV file asynchronously and counting the number of students, along with the number of students in each field.
- **Where**: The program is executed from the terminal and reads the CSV file from the provided path.
- **Why**: This task helps understand how to handle asynchronous file reading and parsing of CSV data in Node.js.
- **How**: The `fs.promises.readFile()` method is used to read the file, and the data is processed by splitting the lines and categorizing students by their fields.
- **Who**: This task is relevant for developers working with file systems in Node.js.
- **When**: This function can be executed anytime to read a student database file and log the student data.

</details>
