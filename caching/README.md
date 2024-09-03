# Caching

In this project, we will learn different caching algorithms and their implementations in Python. Caching is a technique that improves performance by storing frequently accessed data in a temporary storage area, or "cache." Various caching strategies are used to decide which data to store in the cache and which to evict when the cache is full.

## Learning Objectives

By the end of this project, you will be able to explain:

- What a caching system is
- What FIFO (First In, First Out) means
- What LIFO (Last In, First Out) means
- What LRU (Least Recently Used) means
- What MRU (Most Recently Used) means
- What LFU (Least Frequently Used) means
- The purpose of a caching system
- The limitations of a caching system

## Resources

To complete this project, refer to the following resources:

- [Cache replacement policies - FIFO](https://en.wikipedia.org/wiki/Cache_replacement_policies#First_In_First_Out_%28FIFO%29)
- [Cache replacement policies - LIFO](https://en.wikipedia.org/wiki/Cache_replacement_policies#Last_In_First_Out_%28LIFO%29)
- [Cache replacement policies - LRU](https://en.wikipedia.org/wiki/Cache_replacement_policies#Least_Recently_Used_%28LRU%29)
- [Cache replacement policies - MRU](https://en.wikipedia.org/wiki/Cache_replacement_policies#Most_Recently_Used_%28MRU%29)
- [Cache replacement policies - LFU](https://en.wikipedia.org/wiki/Cache_replacement_policies#Least-Frequently_Used_%28LFU%29)

## Requirements

- **Python Scripts**: All scripts will be interpreted/compiled on Ubuntu 20.04 LTS using Python 3.9.
- **Code Style**: Adhere to the `pycodestyle` style (version 2.5).
- **Documentation**: All modules, classes, and functions must be documented with purpose-explaining sentences.
- **File Naming**: All files must end with a new line and should have appropriate permissions to be executable.
- **Class and Functionality**: All classes should inherit from the `BaseCaching` parent class.

## BaseCaching Class

<details> <summary>The `BaseCaching` class serves as the parent class for all your caching systems. Here is the provided implementation:</summary>


```python
#!/usr/bin/python3
""" BaseCaching module
"""

class BaseCaching():
    """ BaseCaching defines:
      - constants of your caching system
      - where your data are stored (in a dictionary)
    """
    MAX_ITEMS = 4

    def __init__(self):
        """ Initialize
        """
        self.cache_data = {}

    def print_cache(self):
        """ Print the cache
        """
        print("Current cache:")
        for key in sorted(self.cache_data.keys()):
            print("{}: {}".format(key, self.cache_data.get(key)))

    def put(self, key, item):
        """ Add an item in the cache
        """
        raise NotImplementedError("put must be implemented in your cache class")

    def get(self, key):
        """ Get an item by key
        """
        raise NotImplementedError("get must be implemented in your cache class")
```
</details>

## Tasks and Detailed Usage

### Task 0: Basic dictionary

<details> 
<summary> Create a class BasicCache that inherits from BaseCaching and is a caching system:
You must use self.cache_data - dictionary from the parent class BaseCaching
This caching system doesn’t have limit
def put(self, key, item):
Must assign to the dictionary self.cache_data the item value for the key key.
If key or item is None, this method should not do anything.
def get(self, key):
Must return the value in self.cache_data linked to key.
If key is None or if the key doesn’t exist in self.cache_data, return None.
</summary>
<br>

**Description:**
The `BasicCache` class is a simple caching system that inherits from the `BaseCaching` parent class. Unlike other caching systems, this cache has no limit on the number of items it can store. The class provides two primary methods:

- `put(key, item)`: Adds an item to the cache.
- `get(key)`: Retrieves an item by key from the cache.

**Implementation**:
```python
#!/usr/bin/env python3
''' Module for BasicCache class.
This module contains the BasicCache class, a simple caching system
that inherits from the BaseCaching parent class. It has no limit on
the number of items it can store in the cache.
'''
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    ''' BasicCache defines a caching system with no item limit.
    It inherits from BaseCaching.
    '''

    def put(self, key, item):
        ''' Add an item to the cache.
        If key or item is None, this method does nothing.
        '''
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        ''' Retrieve an item by key from the cache.
        If key is None or doesn't exist in the cache, returns None.
        '''
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]

```

**Usage:**


1. **Initialization**:
   To use the `BasicCache` class, import it from the `0-basic_cache.py` file and create an instance:

   ```python
   BasicCache = __import__('0-basic_cache').BasicCache

   my_cache = BasicCache()
   ```

2. **Adding items to the cache**:
   Use the `put` method to add key-value pairs to the cache. If either the `key` or `item` is `None`, the method does nothing.

   ```python
   my_cache.put("A", "Hello")  # Adds "A": "Hello" to the cache
   my_cache.put("B", "World")  # Adds "B": "World" to the cache
   my_cache.put("C", "Holberton")  # Adds "C": "Holberton" to the cache
   ```

3. **Retrieving items from the cache**:
   Use the `get` method to retrieve values from the cache using their keys. If the `key` is `None` or doesn't exist, the method returns `None`.

   ```python
   print(my_cache.get("A"))  # Output: Hello
   print(my_cache.get("B"))  # Output: World
   print(my_cache.get("C"))  # Output: Holberton
   print(my_cache.get("D"))  # Output: None
   ```

4. **Displaying the current cache**:
   The `print_cache` method of the `BaseCaching` class can be used to display the current state of the cache.

   ```python
   my_cache.print_cache()
   ```

5. **Running the script to test the class**:
   To test the functionality of the `BasicCache` class, create a test script named `0-main.py` with the following content:

   ```python
   #!/usr/bin/python3
   ''' 0-main module
   Tests the BasicCache class.
   '''

   BasicCache = __import__('0-basic_cache').BasicCache

   my_cache = BasicCache()
   my_cache.print_cache()  # Expected output: "Current cache:" (empty)
   my_cache.put("A", "Hello")
   my_cache.put("B", "World")
   my_cache.put("C", "Holberton")
   my_cache.print_cache()
   # Expected output:
   # Current cache:
   # A: Hello
   # B: World
   # C: Holberton

   print(my_cache.get("A"))  # Output: Hello
   print(my_cache.get("B"))  # Output: World
   print(my_cache.get("C"))  # Output: Holberton
   print(my_cache.get("D"))  # Output: None

   my_cache.put("D", "School")
   my_cache.put("E", "Battery")
   my_cache.put("A", "Street")
   my_cache.print_cache()
   # Expected output:
   # Current cache:
   # A: Street
   # B: World
   # C: Holberton
   # D: School
   # E: Battery

   print(my_cache.get("A"))  # Output: Street
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
Current cache:
Current cache:
A: Hello
B: World
C: Holberton
Hello
World
Holberton
None
Current cache:
A: Hello
B: World
C: Holberton
Current cache:
A: Street
B: World
C: Holberton
D: School
E: Battery
Street
```

**Explanation**

- **`put` Method**: Adds an item to the cache if both `key` and `item` are not `None`.
- **`get` Method**: Retrieves the value associated with the `key` from the cache. Returns `None` if `key` is `None` or does not exist in the cache.
- **Cache Display**: The cache state is printed using the `print_cache` method.


</details>
