
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

2. **Make the `main.py` script executable**:
   - In the terminal, run the following command to ensure the `main.py` script is executable:
   ```bash
   chmod +x main.py
   ```

3. **Test the model**:
   - Create a file `main.py` and add the following script to test your model and print out the table and column details:
   
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
   - Execute the `main.py` file to verify that the model is correctly created:
   ```bash
   python3 main.py
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
  - When you run `main.py`, SQLAlchemy introspects the `User` class, and the `__table__` attribute holds the table structure.
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
   - Update `main_1.py` to test the functionality of the `add_user` method.

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
   python3 main_1.py
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
   - Update `main_2.py` to test the functionality of the `find_user_by` method.

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
   python3 main_2.py
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
   - Update `main_3.py` to test the functionality of the `update_user` method.

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
   python3 main_3.py
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
