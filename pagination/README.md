# Pagination
This project focuses on implementing efficient pagination techniques for managing large datasets in Python. It includes simple pagination using page and page_size parameters, hypermedia pagination with metadata for enhanced API navigation, and deletion-resilient pagination to maintain dataset integrity even when items are removed. The project demonstrates best practices for building scalable and user-friendly data management features in web applications

### Resources

- [REST API Design: Pagination](https://www.moesif.com/blog/technical/api-design/REST-API-Design-Filtering-Sorting-and-Pagination/#pagination)  
  This article explains different pagination strategies in REST APIs, including offset-based, cursor-based, and keyset pagination, and their impact on API performance and user experience.

- [HATEOAS](https://en.wikipedia.org/wiki/HATEOAS)  
  The Wikipedia entry on HATEOAS describes Hypermedia as the Engine of Application State, a constraint of REST application architecture that allows clients to interact dynamically with the server through hypermedia links.

- [How to Do Pagination in Python](https://www.geeksforgeeks.org/how-to-do-pagination-in-python/?ref=header_outind)  
  This guide demonstrates implementing pagination in Python using various techniques and libraries, focusing on efficient data management in web applications.

- [Pagination Design Pattern](https://www.geeksforgeeks.org/pagination-design-pattern/?ref=header_outind)  
  This article covers the pagination design pattern, including its purpose, benefits, and different approaches like numbered pages, "Load More" buttons, and infinite scrolling.

- [HATEOAS and Why It’s Needed in RESTful API](https://www.geeksforgeeks.org/hateoas-and-why-its-needed-in-restful-api/?ref=header_outind)  
  An explanation of HATEOAS, its importance in RESTful APIs, and how it enhances the flexibility and usability of API-driven applications.

- [Pagination on an API](https://www.geeksforgeeks.org/pagination-on-an-api/?ref=header_outind)  
  This resource discusses implementing pagination on an API, covering different techniques and best practices for managing large datasets efficiently.


## Learning Objectives

<details> 
<summary> Explain how to paginate a dataset with simple `page` and `page_size` parameters. </summary>
<br>

**Pagination with Simple `page` and `page_size` Parameters:**

Pagination with simple `page` and `page_size` parameters involves dividing a dataset into discrete pages based on the number of items (`page_size`) that should be included on each page. The parameters are:

- `page`: The current page number (1-indexed).
- `page_size`: The number of items to be displayed on each page.


  In **Task 1**, we implemented a `get_page` method in the `Server` class that takes `page` and `page_size` parameters and returns the appropriate subset of the dataset corresponding to the specified page. The method calculates the start and end indices for the page using these parameters and retrieves the correct data slice from the dataset.
</details>

<details> 
<summary> Explain how to paginate a dataset with hypermedia metadata. </summary>
<br>

**Pagination with Hypermedia Metadata:**

Hypermedia pagination extends the basic pagination by including additional metadata that provides navigation details about the dataset. This metadata often includes:

- `page_size`: The size of the current page.
- `page`: The current page number.
- `data`: The dataset page being returned.
- `next_page`: The number of the next page, if it exists.
- `prev_page`: The number of the previous page, if it exists.
- `total_pages`: The total number of pages available in the dataset.

  In **Task 2**, we implemented the `get_hyper` method in the `Server` class, which returns a dictionary containing these metadata fields. This allows the client to understand not only the current state of the pagination but also navigate to other pages effectively using the provided metadata.
</details>

<details> 
<summary> Explain how to paginate in a deletion-resilient manner. </summary>
<br>

**Deletion-Resilient Pagination:**

Deletion-resilient pagination ensures that if rows are removed from the dataset between queries, the user does not miss any items when navigating through pages. This type of pagination maintains the integrity of the sequence by using an index that dynamically adjusts to changes in the dataset.

Key elements include:

- `index`: The current start index of the returned page.
- `next_index`: The next index to query from.
- `page_size`: The current page size.
- `data`: The actual page of the dataset being returned.

 In **Task 3**, we implemented the `get_hyper_index` method, which maintains the pagination state even when items are deleted from the dataset. The method ensures that users do not miss any items by calculating the `next_index` based on the current data and any deletions that may have occurred.
</details>


## Requirements

- All files will be interpreted/compiled on Ubuntu 20.04 LTS using Python 3.9.
- All files should end with a new line.
- The first line of all files should be exactly `#!/usr/bin/env python3`.
- A `README.md` file, at the root of the folder of the project, is mandatory.
- Code should follow the `pycodestyle` style guide (version 2.5.*).
- The length of files will be tested using `wc`.
- All modules should have documentation (`python3 -c 'print(__import__("my_module").__doc__)'`).
- All functions should have documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'`).
- Documentation should be a real sentence explaining the purpose of the module, class, or method.
- All functions and coroutines must be type-annotated.

## Setup

Download the dataset used for this project: [Popular_Baby_Names.csv](https://s3.eu-west-3.amazonaws.com/hbtn.intranet/uploads/misc/2020/5/7d3576d97e7560ae85135cc214ffe2b3412c51d7.csv?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA4MYA5JM5DUTZGMZG%2F20240904%2Feu-west-3%2Fs3%2Faws4_request&X-Amz-Date=20240904T182249Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=55d6e800a8b7446f209afaf46a7a8c2401f66806f54b5197bfd944ad2c6ffa2a)

## Tasks and Detailed Usage

### Task 0: Simple Helper Function

<details> 
<summary> Write a function named `index_range` that takes two integer arguments, `page` and `page_size`.
The function should return a tuple of size two containing a start index and an end index corresponding to the range of indexes to return in a list for those particular pagination parameters.
Page numbers are 1-indexed, i.e., the first page is page 1.
</summary>
<br>

**Description:**

The `index_range` function is a helper function that takes two parameters: `page` and `page_size`. It calculates the start and end indexes for pagination based on these parameters. The function ensures that data retrieval is efficient by computing the range of data items that should appear on a given page.

**Implementation:**

```python
#!/usr/bin/env python3
'''
This module contains a helper function to calculate the start and end index
for pagination given the page number and page size.
'''

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    '''
    Calculate the start and end index for pagination.
    '''
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return start_index, end_index
```

**Usage:**

1. **Function Purpose:**
   The `index_range` function computes the range of indices for a given page and page size. This is useful for displaying a subset of data in a paginated format.

2. **Examples of Using the `index_range` Function:**

   You can use the `index_range` function to determine which items should be displayed on a particular page:

   ```python
   # Example 1
   res = index_range(1, 7)  
   print(type(res))  # Expected output: <class 'tuple'>
   print(res)        # Expected output: (0, 7)

   # Example 2
   res = index_range(page=3, page_size=15)  
   print(type(res))  # Expected output: <class 'tuple'>
   print(res)        # Expected output: (30, 45)
   ```

3. **Running the script to test the function:**

   To test the functionality of the `index_range` function, use `0-main.py`:

   ```python
   #!/usr/bin/env python3
   """
   Main file
   """

   index_range = __import__('0-simple_helper_function').index_range

   res = index_range(1, 7)
   print(type(res))  # Expected output: <class 'tuple'>
   print(res)        # Expected output: (0, 7)

   res = index_range(page=3, page_size=15)
   print(type(res))  # Expected output: <class 'tuple'>
   print(res)        # Expected output: (30, 45)
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
<class 'tuple'>
(0, 7)
<class 'tuple'>
(30, 45)
```

**Explanation:**

- **`index_range` Function:** Computes the range of indices for pagination based on the `page` and `page_size` parameters.
- **Usage Example:** The example shows how to determine the start and end indices for various pages and page sizes.
  
</details>

### Task 1: Simple Pagination

<details> 
<summary> Implement a `Server` class to paginate a database of popular baby names.
Add a method named `get_page` that takes two integer arguments, `page` and `page_size`, with default values 1 and 10. The method should return a page of the dataset based on the provided pagination parameters.
</summary>
<br>

**Description:**

The `Server` class is responsible for paginating a dataset of popular baby names from a CSV file. It includes a `get_page` method that returns a specific page of data according to the given `page` and `page_size` parameters.

**Implementation:**

```python
#!/usr/bin/env python3
'''
This module contains a Server class to paginate a database of popular baby names.
'''

import csv
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    '''
    Calculate the start and end index for pagination.
    '''
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return start_index, end_index


class Server:
    '''
    Server class to paginate a database of popular baby names.
    '''
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        '''
        Cached data set
        '''
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        '''
        Returns a page of data from the data set.
        '''
        # Ensure that page and page_size are integers greater than 0
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        start_index, end_index = index_range(page, page_size)
        
        dataset = self.dataset()

        return dataset[start_index:end_index] if start_index < len(dataset) else []
```

**Usage:**

1. **Function Purpose:**
   The `Server` class and its `get_page` method are used to paginate the dataset of popular baby names, allowing efficient retrieval of data based on page numbers.

2. **Examples of Using the `Server` Class and `get_page` Method:**

   Instantiate the `Server` class and call the `get_page` method:

   ```python
   Server = __import__('1-simple_pagination').Server

   server = Server()

   try:
       should_err = server.get_page(-10, 2)
   except AssertionError:
       print("AssertionError raised with negative values")

   try:
       should_err = server.get_page(0, 0)
   except AssertionError:
       print("AssertionError raised with 0")

   try:
       should_err = server.get_page(2, 'Bob')
   except AssertionError:
       print("AssertionError raised when page and/or page_size are not ints")

   print(server.get_page(1, 3))
   print(server.get_page(3, 2))
   print(server.get_page(3000, 100))
   ```

3. **Running the script to test the class:**

   To test the functionality of the `Server` class, use `1-main.py`:

   ```python
   #!/usr/bin/env python3
   """
   Main file
   """

   Server = __import__('1-simple_pagination').Server

   server = Server()

   try:
       should_err = server.get_page(-10, 2)
   except AssertionError:
       print("AssertionError raised with negative values")

   try:
       should_err = server.get_page(0, 0)
   except AssertionError:
       print("AssertionError raised with 0")

   try:
       should_err = server.get_page(2, 'Bob')
   except AssertionError:
       print("AssertionError raised when page and/or page_size are not ints")

   print(server.get_page(1, 3))
   print(server.get_page(3, 2))
   print(server.get_page(3000, 100))
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
AssertionError raised with negative values
AssertionError raised with 0
AssertionError raised when page and/or page_size are not ints
[['2016', 'FEMALE', 'ASIAN AND PACIFIC ISLANDER', 'Olivia', '172', '1'], ['2016', 'FEMALE', 'ASIAN AND PACIFIC ISLANDER', 'Chloe', '112', '2'], ['2016', 'FEMALE', 'ASIAN AND PACIFIC ISLANDER', 'Sophia', '104', '3']]
[['2016', 'FEMALE', 'ASIAN AND PACIFIC ISLANDER', 'Emily', '99', '4'], ['2016', 'FEMALE', 'ASIAN AND PACIFIC ISLANDER', 'Mia', '79', '5']]
[]
```

**Explanation:**

- **`get_page` Method:** Takes `page` and `page_size` as arguments and uses assertions to ensure they are valid integers greater than 0.
- **Data Retrieval:** Utilizes the `index_range` function to determine the start and end indices for the desired page and returns the corresponding data slice from the dataset.
- **Error Handling:** Raises `AssertionError` for invalid input and returns an empty list if the requested page is out of range.

</details>

### Task 2: Hypermedia Pagination

<details> 
<summary> Implement a `get_hyper` method for the `Server` class to provide hypermedia pagination.
The method should take the same arguments (and defaults) as `get_page` and return a dictionary with additional pagination details.
</summary>
<br>

**Description:**

The `get_hyper` method extends the `Server` class to provide hypermedia-style pagination. This method returns a dictionary that includes pagination details such as page size, current page number, dataset page, next page, previous page, and total number of pages.

**Implementation:**

```python
#!/usr/bin/env python3
'''
This module contains a Server class to paginate a database of popular baby names with hypermedia pagination.
'''

import csv
import math
from typing import List, Tuple, Dict


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    '''
    Calculate the start and end index for pagination.
    '''
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return start_index, end_index


class Server:
    '''
    Server class to paginate the database.
    '''
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        '''
        Cached data set
        '''
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        '''
        Returns a page of data from the data set.
        '''
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        start_index, end_index = index_range(page, page_size)
        
        dataset = self.dataset()

        if start_index >= len(dataset):
            return []

        return dataset[start_index:end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        '''
        Returns a dictionary containing hypermedia pagination data.
        '''
        data = self.get_page(page, page_size)
        total_pages = math.ceil(len(self.dataset()) / page_size)

        return {
            'page_size': len(data),
            'page': page,
            'data': data,
            'next_page': page + 1 if page < total_pages else None,
            'prev_page': page - 1 if page > 1 else None,
            'total_pages': total_pages
        }
```

**Usage:**

1. **Function Purpose:**
   The `get_hyper` method provides additional details for paginated data, enabling hypermedia-style pagination by returning metadata about the current state of the pagination.

2. **Examples of Using the `get_hyper` Method:**

   To test the `get_hyper` method, instantiate the `Server` class and call the method:

   ```python
   Server = __import__('2-hypermedia_pagination').Server

   server = Server()

   print(server.get_hyper(1, 2))
   print("---")
   print(server.get_hyper(2, 2))
   print("---")
   print(server.get_hyper(100, 3))
   print("---")
   print(server.get_hyper(3000, 100))
   ```

3. **Running the script to test the class:**

   To test the functionality of the `Server` class with hypermedia pagination, use `2-main.py`:

   ```python
   #!/usr/bin/env python3
   """
   Main file
   """

   Server = __import__('2-hypermedia_pagination').Server

   server = Server()

   print(server.get_hyper(1, 2))
   print("---")
   print(server.get_hyper(2, 2))
   print("---")
   print(server.get_hyper(100, 3))
   print("---")
   print(server.get_hyper(3000, 100))
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
{'page_size': 2, 'page': 1, 'data': [['2016', 'FEMALE', 'ASIAN AND PACIFIC ISLANDER', 'Olivia', '172', '1'], ['2016', 'FEMALE', 'ASIAN AND PACIFIC ISLANDER', 'Chloe', '112', '2']], 'next_page': 2, 'prev_page': None, 'total_pages': 9709}
---
{'page_size': 2, 'page': 2, 'data': [['2016', 'FEMALE', 'ASIAN AND PACIFIC ISLANDER', 'Sophia', '104', '3'], ['2016', 'FEMALE', 'ASIAN AND PACIFIC ISLANDER', 'Emma', '99', '4']], 'next_page': 3, 'prev_page': 1, 'total_pages': 9709}
---
{'page_size': 3, 'page': 100, 'data': [['2016', 'FEMALE', 'BLACK NON HISPANIC', 'Londyn', '14', '39'], ['2016', 'FEMALE', 'BLACK NON HISPANIC', 'Amirah', '14', '39'], ['2016', 'FEMALE', 'BLACK NON HISPANIC', 'McKenzie', '14', '39']], 'next_page': 101, 'prev_page': 99, 'total_pages': 6473}
---
{'page_size': 0, 'page': 3000, 'data': [], 'next_page': None, 'prev_page': 2999, 'total_pages': 195}
```

**Explanation:**

- **`get_hyper` Method:** Provides metadata for hypermedia pagination, including current page details, next and previous pages, and total pages.
- **Data Retrieval:** Reuses the `get_page` method to fetch the current page's data and calculate additional pagination details.
- **Hypermedia Pagination:** Enhances pagination by providing a complete overview of the current state and navigation options.

</details>

### Task 3: Deletion-Resilient Hypermedia Pagination

<details> 
<summary> Implement a `get_hyper_index` method for the `Server` class to provide deletion-resilient hypermedia pagination.
The method should take two integer arguments: `index` (default `None`) and `page_size` (default `10`). It should return a dictionary that ensures items are not missed even if rows are removed between queries.
</summary>
<br>

**Description:**

The `get_hyper_index` method extends the `Server` class to provide deletion-resilient pagination. This method ensures that if rows are deleted from the dataset between queries, the user does not miss any items when paginating through the data.

**Implementation:**

```python
#!/usr/bin/env python3
'''
Deletion-resilient hypermedia pagination
'''

import csv
import math
from typing import List, Dict


class Server:
    '''
    Server class to paginate a database of popular baby names.
    '''
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        '''
        Cached data set
        '''
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        '''
        Data set indexed by sorting position, starting at 0
        '''
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        '''
        Provides deletion-resilient hypermedia pagination
        '''
        assert index is None or (
            isinstance(index, int) and 0 <= index < len(self.indexed_dataset())
        )
        indexed_data = self.indexed_dataset()
        data = []
        current_index = index
        next_index = index

        while len(data) < page_size and next_index < len(indexed_data):
            if next_index in indexed_data:
                data.append(indexed_data[next_index])
            next_index += 1

        return {
            'index': index,
            'data': data,
            'page_size': len(data),
            'next_index': next_index
        }
```

**Usage:**

1. **Function Purpose:**
   The `get_hyper_index` method provides deletion-resilient pagination, ensuring users do not miss any items from the dataset even if rows are removed between queries.

2. **Examples of Using the `get_hyper_index` Method:**

   To test the `get_hyper_index` method, instantiate the `Server` class and call the method:

   ```python
   Server = __import__('3-hypermedia_del_pagination').Server

   server = Server()

   server.indexed_dataset()

   try:
       server.get_hyper_index(300000, 100)
   except AssertionError:
       print("AssertionError raised when out of range")        

   index = 3
   page_size = 2

   print("Nb items: {}".format(len(server._Server__indexed_dataset)))

   # 1- request first index
   res = server.get_hyper_index(index, page_size)
   print(res)

   # 2- request next index
   print(server.get_hyper_index(res.get('next_index'), page_size))

   # 3- remove the first index
   del server._Server__indexed_dataset[res.get('index')]
   print("Nb items: {}".format(len(server._Server__indexed_dataset)))

   # 4- request again the initial index -> the first data retrieved is not the same as the first request
   print(server.get_hyper_index(index, page_size))

   # 5- request again initial next index -> same data page as the request 2-
   print(server.get_hyper_index(res.get('next_index'), page_size))
   ```

3. **Running the script to test the class:**

   To test the functionality of the `Server` class with deletion-resilient hypermedia pagination, use `3-main.py`:

   ```python
   #!/usr/bin/env python3
   """
   Main file
   """

   Server = __import__('3-hypermedia_del_pagination').Server

   server = Server()

   server.indexed_dataset()

   try:
       server.get_hyper_index(300000, 100)
   except AssertionError:
       print("AssertionError raised when out of range")        

   index = 3
   page_size = 2

   print("Nb items: {}".format(len(server._Server__indexed_dataset)))

   # 1- request first index
   res = server.get_hyper_index(index, page_size)
   print(res)

   # 2- request next index
   print(server.get_hyper_index(res.get('next_index'), page_size))

   # 3- remove the first index
   del server._Server__indexed_dataset[res.get('index')]
   print("Nb items: {}".format(len(server._Server__indexed_dataset)))

   # 4- request again the initial index -> the first data retrieved is not the same as the first request
   print(server.get_hyper_index(index, page_size))

   # 5- request again initial next index -> same data page as the request 2-
   print(server.get_hyper_index(res.get('next_index'), page_size))
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
AssertionError raised when out of range
Nb items: 19418
{'index': 3, 'data': [['2016', 'FEMALE', 'ASIAN AND PACIFIC ISLANDER', 'Emma', '99', '4'], ['2016', 'FEMALE', 'ASIAN AND PACIFIC ISLANDER', 'Emily', '99', '4']], 'page_size': 2, 'next_index': 5}
{'index': 5, 'data': [['2016', 'FEMALE', 'ASIAN AND PACIFIC ISLANDER', 'Mia', '79', '5'], ['2016', 'FEMALE', 'ASIAN AND PACIFIC ISLANDER', 'Charlotte', '59', '6']], 'page_size': 2, 'next_index': 7}
Nb items: 19417
{'index': 3, 'data': [['2016', 'FEMALE', 'ASIAN AND PACIFIC ISLANDER', 'Emily', '99', '4'], ['2016', 'FEMALE', 'ASIAN AND PACIFIC ISLANDER', 'Mia', '79', '5']], 'page_size': 2, 'next_index': 6}
{'index': 5, 'data': [['2016', 'FEMALE', 'ASIAN AND PACIFIC ISLANDER', 'Mia', '79', '5'], ['2016', 'FEMALE', 'ASIAN AND PACIFIC ISLANDER', 'Charlotte', '59', '6']], 'page_size': 2, 'next_index': 7}
```

**Explanation:**

- **`get_hyper_index` Method:** Provides a deletion-resilient way to paginate through the dataset, maintaining the correct sequence even if rows are removed.
- **Data Retrieval:** Uses a dictionary indexed by the original position to manage data retrieval efficiently.
- **Resilient Pagination:** Ensures the user continues to see the correct number of rows regardless of deletions, using the correct start and next indices.

</details>


## Author

Vie Paula - [GitHub Profile](https://github.com/ThatsVie)
