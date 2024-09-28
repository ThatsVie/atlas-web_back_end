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
  service redis-server start
  ```

</details>


## Tasks and Usage

### Task 0: Writing Strings to Redis

<details>
  <summary><strong>Curriculum Instruction</strong></summary>

- Create a `Cache` class. In the `__init__` method, store an instance of the Redis client as a private variable named `_redis` (using `redis.Redis()`) and flush the instance using `flushdb`.
- Create a `store` method that takes a `data` argument and returns a string.
- The `store` method should:
  - Generate a random key (e.g. using `uuid`),
  - Store the input data in Redis using the random key, and
  - Return the generated key.
- Ensure correct type annotations for the `store` method. The `data` argument can be a `str`, `bytes`, `int`, or `float`.
</details>

<details>
  <summary><strong>Steps and Code Implementation</strong></summary>

### Steps:

1. **Initialize the Redis Client**: In the `__init__` method, instantiate the Redis client and flush the database.
   - Example:
     ```python
     self._redis = redis.Redis()
     self._redis.flushdb()
     ```

2. **Create the `store` Method**: This method generates a random key using `uuid`, stores the provided data in Redis, and returns the key.

3. **Type Annotations**: Annotate the method to ensure the `data` parameter can accept `str`, `bytes`, `int`, or `float`, and the return type should be a `str`.

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

4. **Testing**: Test the class and method by storing a string and retrieving it using Redis.

#### 0-main.py:
```python
#!/usr/bin/env python3
"""
Main file for Task 0
"""
import redis

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
   Before executing the script, ensure that the Redis server is running:
   ```bash
   sudo service redis-server start
   ```

2. **Run the test script**:
   You can now execute the script either using `python3` or by making it executable and using `./`:
   ```bash
   ./0-main.py
   ```
**Output:**
```bash
034c0dea-0bd8-4811-94a8-40c0e5762191
b'hello'
```

3. **Explanation of Output**:
   - The first output (`034c0dea-0bd8-4811-94a8-40c0e5762191`) is a randomly generated UUID key, which acts like a unique name for the data in Redis.
   - The second output (`b'hello'`) is the stored value retrieved from Redis, showing that the data was successfully stored and can be fetched by the key.

4. **Why this Output**:
   - **What**: A unique key and the stored data.
   - **Where**: The key and data are stored in Redis, a powerful in-memory key-value store.
   - **Why**: The unique key ensures that each piece of data can be stored without conflict. Redis retrieves the data exactly as it was input (in this case, as a byte string).
   - **How**: Redis uses the `set` and `get` methods to store and retrieve data based on the key.
   - **When**: The `store` method is called to save the data, and the `get` method is used to retrieve it.

</details>


## Author

GitHub: [ThatsVie](https://github.com/ThatsVie)
