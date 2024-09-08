
<div align="center">
  <img src="https://github.com/user-attachments/assets/339a329c-681f-4e1e-9d60-f8c2aedf1f39" alt="detectivepuggy">
</div>

<br>
This project focuses on understanding and handling Personally Identifiable Information (PII) and implementing best practices for data privacy and security in Python. It covers how to filter logs, encrypt passwords, and authenticate securely using environment variables.

## Resources

- **[What Is PII, non-PII, and Personal Data?](https://piwik.pro/blog/what-is-pii-personal-data/):** This article explains what constitutes PII (Personally Identifiable Information), non-PII, and personal data, and provides examples and best practices for handling such data securely.

- **[Logging Documentation](https://docs.python.org/3/library/logging.html):** Official Python documentation on the logging module, detailing how to configure loggers, set levels, create handlers, and format log messages to capture important information while avoiding sensitive data exposure.

- **[bcrypt Package](https://github.com/pyca/bcrypt/):** A Python library for password hashing and encryption. This package helps ensure that passwords are stored securely and can be validated effectively.

- **[Logging to Files, Setting Levels, and Formatting](https://www.youtube.com/watch?v=-ARI4Cz-awo):** A YouTube tutorial explaining how to set up logging in Python, including writing logs to files, setting log levels, and formatting log messages for clarity and security.

## Learning Objectives


- Identify examples of Personally Identifiable Information (PII).
- Implement a log filter that obfuscates PII fields.
- Encrypt a password and check the validity of an input password.
- Authenticate to a database using environment variables.

## Requirements

- All files will be interpreted/compiled on Ubuntu 20.04 LTS using Python 3.9.
- Each file should end with a new line.
- The first line of all your files should be `#!/usr/bin/env python3`.
- A `README.md` file at the root of the folder is mandatory.
- Code must adhere to the pycodestyle style (version 2.5).
- All files must be executable.
- The length of your files will be tested using `wc`.
- All modules, classes, and functions should have detailed documentation explaining their purpose.
- All functions should be type annotated.

## Tasks and Detailed Usage

### Task 0: Regex-ing

<details> 
<summary>Write a function named `filter_datum` that returns the log message obfuscated:</summary>
<br>

Arguments:
fields: a list of strings representing all fields to obfuscate
redaction: a string representing by what the field will be obfuscated
message: a string representing the log line
separator: a string representing by which character is separating all fields in the log line (message)
The function should use a regex to replace occurrences of certain field values.
filter_datum should be less than 5 lines long and use re.sub to perform the substitution with a single regex.



**Description:**

The `filter_datum` function is designed to obfuscate sensitive fields in log messages using regular expressions (regex). This function ensures that Personally Identifiable Information (PII) like `password` and `date_of_birth` are replaced with a redaction string to maintain data privacy and security.

**Implementation:**

```python
#!/usr/bin/env python3
'''
This module contains a function for filtering log messages.
'''

import re  # Import the 're' module for regular expression operations
from typing import List  # Import 'List' from 'typing' module for type annotations

def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    '''
    Obfuscates fields in a log message.

    Args:
        fields (List[str]): A list of strings representing all fields to obfuscate.
        redaction (str): A string representing the text to replace each field value.
        message (str): A string representing the log line.
        separator (str): A string representing the character that separates fields in the log line.

    Returns:
        str: A string with specified fields obfuscated.
    '''
    # Create a regex pattern that matches any of the fields to be obfuscated
    # '|' joins the fields list into an alternation pattern (e.g., "password|date_of_birth")
    # '.+?' matches any character(s) non-greedily up to the next separator
    pattern = f"({'|'.join(fields)})=.+?{separator}"

    # Use re.sub to substitute the matched pattern with the redacted value
    # The lambda function ensures that the field name is preserved and only the value is replaced
    # m.group(1) extracts the field name that was matched by the regex
    return re.sub(
        pattern, lambda m: f"{m.group(1)}={redaction}{separator}", message
    )
```

**Usage:**

1. **Function Purpose:**
   The `filter_datum` function obfuscates specific fields in a log message to prevent the exposure of sensitive data. It takes a list of fields to obfuscate, a redaction string, the log message, and the separator used in the log message.

2. **Examples of Using the `filter_datum` Function:**

   You can use the `filter_datum` function to hide sensitive information in log messages:

   ```python
   # Example 1
   fields = ["password", "date_of_birth"]
   message = "name=egg;email=eggmin@eggsample.com;password=eggcellent;date_of_birth=12/12/1986;"
   result = filter_datum(fields, 'xxx', message, ';')
   print(result)  # Expected output: name=egg;email=eggmin@eggsample.com;password=xxx;date_of_birth=xxx;

   # Example 2
   fields = ["password", "date_of_birth"]
   message = "name=bob;email=bob@dylan.com;password=bobbycool;date_of_birth=03/04/1993;"
   result = filter_datum(fields, 'xxx', message, ';')
   print(result)  # Expected output: name=bob;email=bob@dylan.com;password=xxx;date_of_birth=xxx;
   ```

3. **Running the script to test the function:**

   To test the functionality of the `filter_datum` function, use `0-main.py`:

   ```python
   #!/usr/bin/env python3
   """
   Main file
   """

   filter_datum = __import__('filtered_logger').filter_datum

   fields = ["password", "date_of_birth"]
   messages = [
       "name=egg;email=eggmin@eggsample.com;password=eggcellent;date_of_birth=12/12/1986;",
       "name=bob;email=bob@dylan.com;password=bobbycool;date_of_birth=03/04/1993;"
   ]

   for message in messages:
       print(filter_datum(fields, 'xxx', message, ';'))
   ```

   Make the script executable by running:

   ```sh
   chmod +x 0-main.py
   ```

   Then, run the script to test:

   ```sh
   ./0-main.py
   ```

   Verify the output matches the expected results.

**Expected Output:**

```bash
name=egg;email=eggmin@eggsample.com;password=xxx;date_of_birth=xxx;
name=bob;email=bob@dylan.com;password=xxx;date_of_birth=xxx;
```

**Explanation:**

- **`filter_datum` Function:**
  - **Regex Pattern Creation**: The pattern is constructed dynamically to match any of the field names in the `fields` list followed by `=` and any characters up to the next `separator`. The pattern uses `('|'.join(fields))` to create an alternation group that matches any of the fields listed.
  - **Regex Substitution**: The `re.sub` method replaces the matched patterns with the redaction string using a lambda function. The lambda function takes the match object `m` and formats it to retain the field name (`m.group(1)`) while substituting its value with the redaction string.
  - **Purpose**: This method ensures sensitive data fields are obfuscated effectively while keeping the log structure intact.

</details>

### Task 1: Log Formatter

<details> 
<summary>Write a class named `RedactingFormatter` that redacts sensitive information in log records:</summary>
<br>


Copy the following code into filtered_logger.py.
```python
import logging


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self):
        super(RedactingFormatter, self).__init__(self.FORMAT)

    def format(self, record: logging.LogRecord) -> str:
        NotImplementedError
```
Update the class to accept a list of strings fields constructor argument.
Implement the format method to filter values in incoming log records using filter_datum. Values for fields in fields should be filtered.
DO NOT extrapolate FORMAT manually. The format method should be less than 5 lines long.


**Description:**

The `RedactingFormatter` class extends the `logging.Formatter` class and is used to format log records while redacting specified sensitive fields. It takes advantage of the `filter_datum` function to ensure that fields such as `email`, `ssn`, and `password` are replaced with a redaction string (`***`) to maintain privacy and security.

**Implementation:**

```python
#!/usr/bin/env python3
'''
This module contains a function for filtering log messages and a formatter
class that redacts sensitive information in log records.
'''

import re  # For regular expression operations
import logging  # To handle logging and formatting
from typing import List  # For type annotations


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    '''
    Obfuscates fields in a log message.

    Args:
        fields (List[str]): A list of strings representing all fields to
                            obfuscate.
        redaction (str): A string representing the text to replace each field
                         value.
        message (str): A string representing the log line.
        separator (str): A string representing the character that separates
                         fields in the log line.

    Returns:
        str: A string with specified fields obfuscated.
    '''
    pattern = f"({'|'.join(fields)})=.+?{separator}"

    return re.sub(
        pattern, lambda m: f"{m.group(1)}={redaction}{separator}", message
    )


class RedactingFormatter(logging.Formatter):
    '''
    Redacting Formatter class
    '''

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        '''
        Initializes the formatter with the specified fields to redact.

        Args:
            fields (List[str]): A list of strings representing the fields to
                                obfuscate.
        '''
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        '''
        Formats the log record, redacting specified fields.

        Args:
            record (logging.LogRecord): The log record to format.

        Returns:
            str: The formatted and redacted log record as a string.
        '''
        original_message = super().format(record)
        return filter_datum(self.fields, self.REDACTION, original_message,
                            self.SEPARATOR)
```

**Usage:**

1. **Class Purpose:**
   The `RedactingFormatter` class formats log messages while redacting sensitive fields specified in the `fields` list. It uses the `filter_datum` function to replace the values of these fields with a redaction string (`***`).

2. **Examples of Using the `RedactingFormatter` Class:**

   You can use the `RedactingFormatter` class to redact sensitive information in log records:

   ```python
   # Example
   import logging
   from filtered_logger import RedactingFormatter

   message = "name=Bob;email=bob@dylan.com;ssn=000-123-0000;password=bobby2019;"
   log_record = logging.LogRecord("my_logger", logging.INFO, None, None, message, None, None)
   formatter = RedactingFormatter(fields=["email", "ssn", "password"])
   print(formatter.format(log_record))
   ```

3. **Running the script to test the class:**

   To test the functionality of the `RedactingFormatter` class, use `1-main.py`:

   ```python
   #!/usr/bin/env python3
   """
   Main file
   """

   import logging
   from filtered_logger import RedactingFormatter

   message = "name=Bob;email=bob@dylan.com;ssn=000-123-0000;password=bobby2019;"
   log_record = logging.LogRecord("my_logger", logging.INFO, None, None, message, None, None)
   formatter = RedactingFormatter(fields=["email", "ssn", "password"])
   print(formatter.format(log_record))
   ```

   Make the script executable by running:

   ```sh
   chmod +x 1-main.py
   ```

   Then, run the script to test:

   ```sh
   ./1-main.py
   ```

   Verify the output matches the expected results.

**Expected Output:**

```bash
[HOLBERTON] my_logger INFO 2024-09-07 13:59:45,095: name=Bob;email=***;ssn=***;password=***;
```

**Explanation:**

- **`RedactingFormatter` Class:**
  - **Constructor (`__init__` Method):** Accepts a list of fields to be redacted and initializes the formatter.
  - **`format` Method:** Formats the log record using the base formatter and then applies the `filter_datum` function to redact sensitive fields specified in the `fields` list.
  - **Purpose:** This class ensures that sensitive information in log messages is properly obfuscated to maintain privacy and security.

</details>

### Task 2: Create Logger

<details>
<summary>Implement a `get_logger` function that creates and returns a configured logger object:</summary>
<br>

Use user_data.csv for this task

The logger should be named "user_data" and only log up to logging.INFO level. It should not propagate messages to other loggers. It should have a StreamHandler with RedactingFormatter as formatter.
Create a tuple PII_FIELDS constant at the root of the module containing the fields from user_data.csv that are considered PII. PII_FIELDS can contain only 5 fields - choose the right list of fields that can are considered as “important” PIIs or information that you must hide in your logs. Use it to parameterize the formatter.

Tips:
- **[What Is PII, non-PII, and personal data?](https://piwik.pro/blog/what-is-pii-personal-data/):** This article explains the differences between PII, non-PII, and personal data, and provides examples and best practices for handling such data securely.
  
- **[Uncovering Password Habits](https://www.digitalguardian.com/blog/uncovering-password-habits-are-users%E2%80%99-password-security-habits-improving-infographic):** This infographic provides insights into users' password security habits and how they have changed over time.



**Description:**

The `get_logger` function creates a logger named `"user_data"` that is configured to log messages up to the `INFO` level. The logger uses a `StreamHandler` with a custom `RedactingFormatter` to redact sensitive fields in log messages, ensuring Personally Identifiable Information (PII) is protected.

Atuple named `PII_FIELDS` is defined at the root of the module, containing the fields from `user_data.csv` that are considered sensitive PII. The tuple includes 5 fields that are critical to be redacted in logs.

**Implementation:**

```python
#!/usr/bin/env python3
'''
This module contains functions and classes for filtering log messages and
creating loggers that redact sensitive information.
'''

import re  # For regular expression operations
import logging  # To handle logging and formatting
from typing import List  # For type annotations


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    '''
    Obfuscates fields in a log message.

    Args:
        fields (List[str]): A list of strings representing all fields to
                            obfuscate.
        redaction (str): A string representing the text to replace each field
                         value.
        message (str): A string representing the log line.
        separator (str): A string representing the character that separates
                         fields in the log line.

    Returns:
        str: A string with specified fields obfuscated.
    '''
    pattern = f"({'|'.join(fields)})=.+?{separator}"

    return re.sub(
        pattern, lambda m: f"{m.group(1)}={redaction}{separator}", message
    )


class RedactingFormatter(logging.Formatter):
    '''
    Redacting Formatter class
    '''

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        '''
        Initializes the formatter with the specified fields to redact.

        Args:
            fields (List[str]): A list of strings representing the fields to
                                obfuscate.
        '''
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        '''
        Formats the log record, redacting specified fields.

        Args:
            record (logging.LogRecord): The log record to format.

        Returns:
            str: The formatted and redacted log record as a string.
        '''
        original_message = super().format(record)
        return filter_datum(self.fields, self.REDACTION, original_message,
                            self.SEPARATOR)


# Define a tuple containing fields considered as PII in user_data.csv
PII_FIELDS = ("name", "email", "phone", "ssn", "password")


def get_logger() -> logging.Logger:
    '''
    Creates and returns a logger named "user_data" that logs up to INFO level,
    does not propagate to other loggers, and uses a StreamHandler with
    RedactingFormatter to format log records.

    Returns:
        logging.Logger: Configured logger object.
    '''
    # Create a logger object named "user_data"
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)  # Set the logging level to INFO
    logger.propagate = False  # Prevent the logger from propagating messages

    # Create a StreamHandler and set its formatter to RedactingFormatter
    stream_handler = logging.StreamHandler()
    formatter = RedactingFormatter(fields=PII_FIELDS)
    stream_handler.setFormatter(formatter)

    # Add the handler to the logger
    logger.addHandler(stream_handler)

    return logger
```

**Usage:**

1. **Function Purpose:**
   The `get_logger` function returns a `Logger` object that is configured to log messages securely. The logger uses a `StreamHandler` with a `RedactingFormatter` to redact fields considered as PII, such as `name`, `email`, `phone`, `ssn`, and `password`.

2. **Examples of Using the `get_logger` Function:**

   You can use the `get_logger` function to create a logger that redacts sensitive information:

   ```python
   # Example
   import logging
   from filtered_logger import get_logger, PII_FIELDS

   logger = get_logger()
   logger.info("User information: name=John Doe;email=john.doe@example.com;ssn=123-45-6789;password=supersecret;")
   ```

3. **Running the script to test the function:**

   To test the functionality of the `get_logger` function, use `2-main.py`:

   ```python
   #!/usr/bin/env python3
   """
   Main file
   """

   import logging
   from filtered_logger import get_logger, PII_FIELDS

   print(get_logger.__annotations__.get('return'))
   print("PII_FIELDS: {}".format(len(PII_FIELDS)))
   ```

   Make the script executable by running:

   ```sh
   chmod +x 2-main.py
   ```

   Then, run the script to test:

   ```sh
   ./2-main.py
   ```

   Verify the output matches the expected results.

**Expected Output:**

```bash
<class 'logging.Logger'>
PII_FIELDS: 5
```

**Explanation:**

- **`PII_FIELDS` Tuple:** A tuple containing the fields that are considered as Personally Identifiable Information (PII) in the `user_data.csv`. These fields (`"name"`, `"email"`, `"phone"`, `"ssn"`, `"password"`) should be redacted in the log messages.
  
- **`get_logger` Function:**
  - **Creates a Logger** named `"user_data"` that logs messages up to `INFO` level.
  - **Uses `RedactingFormatter`** to redact sensitive fields in log messages, ensuring that PII is not exposed in logs.
  - **Configures the Logger** with a `StreamHandler` to display redacted log messages to the console.

</details>

### Task 3: Connect to Secure Database

<details>
<summary>Implement a `get_db` function that securely connects to a MySQL database using environment variables:</summary>
<br>

Database credentials should NEVER be stored in code or checked into version control. One secure option is to store them as environment variable on the application server.
In this task, you will connect to a secure holberton database to read a users table. The database is protected by a username and password that are set as environment variables on the server named PERSONAL_DATA_DB_USERNAME (set the default as “root”), PERSONAL_DATA_DB_PASSWORD (set the default as an empty string) and PERSONAL_DATA_DB_HOST (set the default as “localhost”).
The database name is stored in PERSONAL_DATA_DB_NAME.
Implement a get_db function that returns a connector to the database (mysql.connector.connection.MySQLConnection object).
Use the os module to obtain credentials from the environment
Use the module mysql-connector-python to connect to the MySQL database (pip3 install mysql-connector-python)


**Description:**

The `get_db` function connects to a secure MySQL database using credentials stored in environment variables. This approach prevents sensitive information, such as usernames and passwords, from being hard-coded in the code or exposed in version control.

**Implementation:**

```python
#!/usr/bin/env python3
'''
This module contains functions and classes for filtering log messages,
creating loggers that redact sensitive information, and connecting securely
to a MySQL database.
'''

import re  # For regular expression operations
import logging  # To handle logging and formatting
from typing import List  # For type annotations
import os  # For environment variable access
import mysql.connector  # For connecting to the MySQL database
from mysql.connector import Error  # For handling MySQL errors


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    '''
    Obfuscates fields in a log message.
    '''
    pattern = f"({'|'.join(fields)})=.+?{separator}"

    return re.sub(
        pattern, lambda m: f"{m.group(1)}={redaction}{separator}", message
    )


class RedactingFormatter(logging.Formatter):
    '''
    Redacting Formatter class
    '''

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        '''
        Initializes the formatter with the specified fields to redact.
        '''
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        '''
        Formats the log record, redacting specified fields.
        '''
        original_message = super().format(record)
        return filter_datum(self.fields, self.REDACTION, original_message,
                            self.SEPARATOR)


# Define a tuple containing fields considered as PII in user_data.csv
PII_FIELDS = ("name", "email", "phone", "ssn", "password")


def get_logger() -> logging.Logger:
    '''
    Creates and returns a logger named user_data that logs up to INFO level,
    does not propagate to other loggers, and uses a StreamHandler with
    RedactingFormatter to format log records.
    '''
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    stream_handler = logging.StreamHandler()
    formatter = RedactingFormatter(fields=PII_FIELDS)
    stream_handler.setFormatter(formatter)

    logger.addHandler(stream_handler)

    return logger


def get_db() -> mysql.connector.connection.MySQLConnection:
    '''
    Connects to a secure MySQL database using credentials from environment
    variables and returns a MySQLConnection object.
    '''
    # Check for missing environment variables
    if not all([os.getenv("PERSONAL_DATA_DB_USERNAME"),
                os.getenv("PERSONAL_DATA_DB_PASSWORD"),
                os.getenv("PERSONAL_DATA_DB_HOST"),
                os.getenv("PERSONAL_DATA_DB_NAME")]):
        raise ValueError("Some required environment variables are missing.")

    try:
        # Create a MySQL database connection using environment variables
        connector = mysql.connector.connect(
            user=os.getenv("PERSONAL_DATA_DB_USERNAME", "root"),
            password=os.getenv("PERSONAL_DATA_DB_PASSWORD", ""),
            host=os.getenv("PERSONAL_DATA_DB_HOST", "localhost"),
            database=os.getenv("PERSONAL_DATA_DB_NAME")
        )
        return connector
    except Error as e:
        # Handle MySQL connection errors
        print(f"Error connecting to MySQL: {e}")
        return None
```


**Usage**

1. **Set Environment Variables:**
   Before running the script, you need to set the necessary environment variables to securely store your database credentials. Run the following commands in your terminal:

   ```sh
   export PERSONAL_DATA_DB_USERNAME=root
   export PERSONAL_DATA_DB_PASSWORD=password  # Replace 'password' with your actual password
   export PERSONAL_DATA_DB_HOST=localhost
   export PERSONAL_DATA_DB_NAME=my_db
   ```

   Verify that the environment variables have been set correctly:

   ```sh
   echo $PERSONAL_DATA_DB_USERNAME
   echo $PERSONAL_DATA_DB_PASSWORD
   echo $PERSONAL_DATA_DB_HOST
   echo $PERSONAL_DATA_DB_NAME
   ```

2. **Function Purpose:**
   The `get_db` function establishes a secure connection to a MySQL database using credentials from environment variables. This function ensures that sensitive data like usernames and passwords are not hardcoded in the code or exposed in version control.

3. **Examples of Using the `get_db` Function:**

   You can use the `get_db` function to connect to a MySQL database securely:

   ```python
   # Example
   from filtered_logger import get_db

   db = get_db()
   if db:
       cursor = db.cursor()
       cursor.execute("SELECT COUNT(*) FROM users;")
       for row in cursor:
           print(row[0])
       cursor.close()
       db.close()
   else:
       print("Failed to connect to the database.")
   ```

4. **Running the Script to Test the Function:**

   To test the functionality of the `get_db` function, use `3-main.py`:

   ```python
   #!/usr/bin/env python3
   """
   Main file
   """

   get_db = __import__('filtered_logger').get_db

   db = get_db()
   if db:
       cursor = db.cursor()
       cursor.execute("SELECT COUNT(*) FROM users;")
       for row in cursor:
           print(row[0])
       cursor.close()
       db.close()
   else:
       print("Failed to connect to the database.")
   ```

   Make the script executable by running:

   ```sh
   chmod +x 3-main.py
   ```

   Then, run the script to test:

   ```sh
   ./3-main.py
   ```

   Verify the output matches the expected results.

**Expected Output:**

```bash
2
```

**Troubleshooting:**

- **Error: Some Required Environment Variables Are Missing**
  - Make sure you have set all necessary environment variables:
    ```sh
    export PERSONAL_DATA_DB_USERNAME=root
    export PERSONAL_DATA_DB_PASSWORD=<your_password>  # Replace with your actual password
    export PERSONAL_DATA_DB_HOST=localhost
    export PERSONAL_DATA_DB_NAME=my_db
    ```

- **Error: `Error connecting to MySQL`**
  - Check if your MySQL server is running.
  - Verify that the credentials (username, password, host, and database name) are correct.
  - Ensure that the user has the necessary permissions to connect to the MySQL database.
  - Restart the MySQL service if needed:
    ```sh
    sudo service mysql restart
    ```


**Explanation:**

- **Environment Variables Usage:** The function securely uses environment variables to retrieve database credentials, enhancing security by avoiding hardcoding sensitive information.
- **Error Handling:** The code includes checks and error handling to ensure that missing credentials or connection errors are handled gracefully, providing clear messages for easier troubleshooting.

</details>

### Task 4: Read and Filter Data

<details>
<summary>Implement a `main` function that connects to a secure database, retrieves user data, and logs it with sensitive information redacted:</summary>
<br>

Implement a main function that takes no arguments and returns nothing.

The function will obtain a database connection using get_db and retrieve all rows in the users table and display each row under a filtered format like this:

```bash
[HOLBERTON] user_data INFO 2019-11-19 18:37:59,596: name=***; email=***; phone=***; ssn=***; password=***; ip=e848:e856:4e0b:a056:54ad:1e98:8110:ce1b; last_login=2019-11-14T06:16:24; user_agent=Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; KTXN);
```

Filtered fields:

name
email
phone
ssn
password
Only your main function should run when the module is executed.

**Description:**

The `main` function connects to a secure MySQL database using credentials stored in environment variables. It retrieves all rows from the `users` table and logs each row using a custom logger that redacts sensitive information (such as `name`, `email`, `phone`, `ssn`, and `password`).

**Implementation:**

```python
#!/usr/bin/env python3
'''
This module contains functions and classes for filtering log messages,
creating loggers that redact sensitive information, and connecting securely
to a MySQL database.
'''

import re  # For regular expression operations
import logging  # To handle logging and formatting
from typing import List  # For type annotations
import os  # For environment variable access
import mysql.connector  # For connecting to the MySQL database
from mysql.connector import Error  # For handling MySQL errors


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    '''
    Obfuscates fields in a log message.
    '''
    pattern = f"({'|'.join(fields)})=.+?{separator}"

    return re.sub(
        pattern, lambda m: f"{m.group(1)}={redaction}{separator}", message
    )


class RedactingFormatter(logging.Formatter):
    '''
    Redacting Formatter class
    '''

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        '''
        Initializes the formatter with the specified fields to redact.
        '''
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        '''
        Formats the log record, redacting specified fields.
        '''
        original_message = super().format(record)
        return filter_datum(self.fields, self.REDACTION, original_message,
                            self.SEPARATOR)


# Define a tuple containing fields considered as PII in user_data.csv
PII_FIELDS = ("name", "email", "phone", "ssn", "password")


def get_logger() -> logging.Logger:
    '''
    Creates and returns a logger named user_data that logs up to INFO level,
    does not propagate to other loggers, and uses a StreamHandler with
    RedactingFormatter to format log records.
    '''
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    stream_handler = logging.StreamHandler()
    formatter = RedactingFormatter(fields=PII_FIELDS)
    stream_handler.setFormatter(formatter)

    logger.addHandler(stream_handler)

    return logger


def get_db() -> mysql.connector.connection.MySQLConnection:
    '''
    Connects to a secure MySQL database using credentials from environment
    variables and returns a MySQLConnection object.
    '''
    # Check for missing environment variables
    if not all([os.getenv("PERSONAL_DATA_DB_USERNAME"),
                os.getenv("PERSONAL_DATA_DB_PASSWORD"),
                os.getenv("PERSONAL_DATA_DB_HOST"),
                os.getenv("PERSONAL_DATA_DB_NAME")]):
        raise ValueError("Some required environment variables are missing.")

    try:
        # Create a MySQL database connection using environment variables
        connector = mysql.connector.connect(
            user=os.getenv("PERSONAL_DATA_DB_USERNAME", "root"),
            password=os.getenv("PERSONAL_DATA_DB_PASSWORD", ""),
            host=os.getenv("PERSONAL_DATA_DB_HOST", "localhost"),
            database=os.getenv("PERSONAL_DATA_DB_NAME")
        )
        return connector
    except Error as e:
        # Handle MySQL connection errors
        print(f"Error connecting to MySQL: {e}")
        return None


def main():
    '''
    Main function that retrieves and prints all user data from the database
    with sensitive information redacted.
    '''
    db = get_db()
    if db:
        cursor = db.cursor()
        cursor.execute(
            "SELECT name, email, phone, ssn, password, ip, last_login, "
            "user_agent FROM users;"
        )

        logger = get_logger()

        for row in cursor:
            message = (
                f"name={row[0]}; email={row[1]}; phone={row[2]}; "
                f"ssn={row[3]}; password={row[4]}; ip={row[5]}; "
                f"last_login={row[6]}; user_agent={row[7]};"
            )
            logger.info(message)

        cursor.close()
        db.close()
    else:
        print("Failed to connect to the database.")


if __name__ == "__main__":
    main()

```

**Usage:**

1. **Set Environment Variables:**
   Before running the script, you need to set the necessary environment variables to securely store your database credentials:

   ```sh
   export PERSONAL_DATA_DB_USERNAME=root
   export PERSONAL_DATA_DB_PASSWORD=password  # Replace 'password' with your actual password
   export PERSONAL_DATA_DB_HOST=localhost
   export PERSONAL_DATA_DB_NAME=my_db
   ```

   Verify that the environment variables have been set correctly:

   ```sh
   echo $PERSONAL_DATA_DB_USERNAME
   echo $PERSONAL_DATA_DB_PASSWORD
   echo $PERSONAL_DATA_DB_HOST
   echo $PERSONAL_DATA_DB_NAME
   ```

2. **Run the Script:**

   Make the script executable and run it:

   ```sh
   chmod +x filtered_logger.py
   PERSONAL_DATA_DB_USERNAME=root PERSONAL_DATA_DB_PASSWORD=password PERSONAL_DATA_DB_HOST=localhost PERSONAL_DATA_DB_NAME=my_db ./filtered_logger.py
   ```

3. **Expected Output:**

   The output should display redacted log messages for each user record in the database:

   ```bash
[HOLBERTON] user_data INFO 2024-09-08 12:41:10,638: name=***; email=***; phone=***; ssn=***; password=***; ip=60ed:c396:2ff:244:bbd0:9208:26f2:93ea; last_login=2019-11-14 06:14:24; user_agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36;
[HOLBERTON] user_data INFO 2024-09-08 12:41:10,638: name=***; email=***; phone=***; ssn=***; password=***; ip=f724:c5d1:a14d:c4c5:bae2:9457:3769:1969; last_login=2019-11-14 06:16:19; user_agent=Mozilla/5.0 (Linux; U; Android 4.1.2; de-de; GT-I9100 Build/JZO54K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30;

   ```

**Troubleshooting:**

- **Error: Failed to connect to the database.**
  - Ensure that the environment variables are set correctly.
  - Verify that the MySQL server is running and accessible.

- **Error: Some required environment variables are missing.**
  - Make sure all necessary environment variables are exported before running the script.

**Explanation:**

- **Environment Variables Usage:** The function securely uses environment variables to retrieve database credentials, enhancing security by avoiding hardcoding sensitive information.
- **Error Handling:** The code includes checks and error handling to ensure that missing credentials or connection errors are handled gracefully, providing clear messages for easier troubleshooting.
- **Logging Redacted Information:** The `main` function uses the custom logger to log each user record with sensitive information redacted, ensuring compliance with privacy requirements.

</details>

### Task 5: Encrypting Passwords

<details> 
<summary>Implement a `hash_password` function that hashes user passwords securely:</summary>
<br>

User passwords should NEVER be stored in plain text in a database.
Implement a hash_password function that expects one string argument name password and returns a salted, hashed password, which is a byte string.
Use the bcrypt package to perform the hashing (with hashpw).


**Description:**

The `hash_password` function hashes a plain text password using the `bcrypt` package. This ensures that passwords are not stored in plain text, which is a critical security measure for protecting user data.

**Installation:**

To use the `bcrypt` package for password hashing, you must first install it. Run the following command to install `bcrypt` using `pip3`:

```sh
pip3 install bcrypt
```

This will install the necessary package to perform secure password hashing.

**Implementation:**

```python
#!/usr/bin/env python3
'''
This module contains a function for securely hashing passwords
using the bcrypt package.
'''

import bcrypt  # Import bcrypt for password hashing


def hash_password(password: str) -> bytes:
    '''
    Hashes a password using bcrypt with a salt.

    Args:
        password (str): The plain text password to be hashed.

    Returns:
        bytes: A salted, hashed password as a byte string.
    '''
    # Generate a salt
    salt = bcrypt.gensalt()

    # Hash the password using the generated salt
    hashed_password = bcrypt.hashpw(password.encode(), salt)

    return hashed_password
```

**Usage:**

1. **Function Purpose:**
   The `hash_password` function securely hashes a plain text password by generating a random salt and using the `bcrypt` package to create a hashed password. The resulting hash is a byte string that can be safely stored in a database.

2. **Examples of Using the `hash_password` Function:**

   You can use the `hash_password` function to hash any password:

   ```python
   # Example Usage
   from encrypt_password import hash_password

   password = "MyAmazingPassw0rd"
   print(hash_password(password))  # Output: A salted, hashed password in bytes
   print(hash_password(password))  # Output: A different salted, hashed password in bytes
   ```

3. **Running the script to test the function:**

   To test the functionality of the `hash_password` function, use `5-main.py`:

   ```python
   #!/usr/bin/env python3
   """
   Main file
   """

   hash_password = __import__('encrypt_password').hash_password

   password = "MyAmazingPassw0rd"
   print(hash_password(password))
   print(hash_password(password))
   ```

   Make the script executable by running:

   ```sh
   chmod +x encrypt_password.py
   chmod +x 5-main.py
   ```

   Then, run the script to test:

   ```sh
   ./5-main.py
   ```

**Expected Output:**

```bash
b'$2b$12$KCxqwXXe5dxD9XFmKYIOme0.oUHFYs3/xu8uVXQ1kQjXq42sa9Bla'
b'$2b$12$5Hbld/nDiOMhij/GMR17MOYHMLwOkkMcAgNYA9ujC5nVjsi7GLPb2'

```

- The output should display two different salted, hashed passwords. Each time you run the script, the hashes will be different due to the use of a random salt.

**Explanation:**

- **bcrypt Package:** Uses the `bcrypt` package to generate a secure, salted hash of the password, making it resistant to various attacks.
- **Hashing with Salt:** The function generates a new random salt every time it is called, ensuring that even if the same password is hashed multiple times, the resulting hashes will be different.
- **Security Measure:** This method of hashing is secure against rainbow table attacks and adds an extra layer of protection for stored user passwords.

</details>

