
![cachingpuggie!](https://github.com/user-attachments/assets/3f7251bf-3f91-4930-860b-edf12b357843)


This project covers different caching algorithms, including FIFO, LIFO, LRU, MRU, and LFU, to optimize data retrieval performance by managing temporary storage of frequently accessed data. It demonstrates various cache replacement strategies to efficiently handle limited cache size and improve system responsiveness. By implementing these algorithms, the project highlights the trade-offs and effectiveness of each caching method in different scenarios.

## Learning Objectives

<details>
<summary>What a caching system is</summary>
  
A caching system temporarily stores frequently accessed data to improve data retrieval speed and reduce the need to access the underlying slower storage. By keeping a small amount of frequently or recently used data in a cache, a system can significantly reduce the time it takes to retrieve that data.  
Covered in **all tasks**.

</details>

<details>
<summary>What FIFO (First In, First Out) means</summary>

FIFO is a cache replacement policy where the oldest added item (first in) is the first to be removed (first out) when the cache reaches its maximum size. This strategy is simple but may not always provide the best performance if the older data is frequently accessed.  
Covered in **Task 1: FIFO Caching**.

</details>

<details>
<summary>What LIFO (Last In, First Out) means</summary>

LIFO is a cache replacement policy where the most recently added item (last in) is the first to be removed (first out) when the cache reaches its maximum size. This strategy prioritizes keeping older data while discarding the newest, which might not be optimal if new data is frequently accessed.  
Covered in **Task 2: LIFO Caching**.

</details>

<details>
<summary>What LRU (Least Recently Used) means</summary>

LRU is a cache replacement policy that removes the least recently accessed item when the cache reaches its maximum size. This strategy assumes that items not recently used are less likely to be accessed soon, making it a good choice for workloads where data locality is important.  
Covered in **Task 3: LRU Caching**.

</details>

<details>
<summary>What MRU (Most Recently Used) means</summary>

MRU is a cache replacement policy that removes the most recently accessed item when the cache reaches its maximum size. This strategy assumes that the most recently used items are less likely to be accessed again soon. It can be useful in scenarios where older data is more likely to be reused than the newest data.  
Covered in **Task 4: MRU Caching**.

</details>

<details>
<summary>What LFU (Least Frequently Used) means</summary>

LFU is a cache replacement policy that removes the item with the least frequency of access when the cache reaches its maximum size. If multiple items have the same frequency, the least recently used (LRU) item among them is discarded. This strategy is effective when items are frequently reused over time.  
Covered in **Task 5: LFU Caching**.

</details>

<details>
<summary>The purpose of a caching system</summary>

The primary purpose of a caching system is to reduce data access times and improve overall system performance by temporarily storing frequently or recently accessed data in a faster storage medium. Caching reduces the need to repeatedly access slower backend storage, thereby speeding up data retrieval and reducing the load on the main storage.  
Covered in **all tasks**.

</details>

<details>
<summary>The limitations of a caching system</summary>

Caching systems have several limitations:  
- **Limited Size:** Caches have a limited size and can only store a small subset of the total data, requiring an effective replacement strategy to manage the cache contents.  
- **Cache Invalidation:** Data in the cache may become outdated (stale), requiring mechanisms to invalidate or update cache entries.  
- **Increased Complexity:** Implementing caching adds complexity to the system design, including cache management, eviction strategies, and synchronization with the main storage.  
- **Cache Misses:** When a requested item is not in the cache (cache miss), there is an added cost of fetching data from the slower backend storage.  

</details>


## Resources

- [Cache replacement policies - FIFO](https://en.wikipedia.org/wiki/Cache_replacement_policies#First_In_First_Out_%28FIFO%29): Describes the FIFO (First In, First Out) policy, where the oldest cached data is removed first when the cache is full.
  
- [Cache replacement policies - LIFO](https://en.wikipedia.org/wiki/Cache_replacement_policies#Last_In_First_Out_%28LIFO%29): Explains the LIFO (Last In, First Out) policy, which removes the most recently added data from the cache first.
  
- [Cache replacement policies - LRU](https://en.wikipedia.org/wiki/Cache_replacement_policies#Least_Recently_Used_%28LRU%29): Details the LRU (Least Recently Used) policy, which discards the least recently accessed data to manage cache size.
  
- [Cache replacement policies - MRU](https://en.wikipedia.org/wiki/Cache_replacement_policies#Most_Recently_Used_%28MRU%29): Covers the MRU (Most Recently Used) policy, where the most recently accessed data is discarded first when the cache needs to be cleared.
  
- [Cache replacement policies - LFU](https://en.wikipedia.org/wiki/Cache_replacement_policies#Least-Frequently_Used_%28LFU%29): Discusses the LFU (Least Frequently Used) policy, which removes the data with the lowest access frequency, using LRU as a tie-breaker if needed.

- [Difference Between LRU and FIFO Page Replacement Algorithms in Operating Systems](https://www.geeksforgeeks.org/difference-between-lru-and-fifo-page-replacement-algorithms-in-operating-system/?ref=gcse_ind): Compares LRU (Least Recently Used) and FIFO (First In, First Out) algorithms, explaining their differences and suitable use cases.

- [Page Replacement Algorithms in Operating Systems](https://www.geeksforgeeks.org/page-replacement-algorithms-in-operating-systems/?ref=gcse_ind): Provides an overview of various page replacement algorithms, including FIFO, LRU, LFU, and others, used in operating systems.

- [Least Frequently Used (LFU) Cache Implementation](https://www.geeksforgeeks.org/least-frequently-used-lfu-cache-implementation/?ref=header_outind): Explains the LFU (Least Frequently Used) caching algorithm with an example implementation in Python.

- [LRU Cache Implementation](https://www.geeksforgeeks.org/lru-cache-implementation/?ref=header_outind): Details the LRU (Least Recently Used) caching algorithm and provides a step-by-step guide to implementing it in Python.

- [Cache Eviction Policies | System Design](https://www.geeksforgeeks.org/cache-eviction-policies-system-design/?ref=header_outind): Discusses different cache eviction policies like LRU, LFU, FIFO, and others, focusing on their applications in system design.


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
   To test the functionality of the `BasicCache` class, use `0-main.py`:

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

### Task 1: FIFO caching

<details> 
<summary> Create a class FIFOCache that inherits from BaseCaching and implements a FIFO (First In, First Out) caching system:
You must use self.cache_data - dictionary from the parent class BaseCaching
You can overload def __init__(self): but don’t forget to call the parent init: super().__init__()
def put(self, key, item):
Must assign to the dictionary self.cache_data the item value for the key key.
If key or item is None, this method should not do anything.
If the number of items in self.cache_data is higher than BaseCaching.MAX_ITEMS:
you must discard the first item put in cache (FIFO algorithm)
you must print DISCARD: with the key discarded followed by a new line
def get(self, key):
Must return the value in self.cache_data linked to key.
If key is None or if the key doesn’t exist in self.cache_data, return None.
</summary>
<br>

**Description:**
The `FIFOCache` class is a caching system that inherits from the `BaseCaching` parent class. It uses a FIFO (First In, First Out) caching algorithm. The class maintains the order in which items are added to the cache and removes the oldest item when the cache exceeds its size limit (`MAX_ITEMS`).

- `put(key, item)`: Adds an item to the cache. If the cache exceeds its size limit, it discards the oldest item following the FIFO policy.
- `get(key)`: Retrieves an item by key from the cache.

**Implementation**:
```python
#!/usr/bin/env python3
'''
This module contains the FIFOCache class, a caching system
that inherits from the BaseCaching parent class. It uses the
FIFO (First In, First Out) caching algorithm.
'''
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    ''' FIFOCache defines a caching system with a FIFO eviction policy.
    '''

    def __init__(self):
        '''
        Calls the parent class' init method and initializes
        an order list to keep track of the insertion order.
        '''
        super().__init__()
        self.order = []

    def put(self, key, item):
        ''' Add an item to the cache.
        If key or item is None this method does nothing.
        If the number of items in the cache exceeds MAX_ITEMS
        the first item added is discarded following FIFO.
        '''
        if key is not None and item is not None:
            if key not in self.cache_data:
                self.order.append(key)
            self.cache_data[key] = item

            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                first_key = self.order.pop(0)
                del self.cache_data[first_key]
                print(f"DISCARD: {first_key}")

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
   To use the `FIFOCache` class, import it from the `1-fifo_cache.py` file and create an instance:

   ```python
   FIFOCache = __import__('1-fifo_cache').FIFOCache

   my_cache = FIFOCache()
   ```

2. **Adding items to the cache**:
   Use the `put` method to add key-value pairs to the cache. If either the `key` or `item` is `None`, the method does nothing. If the cache exceeds its size limit, the oldest item will be removed following the FIFO algorithm.

   ```python
   my_cache.put("A", "Hello")
   my_cache.put("B", "World")
   my_cache.put("C", "Holberton")
   my_cache.put("D", "School")
   my_cache.print_cache()
   ```

3. **Evicting items based on FIFO**:
   When the cache exceeds `MAX_ITEMS`, the `put` method discards the first item added to the cache and prints a message indicating which item was discarded.

4. **Retrieving items from the cache**:
   Use the `get` method to retrieve values from the cache using their keys. If the `key` is `None` or doesn't exist, the method returns `None`.

   ```python
   print(my_cache.get("A"))  # May output: None (if "A" has been discarded)
   print(my_cache.get("B"))  # Output: World
   ```

5. **Running the script to test the class**:
   To test the functionality of the `FIFOCache` class, use `1-main.py`:

   ```python
   #!/usr/bin/python3
   """ 1-main """
   FIFOCache = __import__('1-fifo_cache').FIFOCache

   my_cache = FIFOCache()
   my_cache.put("A", "Hello")
   my_cache.put("B", "World")
   my_cache.put("C", "Holberton")
   my_cache.put("D", "School")
   my_cache.print_cache()
   my_cache.put("E", "Battery")
   my_cache.print_cache()
   my_cache.put("C", "Street")
   my_cache.print_cache()
   my_cache.put("F", "Mission")
   my_cache.print_cache()
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
Current cache:
A: Hello
B: World
C: Holberton
D: School
DISCARD: A
Current cache:
B: World
C: Holberton
D: School
E: Battery
Current cache:
B: World
C: Street
D: School
E: Battery
DISCARD: B
Current cache:
C: Street
D: School
E: Battery
F: Mission
```

**Explanation**

- **`put` Method**: Adds an item to the cache if both `key` and `item` are not `None`. If the cache exceeds `MAX_ITEMS`, the first item is discarded.
- **`get` Method**: Retrieves the value associated with the `key` from the cache. Returns `None` if `key` is `None` or does not exist in the cache.
- **Cache Display**: The cache state is printed using the `print_cache` method, and items are evicted based on the FIFO policy.

</details>

### Task 2: LIFO Caching

<details> 
<summary> Create a class LIFOCache that inherits from BaseCaching and implements a LIFO (Last In, First Out) caching system:
You must use `self.cache_data` - dictionary from the parent class `BaseCaching`.
You can overload `__init__()` but don't forget to call the parent init: `super().__init__()`.
`put(self, key, item)`: Must assign to the dictionary `self.cache_data` the item value for the key `key`. If `key` or `item` is `None`, this method should not do anything. If the number of items in `self.cache_data` is higher than `BaseCaching.MAX_ITEMS`, discard the last item put in cache (LIFO algorithm) and print `DISCARD:` with the key discarded followed by a new line.
`get(self, key)`: Must return the value in `self.cache_data` linked to `key`. If `key` is `None` or if the key doesn’t exist in `self.cache_data`, return `None`.
</summary>
<br>

**Description:**
The `LIFOCache` class is a caching system that inherits from the `BaseCaching` parent class. It uses a LIFO (Last In, First Out) caching algorithm. The class removes the most recently added item from the cache when the cache exceeds its size limit (`MAX_ITEMS`).

- `put(key, item)`: Adds an item to the cache. If the cache exceeds its size limit, it discards the last item added following the LIFO policy.
- `get(key)`: Retrieves an item by key from the cache.

**Implementation:**
```python
#!/usr/bin/env python3
'''
This module contains the LIFOCache class, a caching system
that inherits from the BaseCaching parent class. It uses the
LIFO (Last In, First Out) caching algorithm.
'''
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    ''' LIFOCache defines a caching system with a LIFO eviction policy.
    '''

    def __init__(self):
        '''
        Calls the parent class' init method and initializes
        a list to keep track of the order of insertion.
        '''
        super().__init__()
        self.stack = []

    def put(self, key, item):
        ''' Add an item to the cache.
        If key or item is None this method does nothing.
        If the number of items in the cache exceeds MAX_ITEMS,
        the last item added is discarded following LIFO.
        '''
        if key is not None and item is not None:
            self.cache_data[key] = item
            self.stack.append(key)

            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                # Remove the most recently added item
                last_key = self.stack.pop(-2)
                del self.cache_data[last_key]
                print(f"DISCARD: {last_key}")

    def get(self, key):
        ''' Retrieve an item by key from the cache.
        If key is None or doesn't exist in the cache, it returns None.
        '''
        return self.cache_data.get(key, None)
```

**Usage:**

1. **Initialization**:
   To use the `LIFOCache` class, import it from the `2-lifo_cache.py` file and create an instance:

   ```python
   LIFOCache = __import__('2-lifo_cache').LIFOCache

   my_cache = LIFOCache()
   ```

2. **Adding items to the cache**:
   Use the `put` method to add key-value pairs to the cache. If either the `key` or `item` is `None`, the method does nothing. If the cache exceeds its size limit, the most recently added item will be removed following the LIFO algorithm.

   ```python
   my_cache.put("A", "Hello")
   my_cache.put("B", "World")
   my_cache.put("C", "Holberton")
   my_cache.put("D", "School")
   my_cache.print_cache()
   ```

3. **Evicting items based on LIFO**:
   When the cache exceeds `MAX_ITEMS`, the `put` method discards the most recently added item to the cache and prints a message indicating which item was discarded.

4. **Retrieving items from the cache**:
   Use the `get` method to retrieve values from the cache using their keys. If the `key` is `None` or doesn't exist, the method returns `None`.

   ```python
   print(my_cache.get("A"))  # Output: Hello
   print(my_cache.get("B"))  # Output: World
   ```

5. **Running the script to test the class**:
   To test the functionality of the `LIFOCache` class, use `2-main.py`:
   ```python
   #!/usr/bin/python3
   """ 2-main """
   LIFOCache = __import__('2-lifo_cache').LIFOCache

   my_cache = LIFOCache()
   my_cache.put("A", "Hello")
   my_cache.put("B", "World")
   my_cache.put("C", "Holberton")
   my_cache.put("D", "School")
   my_cache.print_cache()
   my_cache.put("E", "Battery")
   my_cache.print_cache()
   my_cache.put("C", "Street")
   my_cache.print_cache()
   my_cache.put("F", "Mission")
   my_cache.print_cache()
   my_cache.put("G", "San Francisco")
   my_cache.print_cache()
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
Current cache:
A: Hello
B: World
C: Holberton
D: School
DISCARD: D
Current cache:
A: Hello
B: World
C: Holberton
E: Battery
Current cache:
A: Hello
B: World
C: Street
E: Battery
DISCARD: C
Current cache:
A: Hello
B: World
E: Battery
F: Mission
DISCARD: F
Current cache:
A: Hello
B: World
E: Battery
G: San Francisco
```

**Explanation**

- **`put` Method**: Adds an item to the cache if both `key` and `item` are not `None`. If the cache exceeds `MAX_ITEMS`, the most recently added item is discarded.
- **`get` Method**: Retrieves the value associated with the `key` from the cache. Returns `None` if `key` is `None` or does not exist in the cache.
- **Cache Display**: The cache state is printed using the `print_cache` method, and items are evicted based on the LIFO policy.

</details>

### Task 3: LRU Caching

<details> 
<summary> Create a class LRUCache that inherits from BaseCaching and implements an LRU (Least Recently Used) caching system:
You must use `self.cache_data` - dictionary from the parent class `BaseCaching`.
You can overload `__init__()` but don't forget to call the parent init: `super().__init__()`.
`put(self, key, item)`: Must assign to the dictionary `self.cache_data` the item value for the key `key`. If `key` or `item` is `None`, this method should not do anything. If the number of items in `self.cache_data` is higher than `BaseCaching.MAX_ITEMS`, discard the least recently used item (LRU algorithm) and print `DISCARD:` with the key discarded followed by a new line.
`get(self, key)`: Must return the value in `self.cache_data` linked to `key`. If `key` is `None` or if the key doesn’t exist in `self.cache_data`, return `None`.
</summary>
<br>

**Description:**
The `LRUCache` class is a caching system that inherits from the `BaseCaching` parent class. It uses an LRU (Least Recently Used) caching algorithm. The class keeps track of the order in which keys are accessed and removes the least recently used item from the cache when it exceeds its size limit (`MAX_ITEMS`).

- `put(key, item)`: Adds an item to the cache. If the cache exceeds its size limit, it discards the least recently used item following the LRU policy.
- `get(key)`: Retrieves an item by key from the cache.

**Implementation:**
```python
#!/usr/bin/env python3
'''
This module contains the LRUCache class, a caching system
that inherits from the BaseCaching parent class. It uses the
LRU (Least Recently Used) caching algorithm.
'''
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    ''' LRUCache defines a caching system with an LRU eviction policy.
    '''

    def __init__(self):
        '''
        Calls the parent class' init method and initializes
        an ordered list to keep track of the usage order.
        '''
        super().__init__()
        self.usage_order = []

    def put(self, key, item):
        ''' Add an item to the cache.
        If key or item is None this method does nothing.
        If the number of items in the cache exceeds MAX_ITEMS,
        the least recently used item is discarded following LRU.
        '''
        if key is not None and item is not None:
            # If the key already exists update the item and move key to the end
            if key in self.cache_data:
                self.usage_order.remove(key)
            self.cache_data[key] = item
            self.usage_order.append(key)

            # If cache exceeds the max size remove the LRU item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                lru_key = self.usage_order.pop(0)
                del self.cache_data[lru_key]
                print(f"DISCARD: {lru_key}")

    def get(self, key):
        ''' Retrieve an item by key from the cache.
        If key is None or doesn't exist in the cache it returns None.
        '''
        if key is not None and key in self.cache_data:
            # Since this key was recently accessed update the usage order
            self.usage_order.remove(key)
            self.usage_order.append(key)
            return self.cache_data[key]
        return None
```

**Usage:**

1. **Initialization**:
   To use the `LRUCache` class, import it from the `3-lru_cache.py` file and create an instance:

   ```python
   LRUCache = __import__('3-lru_cache').LRUCache

   my_cache = LRUCache()
   ```

2. **Adding items to the cache**:
   Use the `put` method to add key-value pairs to the cache. If either the `key` or `item` is `None`, the method does nothing. If the cache exceeds its size limit, the least recently used item will be removed following the LRU algorithm.

   ```python
   my_cache.put("A", "Hello")
   my_cache.put("B", "World")
   my_cache.put("C", "Holberton")
   my_cache.put("D", "School")
   my_cache.print_cache()
   ```

3. **Evicting items based on LRU**:
   When the cache exceeds `MAX_ITEMS`, the `put` method discards the least recently used item in the cache and prints a message indicating which item was discarded.

4. **Retrieving items from the cache**:
   Use the `get` method to retrieve values from the cache using their keys. If the `key` is `None` or doesn't exist, the method returns `None`.

   ```python
   print(my_cache.get("B"))  # Output: World
   ```

5. **Running the script to test the class**:
   To test the functionality of the `LRUCache` class, use `3-main.py`:

   ```python
   #!/usr/bin/python3
   """ 3-main """
   LRUCache = __import__('3-lru_cache').LRUCache

   my_cache = LRUCache()
   my_cache.put("A", "Hello")
   my_cache.put("B", "World")
   my_cache.put("C", "Holberton")
   my_cache.put("D", "School")
   my_cache.print_cache()
   print(my_cache.get("B"))
   my_cache.put("E", "Battery")
   my_cache.print_cache()
   my_cache.put("C", "Street")
   my_cache.print_cache()
   print(my_cache.get("A"))
   print(my_cache.get("B"))
   print(my_cache.get("C"))
   my_cache.put("F", "Mission")
   my_cache.print_cache()
   my_cache.put("G", "San Francisco")
   my_cache.print_cache()
   my_cache.put("H", "H")
   my_cache.print_cache()
   my_cache.put("I", "I")
   my_cache.print_cache()
   my_cache.put("J", "J")
   my_cache.print_cache()
   my_cache.put("K", "K")
   my_cache.print_cache()
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
Current cache:
A: Hello
B: World
C: Holberton
D: School
World
DISCARD: A
Current cache:
B: World
C: Holberton
D: School
E: Battery
Current cache:
B: World
C: Street
D: School
E: Battery
None
World
Street
DISCARD: D
Current cache:
B: World
C: Street
E: Battery
F: Mission
DISCARD: E
Current cache:
B: World
C: Street
F: Mission
G: San Francisco
DISCARD: B
Current cache:
C: Street
F: Mission
G: San Francisco
H: H
DISCARD: C
Current cache:
F: Mission
G: San Francisco
H: H
I: I
DISCARD: F
Current cache:
G: San Francisco
H: H
I: I
J: J
DISCARD: G
Current cache:
H: H
I: I
J: J
K: K
```

**Explanation**

- **`put` Method**: Adds an item to the cache if both `key` and `item` are not `None`. If the cache exceeds `MAX_ITEMS`, the least recently used item is discarded.
- **`get` Method**: Retrieves the value associated with the `key` from the cache. Updates the usage order to reflect recent access. Returns `None` if `key` is `None` or does not exist in the cache.
- **Cache Display**: The cache state is printed using the `print_cache` method, and items are evicted based on the LRU policy.

</details>

### Task 4: MRU Caching

<details> 
<summary> Create a class MRUCache that inherits from BaseCaching and implements an MRU (Most Recently Used) caching system:
You must use `self.cache_data` - dictionary from the parent class `BaseCaching`.
You can overload `__init__()` but don't forget to call the parent init: `super().__init__()`.
`put(self, key, item)`: Must assign to the dictionary `self.cache_data` the item value for the key `key`. If `key` or `item` is `None`, this method should not do anything. If the number of items in `self.cache_data` is higher than `BaseCaching.MAX_ITEMS`, discard the most recently used item (MRU algorithm) and print `DISCARD:` with the key discarded followed by a new line.
`get(self, key)`: Must return the value in `self.cache_data` linked to `key`. If `key` is `None` or if the key doesn’t exist in `self.cache_data`, return `None`.
</summary>
<br>

**Description:**
The `MRUCache` class is a caching system that inherits from the `BaseCaching` parent class. It uses an MRU (Most Recently Used) caching algorithm. The class keeps track of the order in which keys are accessed and removes the most recently used item from the cache when it exceeds its size limit (`MAX_ITEMS`).

- `put(key, item)`: Adds an item to the cache. If the cache exceeds its size limit, it discards the most recently used item following the MRU policy.
- `get(key)`: Retrieves an item by key from the cache.

**Implementation:**
```python
#!/usr/bin/env python3
'''
This module contains the MRUCache class, a caching system
that inherits from the BaseCaching parent class. It uses the
MRU (Most Recently Used) caching algorithm.
'''
BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    ''' MRUCache defines a caching system with an MRU eviction policy.
    '''

    def __init__(self):
        '''
        Calls the parent class' init method and initializes
        a list to keep track of the usage order.
        '''
        super().__init__()
        self.usage_order = []

    def put(self, key, item):
        ''' Add an item to the cache.
        If key or item is None this method does nothing.
        If the number of items in the cache exceeds MAX_ITEMS
        the most recently used item is discarded following MRU.
        '''
        if key is not None and item is not None:
            # If the key already exists update the item and move key to the end
            if key in self.cache_data:
                self.usage_order.remove(key)
            self.cache_data[key] = item
            self.usage_order.append(key)

            # If cache exceeds the maximum size remove the MRU item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                mru_key = self.usage_order.pop(-2)
                del self.cache_data[mru_key]
                print(f"DISCARD: {mru_key}")

    def get(self, key):
        ''' Retrieve an item by key from the cache.
        If key is None or doesn't exist in the cache it returns None.
        '''
        if key is not None and key in self.cache_data:
            # Since this key was recently accessed update the usage order
            self.usage_order.remove(key)
            self.usage_order.append(key)
            return self.cache_data[key]
        return None
```

**Usage:**

1. **Initialization**:
   To use the `MRUCache` class, import it from the `4-mru_cache.py` file and create an instance:

   ```python
   MRUCache = __import__('4-mru_cache').MRUCache

   my_cache = MRUCache()
   ```

2. **Adding items to the cache**:
   Use the `put` method to add key-value pairs to the cache. If either the `key` or `item` is `None`, the method does nothing. If the cache exceeds its size limit, the most recently used item will be removed following the MRU algorithm.

   ```python
   my_cache.put("A", "Hello")
   my_cache.put("B", "World")
   my_cache.put("C", "Holberton")
   my_cache.put("D", "School")
   my_cache.print_cache()
   ```

3. **Evicting items based on MRU**:
   When the cache exceeds `MAX_ITEMS`, the `put` method discards the most recently used item in the cache and prints a message indicating which item was discarded.

4. **Retrieving items from the cache**:
   Use the `get` method to retrieve values from the cache using their keys. If the `key` is `None` or doesn't exist, the method returns `None`.

   ```python
   print(my_cache.get("B"))  # Output: World
   ```

5. **Running the script to test the class**:
   To test the functionality of the `MRUCache` class, use `4-main.py`:

   ```python
   #!/usr/bin/python3
   """ 4-main """
   MRUCache = __import__('4-mru_cache').MRUCache

   my_cache = MRUCache()
   my_cache.put("A", "Hello")
   my_cache.put("B", "World")
   my_cache.put("C", "Holberton")
   my_cache.put("D", "School")
   my_cache.print_cache()
   print(my_cache.get("B"))
   my_cache.put("E", "Battery")
   my_cache.print_cache()
   my_cache.put("C", "Street")
   my_cache.print_cache()
   print(my_cache.get("A"))
   print(my_cache.get("B"))
   print(my_cache.get("C"))
   my_cache.put("F", "Mission")
   my_cache.print_cache()
   my_cache.put("G", "San Francisco")
   my_cache.print_cache()
   my_cache.put("H", "H")
   my_cache.print_cache()
   my_cache.put("I", "I")
   my_cache.print_cache()
   my_cache.put("J", "J")
   my_cache.print_cache()
   my_cache.put("K", "K")
   my_cache.print_cache()
   ```

   Make the script executable by running:

   ```sh
   chmod +x 4-main.py
   ```

   Then, run the script to test:

   ```sh
   ./4-main.py
   ```

   Verify the output matches the expected results.

**Expected Output:**
```bash
Current cache:
A: Hello
B: World
C: Holberton
D: School
World
DISCARD: B
Current cache:
A: Hello
C: Holberton
D: School
E: Battery
Current cache:
A: Hello
C: Street
D: School
E: Battery
Hello
None
Street
DISCARD: C
Current cache:
A: Hello
D: School
E: Battery
F: Mission
DISCARD: F
Current cache:
A: Hello
D: School
E: Battery
G: San Francisco
DISCARD: G
Current cache:
A: Hello
D: School
E: Battery
H: H
DISCARD: H
Current cache:
A: Hello
D: School
E: Battery
I: I
DISCARD: I
Current cache:
A: Hello
D: School
E: Battery
J: J
DISCARD: J
Current cache:
A: Hello
D: School
E: Battery
K: K
```

**Explanation**

- **`put` Method**: Adds an item to the cache if both `key` and `item` are not `None`. If the cache exceeds `MAX_ITEMS`, the most recently used item is discarded.
- **`get` Method**: Retrieves the value associated with the `key` from the cache. Updates the usage order to reflect recent access. Returns `None` if `key` is `None` or does not exist in the cache.
- **Cache Display**: The cache state is printed using the `print_cache` method, and items are evicted based on the MRU policy.

</details>

### Task 5: LFU Caching

<details> 
<summary> Create a class LFUCache that inherits from BaseCaching and implements an LFU (Least Frequently Used) caching system:
You must use `self.cache_data` - dictionary from the parent class `BaseCaching`.
You can overload `__init__()` but don't forget to call the parent init: `super().__init__()`.
`put(self, key, item)`: Must assign to the dictionary `self.cache_data` the item value for the key `key`. If `key` or `item` is `None`, this method should not do anything. If the number of items in `self.cache_data` is higher than `BaseCaching.MAX_ITEMS`, discard the least frequently used item (LFU algorithm). If multiple items have the same frequency, use the LRU algorithm to discard the least recently used item.
`get(self, key)`: Must return the value in `self.cache_data` linked to `key`. If `key` is `None` or if the key doesn’t exist in `self.cache_data`, return `None`.
</summary>
<br>

**Description:**
The `LFUCache` class is a caching system that inherits from the `BaseCaching` parent class. It uses an LFU (Least Frequently Used) caching algorithm with LRU (Least Recently Used) as a tie-breaker. The class keeps track of both the frequency of accesses and the order in which keys are accessed.

- `put(key, item)`: Adds an item to the cache. If the cache exceeds its size limit, it discards the least frequently used item. If there is a tie, it uses LRU as a tie-breaker.
- `get(key)`: Retrieves an item by key from the cache.

**Implementation:**
```python
#!/usr/bin/env python3
'''
This module contains the LFUCache class, a caching system
that inherits from the BaseCaching parent class. It uses the
LFU (Least Frequently Used) caching algorithm with LRU as a
tie-breaker.
'''
BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    ''' LFUCache defines a caching system with an LFU eviction policy.
    '''

    def __init__(self):
        '''
        Calls the parent class' init method and initializes
        a dictionary to keep track of usage frequency and order.
        '''
        super().__init__()
        self.usage_frequency = {}
        self.usage_order = []

    def put(self, key, item):
        ''' Add an item to the cache.
        If key or item is None this method does nothing.
        If the number of items in the cache exceeds MAX_ITEMS
        the least frequently used item is discarded
        Uses LRU as a tie-breaker.
        '''
        if key is None or item is None:
            return

        # If the key already exists update the item and usage frequency
        if key in self.cache_data:
            self.cache_data[key] = item
            self.usage_frequency[key] += 1
            self.usage_order.remove(key)
            self.usage_order.append(key)
        else:
            # If the cache is full remove the LFU item
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Find the least frequently used items
                min_freq = min(self.usage_frequency.values())
                lfu_keys = [k for k in self.usage_order
                            if self.usage_frequency[k] == min_freq]

                # Discard least recently used among the least frequently used
                lfu_key = lfu_keys[0]
                del self.cache_data[lfu_key]
                del self.usage_frequency[lfu_key]
                self.usage_order.remove(lfu_key)
                print(f"DISCARD: {lfu_key}")

            # Add the new item to the cache
            self.cache_data[key] = item
            self.usage_frequency[key] = 1
            self.usage_order.append(key)

    def get(self, key):
        ''' Retrieve an item by key from the cache.
        If key is None or doesn't exist in the cache it returns None.
        '''
        if key is None or key not in self.cache_data:
            return None

        # Since this key was recently accessed, update the usage order
        # and frequency
        self.usage_frequency[key] += 1
        self.usage_order.remove(key)
        self.usage_order.append(key)
        return self.cache_data[key]
```

**Usage:**

1. **Initialization**:
   To use the `LFUCache` class, import it from the `100-lfu_cache.py` file and create an instance:

   ```python
   LFUCache = __import__('100-lfu_cache').LFUCache

   my_cache = LFUCache()
   ```

2. **Adding items to the cache**:
   Use the `put` method to add key-value pairs to the cache. If either the `key` or `item` is `None`, the method does nothing. If the cache exceeds its size limit, the least frequently used item will be removed, with LRU as a tie-breaker.

   ```python
   my_cache.put("A", "Hello")
   my_cache.put("B", "World")
   my_cache.put("C", "Holberton")
   my_cache.put("D", "School")
   my_cache.print_cache()
   ```

3. **Evicting items based on LFU with LRU tie-breaking**:
   When the cache exceeds `MAX_ITEMS`, the `put` method discards the least frequently used item in the cache and prints a message indicating which item was discarded.

4. **Retrieving items from the cache**:
   Use the `get` method to retrieve values from the cache using their keys. If the `key` is `None` or doesn't exist, the method returns `None`.

   ```python
   print(my_cache.get("B"))  # Output: World
   ```

5. **Running the script to test the class**:
   To test the functionality of the `LFUCache` class, use`100-main.py`:

   ```python
   #!/usr/bin/python3
   """ 100-main """
   LFUCache = __import__('100-lfu_cache').LFUCache

   my_cache = LFUCache()
   my_cache.put("A", "Hello")
   my_cache.put("B", "World")
   my_cache.put("C", "Holberton")
   my_cache.put("D", "School")
   my_cache.print_cache()
   print(my_cache.get("B"))
   my_cache.put("E", "Battery")
   my_cache.print_cache()
   my_cache.put("C", "Street")
   my_cache.print_cache()
   print(my_cache.get("A"))
   print(my_cache.get("B"))
   print(my_cache.get("C"))
   my_cache.put("F", "Mission")
   my_cache.print_cache()
   my_cache.put("G", "San Francisco")
   my_cache.print_cache()
   my_cache.put("H", "H")
   my_cache.print_cache()
   my_cache.put("I", "I")
   my_cache.print_cache()
   print(my_cache.get("I"))
   print(my_cache.get("H"))
   print(my_cache.get("I"))
   print(my_cache.get("H"))
   print(my_cache.get("I"))
   print(my_cache.get("H"))
   my_cache.put("J", "J")
   my_cache.print_cache()
   my_cache.put("K", "K")
   my_cache.print_cache()
   my_cache.put("L", "L")
   my_cache.print_cache()
   my_cache.put("M", "M")
   my_cache.print_cache()
   ```

   Make the script executable by running:

   ```sh
   chmod +x 100-main.py
   ```

   Then, run the script to test:

   ```sh
   ./100-main.py
   ```

   Verify the output matches the expected results.

**Expected Output:**
```bash
Current cache:
A: Hello
B: World
C: Holberton
D: School
World
DISCARD: A
Current cache:
B: World
C: Holberton
D: School
E: Battery
Current cache:
B: World
C: Street
D: School
E: Battery
None
World
Street
DISCARD: D
Current cache:
B: World
C: Street
E: Battery
F: Mission
DISCARD: E
Current cache:
B: World
C: Street
F: Mission
G: San Francisco
DISCARD: F
Current cache:
B: World
C: Street
G: San Francisco
H: H
DISCARD: G
Current cache:
B: World
C: Street
H: H
I: I
I
H
I
H
I
H
DISCARD: B
Current cache:
C: Street
H: H
I: I
J: J
DISCARD: J
Current cache:
C: Street
H: H
I: I
K: K
DISCARD: K
Current cache:
C: Street
H: H
I: I
L: L
DISCARD: L
Current cache:
C: Street
H: H
I: I
M: M
```

**Explanation**

- **`put` Method**: Adds an item to the cache if both `key` and `item` are not `None`. If the cache exceeds `MAX_ITEMS`, the least frequently used item is discarded, with LRU as a tie-breaker.
- **`get` Method**: Retrieves the value associated with the `key` from the cache. Updates the usage order and frequency to reflect recent access. Returns `None` if `key` is `None` or does not exist in the cache.
- **Cache Display**: The cache state is printed using the `print_cache` method, and items are evicted based on the LFU policy with LRU tie-breaking.

</details>

## Author

Vie Paula - [GitHub Profile](https://github.com/ThatsVie)
