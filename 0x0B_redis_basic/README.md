<div align="center">
    <img src="https://github.com/user-attachments/assets/1f009f71-4307-4c41-b1f5-f10192a9d8b1" alt="RedisBasicBlackPuggy">
    <p>This project implements a Redis-based caching system using Python. It explores key Redis functionalities such as storing, retrieving, and incrementing data, as well as tracking method call history with input and output logging. By leveraging Redis as an efficient in-memory data store, the project provides a simple yet powerful solution for caching and real-time data management.</p>
</div>

---

## Table of Contents
- [Resources](#resources)
- [Learning Objectives](#learning-objectives)
- [What is Redis?](#what-is-redis)
- [Redis Use Cases](#redis-use-cases)
- [Requirements](#requirements)
- [Installation](#installation)
- [Troubleshooting](#troubleshooting)
- [Tasks and Usage](#tasks-and-usage)
  - [Task 0: Writing Strings to Redis](#task-0-writing-strings-to-redis)
  - [Task 1: Reading from Redis and Recovering Original Type](#task-1-reading-from-redis-and-recovering-original-type)
  - [Task 2: Incrementing Values](#task-2-incrementing-values)
  - [Task 3: Storing Lists](#task-3-storing-lists)
  - [Task 4: Retrieving Lists](#task-4-retrieving-lists)
  - [Task 5: Implementing an Expiring Web Cache and Tracker](#task-5-implementing-an-expiring-web-cache-and-tracker)


## Resources

  - [Redis commands](https://redis.io/docs/latest/commands/)
  - [Redis Python client](https://redis-py.readthedocs.io/en/stable/)
  - [How to Use Redis With Python](https://realpython.com/python-redis/)
  - [Redis Crash Course Tutorial](https://www.youtube.com/watch?v=Hbt56gFj998)

## Learning Objectives:

### 1. **Use Redis for Basic Operations**
   - Redis is a powerful in-memory key-value store. Basic operations include storing, retrieving, incrementing, and managing lists of data.
     - **Task 0: Writing Strings to Redis**: Demonstrates how to store data in Redis using the `set` operation and retrieve it using `get`.
     - **Task 1: Reading from Redis and Recovering Original Type**: Shows how Redis stores everything as byte strings and how to convert the retrieved data back into its original form.
     - **Task 2: Incrementing Values**: Demonstrates the use of the `incr` command to count how many times a method is called.
     - **Task 3: Storing Lists**: Introduces `RPUSH` and `LPUSH` for managing lists in Redis, storing inputs and outputs of method calls.
     - **Task 4: Retrieving Lists**: Explores using `LRANGE` to retrieve data from Redis lists and display the history of method calls.

### 2. **Use Redis as a Simple Cache**
   - A cache temporarily stores data for quick retrieval without needing to access a slower data source repeatedly.
     - **Task 0: Writing Strings to Redis**: Implements a simple caching system where data is stored with unique keys for fast retrieval.
     - **Task 1: Reading from Redis and Recovering Original Type**: Shows how Redis is used as a cache to store various types of data and retrieve them with the correct format.
     - **Task 2: Incrementing Values**: Enhances the cache by keeping track of how many times specific methods are called.
     - **Task 3: Storing Lists**: Extends caching functionality to log inputs and outputs of method calls, ensuring that both can be quickly retrieved later.
     - **Task 4: Retrieving Lists**: Demonstrates the replay functionality, which retrieves and displays cached method call history, further using Redis as a cache for this information.

## What is Redis?

**Redis** (Remote Dictionary Server) is an open-source, in-memory data store that functions as a key-value database, cache, and message broker. Known for its high speed and efficiency, Redis allows for real-time data storage and retrieval, making it ideal for applications requiring low-latency access. It supports various data structures such as strings, lists, sets, and hashes, and provides persistence options to store data even after server restarts.

## Redis Use Cases:

1. **Caching**: Redis stores frequently accessed data in memory, reducing the load on traditional databases and improving response times for web pages, APIs, and other data-heavy applications.
   
2. **Session Management**: It efficiently manages session data, ensuring quick access to user information like logins or preferences, while offering persistence options to retain data across server restarts.

3. **Real-Time Analytics**: Redis processes and tracks real-time data, such as event counts or live metrics, making it ideal for leaderboards, live tracking systems, and monitoring applications.

4. **Message Queues**: Using Redis’s publish/subscribe model, it enables real-time communication between services or microservices, facilitating distributed task management and efficient messaging.

5. **Distributed Caching**: In large-scale systems, Redis acts as a distributed cache across multiple servers, ensuring fast and scalable data access for high-traffic applications.


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

### Task 2: Incrementing Values

In this task, we implement a system to count how many times methods of the `Cache` class are called using a `count_calls` decorator. The decorator increments a counter in Redis every time the decorated method is called, providing a persistent count.

<details>
  <summary><strong>Curriculum Instruction</strong></summary>

Familiarize yourself with the `INCR` command and its Python equivalent.

In this task, we will implement a system to count how many times methods of the `Cache` class are called.

- Above `Cache`, define a `count_calls` decorator that takes a single method `Callable` argument and returns a `Callable`.
- As a key, use the qualified name of the method using the `__qualname__` dunder method.
- Create and return a function that increments the count for that key every time the method is called and returns the value returned by the original method.
- Remember that the first argument of the wrapped function will be `self` (which is the instance itself), which lets you access the Redis instance.
- Protip: when defining a decorator, it is useful to use `functools.wraps` to conserve the original function’s name, docstring, etc. Make sure you use it as described here.
- Decorate `Cache.store` with `count_calls`.
</details>

<details>
  <summary><strong>Steps and Code Implementation</strong></summary>

### Steps:

1. **Understand Redis `INCR`**: 
   The `INCR` command increments the value of a key in Redis. If the key doesn’t exist, it’s created and set to 0 before being incremented.

2. **Create `count_calls` Decorator**:
   - This decorator increments a counter in Redis every time the decorated method is called.
   - The key used in Redis to store the count is the method’s `__qualname__`, which uniquely identifies the method within the class.

3. **Use `functools.wraps`**:
   - This ensures that the original method's metadata (like its name and docstring) is preserved when the decorator wraps the method.

4. **Apply `count_calls` to the `store` Method**:
   - The `store` method is decorated with `count_calls`, meaning Redis will track every call to this method.

#### Code:
```python
#!/usr/bin/env python3
'''
This module provides a Cache class that interacts with Redis
to store and retrieve data. It also keeps count of method calls.
Redis is like a cosmic accountant, tracking every call like it’s
preparing for the next apocalypse or tallying pug snacks.
'''
import redis
import uuid
import functools
from typing import Union, Callable, Optional


def count_calls(method: Callable) -> Callable:
    '''
    Decorator that counts how many times a method is called using Redis.
    Imagine counting how many times you've ignored the news about rising
    sea levels. Redis does this for your method calls, one existential dread
    at a time.
    '''
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        '''
        Wrapper function that increments the count each time
        the decorated method is called. Redis tracks it all like
        keeping tabs on how many ice caps we have left or how many times
        your pug asks for dinner.
        '''
        key = method.__qualname__  # Use the method's qualified name as the key
        self._redis.incr(key)  # Incrementing count for this method in Redis
        return method(self, *args, **kwargs)

    return wrapper


class Cache:
    '''
    Cache class for storing and retrieving data in Redis.
    Now it also tracks how many times its methods are called.
    Think of it like counting the inevitable whether it’s climate change
    or how many belly rubs your pug demands.
    '''

    def __init__(self):
        '''
        Initialize the Redis client and flush the database.
        Basically wiping everything clean like deleting the record
        of all those carbon emissions, so we can pretend everything’s fine.
        '''
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        '''
        Store data in Redis with a unique key and count how many times
        this method has been called.
        Like storing away little pieces of hope, except Redis never
        forgets how many you've tried to hide.
        '''
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(
        self, key: str, fn: Optional[Callable] = None
    ) -> Optional[Union[str, bytes, int, float]]:
        '''
        Retrieve data from Redis, possibly transforming it.
        Redis gives everything back in bytes, like handing you
        a confusing climate report. You’ll need to decode it if you
        want it to make sense.
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
        Translates Redis bytespeak into human-readable form, kind of like
        turning scientific data into something we can understand.
        '''
        return self.get(key, lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> Optional[int]:
        '''
        Retrieve an integer from Redis.
        Converts byte gibberish into something countable, like measuring
        the sea level rise except Redis makes it easier to ignore.
        '''
        return self.get(key, int)

```

### How to Run and Test `count_calls`

#### 2-main.py (for Task 2):
```python
#!/usr/bin/env python3
"""
Main file for Task 2
"""
Cache = __import__('exercise').Cache

cache = Cache()

# Storing data and printing how many times store was called
cache.store(b"first")
print(cache.get(cache.store.__qualname__))  # Should print b'1'

cache.store(b"second")
cache.store(b"third")
print(cache.get(cache.store.__qualname__))  # Should print b'3'
```

### Testing and Usage

1. **Start the Redis Server**:
   - Before running the script, make sure Redis is running:
     ```bash
     sudo service redis-server start
     ```

2. **Make the test script executable**:
   - Run the following to make `2-main.py` executable:
     ```bash
     chmod +x 2-main.py
     ```

3. **Run the test script**:
   - Now you can execute the script using:
     ```bash
     ./2-main.py
     ```

#### Expected Output:
```bash
b'1'
b'3'
```

### Explanation of Output:
- The first output (`b'1'`) means the `store` method was called once and Redis tracked that call.
- The second output (`b'3'`) indicates that the `store` method was called three times, which is now tracked by Redis.

### Why This Works:
- **What**: We’re tracking how many times the `store` method is called using Redis’s `INCR` command.
- **Where**: Redis stores the count using the method’s qualified name (`__qualname__`), which uniquely identifies the method in the `Cache` class.
- **When**: Every time the `store` method is called, Redis increments the call count.
- **Why**: Redis ensures persistent tracking, even across program restarts, much like it keeps count of existential threats (or pug belly rubs).
- **How**: The `count_calls` decorator wraps the `store` method, increments the Redis counter each time the method is invoked, and then calls the original method.

</details>

### Task 3: Storing Lists

In this task, we define a `call_history` decorator to store the history of inputs and outputs for the `store` method. Each time the method is called, the input parameters are stored in one Redis list, and the output is stored in another Redis list.

<details>
  <summary><strong>Curriculum Instruction</strong></summary>

Familiarize yourself with Redis commands `RPUSH`, `LPUSH`, `LRANGE`, etc.

In this task, we will define a `call_history` decorator to store the history of inputs and outputs for a particular function.

- Every time the original function is called, we will add its input parameters to one list in Redis, and store its output into another list.
- In `call_history`, use the decorated function’s qualified name and append `":inputs"` and `":outputs"` to create input and output list keys, respectively.
- `call_history` has a single parameter named `method` that is a `Callable` and returns a `Callable`.
- In the new function that the decorator will return, use `RPUSH` to append the input arguments. Remember that Redis can only store strings, bytes, and numbers. Therefore, we can simply use `str(args)` to normalize the input. We can ignore potential `kwargs` for now.
- Execute the wrapped function to retrieve the output. Store the output using `RPUSH` in the `"...:outputs"` list, then return the output.
- Decorate `Cache.store` with `call_history`.
</details>

<details>
  <summary><strong>Steps and Code Implementation</strong></summary>

### Steps:

1. **Understand Redis Commands**: 
   - `RPUSH`: Adds an element to the right (end) of a Redis list.
   - `LRANGE`: Returns elements of a list within a specified range.

2. **Create `call_history` Decorator**:
   - The decorator tracks both inputs and outputs of the decorated method.
   - Two Redis lists are used: one for inputs (`...:inputs`) and one for outputs (`...:outputs`).

3. **Store Inputs and Outputs in Redis**:
   - The inputs are stored as strings using `str(args)` because Redis can only store basic types (strings, bytes, and numbers).
   - The outputs are stored as they are returned by the method.

4. **Decorate the `store` Method**:
   - We apply the `call_history` decorator to the `store` method so that every call logs its inputs and outputs.

#### Code:
```python
#!/usr/bin/env python3
'''
This module provides a Cache class that interacts with Redis
to store and retrieve data. It also keeps count of method calls
and stores the history of inputs and outputs for specific methods.
Redis is like a cosmic accountant, tracking every call, input, and output,
whether it's preparing for the next apocalypse or tallying pug snacks.
'''
import redis
import uuid
import functools
from typing import Union, Callable, Optional


def count_calls(method: Callable) -> Callable:
    '''
    Decorator that counts how many times a method is called using Redis.
    Imagine counting how many times you've ignored the news about rising
    sea levels. Redis does this for your method calls, one existential dread
    at a time.
    '''
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        '''
        Wrapper function that increments the count each time
        the decorated method is called. Redis tracks it all like
        keeping tabs on how many ice caps we have left or how many times
        your pug asks for dinner.
        '''
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)

    return wrapper


def call_history(method: Callable) -> Callable:
    '''
    Decorator to store the history of inputs and outputs for a method.
    Every time the method is called, the input is logged into one list,
    and the output into another. Like keeping track of all your thoughts,
    but in Redis, and they never fade away.
    '''
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        inputs_key = method.__qualname__ + ":inputs"
        outputs_key = method.__qualname__ + ":outputs"

        # Store input arguments as a string in the Redis list
        self._redis.rpush(inputs_key, str(args))

        # Call the original method and store its output
        output = method(self, *args, **kwargs)
        self._redis.rpush(outputs_key, str(output))

        return output

    return wrapper


class Cache:
    '''
    Cache class for storing and retrieving data in Redis.
    Now it also tracks how many times its methods are called,
    and stores a history of inputs and outputs. Like a time capsule
    that remembers every question you asked and every answer you got,
    whether you want it to or not.
    '''

    def __init__(self):
        '''
        Initialize the Redis client and flush the database.
        Basically wiping everything clean like deleting the record
        of all those carbon emissions, so we can pretend everything’s fine.
        '''
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        '''
        Store data in Redis with a unique key, count how many times
        this method has been called, and keep a history of inputs and outputs.
        Like storing away little pieces of hope and also remembering every
        time you've tried to, in case you need to revisit your optimism later.
        '''
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(
        self, key: str, fn: Optional[Callable] = None
    ) -> Optional[Union[str, bytes, int, float]]:
        '''
        Retrieve data from Redis, possibly transforming it.
        Redis gives everything back in bytes, like handing you
        a confusing climate report. You’ll need to decode it if you
        want it to make sense.
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
        Translates Redis bytespeak into human-readable form, kind of like
        turning scientific data into something we can understand.
        '''
        return self.get(key, lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> Optional[int]:
        '''
        Retrieve an integer from Redis.
        Converts byte gibberish into something countable, like measuring
        the sea level rise except Redis makes it easier to ignore.
        '''
        return self.get(key, int)

```

### How to Run and Test `call_history`

#### 3-main.py (for Task 3):
```python
#!/usr/bin/env python3
"""
Main file for Task 3
"""
Cache = __import__('exercise').Cache

cache = Cache()

s1 = cache.store("first")
print(s1)
s2 = cache.store("second")
print(s2)
s3 = cache.store("third")
print(s3)

# Retrieve the history of inputs and outputs
inputs = cache._redis.lrange(f"{cache.store.__qualname__}:inputs", 0, -1)
outputs = cache._redis.lrange(f"{cache.store.__qualname__}:outputs", 0, -1)

print(f"inputs: {inputs}")
print(f"outputs: {outputs}")
```

### Testing and Usage

1. **Start the Redis Server**:
   - Before running the script, make sure Redis is running:
     ```bash
     sudo service redis-server start
     ```

2. **Make the test script executable**:
   - Run the following to make `3-main.py` executable:
     ```bash
     chmod +x 3-main.py
     ```

3. **Run the test script**:
   - Now you can execute the script using:
     ```bash
     ./3-main.py
     ```

#### Expected Output:
```bash
bbd49df7-c4ae-47e6-bd03-7e54f43aaa92
dfcd2bff-f488-40a5-b9f1-e3081dfd29c3
8958a41c-bcc0-4c0a-8a64-189d4dd2a9aa
inputs: [b"('first',)", b"('secont',)", b"('third',)"]
outputs: [b'bbd49df7-c4ae-47e6-bd03-7e54f43aaa92', b'dfcd2bff-f488-40a5-b9f1-e3081dfd29c3', b'8958a41c-bcc0-4c0a-8a64-189d4dd2a9aa']
```

### Explanation of Output:

- **Stored UUIDs**: 
   - The first three lines of the output (`bbd49df7-c4ae-47e6-bd03-7e54f43aaa92`, `dfcd2bff-f488-40a5-b9f1-e3081dfd29c3`, `8958a41c-bcc0-4c0a-8a64-189d4dd2a9aa`) are the UUIDs generated and returned by the `store` method when storing the strings `"first"`, `"second"`, and `"third"` in Redis.
   
- **Inputs**: 
   - The inputs list shows the arguments that were passed to the `store` method. Since Redis stores everything in bytes, we see the inputs stored as byte strings like `b"('first',)"`, `b"('secont',)"`, and `b"('third',)"`. (Note the typo in "second

" was preserved).

- **Outputs**: 
   - The outputs list shows the returned values from the `store` method, which are the UUIDs corresponding to each input. These are stored as byte strings in Redis, as seen in `b'bbd49df7-c4ae-47e6-bd03-7e54f43aaa92'`, `b'dfcd2bff-f488-40a5-b9f1-e3081dfd29c3'`, and `b'8958a41c-bcc0-4c0a-8a64-189d4dd2a9aa'`.

### Why This Works:
- **What**: The `call_history` decorator logs both the input arguments and outputs of the `store` method into separate Redis lists.
- **Where**: Two Redis lists are used—one for inputs (`...:inputs`) and one for outputs (`...:outputs`).
- **Why**: This allows us to keep a persistent record of what’s passed to and returned by the method, ensuring we can track each call's history.
- **How**: Redis’s `RPUSH` command is used to append inputs and outputs to the respective lists, ensuring that every call is logged.

</details>

### Task 4: Retrieving Lists


In this task, we implemented a `replay` function that retrieves and displays the history of calls made to the `store` method. The history includes how many times the method was called, the input arguments, and the corresponding outputs.

<details>
  <summary><strong>Curriculum Instruction</strong></summary>

In this task, we will implement a `replay` function to display the history of calls of a particular function.

- Use keys generated in previous tasks to generate the following output:

```
>>> cache = Cache()
>>> cache.store("foo")
>>> cache.store("bar")
>>> cache.store(42)
>>> replay(cache.store)
Cache.store was called 3 times:
Cache.store(*('foo',)) -> 13bf32a9-a249-4664-95fc-b1062db2038f
Cache.store(*('bar',)) -> dcddd00c-4219-4dd7-8877-66afbe8e7df8
Cache.store(*(42,)) -> 5e752f2b-ecd8-4925-a3ce-e2efdee08d20
```

Tip: Use `lrange` and `zip` to loop over inputs and outputs.

</details>

<details>
  <summary><strong>Steps and Code Implementation</strong></summary>

### Steps

1. **Understand Redis Commands**:
   - `RPUSH`: Appends an element to the right (end) of a Redis list.
   - `LRANGE`: Retrieves elements from a list within a specified range.
   - `GET`: Retrieves the value of a key (used to get the count of method calls).

2. **Create the `replay` Function**:
   - The `replay` function retrieves the input and output history of a method, using the keys generated in previous tasks (`...:inputs` and `...:outputs`).
   - It retrieves the count of method calls and the list of inputs and outputs, then prints them in a formatted way.

#### Code:
```python
#!/usr/bin/env python3
'''
This module provides a Cache class that interacts with Redis
to store and retrieve data. It also keeps count of method calls,
stores the history of inputs and outputs, and can replay method call history.
Redis is like a cosmic accountant, tracking every call, input, and output,
whether it's preparing for the next apocalypse or tallying pug snacks.
'''
import redis
import uuid
import functools
from typing import Union, Callable, Optional


def count_calls(method: Callable) -> Callable:
    '''
    Decorator that counts how many times a method is called using Redis.
    Imagine counting how many times you've ignored the news about rising
    sea levels. Redis does this for your method calls, one existential dread
    at a time.
    '''
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        '''
        Wrapper function that increments the count each time
        the decorated method is called. Redis tracks it all like
        keeping tabs on how many ice caps we have left or how many times
        your pug asks for dinner.
        '''
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)

    return wrapper


def call_history(method: Callable) -> Callable:
    '''
    Decorator to store the history of inputs and outputs for a method.
    Every time the method is called, the input is logged into one list,
    and the output into another. Like keeping track of all your thoughts,
    but in Redis, and they never fade away.
    '''
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        inputs_key = method.__qualname__ + ":inputs"
        outputs_key = method.__qualname__ + ":outputs"

        # Store input arguments as a string in the Redis list
        self._redis.rpush(inputs_key, str(args))

        # Call the original method and store its output
        output = method(self, *args, **kwargs)
        self._redis.rpush(outputs_key, str(output))

        return output

    return wrapper


def replay(method: Callable):
    '''
    Function to display the history of calls made to a particular method.
    Shows how many times the method was called, and replays the inputs and
    outputs from previous calls. Like revisiting your embarrassing past, one
    function call at a time, except now it's logged in Redis.
    '''
    redis_instance = method.__self__._redis
    method_name = method.__qualname__
    inputs_key = f"{method_name}:inputs"
    outputs_key = f"{method_name}:outputs"

    # Get the number of times the method was called
    call_count = redis_instance.get(method_name).decode("utf-8")

    print(f"{method_name} was called {call_count} times:")

    # Get the list of inputs and outputs
    inputs = redis_instance.lrange(inputs_key, 0, -1)
    outputs = redis_instance.lrange(outputs_key, 0, -1)

    # Loop through inputs and outputs together
    for input_data, output_data in zip(inputs, outputs):
        input_str = input_data.decode("utf-8")
        output_str = output_data.decode("utf-8")
        print(f"{method_name}(*{input_str}) -> {output_str}")


class Cache:
    '''
    Cache class for storing and retrieving data in Redis.
    It now tracks how many times its methods are called,
    stores a history of inputs and outputs, and can replay the history
    of method calls like a detailed audit of every little thing you've done.
    '''

    def __init__(self):
        '''
        Initialize the Redis client and flush the database.
        Basically wiping everything clean like deleting the record
        of all those carbon emissions, so we can pretend everything’s fine.
        '''
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        '''
        Store data in Redis with a unique key, count how many times
        this method has been called, and keep a history of inputs and outputs.
        Like storing away little pieces of hope and also remembering every
        time you've tried to, in case you need to revisit your optimism later.
        '''
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(
        self, key: str, fn: Optional[Callable] = None
    ) -> Optional[Union[str, bytes, int, float]]:
        '''
        Retrieve data from Redis, possibly transforming it.
        Redis gives everything back in bytes, like handing you
        a confusing climate report. You’ll need to decode it if you
        want it to make sense.
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
        Redis speaks in bytecode, but this translates it back into words.
        '''
        return self.get(key, lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> Optional[int]:
        '''
        Retrieve an integer from Redis.
        Converts the chaos into a number you can count on—hopefully.
        '''
        return self.get(key, int)
```

### Example Usage:

#### 4-main.py (for Task 4):
```python
#!/usr/bin/env python3
"""
Main file for Task 4
"""
Cache = __import__('exercise').Cache
replay = __import__('exercise').replay

cache = Cache()

cache.store("foo")
cache.store("bar")
cache.store(42)

# Replay the history of the store method
replay(cache.store)
```


### Testing and Usage

1. **Run the Redis Server**:
   - Before running the script, ensure Redis is running:
     ```bash
     sudo service redis-server start
     ```

2. **Make the test script executable**:
   - Run the following to make `4-main.py` executable:
     ```bash
     chmod +x 4-main.py
     ```

3. **Run the test script**:
   - Execute the script using:
     ```bash
     ./4-main.py
     ```

#### Expected Output:

```bash
Cache.store was called 3 times:
Cache.store(*('foo',)) -> 17204be4-1e41-400b-b8a7-b094efa7af5a
Cache.store(*('bar',)) -> bb6f5130-58d3-497d-8cac-cbe7e0f4bf42
Cache.store(*(42,)) -> e5cbdec0-1788-43bf-979a-e236c708f7fa
```


### Explanation of Output:

1. **Cache.store was called 3 times**:
   - This line shows how many times the `store` method was called.

2. **Cache.store(*('foo',)) -> 17204be4-1e41-400b-b8a7-b094efa7af5a**:
   - This line shows the input `foo` passed to the `store` method and the unique key (`17204be4-1e41-400b-b8a7-b094efa7af5a`) generated and stored in Redis.

3. **Cache.store(*('bar',)) -> bb6f

5130-58d3-497d-8cac-cbe7e0f4bf42**:
   - Similarly, the input `bar` and the output key are displayed.

4. **Cache.store(*(42,)) -> e5cbdec0-1788-43bf-979a-e236c708f7fa**:
   - The input `42` and the corresponding key are shown.

### Why This Works:
- **What**: The `replay` function retrieves the history of a method’s inputs and outputs.
- **Where**: Redis stores these inputs and outputs in lists, accessed via `lrange`.
- **Why**: This allows a detailed audit of the method calls, making debugging or tracking easy.
- **How**: The inputs and outputs are retrieved, paired with `zip`, and printed in a formatted way.

</details>

### Task 5: Implementing an Expiring Web Cache and Tracker

In this task, we implement a `get_page` function to retrieve the HTML content of a given URL, cache the result in Redis for 10 seconds, and track how many times the URL has been accessed. Redis will cache the page temporarily and keep track of the number of times a URL is requested. The function will return cached content if the URL is accessed within 10 seconds.

<details>
  <summary><strong>Curriculum Instruction</strong></summary>

- Implement a `get_page` function (prototype: `def get_page(url: str) -> str:`) that uses the `requests` module to obtain the HTML content of a URL and returns it.
- Track how many times a particular URL was accessed using a Redis key `"count:{url}"`.
- Cache the result with an expiration time of 10 seconds.
- Bonus: Implement this functionality with decorators.

<details>
  <summary>Tip</summary>
  Use `http://slowwly.robertomurray.co.uk` to simulate a slow response and test your caching.
</details>

</details>

<details>
  <summary><strong>Steps and Code Implementation</strong></summary>

### Steps:

1. **Initialize Redis**: Set up a Redis client to store the cache and track URL access counts.
   
2. **Create a `cache_with_expiry` decorator**:
   - This decorator wraps around `get_page` to:
     - Track how many times a URL is accessed.
     - Cache the result with a 10-second expiration time.

3. **Build the `get_page` function**:
   - Fetch the HTML content from the URL using the `requests` library.
   - Redis stores the HTML for 10 seconds to avoid re-fetching.

4. **Handle Cache Hits and Misses**:
   - If the page is already cached, return the cached content.
   - If not, fetch the page and store it in Redis with an expiration time.

#### Code:

```python
#!/usr/bin/env python3
'''
This module implements a web cache using Redis and tracks URL access counts.
Imagine Redis as the last bunker on Earth, hoarding bits of information while
the world burns. You ask for the same data over and over, and Redis,
like a weary survivalist, reminds you it already stored that info-temporarily.
'''
import redis
import requests
from typing import Callable
from functools import wraps


# Initialize Redis client
r = redis.Redis()


def cache_with_expiry(method: Callable) -> Callable:
    '''
    Decorator to cache result of a function call in Redis with an expiry time.
    Think of it as rationing your dwindling resources. You only get to keep
    that precious web content for 10 seconds, and then it's gone,
    like fresh water in a drought.
    '''
    @wraps(method)
    def wrapper(url: str) -> str:
        '''
        Tracks how many times a URL is accessed and caches the result.
        It’s like rationing supplies during the apocalypse.
        Redis reminds you how many times you've come back for the same stale
        resources, only to serve them cold from the cache,
        until it’s time to scavenge again.
        '''
        access_count_key = f"count:{url}"
        r.incr(access_count_key)

        # Check if the URL is already cached
        cached_key = f"cached:{url}"
        cached_page = r.get(cached_key)
        if cached_page:
            return cached_page.decode("utf-8")

        # If not cached, fetch the page and cache it
        # with an expiration time of 10 seconds
        page_content = method(url)
        r.setex(cached_key, 10, page_content)
        return page_content

    return wrapper


@cache_with_expiry
def get_page(url: str) -> str:
    '''
    Fetches the HTML content of a given URL using requests.
    It's like venturing into a wasteland to gather resources.
    Redis caches the page for 10 seconds, ensuring you don’t have to risk
    life and limb to retrieve the same dwindling supplies over and over.
    '''
    response = requests.get(url)
    return response.text


if __name__ == "__main__":
    url = (
        "http://slowwly.robertomurray.co.uk/delay/5000/url/"
        "http://www.example.com"
    )

    # Fetch the page for the first time
    print(get_page(url))

    # Fetch it again (should be served from cache)
    print(get_page(url))

    # Check how many times the URL was accessed
    print(f"URL accessed {r.get(f'count:{url}').decode('utf-8')} times.")
```

<details>
  <summary><strong>Testing and Usage</strong></summary>

1. **Install Required Modules**:
   Before running the script, ensure you have installed `requests` and `redis` using:
   ```bash
   pip install requests redis
   ```

2. **Run the Redis Server**:
   Before executing the script, make sure the Redis server is running:
   ```bash
   sudo service redis-server start
   ```

3. **Testing**:
   - Save the code in a file called `web.py`.
   - Make the file executable:
     ```bash
     chmod +x web.py
     ```
   - Run the script to fetch the web page:
     ```bash
     ./web.py
     ```

4. **Expected Output**:
   ```bash
   <!doctype html>
   <html data-adblockkey="MFwwDQYJKoZIhvcNAQEBBQADSwAwSAJBANDrp2lz7AOmADaN8tA50LsWcjLFyQFcb/P2Txc58oYOeILb3vBw7J6f4pamkAQVSQuqYsKx3YzdUHCvbVZvFUsCAwEAAQ==_kDpBCoRxhm86nXIJPrPM+lbLn+v5cstkT1T1QXvXbhf4kf+IzZzAV+SKctJ5bZVa1HqU+p1A4vbSHR8fhh5gzQ==" lang="en" style="background: #2B2B2B;">
   <head>
       <meta charset="utf-8">
       <meta name="viewport" content="width=device-width, initial-scale=1">
       <link rel="icon" href="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAIAAACQd1PeAAAADElEQVQI12P4//8/AAX+Av7czFnnAAAAAElFTkSuQmCC">
       <link rel="preconnect" href="https://www.google.com" crossorigin>
   </head>
   <body>
   <div id="target" style="opacity: 0"></div>
   <script>window.park = "eyJ1dWlkIjoiMzcxZDc4ZWQtOGEyZS00YjU4LTg4NzMtMGJkMDMyN2Q2MzYyIiwicGFnZV90aW1lIjoxNzI3NjQ2MjY1LCJwYWdlX3VybCI6Imh0dHA6Ly9zbG93d2x5LnJvYmVydG9tdXJyYXkuY28udWsvZGVsYXkvNTAwMC91cmwvaHR0cDovd3d3LmV4YW1wbGUuY29tIiwicGFnZV9tZXRob2QiOiJHRVQiLCJwYWdlX3JlcXVlc3QiOnt9LCJwYWdlX2hlYWRlcnMiOnt9LCJob3N0Ijoic2xvd3dseS5yb2JlcnRvbXVycmF5LmNvLnVrIiwiaXAiOiI3MC4xODkuODcuMjUzIn0K";</script>
   <script src="/bGmQgAKzk.js"></script>
   </body>
   </html>

   URL accessed 2 times.
   ```

5. **Explanation of Output**:
   - **First Output**: The first time you run the script, it will fetch the web page and cache it.
   - **Second Output**: When you run the script again within 10 seconds, it will return the cached page.
   - **Access Count**: Redis keeps track of how many times the URL is accessed (whether it’s cached or not).

6. **Why this Output**:
   - **What**: The HTML content is fetched or served from Redis, and the number of times the URL was accessed is displayed.
   - **Where**: Redis stores the cached content and the access count.
   - **Why**: Caching improves efficiency by avoiding redundant requests to the server.
   - **How**: The `cache_with_expiry` decorator handles caching and tracks access counts.
   - **When**: The access count is updated every time `get_page` is called, and the cache lasts for 10 seconds.

    </details>

