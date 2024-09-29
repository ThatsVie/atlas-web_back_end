# Redis Basic

## Resources

  - [Redis commands](https://redis.io/docs/latest/commands/)
  - [Redis Python client](https://redis-py.readthedocs.io/en/stable/)
  - [How to Use Redis With Python](https://realpython.com/python-redis/)
  - [Redis Crash Course Tutorial](https://www.youtube.com/watch?v=Hbt56gFj998)

## Learning Objectives

- Use Redis for basic operations
- Use Redis as a simple cache


## Requirements

<details>
  <summary>General</summary>

  - All of your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.9)
  - All of your files should end with a new line
  - A `README.md` file, at the root of the folder of the project, is mandatory
  - The first line of all your files should be exactly `#!/usr/bin/env python3`
  - Your code should use the `pycodestyle` style (version 2.5)
  - All your modules should have documentation (e.g., `python3 -c 'print(__import__("my_module").__doc__)'`)
  - All your classes should have documentation (e.g., `python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
  - All your functions and methods should have documentation (e.g., `python3 -c 'print(__import__("my_module").my_function.__doc__)' and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)`)
  - Documentation is not a simple word but a real sentence explaining the purpose of the module, class, or method. The length of it will be verified.
  - All your functions and coroutines must be type-annotated.
</details>


## Installation

**Install Redis on Ubuntu 18.04**

  ```bash
  $ sudo apt-get -y install redis-server
  $ pip3 install redis
  $ sed -i "s/bind .*/bind 127.0.0.1/g" /etc/redis/redis.conf
  ```

## Troubleshooting

### Issue: Permission Denied When Modifying redis.conf

  When running the `sed` command to modify `/etc/redis/redis.conf`, a "Permission denied" error may occur due to the file being a system configuration file. To resolve this, the command should be run with `sudo`:

  ```bash
  sudo sed -i "s/bind .*/bind 127.0.0.1/g" /etc/redis/redis.conf
  ```

  Using `sudo` ensures the necessary permissions are granted to edit the configuration file.
</details>

**Use Redis in a container**

  Redis server is stopped by default. When you are starting a container, you should start it with:

  ```bash
  sudo service redis-server start
  ```

</details>


## Tasks and Usage

### Task 0: Writing Strings to Redis

In this task, we implemented a `store` method in the `Cache` class to store data in Redis. The method generates a random key using `uuid`, stores the data in Redis using the generated key, and returns the key. The data can be a string, bytes, integer, or float.

<details>
  <summary><strong>Curriculum Instruction</strong></summary>

- Create a `Cache` class. In the `__init__` method, store an instance of the Redis client as a private variable named `_redis` (using `redis.Redis()`) and flush the instance using `flushdb`.
- Create a `store` method that takes a `data` argument and returns a string.
- The `store` method should:
  - Generate a random key (e.g., using `uuid`),
  - Store the input data in Redis using the random key, and
  - Return the generated key.
- Ensure correct type annotations for the `store` method. The `data` argument can be a `str`, `bytes`, `int`, or `float`.
</details>

<details>
  <summary><strong>Steps and Code Implementation</strong></summary>

### Steps:

1. **Initialize the Redis Client**: In the `__init__` method, we instantiate the Redis client and flush the database to clear any previous data. This ensures that each time we run the script, we start with a clean Redis instance.
   ```python
   self._redis = redis.Redis()
   self._redis.flushdb()
   ```

2. **Create the `store` Method**: This method generates a random key using `uuid`, stores the provided data in Redis under that key, and returns the key.
   - The data can be of various types (`str`, `bytes`, `int`, or `float`), and we used type annotations to ensure flexibility.
   - Redis automatically converts the data to byte strings when stored.
   ```python
   def store(self, data: Union[str, bytes, int, float]) -> str:
       key = str(uuid.uuid4())
       self._redis.set(key, data)
       return key
   ```

3. **Type Annotations**: The method is annotated to ensure that `data` can accept `str`, `bytes`, `int`, or `float`, and it returns the key as a `str`.

#### Code:
```python
#!/usr/bin/env python3
'''
This module provides a Cache class that interacts with Redis
to store and retrieve data.
It's like a pug hiding its toys in a sea of life's meaningless chaos
Redis is the pug's secret vault amidst the void.
'''
import redis
import uuid
from typing import Union


class Cache:
    '''
    Cache class that interacts with Redis, like storing away the things that
    make sense in a world that doesn't.
    '''

    def __init__(self):
        '''
        Initialize the Redis client and flush the database.
        You know that feeling when you clear your mind after an
        existential crisis, only to prepare for another one?
        That's flushdb. Wipe it all away and start again,
        like a pug waking up each day ready for belly rubs despite everything.
        '''
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        '''
        Store data in Redis and return the generated key.
        It's like trying to keep track of all the things
        that don't really matter, but you're giving them names anyway.
        Just like a pug hiding its bones in random spots, Redis gives each
        piece of data a unique name, as if that makes life more organized.
        '''
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
```

4. **Testing**: To test the `store` method, we store a string (in byte form) and then retrieve it from Redis using the generated key.

#### 0-main.py:
```python
#!/usr/bin/env python3
"""
Main file for Task 0
"""
Cache = __import__('exercise').Cache

cache = Cache()

data = b"hello"
key = cache.store(data)
print(key)

local_redis = redis.Redis()
print(local_redis.get(key))
```

#### Testing and Usage

1. **Run the Redis Server**:
   Before executing the script, ensure that the Redis server is running. You can start Redis with the following command:
   ```bash
   sudo service redis-server start
   ```

2. **Run the test script**:
   You can now execute the test script using `python3` or by making it executable and using `./`:
   ```bash
   ./0-main.py
   ```

**Output:**
```bash
034c0dea-0bd8-4811-94a8-40c0e5762191
b'hello'
```

3. **Explanation of Output**:
   - The first output (`034c0dea-0bd8-4811-94a8-40c0e5762191`) is a randomly generated UUID key, which serves as a unique identifier for the stored data in Redis.
   - The second output (`b'hello'`) is the value retrieved from Redis using the key, showing that the data was successfully stored and retrieved.

4. **Why this Output**:
   - **What**: The output includes the generated UUID key and the data retrieved from Redis.
   - **Where**: The key and data are stored in Redis, a powerful in-memory key-value store.
   - **Why**: The unique key ensures that each piece of data can be stored without conflict. Redis retrieves the data exactly as it was input (in this case, as a byte string).
   - **How**: Redis uses the `set` method to store data with the key and the `get` method to retrieve it based on the key.
   - **When**: The `store` method is called to save the data, and the `get` method is used to retrieve it.

</details>



### Task 1: Reading from Redis and Recovering Original Type

In this task, we created a `get` method that retrieves data from Redis and applies an optional function to convert the data back to its original format. We also implemented two additional methods, `get_str` and `get_int`, which automatically convert Redis data to strings and integers, respectively.

<details>
  <summary><strong>Curriculum Instruction</strong></summary>

Redis only allows to store string, bytes and numbers (and lists thereof). Whatever you store as single elements, it will be returned as a byte string. Hence if you store `"a"` as a UTF-8 string, it will be returned as `b"a"` when retrieved from the server.

In this exercise we will create a `get` method that takes a key string argument and an optional `Callable` argument named `fn`. This callable will be used to convert the data back to the desired format.

Remember to conserve the original `Redis.get` behavior if the key does not exist.

Also, implement 2 new methods: `get_str` and `get_int` that will automatically parametrize `Cache.get` with the correct conversion function.

The following code should not raise:
```python
cache = Cache()

TEST_CASES = {
    b"foo": None,
    123: int,
    "bar": lambda d: d.decode("utf-8")
}

for value, fn in TEST_CASES.items():
    key = cache.store(value)
    assert cache.get(key, fn=fn) == value
```
</details>

<details>
  <summary><strong>Steps and Code Implementation</strong></summary>

### Steps:


1. **Create the `get` Method**:
   - Retrieve data from Redis using the `key`.
   - Apply an optional function (`fn`) to convert the data back to its original format.
   - Ensure Redis behaves normally (returns `None`) if the key does not exist.

2. **Create `get_str` and `get_int`**:
   - `get_str`: Converts byte data from Redis into a UTF-8 string.
   - `get_int`: Converts byte data from Redis into an integer.

#### Code:
```python
#!/usr/bin/env python3
'''
This module provides a Cache class that interacts with Redis
to store and retrieve data. Think of it as hiding things in
Redis, like stashing secrets in a vault that sometimes misplaces
the key.
'''
import redis
import uuid
from typing import Union, Callable, Optional


class Cache:
    '''
    Cache class for storing and retrieving data in Redis.
    Like organizing your chaotic thoughts, but in byte form.
    '''

    def __init__(self):
        '''
        Initialize the Redis client and flush the database.
        Basically, we’re clearing out all of yesterday's nonsense,
        so today’s nonsense can take its place.
        '''
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        '''
        Store data in Redis with a unique key.
        Think of it like giving a name to every random thought
        or piece of data, so you can find it later (hopefully).
        '''
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(
        self, key: str, fn: Optional[Callable] = None
    ) -> Optional[Union[str, bytes, int, float]]:
        '''
        Retrieve data from Redis, possibly transforming it.
        Redis returns byte strings for everything, like that friend who always
        speaks in riddles. If you want something more useful, apply the fn to
        decode it. If the key doesn't exist, Redis just shrugs.
        '''
        value = self._redis.get(key)
        if value is None:
            return None
        if fn:
            return fn(value)
        return value

    def get_str(self, key: str) -> Optional[str]:
        '''
        Retrieve a string from Redis.
        Translates Redis byte-speak into human-readable words.
        '''
        return self.get(key, lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> Optional[int]:
        '''
        Retrieve an integer from Redis.
        Converts byte-gibberish into a number, like turning
        chaotic data into something you can count on.
        '''
        return self.get(key, int)
```

### How We Created and Structured `1-main.py`

The testing file (`1-main.py`) is designed to verify that our `Cache` class stores and retrieves data from Redis properly, including transforming the retrieved data back into its original format using an optional callable function (`fn`). Here's what it contains:

- **Cache Instantiation**: We create an instance of the `Cache` class.
- **Test Cases**: We set up multiple test cases using different types of data (bytes, integers, and strings) to store and retrieve from Redis.
- **Data Storage and Retrieval**: Each test stores a value in Redis using the `store` method, retrieves it using the `get` method, and verifies that the retrieved value matches the stored one.
- **Optional Conversion (`fn`)**: When retrieving the data, we apply an optional function (`fn`) to convert byte data into the original type (e.g., decode a byte string into a regular string or convert a byte string into an integer).

Here’s the testing file (`1-main.py`):

#### Code:
```python
#!/usr/bin/env python3
"""
Main file for Task 1
"""
Cache = __import__('exercise').Cache

cache = Cache()

TEST_CASES = {
    b"foo": None,
    123: int,
    "bar": lambda d: d.decode("utf-8")
}

for value, fn in TEST_CASES.items():
    key = cache.store(value)
    result = cache.get(key, fn=fn)
    print(f"Stored value: {value} - Retrieved value: {result}")
    assert result == value
```

### How to Run the Test (`1-main.py`)

#### Steps:
1. **Make the file executable**:
   - Before you can run `1-main.py`, you need to make it executable using `chmod`:
     ```bash
     chmod +x 1-main.py
     ```

2. **Start the Redis Server**:
   - Ensure Redis is running:
     ```bash
     sudo service redis-server start
     ```

3. **Run the test**:
   - Now, you can run the script with:
     ```bash
     ./1-main.py
     ```

4. **Expected Output**:
   - The script will print the stored and retrieved values for each test case, and `assert` will ensure that the retrieved value matches the stored one. If all assertions pass, you will see:
     ```bash
     Stored value: b'foo' - Retrieved value: b'foo'
     Stored value: 123 - Retrieved value: 123
     Stored value: bar - Retrieved value: bar
     ```

### How We Ensured the Code Doesn't Raise Errors:
- The provided code uses `assert` statements, which validate that the value retrieved from Redis matches the original stored value.
- If the assertion passes (i.e., the values match), nothing happens, and the script runs silently. 
- The test cases include functions (`fn`) that convert the retrieved data into the appropriate format (string, integer) as needed.

### Testing That It Raises Errors:
1. **Force an Assertion to Fail**:
   - You can modify the test cases in `1-main.py` to intentionally fail the assertion. For example:
     ```python
     assert cache.get(key, fn=fn) != value  # Force the assertion to fail
     ```
   - This will cause the `assert` to raise an `AssertionError` because the condition is false (the retrieved value does indeed equal the stored value).

2. **Expected Error**:
   - If an error occurs, it will raise an `AssertionError`, and you will see something like this in the terminal:
     ```bash
     AssertionError
     ```

3. **Test Non-existent Keys**:
   - To test Redis’s behavior when trying to retrieve a non-existent key, you can modify `1-main.py`:
     ```python
     non_existent_key = "non-existent-key"
     result = cache.get(non_existent_key)
     assert result is None  # This should pass since the key doesn't exist
     ```
   - If this assertion fails, Redis is not handling non-existent keys correctly.

### Why This Works:

- **Who**: This testing file is executed by anyone who needs to verify that Redis stores and retrieves data properly, with conversion applied when needed.
- **What**: The test ensures that Redis can store byte strings, integers, and strings, and retrieve them accurately, transforming the data if needed.
- **Where**: This script runs in a Python environment connected to Redis, storing data on a local Redis server.
- **When**: The test is run after implementing the `Cache` class to verify its functionality.
- **Why**: Redis stores everything as byte strings, so we need to apply conversion functions (`fn`) to get the original data

 type back. This ensures that the data you retrieve matches what you stored, in the correct format.
- **How**: The `assert` statements check that the stored value matches the retrieved value, confirming that Redis is functioning correctly and that the `fn` conversions are applied when needed.

</details>


## Author

GitHub: [ThatsVie](https://github.com/ThatsVie)
