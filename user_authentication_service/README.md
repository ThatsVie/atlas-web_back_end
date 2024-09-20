
<p align="center">
  <img src="https://github.com/user-attachments/assets/a68b0eed-dd09-4bf9-b140-ca2fd0a24ec4" alt="2beautifulAIPugs" />
</p>

<h1 align="center">User Pugthentication Service</h1>


This project focuses on building a custom user authentication system for a Flask-based web application. While it's common in the industry to use frameworks such as [Flask-User](https://flask-user.readthedocs.io/en/latest/), this project walks through the process of implementing an authentication mechanism from scratch for educational purposes.

## Resources

- **[Flask documentation](https://flask.palletsprojects.com/en/1.1.x/quickstart/):** Comprehensive guide to Flask, covering everything from app initialization to routing and cookies.
- **[Requests module](https://requests.kennethreitz.org/en/latest/user/quickstart/):** A powerful HTTP library for Python used to make HTTP requests.
- **[HTTP status codes](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html):** Understanding the various status codes and their meaning.

## Learning Objectives

1. **Declare API routes** in a Flask app.
2. **Get and set cookies** for session management.
3. **Retrieve request form data** from clients.
4. **Return various HTTP status codes** in your Flask app.

## Requirements

- Allowed editors: `vi`, `vim`, `emacs`.
- Python version: `python3` (version 3.9), all code is compatible with Ubuntu 20.04 LTS.
- Each file must end with a new line.
- The first line of all files should be exactly `#!/usr/bin/env python3`.
- All code must follow the `pycodestyle` style guide (version 2.5).
- Use **SQLAlchemy** as the ORM for database interactions.
- All files must be executable and will be tested for length using `wc`.
- All modules, classes, and functions must include detailed documentation explaining their purpose and functionality.
- All functions must have **type annotations**.
- The Flask app must interact only with `Auth` and never directly with the database. Only public methods of `Auth` and `DB` classes should be used.

## Setup

Before beginning, install the required `bcrypt` package:

```bash
pip3 install bcrypt
```

## Tasks and Detailed Usage

<details>
<summary><strong>Task 0: User model</strong></summary>

In this task, we will create a SQLAlchemy model named `User` to represent the `users` table in our database. This model will allow us to store user-related information, such as their email and password. The model includes the following attributes:

- `id`: an integer primary key for uniquely identifying each user.
- `email`: a non-nullable string that stores the user’s email address.
- `hashed_password`: a non-nullable string that stores the user’s hashed password for security purposes.
- `session_id`: a nullable string used for managing user sessions.
- `reset_token`: a nullable string used for password reset functionality.

This model will be essential for managing user authentication and security throughout the project.

<details>
<summary><strong>Instructions Provided in Curriculum</strong></summary>

In this task, you will create a SQLAlchemy model named `User` for a database table named `users` (by using the [mapping declaration](https://docs.sqlalchemy.org/en/13/orm/tutorial.html#declare-a-mapping) of SQLAlchemy).


The model will have the following attributes:

- id, the integer primary key
- email, a non-nullable string
- hashed_password, a non-nullable string
- session_id, a nullable string
- reset_token, a nullable string

```bash
bob@dylan:~$ cat main.py
#!/usr/bin/env python3
"""
Main file
"""
from user import User

print(User.__tablename__)

for column in User.__table__.columns:
    print("{}: {}".format(column, column.type))

bob@dylan:~$ python3 main.py
users
users.id: INTEGER
users.email: VARCHAR(250)
users.hashed_password: VARCHAR(250)
users.session_id: VARCHAR(250)
users.reset_token: VARCHAR(250)
bob@dylan:~$
```

</details>

### Step-by-Step Instructions

1. **Create the `User` model**:
   - Create a file named `user.py` and define a SQLAlchemy model called `User`.
   - Use SQLAlchemy’s `declarative_base()` to create a base class for models.
   - Define the following columns in the `User` model:
     - `id`: Integer, primary key.
     - `email`: String(250), non-nullable.
     - `hashed_password`: String(250), non-nullable.
     - `session_id`: String(250), nullable.
     - `reset_token`: String(250), nullable.

   Here’s the `user.py` file content:

   ```python
   #!/usr/bin/env python3
   '''
   This module contains the SQLAlchemy User model for the users table.
   '''

   from sqlalchemy import Column, Integer, String
   from sqlalchemy.ext.declarative import declarative_base

   Base = declarative_base()

   class User(Base):
       '''This class represents the User model for the users table'''
       __tablename__ = 'users'

       id = Column(Integer, primary_key=True)
       email = Column(String(250), nullable=False)
       hashed_password = Column(String(250), nullable=False)
       session_id = Column(String(250), nullable=True)
       reset_token = Column(String(250), nullable=True)
   ```

2. **Rename the `main.py`to `main_0.py` and make it script executable**:
   - In the terminal, run the following command to ensure the `main_0.py` script is executable:
   ```bash
   chmod +x main_0.py
   ```

3. **main_0.py**:
   
   ```python
   #!/usr/bin/env python3
   '''
   This module contains a script to test the User model.
   '''

   from user import User

   print(User.__tablename__)

   for column in User.__table__.columns:
       print("{}: {}".format(column, column.type))
   ```

4. **Run the test script**:
   - Execute the `main_01.py` file to verify that the model is correctly created:
   ```bash
   ./main_01.py
   ```

5. **Expected Output**:

   You should see the following output:

   ```bash
   users
   users.id: INTEGER
   users.email: VARCHAR(250)
   users.hashed_password: VARCHAR(250)
   users.session_id: VARCHAR(250)
   users.reset_token: VARCHAR(250)
   ```

### Explanation

- **Why this works**:
  - The `__tablename__` attribute tells SQLAlchemy that this model maps to a table named `users` in the database.
  - Each column is defined with its respective data type (e.g., `Integer`, `String`). Non-nullable columns, such as `email` and `hashed_password`, are explicitly required for storing user credentials.
  - The `session_id` and `reset_token` are nullable because they may not always be present for a user. The `session_id` is used to track user sessions, and the `reset_token` is only needed when the user requests a password reset.

- **How it works**:
  - When you run `main_0.py`, SQLAlchemy introspects the `User` class, and the `__table__` attribute holds the table structure.
  - The script prints out each column along with its corresponding data type, showing how SQLAlchemy maps Python code to database schema.

This task lays the foundation for managing user data securely, setting the stage for authentication mechanisms in later tasks.

</details>


<details>
<summary><strong>Task 1: Create user</strong></summary>

In this task, we will complete the `DB` class by implementing the `add_user` method. This method will allow us to create a new user in the database by taking an email and a hashed password as inputs. Once the user is added to the database, the method will return the created `User` object. At this stage, no validations are required.

The method is essential for managing user registration and securely handling user data storage.


<details>
<summary><strong>Instructions Provided in Curriculum</strong></summary>

In this task, you will complete the `DB` class provided below to implement the `add_user` method.

```python
"""DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session

from user import Base

class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=True)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session
```

**Note**: `DB._session` is a private property and hence should NEVER be used from outside the `DB` class.

Implement the `add_user` method, which has two required string arguments: `email` and `hashed_password`, and returns a `User` object. The method should save the user to the database. No validations are required at this stage.

```bash
bob@dylan:~$ cat main.py
#!/usr/bin/env python3
"""
Main file
"""

from db import DB
from user import User

my_db = DB()

user_1 = my_db.add_user("test@test.com", "SuperHashedPwd")
print(user_1.id)

user_2 = my_db.add_user("test1@test.com", "SuperHashedPwd1")
print(user_2.id)

bob@dylan:~$ python3 main.py
1
2
bob@dylan:~$
```

</details>

### Step-by-Step Instructions

1. **Update the `DB` class**:
   - Create a file `db.py` and complete the `DB` class to include the `add_user` method.
   - The `add_user` method should take two arguments: `email` and `hashed_password`, and return the newly created `User` object.
   - **Reduce verbosity**: Change the `echo` argument in the `create_engine` function to `False` to suppress verbose SQLAlchemy logs.

   Here’s the updated `db.py`:

   ```python
   #!/usr/bin/env python3
   '''
   This module contains the DB class for managing the database.
   '''
   from sqlalchemy import create_engine
   from sqlalchemy.ext.declarative import declarative_base
   from sqlalchemy.orm import sessionmaker
   from sqlalchemy.orm.session import Session

   from user import Base, User

   class DB:
       '''This class represents the database for user authentication'''

       def __init__(self) -> None:
           '''Initialize a new DB instance'''
           self._engine = create_engine("sqlite:///a.db", echo=False)  # Changed to False for cleaner logs
           Base.metadata.drop_all(self._engine)
           Base.metadata.create_all(self._engine)
           self.__session = None

       @property
       def _session(self) -> Session:
           '''Memoized session object'''
           if self.__session is None:
               DBSession = sessionmaker(bind=self._engine)
               self.__session = DBSession()
           return self.__session

       def add_user(self, email: str, hashed_password: str) -> User:
           '''Add a new user to the database'''
           new_user = User(email=email, hashed_password=hashed_password)
           self._session.add(new_user)
           self._session.commit()
           return new_user
   ```

2. **Rename the test script**:
   - Rename the test script for this task to `main_1.py` for clarity:
   ```bash
   mv main.py main_1.py
   ```

3. **Make the `main_1.py` script executable**:
   - Ensure the test file `main_1.py` is executable:
   ```bash
   chmod +x main_1.py
   ```

4. **Test the `add_user` method**:

   Here’s the content of `main_1.py`:

   ```python
   #!/usr/bin/env python3
   '''
   This module contains a script to test the DB class and add_user method.
   '''
   from db import DB
   from user import User

   my_db = DB()

   user_1 = my_db.add_user("test@test.com", "SuperHashedPwd")
   print(user_1.id)

   user_2 = my_db.add_user("test1@test.com", "SuperHashedPwd1")
   print(user_2.id)
   ```

5. **Run the test script**:
   - Execute the `main_1.py` script to verify that the users are correctly added to the database:
   ```bash
   ./main_1.py
   ```

6. **Expected Output**:

   The expected output should be the IDs of the newly created users:

   ```bash
   1
   2
   ```

### Explanation

- **Why we renamed the main file**:
  - By naming the main test script as `main_1.py` (and doing so for future tasks), we avoid confusion between test files for different tasks. This makes it easier to reference specific scripts as the project grows.

- **Why we changed `echo=True` to `echo=False`**:
  - `echo=True` in SQLAlchemy produces verbose logging of every SQL command, which is helpful during debugging but can clutter the terminal during normal execution. By changing it to `echo=False`, we suppress this output for a cleaner log, making it easier to focus on meaningful output like user IDs.

- **Why this works**:
  - The `add_user` method creates a new `User` object with the provided `email` and `hashed_password` and adds it to the database session.
  - The session is then committed to ensure the changes are saved to the database.
  - The method returns the `User` object, which allows us to access the `id` attribute and verify that the user has been successfully created.

- **How it works**:
  - The `DB` class is initialized with an SQLite database (`a.db`) using SQLAlchemy.
  - The `add_user` method adds the new user to the database using the memoized session.
  - The session is committed, which saves the user to the database, and the `id` of the created user is printed.
  - Running `main_1.py` shows the unique IDs generated for the two users, confirming successful creation and storage in the database.

</details>

<details>
<summary><strong>Task 2: Find user</strong></summary>

In this task, we will implement the `DB.find_user_by` method. This method will take in arbitrary keyword arguments and return the first row found in the `users` table, filtered by the provided arguments. The method will raise specific exceptions based on certain conditions:

- **NoResultFound**: Raised when no results are found in the `users` table for the given query.
- **InvalidRequestError**: Raised when invalid query arguments are provided, such as non-existent or incorrectly typed attributes.


<details>
<summary><strong>Instructions Provided in Curriculum</strong></summary>

You will implement the `DB.find_user_by` method. This method takes in arbitrary keyword arguments and returns the first row found in the `users` table as filtered by the method’s input arguments. No validation of input arguments required at this point.

Make sure that SQLAlchemy’s `NoResultFound` and `InvalidRequestError` are raised when no results are found, or when wrong query arguments are passed, respectively.

```bash
bob@dylan:~$ cat main.py
#!/usr/bin/env python3
"""
Main file
"""
from db import DB
from user import User

from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound


my_db = DB()

user = my_db.add_user("test@test.com", "PwdHashed")
print(user.id)

find_user = my_db.find_user_by(email="test@test.com")
print(find_user.id)

try:
    find_user = my_db.find_user_by(email="test2@test.com")
    print(find_user.id)
except NoResultFound:
    print("Not found")

try:
    find_user = my_db.find_user_by(no_email="test@test.com")
    print(find_user.id)
except InvalidRequestError:
    print("Invalid")        

bob@dylan:~$ python3 main.py
1
1
Not found
Invalid
bob@dylan:~$
```

</details>

### Step-by-Step Instructions

1. **Update the `DB` class**:
   - In the `db.py` file, implement the `find_user_by` method.
   - This method will take arbitrary keyword arguments and use SQLAlchemy’s filtering mechanism to return the first `User` that matches the provided arguments.
   - If no matching result is found, the method should raise a `NoResultFound` exception. If invalid query arguments are provided, it should raise an `InvalidRequestError`.

   Here’s the updated `db.py`:

   ```python
   #!/usr/bin/env python3
   '''
   This module contains the DB class for managing the database.
   '''
   from sqlalchemy import create_engine
   from sqlalchemy.ext.declarative import declarative_base
   from sqlalchemy.orm import sessionmaker
   from sqlalchemy.orm.session import Session
   from sqlalchemy.exc import InvalidRequestError
   from sqlalchemy.orm.exc import NoResultFound
   from user import Base, User

   class DB:
       '''This class represents the database for user authentication'''

       def __init__(self) -> None:
           '''Initialize a new DB instance'''
           self._engine = create_engine("sqlite:///a.db", echo=False)
           Base.metadata.drop_all(self._engine)
           Base.metadata.create_all(self._engine)
           self.__session = None

       @property
       def _session(self) -> Session:
           '''Memoized session object'''
           if self.__session is None:
               DBSession = sessionmaker(bind=self._engine)
               self.__session = DBSession()
           return self.__session

       def add_user(self, email: str, hashed_password: str) -> User:
           '''Add a new user to the database'''
           new_user = User(email=email, hashed_password=hashed_password)
           self._session.add(new_user)
           self._session.commit()
           return new_user

       def find_user_by(self, **kwargs) -> User:
           '''Find a user by arbitrary keyword arguments'''
           try:
               user = self._session.query(User).filter_by(**kwargs).first()
               if user is None:
                   raise NoResultFound
               return user
           except TypeError:
               raise InvalidRequestError(f"Invalid query arguments: {kwargs}")
   ```

2. **Rename the test script**:
   - Rename the test script for this task to `main_2.py` for clarity:
   ```bash
   mv main.py main_2.py
   ```

3. **Make the `main_2.py` script executable**:
   - Ensure the test file `main_2.py` is executable:
   ```bash
   chmod +x main_2.py
   ```

4. **Test the `find_user_by` method**:

   Here’s the content of `main_2.py`:

   ```python
   #!/usr/bin/env python3
   '''
   This module contains a script to test the DB class and find_user_by method.
   '''
   from db import DB
   from user import User

   from sqlalchemy.exc import InvalidRequestError
   from sqlalchemy.orm.exc import NoResultFound

   my_db = DB()

   user = my_db.add_user("test@test.com", "PwdHashed")
   print(user.id)

   # Find user by valid email
   find_user = my_db.find_user_by(email="test@test.com")
   print(find_user.id)

   # Try to find a user with a non-existing email
   try:
       find_user = my_db.find_user_by(email="test2@test.com")
       print(find_user.id)
   except NoResultFound:
       print("Not found")

   # Try to find a user with an invalid query argument
   try:
       find_user = my_db.find_user_by(no_email="test@test.com")
       print(find_user.id)
   except InvalidRequestError:
       print("Invalid")
   ```

5. **Run the test script**:
   - Execute the `main_2.py` script to verify that users can be found, and exceptions are raised as expected:
   ```bash
   ./main_2.py
   ```

6. **Expected Output**:

   The expected output should show the user ID for the first user, followed by the exceptions being raised for the invalid cases:

   ```bash
   1
   1
   Not found
   Invalid
   ```

### Explanation

- **The Issue We Encountered**:
  - Initially, we had a problem where `NoResultFound` was being caught and re-raised as `InvalidRequestError`. This was due to incorrectly handling the exceptions thrown by SQLAlchemy when an invalid query argument was passed.

- **How We Fixed It**:
  - We added an explicit check for `TypeError` within the `find_user_by` method. This allows us to raise `InvalidRequestError` for invalid keyword arguments and handle `NoResultFound` separately, ensuring proper exception handling for different scenarios.

- **Why this works**:
  - The `find_user_by` method leverages SQLAlchemy’s query-building capabilities to filter users from the database.
  - Proper exception handling ensures that edge cases (like no results or invalid queries) are handled gracefully, allowing the rest of the program to continue executing without unexpected crashes.

- **How it works**:
  - The method first tries to query the `users` table using the `filter_by` method and the keyword arguments passed into it.
  - If the query returns `None`, it raises a `NoResultFound` exception.
  - If the query arguments are invalid (e.g., a non-existent field is passed), a `TypeError` is caught and raised as an `InvalidRequestError`.
  - Running `main_2.py` demonstrates this behavior by successfully finding the user with the correct email, raising `NoResultFound` when no user is found, and raising `InvalidRequestError` when an invalid query is made.

</details>

<details>
<summary><strong>Task 3: Update user</strong></summary>

In this task, we will implement the `DB.update_user` method. This method takes two arguments:
1. **user_id** (integer): The ID of the user you want to update.
2. **Arbitrary keyword arguments**: The attributes you want to update on the user, such as `hashed_password`, `email`, etc.

The method will first use `find_user_by` to locate the user based on the provided `user_id`. Once the user is found, it will update the user’s attributes based on the provided keyword arguments. The changes are then committed to the database. If any invalid arguments (attributes that do not exist on the `User` model) are passed, the method will raise a `ValueError`.

### Error Handling
- **NoResultFound**: Raised if the user is not found based on `user_id`.
- **ValueError**: Raised if an invalid attribute is passed in the keyword arguments.

<details>
<summary><strong>Instructions Provided in Curriculum</strong></summary>

You will implement the `DB.update_user` method that takes as argument a required `user_id` integer and arbitrary keyword arguments, and returns `None`.

The method will use `find_user_by` to locate the user to update, then will update the user’s attributes as passed in the method’s arguments and commit changes to the database.

If an argument that does not correspond to a user attribute is passed, raise a `ValueError`.

```bash
bob@dylan:~$ cat main.py
#!/usr/bin/env python3
"""
Main file
"""
from db import DB
from user import User

from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound


my_db = DB()

email = 'test@test.com'
hashed_password = "hashedPwd"

user = my_db.add_user(email, hashed_password)
print(user.id)

try:
    my_db.update_user(user.id, hashed_password='NewPwd')
    print("Password updated")
except ValueError:
    print("Error")

bob@dylan:~$ python3 main.py
1
Password updated
bob@dylan:~$
```

</details>

### Step-by-Step Instructions

1. **Update the `DB` class**:
   - In the `db.py` file, implement the `update_user` method.
   - This method will first locate the user using `find_user_by`. Once the user is found, it will loop through the provided keyword arguments and update the user's attributes. Finally, the changes are committed to the database.
   - If an invalid attribute is passed in the keyword arguments, raise a `ValueError`.

   Here’s the updated `db.py`:

   ```python
   #!/usr/bin/env python3
   '''
   This module contains the DB class for managing the database.
   '''
   from sqlalchemy import create_engine
   from sqlalchemy.ext.declarative import declarative_base
   from sqlalchemy.orm import sessionmaker
   from sqlalchemy.orm.session import Session
   from sqlalchemy.exc import InvalidRequestError
   from sqlalchemy.orm.exc import NoResultFound
   from user import Base, User

   class DB:
       '''This class represents the database for user authentication'''

       def __init__(self) -> None:
           '''Initialize a new DB instance'''
           self._engine = create_engine("sqlite:///a.db", echo=False)
           Base.metadata.drop_all(self._engine)
           Base.metadata.create_all(self._engine)
           self.__session = None

       @property
       def _session(self) -> Session:
           '''Memoized session object'''
           if self.__session is None:
               DBSession = sessionmaker(bind=self._engine)
               self.__session = DBSession()
           return self.__session

       def add_user(self, email: str, hashed_password: str) -> User:
           '''Add a new user to the database'''
           new_user = User(email=email, hashed_password=hashed_password)
           self._session.add(new_user)
           self._session.commit()
           return new_user

       def find_user_by(self, **kwargs) -> User:
           '''Find a user by arbitrary keyword arguments'''
           try:
               user = self._session.query(User).filter_by(**kwargs).first()
               if user is None:
                   raise NoResultFound
               return user
           except TypeError:
               raise InvalidRequestError(f"Invalid query arguments: {kwargs}")

       def update_user(self, user_id: int, **kwargs) -> None:
           '''Update user attributes and commit changes to the database'''
           user = self.find_user_by(id=user_id)
           for key, value in kwargs.items():
               if not hasattr(user, key):
                   raise ValueError(f"Invalid attribute: {key}")
               setattr(user, key, value)
           self._session.commit()
   ```

2. **Rename the test script**:
   - Rename the test script for this task to `main_3.py` for clarity:
   ```bash
   mv main.py main_3.py
   ```

3. **Make the `main_3.py` script executable**:
   - Ensure the test file `main_3.py` is executable:
   ```bash
   chmod +x main_3.py
   ```

4. **Test the `update_user` method**:

   Here’s the content of `main_3.py`:

   ```python
   #!/usr/bin/env python3
   '''
   This module contains a script to test the DB class and update_user method.
   '''
   from db import DB
   from user import User

   from sqlalchemy.exc import InvalidRequestError
   from sqlalchemy.orm.exc import NoResultFound

   my_db = DB()

   email = 'test@test.com'
   hashed_password = "hashedPwd"

   user = my_db.add_user(email, hashed_password)
   print(user.id)

   # Try to update the user's password
   try:
       my_db.update_user(user.id, hashed_password='NewPwd')
       print("Password updated")
   except ValueError:
       print("Error")
   ```

5. **Run the test script**:
   - Execute the `main_3.py` script to verify that users can be updated, and exceptions are raised for invalid cases:
   ```bash
   ./main_3.py
   ```

6. **Expected Output**:

   The expected output should show the user ID for the created user and confirm that the password has been updated:

   ```bash
   1
   Password updated
   ```

### Explanation

- **Why `ValueError` is raised**:
  - The `update_user` method raises a `ValueError` if any invalid attributes are passed in the keyword arguments. This prevents accidental updates to non-existent fields, ensuring that only valid user attributes are updated.

- **Why this works**:
  - The `update_user` method first locates the user in the database using the `find_user_by` method.
  - It then updates the user’s attributes based on the provided keyword arguments and commits the changes.
  - If invalid attributes are passed, a `ValueError` is raised.

- **How it works**:
  - The method first uses `find_user_by` to locate the user by `user_id`.
  - It loops through each provided keyword argument and uses Python’s `setattr` function to dynamically update the user’s attributes.
  - The session is committed to save the changes in the database.
  - Running `main_3.py` demonstrates this behavior by successfully updating the password and raising exceptions for invalid attributes.

</details>

<details>
<summary><strong>Task 4: Hash password</strong></summary>

In this task, we will implement the `_hash_password` method in the `auth.py` file. This method takes in a password string as an argument and returns the password as a salted hash using the `bcrypt.hashpw` function.

### Password Hashing

- **bcrypt.hashpw**: This function applies a hashing algorithm to the password, creating a secure, salted hash that can be stored in the database. The returned value is in bytes, making it secure for use in authentication processes.
  
This method is essential for ensuring user passwords are securely stored in the database.

<details>
<summary><strong>Instructions Provided in Curriculum</strong></summary>

You will define a `_hash_password` method that takes in a password string argument and returns bytes. The returned bytes are a salted hash of the input password, hashed with `bcrypt.hashpw`.

```bash
bob@dylan:~$ cat main.py
#!/usr/bin/env python3
"""
Main file
"""
from auth import _hash_password

print(_hash_password("Hello Holberton"))

bob@dylan:~$ python3 main.py
b'$2b$12$eUDdeuBtrD41c8dXvzh95ehsWYCCAi4VH1JbESzgbgZT.eMMzi.G2'
bob@dylan:~$
```

</details>

### Step-by-Step Instructions

1. **Create  the `auth.py` file**:
   - Implement the `_hash_password` method in `auth.py`. This method takes in a password string and returns a salted hash of that password using `bcrypt.hashpw`.

   Here’s the code for `auth.py`:

   ```python
   #!/usr/bin/env python3
   '''
   This module contains methods for user authentication, including password hashing.
   '''
   import bcrypt

   def _hash_password(password: str) -> bytes:
       '''Hashes a password using bcrypt and returns the hashed password as bytes'''
       salt = bcrypt.gensalt()
       hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
       return hashed
   ```

2. **Create the test script**:

   Here’s the content of `main_4.py`:

   ```python
   #!/usr/bin/env python3
   '''
   This module contains a script to test the _hash_password method in auth.py.
   '''
   from auth import _hash_password

   print(_hash_password("Hello Holberton"))
   ```

3. **Make the `main_4.py` script executable**:
   - Ensure the test file `main_4.py` is executable:
   ```bash
   chmod +x main_4.py
   ```

4. **Run the test script**:
   - Execute the `main_4.py` script to verify that the password hashing method works as expected:
   ```bash
   ./main_4.py
   ```

5. **Expected Output**:

   The expected output should show the salted hash of the password:

   ```bash
   b'$2b$12$yWR1itCMO3AmEtRnnoGjeemAIyDhnz7Xxxk7.XOBjjSRUYodiQ8a.'
   ```

### Explanation

- **Why bcrypt is used**:
  - `bcrypt` is a robust library used for password hashing. It applies a hashing algorithm with salting, which ensures that even identical passwords produce different hashes. This makes it resistant to common attacks such as dictionary attacks.

- **Why this works**:
  - The `_hash_password` method uses `bcrypt.gensalt()` to generate a unique salt for each password. This salt is then combined with the password and hashed using `bcrypt.hashpw`. The resulting hash is stored as bytes and can be used later for password verification.

- **How it works**:
  - The method encodes the password into bytes, generates a salt, and hashes the password using the salt.
  - Running `main_4.py` demonstrates this behavior by hashing the provided password and printing the resulting salted hash.

</details>

<details>
<summary><strong>Task 5: Register user</strong></summary>

In this task, we implemented the `Auth.register_user` method in the `Auth` class. This method is responsible for registering a new user in the system by taking their email and password. It checks if a user with the provided email already exists in the database and raises a `ValueError` if so. If the email is not already registered, it securely hashes the password using `_hash_password` and adds the new user to the database.

### Error Handling

- **ValueError**: Raised if a user with the provided email already exists in the database.

<details>
<summary><strong>Instructions Provided in Curriculum</strong></summary>

You will implement the `Auth.register_user` method in the `Auth` class. This method should take mandatory email and password string arguments and return a `User` object. 

- If a user already exists with the given email, raise a `ValueError` with the message `User <user's email> already exists`.
- If the user does not exist, hash the password using `_hash_password`, save the user to the database, and return the `User` object.

```bash
bob@dylan:~$ cat main.py
#!/usr/bin/env python3
"""
Main file
"""
from auth import Auth

email = 'me@me.com'
password = 'mySecuredPwd'

auth = Auth()

try:
    user = auth.register_user(email, password)
    print("successfully created a new user!")
except ValueError as err:
    print("could not create a new user: {}".format(err))

try:
    user = auth.register_user(email, password)
    print("successfully created a new user!")
except ValueError as err:
    print("could not create a new user: {}".format(err))

bob@dylan:~$ python3 main.py
successfully created a new user!
could not create a new user: User me@me.com already exists
bob@dylan:~$
```

</details>

### Step-by-Step Instructions

1. **Update the `Auth` class**:
   - In the `auth.py` file, implement the `register_user` method. This method first checks if a user with the provided email already exists in the database. If the user exists, it raises a `ValueError`. Otherwise, it hashes the password using `_hash_password`, creates a new user, and adds them to the database.

   Here’s the content of `auth.py`:

   ```python
   #!/usr/bin/env python3
   '''
   This module handles user authentication.
   It provides: 
   - User registration with duplicate email checks.
   - Password hashing using bcrypt for security.
   '''

   import bcrypt
   from db import DB
   from user import User
   from sqlalchemy.orm.exc import NoResultFound


   def _hash_password(password: str) -> bytes:
       '''
       Hashes a password using bcrypt and returns the hashed password as bytes
       '''
       salt = bcrypt.gensalt()
       hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
       return hashed


   class Auth:
       '''Auth class to interact with the authentication database'''

       def __init__(self) -> None:
           '''Initialize the Auth class'''
           self._db = DB()

       def register_user(self, email: str, password: str) -> User:
           '''Registers a new user with a hashed password, returns the User object.
           
           Raises:
               ValueError: If a user with the given email already exists.
           '''
           try:
               # Check if the user already exists
               self._db.find_user_by(email=email)
               raise ValueError(f"User {email} already exists")
           except NoResultFound:
               # Hash the password and create a new user
               hashed_password = _hash_password(password)
               new_user = self._db.add_user(email, hashed_password)
               return new_user
   ```

2. **Create the test script**:

   Here’s the content of `main_5.py`:

   ```python
   #!/usr/bin/env python3
   '''
   This module contains a script to test the Auth.register_user method.
   '''
   from auth import Auth

   email = 'me@me.com'
   password = 'mySecuredPwd'

   auth = Auth()

   try:
       user = auth.register_user(email, password)
       print("successfully created a new user!")
   except ValueError as err:
       print(f"could not create a new user: {err}")

   # Attempting to register the same user again
   try:
       user = auth.register_user(email, password)
       print("successfully created a new user!")
   except ValueError as err:
       print(f"could not create a new user: {err}")
   ```

3. **Make the `main_5.py` script executable**:
   - Ensure the test file `main_5.py` is executable:
   ```bash
   chmod +x main_5.py
   ```

4. **Run the test script**:
   - Execute the `main_5.py` script to verify that user registration works and that duplicate registration attempts raise the appropriate error:
   ```bash
   ./main_5.py
   ```

5. **Expected Output**:

   The expected output should show that the first user registration is successful, while the second attempt to register the same user raises an error:

   ```bash
   successfully created a new user!
   could not create a new user: User me@me.com already exists
   ```

### Explanation

- **Why we check for existing users**:
  - The method first checks if a user with the provided email already exists. If the user exists, the method raises a `ValueError` to prevent duplicate user registrations.
  - This ensures that the system doesn’t allow multiple users with the same email address.

- **Why bcrypt is used for password hashing**:
  - To ensure that passwords are stored securely, the method hashes the password using `_hash_password` before storing it in the database.
  - Hashing passwords prevents plain text passwords from being stored, ensuring that even if the database is compromised, the passwords remain secure.

- **How it works**:
  - The method first calls `find_user_by` to check if the email is already registered. If the user is found, a `ValueError` is raised.
  - If the user is not found, the password is hashed and the user is added to the database using the `add_user` method.
  - Running `main_5.py` demonstrates this behavior by successfully registering a new user and preventing duplicate registrations.

</details>

<details>
<summary><strong>Task 6: Basic Flask app</strong></summary>

In this task, we set up a basic Flask app with a single GET route at `/` that returns a JSON response. The response contains the message `"Bienvenue"`. The app listens on all available network interfaces (`0.0.0.0`) on port `5000`. For testing in the browser, I use **localhost**, but for commands like `curl`, `0.0.0.0` is used. In **Postman**, both `localhost` and `0.0.0.0` can be used.

### Flask App

- **Route**: `GET /`
- **Response**: `{"message": "Bienvenue"}`

This task demonstrates setting up a simple Flask application and handling a basic GET request.

<details>
<summary><strong>Instructions Provided in Curriculum</strong></summary>

You will set up a basic Flask app that has a single GET route (`"/"`) and use `flask.jsonify` to return a JSON payload of the form:

```json
{"message": "Bienvenue"}
```

Add the following code at the end of the module:

```python
if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
```

</details>

### Step-by-Step Instructions

1. **Create `app.py`**:
   - Create a new file named `app.py` in your project directory and add the following code:

   ```python
   #!/usr/bin/env python3
   '''
   This module sets up a basic Flask app with a single route.
   '''

   from flask import Flask, jsonify

   app = Flask(__name__)

   @app.route("/", methods=["GET"])
   def welcome():
       '''Handles GET request and returns a JSON message'''
       return jsonify({"message": "Bienvenue"})

   if __name__ == "__main__":
       app.run(host="0.0.0.0", port="5000")
   ```

2. **Make `app.py` executable**:
   - Before running the app, make sure the script is executable:
   ```bash
   chmod +x app.py
   ```

3. **Run the Flask app**:
   - You can run the app using:
   ```bash
   ./app.py
   ```

4. **Test the app using `curl`**:
   - You can use `curl` to test the app using `0.0.0.0`:
   ```bash
   curl http://0.0.0.0:5000/
   ```
   - **Expected Output**:
   ```json
   {"message": "Bienvenue"}
   ```

5. **Testing in the Browser (`localhost`)**:
   - You can test the app in a browser by navigating to:
   ```bash
   http://localhost:5000/
   ```

6. **Testing with Postman (Optional)**:
   - In Postman, you can use either `localhost` or `0.0.0.0`:
     1. Open **Postman**.
     2. Create a new request.
     3. Set the request method to **GET**.
     4. Enter the URL:
        - `http://localhost:5000/`
        - or `http://0.0.0.0:5000/`
     5. Click **Send**.
     6. The expected response will be:
     ```json
     {"message": "Bienvenue"}
     ```

7. **Reminder to Terminate Before Next Task**:
   - Before starting the next task, make sure to terminate the running Flask server. If you don’t, the port (`5000`) will remain busy, and you won’t be able to start a new server instance:
   ```bash
   CTRL + C
   ```

### Explanation

- **Why Flask**: Flask is a lightweight web framework that makes it easy to create simple web applications with minimal setup. In this case, it handles a basic GET request.
  
- **Why jsonify**: Flask’s `jsonify` function automatically converts Python dictionaries into JSON responses. This ensures the response is correctly formatted as JSON and sets the appropriate content type (`application/json`).

- **How it works**: 
   - The `app.route("/")` decorator sets up the root route (`/`) to handle GET requests. The `welcome` function returns a JSON response when the route is accessed. 
   - The app runs on `0.0.0.0` (all network interfaces) and listens on port `5000`. I use `localhost` in the browser for local testing.
   - Running `curl http://0.0.0.0:5000/` or using Postman with `localhost` or `0.0.0.0` returns the expected JSON response.

</details>

<details>
<summary><strong>Task 7: Register user (POST /users)</strong></summary>

In this task, we implemented the `/users` endpoint that handles user registration via a POST request. The endpoint expects two form data fields: `"email"` and `"password"`. If the user is not already registered, it will create the user and return a success message. If the user is already registered, it will return an error message with a 400 status code.

### POST /users

- **Route**: `POST /users`
- **Request form data**: `email` and `password`
- **Success response**:  
  ```json
  {"email": "<registered email>", "message": "user created"}
  ```
- **Error response (email already registered)**:  
  ```json
  {"message": "email already registered"}
  ```
- **Error status code**: 400

<details>
<summary><strong>Instructions Provided in Curriculum</strong></summary>

You will implement the `/users` route to register a new user. The endpoint should:
- Accept two form data fields: `email` and `password`.
- Register the user if they don't already exist and return a success message.
- If the user is already registered, catch the exception and return a 400 status code with the appropriate error message.

</details>

### Step-by-Step Instructions

1. **Update `app.py`**:
   - In `app.py`, implement the `/users` route:
   
 ```python
#!/usr/bin/env python3
'''
This module sets up a basic Flask app with user registration functionality.
'''

from flask import Flask, jsonify, request
from auth import Auth

app = Flask(__name__)
AUTH = Auth()


@app.route("/", methods=["GET"])
def welcome():
    '''Handles GET request and returns a JSON message'''
    return jsonify({"message": "Bienvenue"})


@app.route("/users", methods=["POST"])
def register_user():
    '''Handles user registration via POST /users route'''
    email = request.form.get("email")
    password = request.form.get("password")

    try:
        user = AUTH.register_user(email, password)
        return jsonify({"email": email, "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")

```

2. **Make `app.py` executable**:
   - Before running the app, make sure the script is executable:
   ```bash
   chmod +x app.py
   ```

3. **Run the Flask app**:
   - Start the Flask app by running:
   ```bash
   ./app.py
   ```

4. **Testing the `/users` endpoint using `curl`**:
   - **To register a new user**:
     ```bash
     curl -XPOST localhost:5000/users -d 'email=bob@me.com' -d 'password=mySuperPwd'
     ```
     Expected output:
     ```json
     {"email":"bob@me.com","message":"user created"}
     ```

   - **To attempt registering the same user again**:
     ```bash
     curl -XPOST localhost:5000/users -d 'email=bob@me.com' -d 'password=mySuperPwd'
     ```
     Expected output:
     ```json
     {"message":"email already registered"}
     ```

5. **Testing the `/users` endpoint in the browser**:
   - You can also use an HTML form to send the `POST` request in the browser. However, testing directly in the browser is more difficult for POST requests.
   - Instead, testing tools like **Postman** are recommended for POST requests.

6. **Testing the `/users` endpoint using Postman**:
   - Open **Postman** and create a new request.
   - Set the method to **POST**.
   - Set the URL to `http://localhost:5000/users`.
   - Under the **Body** tab, select **x-www-form-urlencoded**.
   - Add two keys:  
     - **Key**: `email` | **Value**: `bob@me.com`
     - **Key**: `password` | **Value**: `mySuperPwd`
   - Click **Send**.  
     You should receive a success message:
     ```json
     {"email":"bob@me.com","message":"user created"}
     ```

   - Try sending the request again with the same email. This time, you should receive:
     ```json
     {"message":"email already registered"}
     ```

7. **Reminder to Terminate Before Next Task**:
   - Before starting the next task, make sure to terminate the running Flask server. If you don’t, the port (`5000`) will remain busy, and you won’t be able to start a new server instance:
   ```bash
   CTRL + C
   ```

### Explanation

- **Why POST**: The `POST` method is used when creating new resources, such as registering a new user. Form data is sent securely through the request body.
  
- **Why check for existing users**: The route checks if a user with the provided email is already registered to avoid duplicates. If the user exists, it raises a `ValueError`, and the API responds with a 400 status code.

- **How it works**: 
   - The endpoint processes the form data for `email` and `password`.
   - It attempts to register the user via `AUTH.register_user`. If successful, it returns a success message.
   - If the user already exists, it catches the exception and returns a 400 error message.

</details>


<details>
<summary><strong>Task 8: Credentials validation (Auth.valid_login)</strong></summary>

In this task, we implemented the `Auth.valid_login` method, which checks if the provided email and password are valid for an existing user. This method returns `True` if the credentials are correct and `False` otherwise.

### Auth.valid_login

- **Method**: `valid_login(email: str, password: str) -> bool`
- **Parameters**:
  - `email`: The user’s email address.
  - `password`: The user’s plaintext password.
- **Returns**:
  - `True`: If the email exists and the password matches the hashed password stored in the database.
  - `False`: If the email does not exist or the password is incorrect.

<details>
<summary><strong>Instructions Provided in Curriculum</strong></summary>

In this task, you will implement the Auth.valid_login method. It should expect email and password required arguments and return a boolean.
Try locating the user by email. If it exists, check the password with bcrypt.checkpw. If it matches return True. In any other case, return False.


</details>

### Step-by-Step Instructions

1. **Update `auth.py`**:
   - Add the `valid_login` method to the `Auth` class in `auth.py`:

```python
#!/usr/bin/env python3
'''
This module handles user authentication.
Includes:
User registration with duplicate email checks.
Password hashing using bcrypt for security.
Credentials validation to authenticate users.
'''

import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound


def _hash_password(password: str) -> bytes:
    '''
    Hashes a password using bcrypt and returns the hashed password as bytes
    '''
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed


class Auth:
    '''Auth class to interact with the authentication database'''

    def __init__(self) -> None:
        '''Initialize the Auth class'''
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        '''
        Registers a new user with a hashed password and returns the User object
        '''
        try:
            # Check if the user already exists
            self._db.find_user_by(email=email)
            raise ValueError(f"User {email} already exists")
        except NoResultFound:
            # Hash the password and create a new user
            hashed_password = _hash_password(password)
            new_user = self._db.add_user(email, hashed_password)
            return new_user

    def valid_login(self, email: str, password: str) -> bool:
        '''
        Validates the email and password of a user.

        Returns:
            bool: True if credentials are valid, False otherwise
        '''
        try:
            # Find the user by email
            user = self._db.find_user_by(email=email)
            # Check if the password matches using bcrypt
            if bcrypt.checkpw(password.encode('utf-8'), user.hashed_password):
                return True
            return False
        except (NoResultFound, ValueError):
            return False

```

2. **Make `auth.py` executable**:
   - Ensure the script is executable:
   ```bash
   chmod +x auth.py
   ```

3. **Test the `valid_login` method**:
   -  `main_8.py`:

   ```python
   #!/usr/bin/env python3
   """
   Main file to test Auth.valid_login
   """
   from auth import Auth

   email = 'bob@bob.com'
   password = 'MyPwdOfBob'
   auth = Auth()

   auth.register_user(email, password)

   print(auth.valid_login(email, password))   # Expected output: True
   print(auth.valid_login(email, "WrongPwd"))  # Expected output: False
   print(auth.valid_login("unknown@email", password))  # Expected output: False
   ```

4. **Run the test script**:
   ```bash
   ./main_8.py
   ```

5. **Expected Output**:
   ```bash
   True
   False
   False
   ```

### Explanation

- **Why bcrypt**: Using `bcrypt.checkpw` ensures that passwords are securely compared without revealing the actual password in plaintext.
  
- **Why valid_login**: The `valid_login` method allows for secure verification of user credentials by matching the provided password against the stored hashed password in the database. This prevents unauthorized access while maintaining security.

- **How it works**: 
   - The method retrieves the user by email. 
   - If the user exists, it uses `bcrypt.checkpw` to verify the provided password against the stored hash.
   - If the credentials match, it returns `True`; otherwise, it returns `False`.

</details>




<details>
<summary><strong>Task 9: Generate UUIDs (_generate_uuid)</strong></summary>

In this task, we implemented the `_generate_uuid` function, which generates a new UUID and returns its string representation. This function is private to the `auth.py` module and is meant for internal use only.

### _generate_uuid

- **Function**: `_generate_uuid() -> str`
- **Returns**: A string representation of a new UUID.
- **Purpose**: To generate unique identifiers for various purposes, such as user sessions.

<details>
<summary><strong>Instructions Provided in Curriculum</strong></summary>

In this task, you will implement a `_generate_uuid` function in the `auth.py` module. The function should return a string representation of a new UUID. Use the `uuid` module.

Note that the method is private to the auth module and should NOT be used outside of it.

</details>

### Step-by-Step Instructions

1. **Update `auth.py`**:
   - Add the `_generate_uuid` function to `auth.py`:

```python
   #!/usr/bin/env python3
'''
This module handles user authentication.
Includes:
User registration with duplicate email checks.
Password hashing using bcrypt for security.
Credentials validation to authenticate users.
Generates UUIDs for unique user identification.
'''

import bcrypt
import uuid
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound


def _hash_password(password: str) -> bytes:
    '''
    Hashes a password using bcrypt and returns the hashed password as bytes
    '''
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed


def _generate_uuid() -> str:
    '''
    Generates a new UUID and returns it as a string
    '''
    return str(uuid.uuid4())


class Auth:
    '''Auth class to interact with the authentication database'''

    def __init__(self) -> None:
        '''Initialize the Auth class'''
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        '''
        Registers a new user with a hashed password and returns the User object
        '''
        try:
            # Check if the user already exists
            self._db.find_user_by(email=email)
            raise ValueError(f"User {email} already exists")
        except NoResultFound:
            # Hash the password and create a new user
            hashed_password = _hash_password(password)
            new_user = self._db.add_user(email, hashed_password)
            return new_user

    def valid_login(self, email: str, password: str) -> bool:
        '''
        Validates the email and password of a user.

        Returns:
            bool: True if credentials are valid, False otherwise
        '''
        try:
            # Find the user by email
            user = self._db.find_user_by(email=email)
            # Check if the password matches using bcrypt
            if bcrypt.checkpw(password.encode('utf-8'), user.hashed_password):
                return True
            return False
        except (NoResultFound, ValueError):
            return False

```

2. **Test the `_generate_uuid` function**:
   - To test the UUID generation, create a simple test script called `main_9.py`:

   ```python
   #!/usr/bin/env python3
   """
   Main file to test _generate_uuid
   """
   from auth import _generate_uuid

   print(_generate_uuid())  # Expected output: A unique UUID, e.g., '8d1d3f2b-4e88-4e72-a74e-1a7e6e41e0bb'
   ```

3. **Make `main_9.py` executable**:
   - Ensure the `main_9.py` script is executable:
   ```bash
   chmod +x main_9.py
   ```

4. **Run the test script**:
   - Run the script to see the UUID generated:
   ```bash
   ./main_9.py
   ```

5. **Expected Output**:
   - The output will be a unique UUID in string format, similar to:
     ```bash
     e.g. '8d1d3f2b-4e88-4e72-a74e-1a7e6e41e0bb'
     ```

### Explanation

- **Why UUIDs**: UUIDs are globally unique identifiers that are useful for ensuring that generated IDs, such as session tokens, are unique and not easily guessable.
  
- **Why `_generate_uuid` is private**: This function is intended for internal use within the `auth.py` module. By keeping it private, it helps ensure that UUID generation is handled consistently in the codebase and avoids misuse outside the module.

- **How it works**: 
   - The function leverages Python’s built-in `uuid` module to generate a UUID using `uuid.uuid4()`.
   - It converts the UUID object to a string with `str()` and returns it.

</details>


<details>
<summary><strong>Task 10: Get session ID (Auth.create_session)</strong></summary>

In this task, we implemented the `Auth.create_session` method, which generates and returns a session ID for a user. The method takes the user’s email, locates the user in the database, generates a new session ID, and stores it as the user’s `session_id`.

### Auth.create_session

- **Method**: `create_session(email: str) -> str`
- **Parameters**:
  - `email`: The user’s email address.
- **Returns**:
  - A new session ID as a string (UUID) if the user is found.
  - `None` if the user does not exist.

<details>
<summary><strong>Instructions Provided in Curriculum</strong></summary>

In this task, you will implement the `Auth.create_session` method. It takes an email string argument and returns the session ID as a string.

The method should find the user corresponding to the email, generate a new UUID, and store it in the database as the user’s session_id, then return the session ID.

Remember that only public methods of `self._db` can be used.

</details>

### Step-by-Step Instructions

1. **Update `auth.py`**:
   - Add the `create_session` method to the `Auth` class in `auth.py`:

```python
#!/usr/bin/env python3
'''
This module handles user authentication.
Includes:
- User registration with duplicate email checks.
- Password hashing using bcrypt for security.
- Credentials validation to authenticate users.
- Generates UUIDs for unique user identification.
- Creates session IDs for user authentication.
'''

import bcrypt
import uuid
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound


def _hash_password(password: str) -> bytes:
    '''
    Hashes a password using bcrypt and returns the hashed password as bytes
    '''
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode('utf-8'), salt)


def _generate_uuid() -> str:
    '''
    Generates a new UUID and returns it as a string
    '''
    return str(uuid.uuid4())


class Auth:
    '''Auth class to interact with the authentication database'''

    def __init__(self) -> None:
        '''Initialize the Auth class'''
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        '''
        Registers a new user with a hashed password and returns the User object
        '''
        try:
            self._db.find_user_by(email=email)
            raise ValueError(f"User {email} already exists")
        except NoResultFound:
            hashed_password = _hash_password(password)
            new_user = self._db.add_user(email, hashed_password)
            return new_user

    def valid_login(self, email: str, password: str) -> bool:
        '''
        Validates the email and password of a user.

        Returns:
            bool: True if credentials are valid, False otherwise
        '''
        try:
            user = self._db.find_user_by(email=email)
            if bcrypt.checkpw(password.encode('utf-8'), user.hashed_password):
                return True
            return False
        except (NoResultFound, ValueError):
            return False

    def create_session(self, email: str) -> str:
        '''
        Creates a new session ID for a user based on their email.

        Returns:
            str: The session ID or None if the user does not exist.
        '''
        try:
            # Find the user by email
            user = self._db.find_user_by(email=email)
            # Generate a new session ID
            session_id = _generate_uuid()
            # Update the user's session_id in the database
            self._db.update_user(user.id, session_id=session_id)
            return session_id
        except NoResultFound:
            return None

```

2. **Test the `create_session` method**:
   - Create a test script named `main_10.py`:

   ```python
   #!/usr/bin/env python3
   """
   Main file to test Auth.create_session
   """
   from auth import Auth

   email = 'bob@bob.com'
   password = 'MyPwdOfBob'
   auth = Auth()

   auth.register_user(email, password)

   print(auth.create_session(email))  # Expected output: A valid UUID (session ID)
   print(auth.create_session("unknown@email.com"))  # Expected output: None
   ```

3. **Make `main_10.py` executable**:
   ```bash
   chmod +x main_10.py
   ```

4. **Run the test script**:
   ```bash
   ./main_10.py
   ```

5. **Expected Output**:
   - If the user exists:
     ```bash
     e.g. '5a006849-343e-4a48-ba4e-bbd523fcca58'
     ```
   - If the user does not exist:
     ```bash
     None
     ```

### Explanation

- **Why session IDs**: Session IDs are used to maintain a user’s authentication state across multiple requests. They allow users to stay logged in after initial authentication.
  
- **Why UUIDs for session IDs**: UUIDs provide a unique and unpredictable session ID that enhances security by making it difficult to guess valid session identifiers.

- **How it works**: 
   - The `create_session` method locates a user by email.
   - If the user is found, it generates a unique session ID using `_generate_uuid` and updates the user’s session ID in the database.
   - If the user is not found, it returns `None`.

</details>

<details>
<summary><strong>Task 11: Log in (POST /sessions)</strong></summary>

In this task, we implemented the `/sessions` POST route to handle user login. The request is expected to contain `email` and `password` form data. If the login information is correct, a session ID is created and returned as a cookie.

### Endpoint: POST /sessions

- **Endpoint**: `/sessions`
- **Method**: `POST`
- **Request Body**:
  - `email`: The user's email.
  - `password`: The user's password.
- **Response**:
  - **200 OK**: If the login is successful, a session ID is created, and a cookie is set with the session ID. The response payload will be:
    ```json
    {"email": "<user email>", "message": "logged in"}
    ```
  - **401 Unauthorized**: If the login information is incorrect, the server responds with a 401 status:
    ```html
    <h1>Unauthorized</h1>
    ```

<details>
<summary><strong>Instructions Provided in Curriculum</strong></summary>

In this task, you will implement a login function to respond to the POST `/sessions` route.

The request is expected to contain form data with "email" and a "password" field.

If the login information is incorrect, use `flask.abort` to respond with a 401 HTTP status.

Otherwise, create a new session for the user, store the session ID as a cookie with the key "session_id" on the response, and return a JSON payload of the form:

```json
{"email": "<user email>", "message": "logged in"}
```

</details>

### Step-by-Step Instructions

1. **Update `app.py`**:
   - Add the login route to handle POST requests to `/sessions`:

```python
#!/usr/bin/env python3
'''
This module sets up a basic Flask app with user registration
and login functionality.
'''

from flask import Flask, jsonify, request, abort, make_response
from auth import Auth

app = Flask(__name__)
AUTH = Auth()


@app.route("/", methods=["GET"])
def welcome():
    '''Handles GET request and returns a JSON message'''
    return jsonify({"message": "Bienvenue"})


@app.route("/users", methods=["POST"])
def register_user():
    '''Handles user registration via POST /users route'''
    email = request.form.get("email")
    password = request.form.get("password")

    try:
        user = AUTH.register_user(email, password)
        return jsonify({"email": email, "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


@app.route("/sessions", methods=["POST"])
def login():
    '''Handles user login via POST /sessions route'''
    email = request.form.get("email")
    password = request.form.get("password")

    if not AUTH.valid_login(email, password):
        abort(401)

    # Create a session ID for the user
    session_id = AUTH.create_session(email)

    # Set the session_id as a cookie in the response
    response = make_response(jsonify({"email": email, "message": "logged in"}))
    response.set_cookie("session_id", session_id)

    return response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")

```

### Testing the `/sessions` Route

#### 1. Testing with `curl`:

After starting the Flask app, you can use the following curl commands to test the `/sessions` endpoint:

- **Register a user**:
   ```bash
   curl -XPOST localhost:5000/users -d 'email=bob@bob.com' -d 'password=mySuperPwd'
   ```
   Expected output:
   ```json
   {"email":"bob@bob.com","message":"user created"}
   ```

- **Log in the user**:
   ```bash
   curl -XPOST localhost:5000/sessions -d 'email=bob@bob.com' -d 'password=mySuperPwd' -v
   ```
   Expected output:
   ```json
   {"email":"bob@bob.com","message":"logged in"}
   ```

   In the verbose output, you will see the session ID set in the response:
   ```
   < Set-Cookie: session_id=<session_id_value>; Path=/
   ```

- **Test invalid login**:
   ```bash
   curl -XPOST localhost:5000/sessions -d 'email=bob@bob.com' -d 'password=wrongPwd' -v
   ```
   Expected output:
   ```
   < HTTP/1.0 401 UNAUTHORIZED
   ```

#### 2. Testing in the Browser:

You can test the login functionality in the browser by sending a POST request using JavaScript. Here’s how:

- Open the browser's developer tools (F12) and paste the following code into the console:
   ```javascript
   fetch('http://localhost:5000/sessions', {
       method: 'POST',
       headers: {
           'Content-Type': 'application/x-www-form-urlencoded',
       },
       body: new URLSearchParams({
           'email': 'bob@bob.com',
           'password': 'mySuperPwd'
       })
   })
   .then(response => response.json())
   .then(data => console.log(data))
   ```
   - If the login is successful, the browser console will display:
     ```json
     {"email":"bob@bob.com","message":"logged in"}
     ```

   - You can check the cookie set by the session using the browser's storage inspector (under Application > Cookies in the developer tools).

#### 3. Testing in Postman:

To test the login route in Postman:

- **Create a new POST request** in Postman:
   - **URL**: `http://localhost:5000/sessions`
   - **Body**: Set the request body to `x-www-form-urlencoded` and add the following fields:
     - `email`: `bob@bob.com`
     - `password`: `mySuperPwd`
   - **Send the request**. The expected response is:
     ```json
     {
         "email": "bob@bob.com",
         "message": "logged in"
     }
     ```

   - Check the **Cookies** tab in Postman to confirm the `session_id` cookie has been set.

### Explanation

- **Why the session ID**: Session IDs are important for maintaining a user’s authentication state across multiple requests. By setting the session ID in a cookie, the server can identify the user in subsequent requests.

</details>

<details>
<summary><strong>Task 12: Find user by session ID (Auth.get_user_from_session_id)</strong></summary>

In this task, we implemented the `Auth.get_user_from_session_id` method, which retrieves a user based on their session ID. If the session ID is `None` or no user is found, it returns `None`.

### Method: `Auth.get_user_from_session_id`

- **Method**: `get_user_from_session_id(session_id: str) -> User`
- **Parameters**:
  - `session_id`: The session ID of the user.
- **Returns**:
  - The user corresponding to the session ID, or `None` if the session ID is invalid or no user is found.

<details>
<summary><strong>Instructions Provided in Curriculum</strong></summary>

In this task, you will implement the `Auth.get_user_from_session_id` method. It takes a single `session_id` string argument and returns the corresponding User or `None`.

If the session ID is `None` or no user is found, return `None`. Otherwise, return the corresponding user.

Remember to only use public methods of `self._db`.

</details>

### Step-by-Step Instructions

1. **Update `auth.py`**:
   - Add the `get_user_from_session_id` method to handle session-based user retrieval:

```python
#!/usr/bin/env python3
'''
This module handles user authentication.
Includes:
- User registration with duplicate email checks.
- Password hashing using bcrypt for security.
- Credentials validation to authenticate users.
- Generates UUIDs for unique user identification.
- Creates session IDs for user authentication.
- Retrieves users based on session IDs.
'''

import bcrypt
import uuid
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound


def _hash_password(password: str) -> bytes:
    '''
    Hashes a password using bcrypt and returns the hashed password as bytes
    '''
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode('utf-8'), salt)


def _generate_uuid() -> str:
    '''
    Generates a new UUID and returns it as a string
    '''
    return str(uuid.uuid4())


class Auth:
    '''Auth class to interact with the authentication database'''

    def __init__(self) -> None:
        '''Initialize the Auth class'''
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        '''
        Registers a new user with a hashed password and returns the User object
        '''
        try:
            self._db.find_user_by(email=email)
            raise ValueError(f"User {email} already exists")
        except NoResultFound:
            hashed_password = _hash_password(password)
            new_user = self._db.add_user(email, hashed_password)
            return new_user

    def valid_login(self, email: str, password: str) -> bool:
        '''
        Validates the email and password of a user.

        Returns:
            bool: True if credentials are valid, False otherwise
        '''
        try:
            user = self._db.find_user_by(email=email)
            if bcrypt.checkpw(password.encode('utf-8'), user.hashed_password):
                return True
            return False
        except (NoResultFound, ValueError):
            return False

    def create_session(self, email: str) -> str:
        '''
        Creates a new session ID for a user based on their email.

        Returns:
            str: The session ID or None if the user does not exist.
        '''
        try:
            user = self._db.find_user_by(email=email)
            session_id = _generate_uuid()
            self._db.update_user(user.id, session_id=session_id)
            return session_id
        except NoResultFound:
            return None

    def get_user_from_session_id(self, session_id: str) -> User:
        '''
        Retrieves a user from the session ID.
        '''
        if session_id is None:
            return None
        try:
            user = self._db.find_user_by(session_id=session_id)
            return user
        except NoResultFound:
            return None

```

2. **Test the `get_user_from_session_id` method**:
   - Create a test script named `main_12.py`:

   ```python
   #!/usr/bin/env python3
   """
   Main file to test Auth.get_user_from_session_id
   """
   from auth import Auth

   auth = Auth()

   # Assume user has already logged in and session ID is generated
   email = 'bob@bob.com'
   password = 'MyPwdOfBob'

   # Register and create a session
   auth.register_user(email, password)
   session_id = auth.create_session(email)

   # Retrieve user from session ID
   print(auth.get_user_from_session_id(session_id))  # Should print the user object

   # Test invalid session ID
   print(auth.get_user_from_session_id("invalid_session_id"))  # Should print None

   # Test None session ID
   print(auth.get_user_from_session_id(None))  # Should print None
   ```

3. **Make `main_12.py` executable**:
   ```bash
   chmod +x main_12.py
   ```

4. **Run the test script**:
   ```bash
   ./main_12.py
   ```

5. **Expected Output**:
   - The first call should print the user object based on the valid session ID.
   - The second call with an invalid session ID should print `None`.
   - The third call with `None` as the session ID should also print `None`.

### Detailed Usage and Explanation

- **Why session-based user retrieval**: This functionality allows the app to retrieve user data based on a session ID, which is essential for maintaining user authentication across multiple requests.
  
- **Error handling**: If the session ID is invalid or `None`, the method will gracefully return `None` instead of raising an exception.

</details>

<details>
<summary><strong>Task 13: Destroy session (Auth.destroy_session)</strong></summary>

In this task, we implemented the `Auth.destroy_session` method, which takes a `user_id` and destroys the session by setting the session ID to `None`.

### Method: `Auth.destroy_session`

- **Method**: `destroy_session(user_id: int) -> None`
- **Parameters**:
  - `user_id`: The ID of the user whose session needs to be destroyed.
- **Returns**:
  - `None`

<details>
<summary><strong>Instructions Provided in Curriculum</strong></summary>

In this task, you will implement the `Auth.destroy_session` method. The method takes a single `user_id` integer argument and returns `None`.

The method updates the corresponding user’s session ID to `None`.

Remember to only use public methods of `self._db`.

</details>

### Step-by-Step Instructions

1. **Update `auth.py`**:
   - Add the `destroy_session` method to handle session destruction:

   ```python
   def destroy_session(self, user_id: int) -> None:
       '''
       Destroys a user session by setting the session ID to None.
       '''
       try:
           self._db.update_user(user_id, session_id=None)
       except NoResultFound:
           pass
   ```

2. **Test the `destroy_session` method**:
   - Create a test script named `main_13.py`:

```python
#!/usr/bin/env python3
'''
This module handles user authentication.
Includes:
- User registration with duplicate email checks.
- Password hashing using bcrypt for security.
- Credentials validation to authenticate users.
- Generates UUIDs for unique user identification.
- Creates session IDs for user authentication.
- Retrieves users based on session IDs.
- Destroys user sessions by setting session ID to None.
'''

import bcrypt
import uuid
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound


def _hash_password(password: str) -> bytes:
    '''
    Hashes a password using bcrypt and returns the hashed password as bytes
    '''
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode('utf-8'), salt)


def _generate_uuid() -> str:
    '''
    Generates a new UUID and returns it as a string
    '''
    return str(uuid.uuid4())


class Auth:
    '''Auth class to interact with the authentication database'''

    def __init__(self) -> None:
        '''Initialize the Auth class'''
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        '''
        Registers a new user with a hashed password and returns the User object
        '''
        try:
            self._db.find_user_by(email=email)
            raise ValueError(f"User {email} already exists")
        except NoResultFound:
            hashed_password = _hash_password(password)
            new_user = self._db.add_user(email, hashed_password)
            return new_user

    def valid_login(self, email: str, password: str) -> bool:
        '''
        Validates the email and password of a user.

        Returns:
            bool: True if credentials are valid, False otherwise
        '''
        try:
            user = self._db.find_user_by(email=email)
            if bcrypt.checkpw(password.encode('utf-8'), user.hashed_password):
                return True
            return False
        except (NoResultFound, ValueError):
            return False

    def create_session(self, email: str) -> str:
        '''
        Creates a new session ID for a user based on their email.
        '''
        try:
            user = self._db.find_user_by(email=email)
            session_id = _generate_uuid()
            self._db.update_user(user.id, session_id=session_id)
            return session_id
        except NoResultFound:
            return None

    def get_user_from_session_id(self, session_id: str) -> User:
        '''
        Retrieves a user from the session ID.
        '''
        if session_id is None:
            return None
        try:
            user = self._db.find_user_by(session_id=session_id)
            return user
        except NoResultFound:
            return None

    def destroy_session(self, user_id: int) -> None:
        '''
        Destroys a user session by setting the session ID to None.
        '''
        try:
            self._db.update_user(user_id, session_id=None)
        except NoResultFound:
            pass

```

3. **Make `main_13.py` executable**:
   ```bash
   chmod +x main_13.py
   ```

4. **Run the test script**:
   ```bash
   ./main_13.py
   ```

5. **Expected Output**:
   - The first `print` should return the user object before the session is destroyed:
     ```
     <user.User object at 0x7f639c8c6dd0>
     ```
   - The second `print` should return `None` after the session is destroyed:
     ```
     None
     ```

### Detailed Usage and Explanation

- **Why destroy a session**: Destroying a session is essential for logging a user out and invalidating the session ID, preventing further access.
  
- **How it works**: The `destroy_session` method takes a `user_id` and updates the user's session ID to `None`. This makes the session ID invalid, and any subsequent attempts to retrieve the user using that session ID will return `None`.

</details>

<details>
<summary><strong>Task 14: Log out (DELETE /sessions)</strong></summary>

In this task, we implemented the `DELETE /sessions` route to log out a user by destroying their session. The session ID is expected to be stored as a cookie, and if the session exists, it will be destroyed, logging the user out and redirecting them to the home page (`GET /`). If no valid session exists, a `403 Forbidden` status is returned.

### Endpoint: DELETE /sessions

- **Endpoint**: `/sessions`
- **Method**: `DELETE`
- **Request**: The session ID is expected to be in the `session_id` cookie.
- **Response**:
  - **302 Found**: If the session ID is valid, the session is destroyed and the user is redirected to the home page (`/`).
  - **403 Forbidden**: If the session ID is invalid or missing, the server responds with a `403 Forbidden` status.

<details>
<summary><strong>Instructions Provided in Curriculum</strong></summary>

In this task, you will implement a logout function to respond to the `DELETE /sessions` route.

The request is expected to contain the session ID as a cookie with key `"session_id"`.

Find the user with the requested session ID. If the user exists, destroy the session and redirect the user to `GET /`. If the user does not exist, respond with a `403 HTTP` status.

</details>

### Step-by-Step Instructions

1. **Update `app.py`**:
   - Add the `logout` route to handle DELETE requests to `/sessions`.

```python
#!/usr/bin/env python3
'''
This module sets up a basic Flask app with user registration,
login, and session management functionality.
'''

from flask import Flask, jsonify, request, abort, make_response, redirect
from auth import Auth

app = Flask(__name__)
AUTH = Auth()


@app.route("/", methods=["GET"])
def welcome():
    '''Handles GET request and returns a JSON message'''
    return jsonify({"message": "Bienvenue"})


@app.route("/users", methods=["POST"])
def register_user():
    '''Handles user registration via POST /users route'''
    email = request.form.get("email")
    password = request.form.get("password")

    try:
        user = AUTH.register_user(email, password)
        return jsonify({"email": email, "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


@app.route("/sessions", methods=["POST"])
def login():
    '''Handles user login via POST /sessions route'''
    email = request.form.get("email")
    password = request.form.get("password")

    if not AUTH.valid_login(email, password):
        abort(401)

    # Create a session ID for the user
    session_id = AUTH.create_session(email)

    # Set the session_id as a cookie in the response
    response = make_response(jsonify({"email": email, "message": "logged in"}))
    response.set_cookie("session_id", session_id)

    return response


@app.route("/sessions", methods=["DELETE"])
def logout():
    '''Handles user logout via DELETE /sessions route'''
    session_id = request.cookies.get("session_id")

    if not session_id:
        abort(403)

    user = AUTH.get_user_from_session_id(session_id)

    if not user:
        abort(403)

    # Destroy the user's session
    AUTH.destroy_session(user.id)

    # Redirect the user to the home page
    return redirect("/")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
```

2. **Run the Flask App**:
   - Before testing with curl or any other tool, you need to run the Flask app by opening a terminal and running the following command:
     ```bash
     ./app.py
     ```

   - You should see output like this, indicating the app is running:
     ```
     * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
     ```

3. **Test the `logout` route**:

#### 1. Testing with `curl`:

- **Register and log in a user**:
   ```bash
   curl -XPOST localhost:5000/users -d 'email=bob@bob.com' -d 'password=mySuperPwd'
   curl -XPOST localhost:5000/sessions -d 'email=bob@bob.com' -d 'password=mySuperPwd' -v
   ```

   The output should include the `Set-Cookie` header containing the session ID:
   ```
   < Set-Cookie: session_id=<session_id_value>; Path=/
   ```

- **Log out the user**:
   ```bash
   curl -XDELETE localhost:5000/sessions -b "session_id=<session_id>" -v
   ```

   Expected output:
   - On successful logout, the output should show:
     ```
     < HTTP/1.0 302 FOUND
     < Location: /
     ```

   - If the session ID is missing or invalid, the output should show:
     ```
     < HTTP/1.0 403 FORBIDDEN
     ```

#### 2. Testing in the Browser:

- **Log in**:
   - Perform a POST request to `/sessions` using JavaScript to log in the user and receive the session cookie.

- **Log out**:
   - In the browser's console, run:
     ```javascript
     fetch('http://localhost:5000/sessions', {
         method: 'DELETE',
         credentials: 'include'
     })
     .then(response => {
         if (response.status === 403) {
             console.log("Logout failed: Invalid session");
         } else {
             console.log("Logout successful");
             window.location.href = "/";
         }
     });
     ```

- The user should be logged out, and the page will be redirected to `/` upon success.

#### 3. Testing in Postman:

- **Create a new DELETE request**:
   - **URL**: `http://localhost:5000/sessions`
   - In the **Headers** section, ensure that you include the `Cookie` header with the `session_id`:
     ```
     session_id=<session_id_value>
     ```

- **Expected behavior**:
   - If the session is valid, Postman will show a `302` response and redirect you to `/`.
   - If the session is invalid, you will receive a `403 Forbidden` response.

### Explanation

- **Why log out functionality is important**: This functionality allows users to securely log out by destroying their session. Once logged out, the session ID is invalid, preventing further access.
  
- **Testing in multiple environments**: Using `curl`, Postman, and the browser ensures that the app handles logout correctly in different scenarios.

</details>


<details>
<summary><strong>Task 15: User profile (GET /profile)</strong></summary>

In this task, we implemented the `GET /profile` route to retrieve a user’s profile using their session ID stored in a cookie. The session ID is used to find the corresponding user. If valid, the user’s email is returned in the response. If invalid, a `403 Forbidden` status is returned.

### Endpoint: GET /profile

- **Endpoint**: `/profile`
- **Method**: `GET`
- **Request**: The session ID is expected to be in the `session_id` cookie.
- **Response**:
  - **200 OK**: If the session ID is valid, the response contains the user’s email in JSON format:
    ```json
    {"email": "<user email>"}
    ```
  - **403 Forbidden**: If the session ID is invalid or no user is found, a `403 Forbidden` response is returned.

<details>
<summary><strong>Instructions Provided in Curriculum</strong></summary>

In this task, you will implement a profile function to respond to the `GET /profile` route.

The request is expected to contain a session_id cookie. Use it to find the user. If the user exists, respond with a 200 HTTP status and the following JSON payload:

```json
{"email": "<user email>"}
```

If the session ID is invalid or the user does not exist, respond with a `403 HTTP` status.

</details>

### Step-by-Step Instructions

1. **Update `app.py`**:
   - Add the `profile` route to handle GET requests to `/profile`:

   ```python
   @app.route("/profile", methods=["GET"])
   def profile():
       '''Handles user profile retrieval via GET /profile route'''
       session_id = request.cookies.get("session_id")

       if not session_id:
           abort(403)

       user = AUTH.get_user_from_session_id(session_id)

       if not user:
           abort(403)

       # Return the user's email in the response
       return jsonify({"email": user.email})
   ```

2. **Run the Flask App**:
   - Make sure the Flask app is running:
     ```bash
     ./app.py
     ```

   - You should see output like this, indicating the app is running:
     ```
     * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
     ```

3. **Test the `profile` route**:

#### 1. Testing with `curl`:

- **Register and log in a user**:
   ```bash
   curl -XPOST localhost:5000/users -d 'email=bob@bob.com' -d 'password=mySuperPwd'
   curl -XPOST localhost:5000/sessions -d 'email=bob@bob.com' -d 'password=mySuperPwd' -v
   ```

   The output should include the `Set-Cookie` header with the session ID:
   ```
   < Set-Cookie: session_id=<session_id_value>; Path=/
   ```

- **Get the user’s profile**:
   Replace `<session_id_value>` with the actual session ID you received in the login response:
   ```bash
   curl -XGET localhost:5000/profile -b "session_id=<session_id_value>" -v
   ```

   If the session is valid, you will get the user’s email:
   ```
   {"email": "bob@bob.com"}
   ```

- **Invalid session test**:
   ```bash
   curl -XGET localhost:5000/profile -b "session_id=invalidsessionid" -v
   ```

   This should return a `403 Forbidden` response:
   ```
   < HTTP/1.0 403 FORBIDDEN
   ```

#### 2. Testing in the Browser:

- **Log in**:
   - First, log in using the `/sessions` route to create a session cookie:
     ```javascript
     fetch('http://localhost:5000/sessions', {
         method: 'POST',
         body: new URLSearchParams({
             email: 'bob@bob.com',
             password: 'mySuperPwd'
         }),
         credentials: 'include'
     }).then(response => response.json())
       .then(data => console.log(data));
     ```

- **Retrieve Profile**:
   - Once logged in, open the browser’s console and run this fetch request to get the profile:
     ```javascript
     fetch('http://localhost:5000/profile', {
         method: 'GET',
         credentials: 'include'
     })
     .then(response => response.json())
     .then(data => console.log(data));
     ```

   - You should see the logged-in user’s email in the console:
     ```json
     {"email": "bob@bob.com"}
     ```

#### 3. Testing in Postman:

- **Log in**:
   - Use a **POST** request to `http://localhost:5000/sessions` with form data:
     - **email**: `bob@bob.com`
     - **password**: `mySuperPwd`

   - In the **Cookies** section, you should see the `session_id`.

- **Retrieve Profile**:
   - Use a **GET** request to `http://localhost:5000/profile`.
   - In the **Headers** section, add the `Cookie` header with the `session_id`:
     ```
     session_id=<session_id_value>
     ```

   - You will receive a response containing the user’s email:
     ```json
     {"email": "bob@bob.com"}
     ```

- **Invalid session**:
   - If you use an invalid session ID, you will receive a `403 Forbidden` response.



### Explanation

- **Purpose of the `profile` route**:  
  The `/profile` route is used to allow authenticated users to retrieve their own profile information using a session ID stored in their browser or client as a cookie. This is a common feature in web applications, allowing users to see or edit their personal data after logging in.

- **Session ID-based Authentication**:  
  The session ID is a unique identifier that is generated when the user logs in. This session ID is stored in a cookie on the client-side and is sent with each request to the server. In this task, the session ID is used to find the corresponding user and return their email address as part of their profile information.

- **Security Consideration**:  
  The session ID is essential for ensuring that only logged-in users can access their profile. If the session ID is missing or invalid, the server responds with a `403 Forbidden` status to protect sensitive user information. This ensures that users can only retrieve their own information and that their session remains private and secure.

- **Testing Across Environments**:  
  Testing the `/profile` route in multiple environments, using `curl`, the browser, and Postman, ensures that the functionality works in different client scenarios. For instance, `curl` simulates a command-line HTTP client, the browser tests front-end behavior, and Postman provides a controlled environment for API requests.

- **Common Error Handling**:  
  If a user provides an invalid or missing session ID, the server responds with a `403 Forbidden` status. This is important for maintaining the security of user data, as unauthorized access attempts are denied.

</details>
