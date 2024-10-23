
<div align="center">
  <img src="https://github.com/user-attachments/assets/10921ea3-3667-4cd0-99af-62c6fa45e229" alt="blackpuggyspotlight">

  <h1>Node Express</h1>

  <p>This project focuses on building HTTP servers using both Node.js and the Express framework. Starting with basic server creation using Node’s HTTP module, the project evolves into handling complex routing and asynchronous file reading. We structured the project by organizing code into controllers, routes, and utility functions, using Babel for ES6 compatibility and Nodemon for faster development. The final product is a robust, modular Express server capable of handling requests for student data from a CSV file.</p>
</div>


## Resources

- [Node JS Getting Started](https://nodejs.org/en/learn/getting-started/introduction-to-nodejs)
- [Process API](https://node.readthedocs.io/en/latest/api/process/)
- [Child Process](https://nodejs.org/api/child_process.html)
- [Express Getting Started](https://expressjs.com/en/starter/installing.html)
- [Mocha Documentation](https://mochajs.org/)
- [Nodemon Documentation](https://github.com/remy/nodemon#nodemon)

## Learning Objectives

<details>
  <summary><strong>Run JavaScript using NodeJS</strong></summary>

This objective is covered in **Task 0** where we run basic JavaScript code using Node.js to print a message to the console.

- **Task 0**: Executing Basic JavaScript with Node JS
</details>

<details>
  <summary><strong>Use NodeJS modules</strong></summary>

We import and use modules in several tasks, including using the `fs` module to read files and exporting functions to be reused in other parts of the code.

- **Task 0**: Exporting and using modules.
- **Task 2 and Task 3**: Using `fs` module for file reading.

</details>

<details>
  <summary><strong>Use specific NodeJS modules to read files</strong></summary>

This is covered in tasks where we read the database CSV files using Node.js's `fs` module (synchronous and asynchronous).

- **Task 2**: Reading a file synchronously.
- **Task 3**: Reading a file asynchronously.

</details>

<details>
  <summary><strong>Use process to access command line arguments and the environment</strong></summary>

This is covered in tasks where we use `process.argv` to pass the path of the database file to the server.

- **Task 5**: Creating a more complex HTTP server using Node's HTTP module.
- **Task 7**: Creating a more complex HTTP server using Express.

</details>

<details>
  <summary><strong>Create a small HTTP server using NodeJS</strong></summary>

In these tasks, we create basic HTTP servers using Node.js's built-in `http` module.

- **Task 4**: Creating a small HTTP server using Node's HTTP module.
- **Task 5**: Creating a more complex HTTP server using Node's HTTP module.

</details>

<details>
  <summary><strong>Create a small HTTP server using ExpressJS</strong></summary>

This objective is covered when we create a small HTTP server using the Express framework.

- **Task 6**: Creating a small HTTP server using ExpressJS.

</details>

<details>
  <summary><strong>Create advanced routes with ExpressJS</strong></summary>

This is demonstrated in creating advanced routes for handling requests based on major (`/students/CS`, `/students/SWE`) and error handling for invalid major parameters.

- **Task 7**: Creating a more complex HTTP server using ExpressJS.

</details>

<details>
  <summary><strong>Use ES6 with NodeJS and Babel-node</strong></summary>

We used ES6 features such as `import`, `export`, and promises throughout the project. Babel-node allows us to run these ES6 features in Node.js.

- **Task 8**: Organizing a complex HTTP server using Express with ES6 modules using Babel-node.

</details>

<details>
  <summary><strong>Use Nodemon to develop faster</strong></summary>

Nodemon is set up in the `dev` script of `package.json` to restart the server automatically when file changes are detected.

- **Task 8**: Running the server with Nodemon for faster development.

</details>


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

### Task 3: Reading a File Asynchronously with Node.js

This task involves reading a file asynchronously using Node.js and returning the number of students and their fields from a CSV file.

<details>
  <summary><strong>Curriculum Instruction</strong></summary>

- Create a function `countStudents` that reads a file asynchronously.
- The function must accept a file path as an argument.
- It must return a promise and log the following information:
  - The total number of students.
  - The number of students in each field and their names.
- If the file cannot be found, the function must throw an error with the message `"Cannot load the database"`.
- CSV file can contain empty lines, which should be ignored.

</details>

<details>
  <summary><strong>Steps and Code Implementation</strong></summary>

1. **Create the File `3-read_file_async.js`**:  
   
   ```javascript
   const fs = require('fs').promises;

   // Asynchronous function to count students from a CSV file
   function countStudents(path) {
     return fs.readFile(path, 'utf-8')
       .then((data) => {
         const lines = data.trim().split('\n');

         // Remove empty lines and the header
         const students = lines.filter((line, index) => line.trim() !== '' && index > 0);

         let result = `Number of students: ${students.length}\n`;
         const fields = {};

         // Process each student line
         students.forEach((student) => {
           const [firstname, lastname, age, field] = student.split(',');

           if (!fields[field]) {
             fields[field] = [];
           }
           fields[field].push(firstname);
         });

         // Prepare the output for each field
         for (const [field, names] of Object.entries(fields)) {
           result += `Number of students in ${field}: ${names.length}. List: ${names.join(', ')}\n`;
         }

         // Log the result and return the formatted output
         console.log(result.trim());
         return result.trim();
       })
       .catch(() => {
         throw new Error('Cannot load the database');
       });
   }

   module.exports = countStudents;
   ```

2. **Test with `3-main_1.js`**:
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
  <summary><strong>Troubleshooting</strong></summary>

**What We Tried**:
- Initially, the function logged the student data directly to the console but didn't return any data. This was fine for Task 3 alone, but it prevented the function from being reused elsewhere, such as in Task 5.

**Issue**:
- The function did not return the formatted student data, making it difficult to reuse it in other tasks, especially in HTTP responses for Task 5.

**Final Solution**:
- We updated the `countStudents` function to return the student data as a **string** in addition to logging it. This change allowed the function to work both for Task 3 (where logging was required) and for Task 5 (where the formatted data needs to be returned to the HTTP response).

</details>
<details>
  <summary><strong>Explanation: Who, What, Where, When, Why, How</strong></summary>

- **Who**: This task is for developers learning how to handle asynchronous file reading in Node.js and work with CSV data.
  
- **What**: The task involves creating a function named `countStudents` that reads a CSV file asynchronously, counts the number of students, and categorizes them based on their field of study. If the file is not found or cannot be loaded, the function should throw an error.
  
- **Where**: The `countStudents` function is written in `3-read_file_async.js`, and it is tested by calling it in the `3-main_1.js` file.
  
- **When**: This function is called when the file path is passed to it, typically during runtime when the CSV file (like `database.csv`) is available, or when testing it as part of Task 3.
  
- **Why**: This task demonstrates how to handle asynchronous file reading with promises in Node.js, which is crucial in real-world applications to avoid blocking the main thread and ensure a non-blocking I/O model.
  
- **How**: The function uses Node.js's `fs.promises.readFile` method to read the CSV file asynchronously. It processes the file by removing empty lines and splitting the remaining lines into individual student records. It then counts the total number of students and categorizes them based on their field of study, logging the results to the console. The function also returns a promise, which resolves with the formatted data or rejects with an error if the file cannot be loaded.

</details>



### Task 4: Create a Small HTTP Server Using Node's HTTP Module

This task involves creating a small HTTP server that listens on port 1245 and returns a plain text message.

<details>
  <summary><strong>Curriculum Instruction</strong></summary>

- Create a small HTTP server using Node's `http` module.
- The server should listen on port 1245.
- For any request, the server should respond with `Hello Holberton School!` as plain text.

</details>

<details>
  <summary><strong>Steps and Code Implementation</strong></summary>

1. **Create the File `4-http.js`**:  
   
   ```javascript
   const http = require('http');

   // HTTP server listening on port 1245
   const app = http.createServer((req, res) => {
     res.statusCode = 200;
     res.setHeader('Content-Type', 'text/plain');
     res.end('Hello Holberton School!');
   });

   app.listen(1245);

   module.exports = app;
   ```

2. **Run the Program**:
   Open two terminal windows to test the server.

   **Terminal 1**: Run the HTTP server.
   ```bash
   node 4-http.js
   ```

   **Terminal 2**: Use `curl` to send requests to the server.
   ```bash
   curl localhost:1245 && echo ""
   ```

   **Expected Output**:
   ```bash
   Hello Holberton School!
   ```

   You can also try any endpoint:
   ```bash
   curl localhost:1245/any_endpoint && echo ""
   ```

   **Expected Output**:
   ```bash
   Hello Holberton School!
   ```

</details>

<details>
  <summary><strong>Testing with Browser</strong></summary>

1. **Run the HTTP Server**:  
   Ensure the server is running by executing the command:
   ```bash
   node 4-http.js
   ```

2. **Open a Browser**:  
   In your web browser, enter the following URL:
   ```bash
   http://localhost:1245
   ```

3. **Expected Output in the Browser**:  
   You should see the following plain text message displayed:
   ```bash
   Hello Holberton School!
   ```

   The server will respond with this message for any URL entered in the browser (e.g., `http://localhost:1245/any_path`).

</details>

<details>
  <summary><strong>Testing with Postman</strong></summary>

1. **Open Postman**:  
   Launch the Postman app.

2. **Create a New Request**:  
   - Select **New** > **Request**.
   - Set the request method to **GET**.
   - Enter the URL `http://localhost:1245` in the address bar.

3. **Send the Request**:  
   Click on the **Send** button to send the request to the server.

4. **Expected Output in Postman**:  
   The response body will contain the following message:
   ```bash
   Hello Holberton School!
   ```

5. **Test with Different Endpoints**:  
   - You can test with different paths like `http://localhost:1245/any_path`, and the response will still be:
   ```bash
   Hello Holberton School!
   ```

</details>


  <summary><strong>Explanation: Who, What, Where, When, Why, How</strong></summary>

- **What**: This task involves creating a small HTTP server that listens on port 1245 and returns `Hello Holberton School!` for any request.
- **Where**: The server runs on `localhost` at port 1245.
- **Why**: This task demonstrates how to create a basic HTTP server using Node.js, useful for building web services and handling requests.
- **How**: The `http.createServer()` method is used to create the server, and the `res.end()` method is used to send the response back to the client.
- **Who**: This is relevant for developers learning to handle HTTP requests and responses in Node.js.
- **When**: The server can be executed anytime by running `node 4-http.js` in the terminal, and it can be tested using `curl`, a browser, or Postman.

</details>

### Task 5: Create a More Complex HTTP Server Using Node's HTTP Module

This task involves creating an HTTP server that handles multiple routes and returns either a welcome message or a list of students read asynchronously from a CSV file.

<details>
  <summary><strong>Curriculum Instruction</strong></summary>

- Create an HTTP server using Node’s `http` module.
- The server should listen on port 1245.
- When accessing the root path `/`, the server should return `Hello Holberton School!` in plain text.
- When accessing the `/students` path, the server should display the list of students using the same logic as in Task 3 (`3-read_file_async.js`).
- The CSV file should be passed as an argument to the server.

</details>

<details>
  <summary><strong>Steps and Code Implementation</strong></summary>

1. **Create the File `5-http.js`**:  

   
   ```javascript
   const http = require('http');
   const url = require('url');
   const countStudents = require('./3-read_file_async');

   // Create an HTTP server and listen on port 1245
   const app = http.createServer((req, res) => {
     const parsedUrl = url.parse(req.url, true);

     if (parsedUrl.pathname === '/') {
       res.statusCode = 200;
       res.setHeader('Content-Type', 'text/plain');
       res.end('Hello Holberton School!');
     } else if (parsedUrl.pathname === '/students') {
       res.statusCode = 200;
       res.setHeader('Content-Type', 'text/plain');
       res.write('This is the list of our students\n');

       const databasePath = process.argv[2];

       if (!databasePath) {
         res.end('Cannot load the database');
         return;
       }

       countStudents(databasePath)
         .then((output) => {
           res.write(`${output}\n`);
           res.end();
         })
         .catch((err) => {
           res.end(err.message);
         });
     } else {
       res.statusCode = 404;
       res.setHeader('Content-Type', 'text/plain');
       res.end('Not Found');
     }
   });

   // The server listens on port 1245
   app.listen(1245);

   // Export the server
   module.exports = app;
   ```

2. **Run the Program**:
   In **Terminal 1**, run the server with the `database.csv` file as an argument:
   ```bash
   node 5-http.js database.csv
   ```

3. **Test with Curl**:
   In **Terminal 2**, test the root path:
   ```bash
   curl localhost:1245 && echo ""
   ```
   **Expected Output**:
   ```bash
   Hello Holberton School!
   ```

   Test the `/students` path:
   ```bash
   curl localhost:1245/students && echo ""
   ```
   **Expected Output**:
   ```bash
   This is the list of our students
   Number of students: 10
   Number of students in CS: 6. List: Johann, Arielle, Jonathan, Emmanuel, Guillaume, Katie
   Number of students in SWE: 4. List: Guillaume, Joseph, Paul, Tommy
   ```

</details>
<details>
  <summary><strong>Testing with Browser</strong></summary>

1. **Start the server**:
   - Open a terminal and start the server by running:
     ```bash
     node 5-http.js database.csv
     ```

2. **Test the root path (`/`)**:
   - Open your browser and type the following URL:
     ```
     http://localhost:1245
     ```
   - **Expected output in the browser**:
     ```
     Hello Holberton School!
     ```

3. **Test the `/students` path**:
   - In the browser, type the following URL:
     ```
     http://localhost:1245/students
     ```
   - **Expected output in the browser**:
     ```
     This is the list of our students
     Number of students: 10
     Number of students in CS: 6. List: Johann, Arielle, Jonathan, Emmanuel, Guillaume, Katie
     Number of students in SWE: 4. List: Guillaume, Joseph, Paul, Tommy
     ```

</details>

<details>
  <summary><strong>Testing with Postman</strong></summary>

1. **Start the server**:
   - As before, start the server using the command:
     ```bash
     node 5-http.js database.csv
     ```

2. **Test the root path (`/`)**:
   - Open Postman and create a new **GET** request to the following URL:
     ```
     http://localhost:1245/
     ```
   - Click **Send** to execute the request.
   - **Expected output**:
     - In the response body, you should see:
       ```
       Hello Holberton School!
       ```

3. **Test the `/students` path**:
   - In Postman, create a new **GET** request to the following URL:
     ```
     http://localhost:1245/students
     ```
   - Click **Send** to execute the request.
   - **Expected output**:
     - In the response body, you should see:
       ```
       This is the list of our students
       Number of students: 10
       Number of students in CS: 6. List: Johann, Arielle, Jonathan, Emmanuel, Guillaume, Katie
       Number of students in SWE: 4. List: Guillaume, Joseph, Paul, Tommy
       ```

</details>

<details>
  <summary><strong>Troubleshooting</strong></summary>

**What We Tried**:
- Initially, the `countStudents` function logged data to the console, but when reused in Task 5, the student data wasn’t being returned to the HTTP response.

**Issue**:
- We needed the `countStudents` function to return the student data so it could be used in the response for the `/students` endpoint.

**Final Solution**:
- The `countStudents` function was updated to return the student data as a **string**, which allowed the HTTP server to include this data in its response.

</details>

<details>
  <summary><strong>Explanation: Who, What, Where, When, Why, How</strong></summary>

- **Who**: This task is for developers learning how to set up a basic HTTP server with multiple routes using Node.js's `http` module and process data asynchronously from an external file.

- **What**: The task involves creating an HTTP server that listens on port 1245 and responds to two different paths:
  - **Root path (`/`)**: The server responds with a plain text message, `"Hello Holberton School!"`.
  - **Students path (`/students`)**: The server asynchronously reads a CSV file containing student information and returns the number of students, categorized by field.

- **Where**: The server is implemented in the file `5-http.js` and uses the `countStudents` function from `3-read_file_async.js` to read and process the CSV file.

- **When**: This server runs whenever a request is made to `localhost:1245`. The server can handle requests to both the root endpoint (`/`) and the `/students` endpoint, responding with the appropriate data depending on the path requested.

- **Why**: This task demonstrates the basics of creating a small HTTP server in Node.js that can handle multiple routes and interact with external data asynchronously. It’s useful for understanding how to serve different types of content based on the requested URL and how to process data asynchronously without blocking the main thread.

- **How**: The server is created using Node.js's `http` module. It listens for incoming requests and checks the requested URL path. If the request is for the root path (`/`), it responds with a welcome message. If the request is for the `/students` path, it calls the `countStudents` function, which reads and processes the CSV file asynchronously, then returns the student data in the response. If the path is anything else, the server returns a `404 Not Found` error.

</details>

### Task 6: Create a Small HTTP Server Using Express

This task involves setting up a small HTTP server using the Express framework. The server listens on port 1245 and responds with a welcome message on the root (`/`) endpoint.

<details>
  <summary><strong>Curriculum Instruction</strong></summary>

- Install Express and create a small HTTP server using the Express module.
- The server should:
  - Listen on port 1245.
  - Respond with "Hello Holberton School!" for the `/` endpoint.
  - Return an error page for any other invalid routes.

</details>

<details>
  <summary><strong>Steps and Code Implementation</strong></summary>

1. **Install Express**:  
   Run the following command in your project directory to install Express:
   ```bash
   npm install express
   ```

2. **Create the File `6-http_express.js`**:  
   
   ```javascript
   const express = require('express');

   // Create an Express app
   const app = express();

   // Route for the root endpoint
   app.get('/', (req, res) => {
     res.send('Hello Holberton School!');
   });

   // Make the app listen on port 1245
   app.listen(1245, () => {
     console.log('Server is running on port 1245');
   });

   // Export the app
   module.exports = app;
   ```

3. **Run the Program**:
   In **Terminal 1**, start the server by running:
   ```bash
   node 6-http_express.js
   ```

4. **Test with Curl**:
   In **Terminal 2**, test the root path:
   ```bash
   curl localhost:1245 && echo ""
   ```
   **Expected Output**:
   ```bash
   Hello Holberton School!
   ```

   Test an invalid route:
   ```bash
   curl localhost:1245/any_endpoint && echo ""
   ```
   **Expected Output**:
   ```html
   <!DOCTYPE html>
   <html lang="en">
   <head>
     <meta charset="utf-8">
     <title>Error</title>
   </head>
   <body>
     <pre>Cannot GET /any_endpoint</pre>
   </body>
   </html>
   ```

</details>

<details>
  <summary><strong>Testing with Browser</strong></summary>

1. **Start the server**:
   - Open a terminal and start the server by running:
     ```bash
     node 6-http_express.js
     ```

2. **Test the root path (`/`)**:
   - Open your browser and type the following URL:
     ```
     http://localhost:1245
     ```
   - **Expected output in the browser**:
     ```
     Hello Holberton School!
     ```

3. **Test an invalid route**:
   - In the browser, type the following URL:
     ```
     http://localhost:1245/any_endpoint
     ```
   - **Expected output in the browser**:
     ```
     Cannot GET /any_endpoint
     ```

</details>

<details>
  <summary><strong>Testing with Postman</strong></summary>

1. **Start the server**:
   - As before, start the server using the command:
     ```bash
     node 6-http_express.js
     ```

2. **Test the root path (`/`)**:
   - Open Postman and create a new **GET** request to the following URL:
     ```
     http://localhost:1245/
     ```
   - Click **Send** to execute the request.
   - **Expected output**:
     - In the response body, you should see:
       ```
       Hello Holberton School!
       ```

3. **Test an invalid route**:
   - In Postman, create a new **GET** request to the following URL:
     ```
     http://localhost:1245/any_endpoint
     ```
   - Click **Send** to execute the request.
   - **Expected output**:
```html
<!DOCTYPE html>
<html lang="en">


<head>
    <meta charset="utf-8">
    <title>Error</title>
</head>


<body>
    <pre>Cannot GET /any_endpoint</pre>
</body>


</html>

 ```

</details>


<details>
  <summary><strong>Explanation: Who, What, Where, When, Why, How</strong></summary>

- **Who**: This task is for developers learning how to set up a basic HTTP server using the Express framework, which simplifies routing and server management compared to Node’s built-in `http` module.
  
- **What**: The task involves creating a small HTTP server that responds with "Hello Holberton School!" at the root (`/`) endpoint and returns an error page for any invalid routes.
  
- **Where**: The server is implemented in the file `6-http_express.js` using Express.
  
- **When**: This server runs whenever a request is made to `localhost:1245`. The server can handle requests to both the root endpoint (`/`) and any other invalid routes.
  
- **Why**: Express makes it easier to create and manage routes in a web server. This task introduces how Express simplifies server creation and response management in Node.js applications.
  
- **How**: The server is created using the Express framework. It listens for incoming requests and checks the requested URL path. If the request is for the root path (`/`), it responds with a welcome message. If the request is for any other invalid path, it returns an error page generated by Express.

</details>

### Task 7: Create a More Complex HTTP Server Using Express

This task involves setting up a more complex HTTP server using the Express framework. The server should display a welcome message at the root (`/`) endpoint and provide a list of students based on a CSV file at the `/students` endpoint.

<details>
  <summary><strong>Curriculum Instruction</strong></summary>

- Use the Express module to create a more complex HTTP server.
- The server should:
  - Listen on port 1245.
  - Respond with "Hello Holberton School!" for the `/` endpoint.
  - At the `/students` endpoint, display "This is the list of our students" followed by the list of students from the CSV file.
- The CSV file name should be passed as an argument to the server.
- CSV file can contain empty lines, which should be ignored.

</details>

<details>
  <summary><strong>Steps and Code Implementation</strong></summary>

1. **Install Express** (if not already installed):  
   Run the following command in your project directory to install Express:
   ```bash
   npm install express
   ```

2. **Create the File `7-http_express.js`**:  
   
   
   ```javascript
   const express = require('express');
   const countStudents = require('./3-read_file_async');

   // Create an Express app
   const app = express();

   // Route for the root endpoint
   app.get('/', (req, res) => {
     res.send('Hello Holberton School!');
   });

   // Route for the /students endpoint
   app.get('/students', (req, res) => {
     const databasePath = process.argv[2];

     if (!databasePath) {
       res.status(500).send('Cannot load the database');
       return;
     }

     countStudents(databasePath)
       .then((output) => {
         res.send(`This is the list of our students\n${output}`);
       })
       .catch((err) => {
         res.status(500).send(err.message);
       });
   });

   // Make the app listen on port 1245
   app.listen(1245, () => {
     console.log('Server is running on port 1245');
   });

   // Export the app
   module.exports = app;
   ```

3. **Run the Program**:
   In **Terminal 1**, start the server with the `database.csv` file as an argument:
   ```bash
   node 7-http_express.js database.csv
   ```

4. **Test with Curl**:
   In **Terminal 2**, test the root path:
   ```bash
   curl localhost:1245 && echo ""
   ```
   **Expected Output**:
   ```bash
   Hello Holberton School!
   ```

   Test the `/students` path:
   ```bash
   curl localhost:1245/students && echo ""
   ```
   **Expected Output**:
   ```bash
   This is the list of our students
   Number of students: 10
   Number of students in CS: 6. List: Johann, Arielle, Jonathan, Emmanuel, Guillaume, Katie
   Number of students in SWE: 4. List: Guillaume, Joseph, Paul, Tommy
   ```

</details>

<details>
  <summary><strong>Testing with Browser</strong></summary>

1. **Start the server**:
   - Open a terminal and start the server by running:
     ```bash
     node 7-http_express.js database.csv
     ```

2. **Test the root path (`/`)**:
   - Open your browser and type the following URL:
     ```
     http://localhost:1245
     ```
   - **Expected output in the browser**:
     ```
     Hello Holberton School!
     ```

3. **Test the `/students` path**:
   - In the browser, type the following URL:
     ```
     http://localhost:1245/students
     ```
   - **Expected output in the browser**:
     ```
     This is the list of our students
     Number of students: 10
     Number of students in CS: 6. List: Johann, Arielle, Jonathan, Emmanuel, Guillaume, Katie
     Number of students in SWE: 4. List: Guillaume, Joseph, Paul, Tommy
     ```

</details>

<details>
  <summary><strong>Testing with Postman</strong></summary>

1. **Start the server**:
   - As before, start the server using the command:
     ```bash
     node 7-http_express.js database.csv
     ```

2. **Test the root path (`/`)**:
   - Open Postman and create a new **GET** request to the following URL:
     ```
     http://localhost:1245/
     ```
   - Click **Send** to execute the request.
   - **Expected output**:
     - In the response body, you should see:
       ```
       Hello Holberton School!
       ```

3. **Test the `/students` path**:
   - In Postman, create a new **GET** request to the following URL:
     ```
     http://localhost:1245/students
     ```
   - Click **Send** to execute the request.
   - **Expected output**:
     ```
     This is the list of our students
     Number of students: 10
     Number of students in CS: 6. List: Johann, Arielle, Jonathan, Emmanuel, Guillaume, Katie
     Number of students in SWE: 4. List: Guillaume, Joseph, Paul, Tommy
     ```

</details>


<details>
  <summary><strong>Explanation: Who, What, Where, When, Why, How</strong></summary>

- **Who**: This task is for developers learning how to build more complex HTTP servers using Express, especially ones that handle multiple endpoints and process external data.
  
- **What**: The task involves creating a more complex HTTP server using Express that responds with a welcome message at the root endpoint (`/`) and lists students from a CSV file at the `/students` endpoint.
  
- **Where**: The server is implemented in the file `7-http_express.js` using Express and the `countStudents` function from `3-read_file_async.js` to read the student data from a CSV file.
  
- **When**: This server runs whenever a request is made to `localhost:1245`, handling requests to both the root endpoint (`/`) and the `/students` endpoint.
  
- **Why**: Express simplifies server creation and routing, and this task demonstrates how to create an HTTP server that can serve different types of content, including dynamically generated data from external files.
  
- **How**: The server is created using Express. It listens for incoming requests and checks the requested URL path. If the request is for the root path (`/`), it responds with a welcome message. If the request is for `/students`, it reads and processes a CSV file using the `countStudents` function, then returns the student data. If an error occurs, the server handles it and responds with a `500` error message.

</details>


### Task 8: Organize a Complex HTTP Server Using Express

This task involves organizing a complex Express server into multiple files and directories. The server should respond to routes for displaying a welcome message and listing students based on the data in a CSV file.

<details>
  <summary><strong>Curriculum Instruction</strong></summary>

- Organize the server code into separate directories: `controllers`, `routes`, and `utils`.
- Use `babel-node` to run the server with ES6 syntax.
- Implement several routes:
  - The root (`/`) should display "Hello Holberton School!".
  - `/students` should display the list of students.
  - `/students/:major` should display the list of students filtered by major (either `CS` or `SWE`).
- Return appropriate status codes and error messages if there are issues with the database or invalid parameters.

</details>

<details>
  <summary><strong>Steps and Code Implementation</strong></summary>

1. **Create the folder structure**:
   Create the following directories inside the `full_server` folder:
   ```
   controllers/
   routes/
   ```

2. **Create the `readDatabase` function**:
   Inside `full_server/utils.js`, implement the `readDatabase` function:
   
   ```javascript
   const fs = require('fs').promises;

   // Function to read the database asynchronously
   async function readDatabase(filePath) {
     try {
       const data = await fs.readFile(filePath, 'utf-8');
       const lines = data.trim().split('\n');
       const fields = {};

       lines.slice(1).forEach((line) => {
         const [firstname, lastname, age, field] = line.split(',');
         if (field && firstname) {
           if (!fields[field]) {
             fields[field] = [];
           }
           fields[field].push(firstname);
         }
       });

       return fields;
     } catch (error) {
       throw new Error('Cannot load the database');
     }
   }

   module.exports = readDatabase;
   ```

3. **Create the `AppController`**:
   Inside `full_server/controllers/AppController.js`, create a class `AppController`:
   
   ```javascript
   class AppController {
     static getHomepage(req, res) {
       res.status(200).send('Hello Holberton School!');
     }
   }

   module.exports = AppController;
   ```

4. **Create the `StudentsController`**:
   Inside `full_server/controllers/StudentsController.js`, create a class `StudentsController`:
   
   ```javascript
   const readDatabase = require('../utils');

   class StudentsController {
     static async getAllStudents(req, res) {
       const databasePath = process.argv[2];

       try {
         const data = await readDatabase(databasePath);
         let response = 'This is the list of our students\n';

         Object.keys(data).sort().forEach((field) => {
           response += `Number of students in ${field}: ${data[field].length}. List: ${data[field].join(', ')}\n`;
         });

         res.status(200).send(response.trim());
       } catch (error) {
         res.status(500).send('Cannot load the database');
       }
     }

     static async getAllStudentsByMajor(req, res) {
       const { major } = req.params;
       const databasePath = process.argv[2];

       if (major !== 'CS' && major !== 'SWE') {
         res.status(500).send('Major parameter must be CS or SWE');
         return;
       }

       try {
         const data = await readDatabase(databasePath);
         const students = data[major] || [];

         res.status(200).send(`List: ${students.join(', ')}`);
       } catch (error) {
         res.status(500).send('Cannot load the database');
       }
     }
   }

   module.exports = StudentsController;
   ```

5. **Create the routes**:
   Inside `full_server/routes/index.js`, define the routes for your app:
   
   ```javascript
   const express = require('express');
   const AppController = require('../controllers/AppController');
   const StudentsController = require('../controllers/StudentsController');

   const router = express.Router();

   router.get('/', AppController.getHomepage);
   router.get('/students', StudentsController.getAllStudents);
   router.get('/students/:major', StudentsController.getAllStudentsByMajor);

   module.exports = router;
   ```

6. **Create the Express server**:
   Inside `full_server/server.js`, set up the server:
   
   ```javascript
   const express = require('express');
   const router = require('./routes');

   const app = express();
   app.use('/', router);

   const PORT = 1245;
   app.listen(PORT, () => {
     console.log(`Server is running on port ${PORT}`);
   });

   module.exports = app;
   ```

7. **Update `package.json`**:
   Ensure that the `dev` command runs the server using `babel-node`. Your `package.json` should look like this:
   
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
      "dev": "nodemon --exec babel-node --presets babel-preset-env ./full_server/server.js ./database.csv"
    },
    "author": "",
    "license": "ISC",
    "dependencies": {
      "chai-http": "^4.3.0",
      "express": "^4.21.1"
    },
    "devDependencies": {
      "babel-cli": "^6.26.0",
      "babel-preset-env": "^1.7.0",
      "chai": "^4.2.0",
      "eslint": "^6.4.0",
      "eslint-config-airbnb-base": "^14.0.0",
      "eslint-plugin-import": "^2.18.2",
      "eslint-plugin-jest": "^22.17.0",
      "mocha": "^6.2.2",
      "nodemon": "^2.0.2",
      "request": "^2.88.0",
      "sinon": "^7.5.0"
    }
  }
   ```

8. **Add the `.babelrc` file**:
   You need to add a `.babelrc` file to allow the use of ES6 features like `import` and `export`. Create a `.babelrc` file with the following content:

   ```json
   {
     "presets": [["env", { "exclude": ["transform-regenerator"] }]]
   }
   ```

   This file ensures that `babel-node` works correctly by using the `env` preset.

9. **Test the server**:
   In **Terminal 1**, start the server:
   ```bash
   npm run dev
   ```

10. **Test with Curl**:
   In **Terminal 2**, test the root path:
   ```bash
   curl localhost:1245 && echo ""
   ```
   **Expected Output**:
   ```bash
   Hello Holberton School!
   ```

   Test the `/students` path:
   ```bash
   curl localhost:1245/students && echo ""
   ```
   **Expected Output**:
   ```bash
   This is the list of our students
   Number of students in CS: 6. List: Johann, Arielle, Jonathan, Emmanuel, Guillaume, Katie
   Number of students in SWE: 4. List: Guillaume, Joseph, Paul, Tommy
   ```

   Test the `/students/:major` path (with `CS` or `SWE` as the major):
   ```bash
   curl localhost:1245/students/CS && echo ""
   ```
   **Expected Output**:
   ```bash
   List: Johann, Arielle, Jonathan, Emmanuel, Guillaume, Katie
   ```

11. **Test Invalid Major**:
   Test the `/students/:major` path with an invalid major:
   ```bash
   curl localhost:1245/students/French && echo ""
   ```
   **Expected Output**:
   ```bash
   Major parameter must be CS or SWE
   ```

</details>

<details>
  <summary><strong>Testing with Browser and Postman</strong></summary>

1. **Start the server**:
   - Open a terminal and start the server by running:
     ```bash
     npm run dev
     ```

2. **Test the root path (`/`)**:
   - Open your browser and go to:
     ```
     http://localhost:1245
     ```
   - **Expected output**:
     ```
     Hello Holberton School!
     ```

3. **Test the `/students` path**:
   - Go to the URL:
     ```
     http://localhost:1245/students
     ```
   - **Expected output**:
     ```
     This is the list of our students
     Number of students in CS: 6. List: Johann, Arielle, Jonathan, Emmanuel, Guillaume, Katie
     Number of students in SWE: 4. List: Guillaume, Joseph, Paul, Tommy
     ```

4. **Test with Postman**:
   - Open Postman and create a new

 **GET** request to:
     ```
     http://localhost:1245/students
     ```
   - Click **Send**.  
   - **Expected output**:
     ```
     This is the list of our students
     Number of students in CS: 6. List: Johann, Arielle, Jonathan, Emmanuel, Guillaume, Katie
     Number of students in SWE: 4. List: Guillaume, Joseph, Paul, Tommy
     ```

5. **Test the `/students/:major` path**:
   - Test a valid major (`CS` or `SWE`):
     ```
     http://localhost:1245/students/CS
     ```
   - **Expected output**:
     ```
     List: Johann, Arielle, Jonathan, Emmanuel, Guillaume, Katie
     ```

   - Test an invalid major (`French`):
     ```
     http://localhost:1245/students/French
     ```
   - **Expected output**:
     ```
     Major parameter must be CS or SWE
     ```

</details>


<details>
  <summary><strong>Explanation: Who, What, Where, When, Why, How</strong></summary>

- **Who**: This task is for developers learning how to create modular server structures using Express and handle dynamic routes based on external data.
  
- **What**: The task involves organizing a complex HTTP server into separate files for better maintainability, and creating routes to display student data from a CSV file.
  
- **Where**: The server is implemented in multiple files within the `full_server` directory, including controllers, routes, and utility functions.
  
- **When**: This server runs whenever requests are made to `localhost:1245` for the root (`/`), `/students`, and `/students/:major` endpoints.
  
- **Why**: This task demonstrates how to structure an Express server to handle various routes and how to process data from external files (like a CSV).
  
- **How**: The server is created using Express and modularized by separating routes and logic into different files. It processes requests to different endpoints, reading student data from a CSV file and filtering it by major.

</details>
