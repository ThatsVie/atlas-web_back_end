# Personal Data

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

def filter_datum(fields: List[str], redaction: str, message: str, separator: str) -> str:
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
    # '|' is used to join the fields list into an alternation pattern (e.g., "password|date_of_birth")
    # '.+?' matches any character(s) non-greedily up to the next separator
    pattern = f"({'|'.join(fields)})=.+?{separator}"

    # Use re.sub to substitute the matched pattern with the redacted value
    # The lambda function ensures that the field name is preserved and only the value is replaced
    # m.group(1) extracts the field name that was matched by the regex
    return re.sub(pattern, lambda m: f"{m.group(1)}={redaction}{separator}", message)

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

- **`filter_datum` Function:** Uses regex to identify and obfuscate sensitive fields specified in the `fields` list. The function replaces the field values with the `redaction` string, while keeping the rest of the log message intact.
  
</details>
