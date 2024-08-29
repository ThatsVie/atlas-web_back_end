# Python - Variable Annotations

## Table of Contents
- [Project Overview](#project-overview)
- [Concepts](#concepts)
  - [Advanced Python](#advanced-python)
- [Learning Objectives](#learning-objectives)
- [Resources](#resources)
- [Requirements](#requirements)
- [Tasks and Detailed Usage](#tasks-and-detailed-usage)
  - [Task 0: Basic Annotations - Add](#task-0-basic-annotations---add)
  - [Task 1: Basic Annotations - Concat](#task-1-basic-annotations---concat)
  - [Task 2: Basic Annotations - Floor](#task-2-basic-annotations---floor)
  - [Task 3: Basic Annotations - To String](#task-3-basic-annotations---to-string)
  - [Task 4: Define Variables](#task-4-define-variables)
  - [Task 5: Complex Types - List of Floats](#task-5-complex-types---list-of-floats)
  - [Task 6: Complex Types - Mixed List](#task-6-complex-types---mixed-list)
  - [Task 7: Complex Types - String and Int/Float to Tuple](#task-7-complex-types---string-and-intfloat-to-tuple)
  - [Task 8: Complex Types - Functions](#task-8-complex-types---functions)
  - [Task 9: Let's Duck Type an Iterable Object](#task-9-lets-duck-type-an-iterable-object)

## Project Overview

This project focuses on understanding and applying variable annotations in Python. Python is a dynamically-typed language, meaning variable types are set at runtime upon assignment. In Python 3, type annotations allow developers to specify expected types for variables, parameters, and return values, enhancing code readability and validation.


## Concepts

### Advanced Python
<details>
  <summary>Click to expand</summary>

  Python’s dynamic typing allows variables to take on any type at runtime, making it flexible but prone to type-related errors if misused. For example:

  ```python
  def fn(a, b):
      return a + b
  ```

  In this function, the types of `a` and `b` are not known until runtime. If called with incompatible types, such as `fn("a", 1)`, a `TypeError` occurs:

  ```python
  >>> fn("a", 1)
  Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
  TypeError: can only concatenate str (not "int") to str
  ```

  Type annotations help mitigate these issues by documenting the expected types, though they do not enforce type checking at runtime.

</details>

## Learning Objectives

<details>
  <summary>Click to expand</summary>

  ### 1. Type Annotations in Python 3

  Type annotations in Python 3 allow developers to explicitly specify the expected types of variables, function parameters, and return values. These annotations help improve code readability, provide better documentation, and aid in catching errors early through tools like linters and type checkers.

  **Example from Task 0**:
  In Task 0, the function `add` is annotated to take two float arguments and return their sum as a float:

  ```python
  def add(a: float, b: float) -> float:
      '''Return the sum of two float numbers.'''
      return a + b
  ```

  Here, `a` and `b` are both annotated as floats, and the function's return type is also specified as a float.

  ### 2. How You Can Use Type Annotations to Specify Function Signatures and Variable Types

  Type annotations are used to specify the types of function parameters and return values, providing a clear and unambiguous function signature. This helps other developers understand the expected input and output of functions without having to read the entire implementation.

  **Example from Task 4**:
  In Task 4, variables are defined and annotated with their respective types:

  ```python
  a: int = 1
  pi: float = 3.14
  i_understand_annotations: bool = True
  school: str = "Holberton"
  ```

  These annotations make it explicit that `a` is an integer, `pi` is a float, `i_understand_annotations` is a boolean, and `school` is a string.

  **Example from Task 6**:
  The function `sum_mixed_list` takes a list of integers and floats, and the annotations specify both the input list and the return type:

  ```python
  from typing import List, Union

  def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
      '''Return the sum of a list of integers and floats.'''
      return sum(mxd_lst)
  ```

  Here, `mxd_lst` is annotated as a list containing either integers or floats (`List[Union[int, float]]`), and the return type is annotated as a float.

  ### 3. Duck Typing

  Duck typing is a concept in Python where the type or class of an object is less important than the methods it defines. If an object implements the necessary methods or behaviors, it can be used regardless of its specific type.

  **Example from Task 9**:
  In Task 9, the function `element_length` uses duck typing by working with any iterable of sequences, without requiring the elements to be of a specific type:

  ```python
  from typing import Iterable, Sequence, List, Tuple

  def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
      '''Return a list of tuples with each sequence and its length.'''
      return [(i, len(i)) for i in lst]
  ```

  Here, `lst` can be any iterable of sequences, demonstrating duck typing. The function doesn’t care about the specific type of each sequence; it only requires that each element has a `len()` method.

  ### 4. How to Validate Your Code with `mypy`

  `mypy` is a static type checker for Python that helps validate your code against the specified type annotations. It checks whether the types used in the code match the annotations, catching potential type-related errors before runtime.

  **Example**:
  To validate the functions with `mypy`, you can run:

  ```bash
  mypy 0-add.py 1-concat.py 2-floor.py 3-to_str.py 4-define_variables.py 5-sum_list.py 6-sum_mixed_list.py 7-to_kv.py 8-make_multiplier.py 9-element_length.py
  ```

  This command checks all the files for type consistency as per the annotations. For example, if a function is expected to return a float but returns a string instead, `mypy` will flag this as an error.

</details>


## Resources

To aid your learning, refer to:

- [Python Typing Documentation](https://docs.python.org/3/library/typing.html)
- [Mypy Cheat Sheet](https://mypy.readthedocs.io/en/latest/cheat_sheet_py3.html)

## Requirements

- **Editors**: vi, vim, emacs
- **Environment**: Ubuntu 20.04 LTS, Python 3.9
- **Code Style**: Follow pycodestyle (version 2.5)
- **Execution**: All scripts must be executable and start with `#!/usr/bin/env python3`.
- **Documentation**: All modules, classes, and functions must have detailed docstrings explaining their purpose.

## Tasks and Detailed Usage

Below, each task will be explained in detail, including code snippets, expected input/output, and annotations used.


### Task 0: Basic Annotations - Add
<details>
  <summary>Click to expand</summary>

**Objective**: Write a type-annotated function `add` that takes two float arguments `a` and `b` and returns their sum as a float.

**Code**:

File: `0-add.py`

```python
#!/usr/bin/env python3
'''Defines a type-annotated function to add two float numbers.'''


def add(a: float, b: float) -> float:
    '''Return the sum of two float numbers.'''
    return a + b

```

**Explanation**:
- The function `add` is defined with parameters `a` and `b`, both annotated as floats.
- The function's return type is also annotated as a float, indicating that the result will be a float.

**Usage**:

To test the function, use the provided main script (`0-main.py`):

File: `0-main.py`

```python
#!/usr/bin/env python3
add = __import__('0-add').add

print(add(1.11, 2.22) == 1.11 + 2.22)
print(add.__annotations__)
```

Run the main script:

```bash
chmod +x 0-main.py
./0-main.py
```

Expected Output:

```
True
{'a': <class 'float'>, 'b': <class 'float'>, 'return': <class 'float'>}
```

This output confirms that the function correctly adds two floats and that the annotations are set as expected.
</details>

### Task 1: Basic Annotations - Concat

<details>
  <summary>Click to expand</summary>

**Objective**: Write a type-annotated function `concat` that takes two string arguments `str1` and `str2` and returns their concatenated result as a string.

**Code**:

File: `1-concat.py`

```python
#!/usr/bin/env python3
'''Defines a type-annotated function to concatenate two strings.'''


def concat(str1: str, str2: str) -> str:
    '''Return the concat string of str1 and str2.'''
    return str1 + str2

```

**Explanation**:
- The function `concat` takes two parameters, `str1` and `str2`, both annotated as strings.
- The function's return type is annotated as a string, indicating the result will be the concatenation of `str1` and `str2`.

**Usage**:

To test the function, use the provided main script (`1-main.py`):

File: `1-main.py`

```python
#!/usr/bin/env python3
concat = __import__('1-concat').concat

str1 = "egg"
str2 = "shell"

print(concat(str1, str2) == "{}{}".format(str1, str2))
print(concat.__annotations__)
```

Run the main script:

```bash
chmod +x 1-main.py
./1-main.py
```

Expected Output:

```
True
{'str1': <class 'str'>, 'str2': <class 'str'>, 'return': <class 'str'>}
```

This output confirms that the function correctly concatenates two strings and that the annotations are set as expected.
</details>

### Task 2: Basic Annotations - Floor
<details>
  <summary>Click to expand</summary>

**Objective**: Write a type-annotated function `floor` that takes a float `n` as an argument and returns the floor of the float as an integer.

**Code**:

File: `2-floor.py`

```python
#!/usr/bin/env python3
'''Defines a type-annotated function to return the floor of a float.'''
import math


def floor(n: float) -> int:
    '''Return the floor of float n.'''
    return math.floor(n)

```

**Explanation**:
- The function `floor` is defined with a parameter `n`, annotated as a float.
- The function returns the floor of the float, which is an integer. This is achieved using Python's `math.floor` function.

**Usage**:

To test the function, use the provided main script (`2-main.py`):

File: `2-main.py`

```python
#!/usr/bin/env python3

import math

floor = __import__('2-floor').floor

ans = floor(3.14)

print(ans == math.floor(3.14))
print(floor.__annotations__)
print("floor(3.14) returns {}, which is a {}".format(ans, type(ans)))
```

Run the main script:

```bash
chmod +x 2-main.py
./2-main.py
```

Expected Output:

```
True
{'n': <class 'float'>, 'return': <class 'int'>}
floor(3.14) returns 3, which is a <class 'int'>
```

This output confirms that the function correctly calculates the floor of a float and that the annotations are set as expected.
</details>

### Task 3: Basic Annotations - To String
<details>
  <summary>Click to expand</summary>

**Objective**: Write a type-annotated function `to_str` that takes a float `n` as an argument and returns its string representation.

**Code**:

File: `3-to_str.py`

```python
#!/usr/bin/env python3
''' Defines a type-annotated function to return the
string representation of a float.'''


def to_str(n: float) -> str:
    '''Return the string representation of the float n.'''
    return str(n)

```

**Explanation**:
- The function `to_str` takes a parameter `n` annotated as a float.
- The function returns the string representation of the float using Python's built-in `str()` function.

**Usage**:

To test the function, use the provided main script (`3-main.py`):

File: `3-main.py`

```python
#!/usr/bin/env python3
to_str = __import__('3-to_str').to_str

pi_str = to_str(3.14)
print(pi_str == str(3.14))
print(to_str.__annotations__)
print("to_str(3.14) returns {} which is a {}".format(pi_str, type(pi_str)))
```

Run the main script:

```bash
chmod +x 3-main.py
./3-main.py
```

Expected Output:

```
True
{'n': <class 'float'>, 'return': <class 'str'>}
to_str(3.14) returns 3.14, which is a <class 'str'>
```

This output confirms that the function correctly converts a float to its string representation and that the annotations are set as expected.
</details>

### Task 4: Define Variables

<details>
  <summary>Click to expand</summary>

**Objective**: Define and annotate the following variables with the specified values:
- `a`: an integer with a value of 1
- `pi`: a float with a value of 3.14
- `i_understand_annotations`: a boolean with a value of True
- `school`: a string with a value of "Holberton"

**Code**:

File: `4-define_variables.py`

```python
#!/usr/bin/env python3
'''Defines and annotates variables with specified values.'''

a: int = 1
pi: float = 3.14
i_understand_annotations: bool = True
school: str = "Holberton"

```

**Explanation**:
- `a` is an integer set to `1`.
- `pi` is a float set to `3.14`.
- `i_understand_annotations` is a boolean set to `True`.
- `school` is a string set to `"Holberton"`.

**Usage**:

To test the variables, use the provided main script (`4-main.py`):

File: `4-main.py`

```python
#!/usr/bin/env python3

a = __import__('4-define_variables').a
pi = __import__('4-define_variables').pi
i_understand_annotations = __import__('4-define_variables').i_understand_annotations
school = __import__('4-define_variables').school

print("a is a {} with a value of {}".format(type(a), a))
print("pi is a {} with a value of {}".format(type(pi), pi))
print("i_understand_annotations is a {} with a value of {}".format(type(i_understand_annotations), i_understand_annotations))
print("school is a {} with a value of {}".format(type(school), school))
```

Run the main script:

```bash
chmod +x 4-main.py
./4-main.py
```

Expected Output:

```
a is a <class 'int'> with a value of 1
pi is a <class 'float'> with a value of 3.14
i_understand_annotations is a <class 'bool'> with a value of True
school is a <class 'str'> with a value of Holberton
```

This output confirms that the variables are defined and annotated correctly as per the task requirements.

</details>

### Task 5: Complex Types - List of Floats

<details>
  <summary>Click to expand</summary>

**Objective**: Write a type-annotated function `sum_list` that takes a list `input_list` of floats as an argument and returns their sum as a float.

**Code**:

File: `5-sum_list.py`

```python
#!/usr/bin/env python3
'''Defines a type-annotated function to sum a list of floats.'''
from typing import List


def sum_list(input_list: List[float]) -> float:
    '''Return the sum of a list of floats.'''
    return sum(input_list)
```

**Explanation**:
- The function `sum_list` takes a parameter `input_list`, which is annotated as a list of floats (`List[float]`).
- The function returns the sum of the floats in the list as a float using Python's built-in `sum()` function.

**Usage**:

To test the function, use the provided main script (`5-main.py`):

File: `5-main.py`

```python
#!/usr/bin/env python3

sum_list = __import__('5-sum_list').sum_list

floats = [3.14, 1.11, 2.22]
floats_sum = sum_list(floats)
print(floats_sum == sum(floats))
print(sum_list.__annotations__)
print("sum_list(floats) returns {} which is a {}".format(floats_sum, type(floats_sum)))
```

Run the main script:

```bash
chmod +x 5-main.py
./5-main.py
```

Expected Output:

```
True
{'input_list': typing.List[float], 'return': <class 'float'>}
sum_list(floats) returns 6.470000000000001 which is a <class 'float'>
```

This output confirms that the function correctly sums a list of floats and that the annotations are set as expected.

</details>

### Task 6: Complex Types - Mixed List

<details>
  <summary>Click to expand</summary>

**Objective**: Write a type-annotated function `sum_mixed_list` that takes a list `mxd_lst` of integers and floats and returns their sum as a float.

**Code**:

File: `6-sum_mixed_list.py`

```python
#!/usr/bin/env python3
'''Defines a type-annotated function to sum a mixed list of integers and floats.'''
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    '''Return the sum of a list of integers and floats.'''
    return sum(mxd_lst)
```

**Explanation**:
- The function `sum_mixed_list` takes a parameter `mxd_lst`, which is annotated as a list containing either integers or floats (`List[Union[int, float]]`).
- The function returns the sum of the elements in the list as a float using Python's built-in `sum()` function.

**Usage**:

To test the function, use the provided main script (`6-main.py`):

File: `6-main.py`

```python
#!/usr/bin/env python3

sum_mixed_list = __import__('6-sum_mixed_list').sum_mixed_list

print(sum_mixed_list.__annotations__)
mixed = [5, 4, 3.14, 666, 0.99]
ans = sum_mixed_list(mixed)
print(ans == sum(mixed))
print("sum_mixed_list(mixed) returns {} which is a {}".format(ans, type(ans)))
```

Run the main script:

```bash
chmod +x 6-main.py
./6-main.py
```

Expected Output:

```
{'mxd_lst': typing.List[typing.Union[int, float]], 'return': <class 'float'>}
True
sum_mixed_list(mixed) returns 679.13 which is a <class 'float'>
```

This output confirms that the function correctly sums a mixed list of integers and floats, and that the annotations are set as expected.

</details>

### Task 7: Complex Types - String and Int/Float to Tuple

<details>
  <summary>Click to expand</summary>

**Objective**: Write a type-annotated function `to_kv` that takes a string `k` and an int or float `v` as arguments and returns a tuple. The first element of the tuple is the string `k`, and the second element is the square of the int/float `v`, annotated as a float.

**Code**:

File: `7-to_kv.py`

```python
#!/usr/bin/env python3
'''
Defines a type-annotated function to return a tuple from a string
and an int/float.
'''
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''Return a tuple with a string and the square of an int/float.'''
    return (k, float(v ** 2))

```

**Explanation**:
- The function `to_kv` takes two parameters: `k`, which is a string, and `v`, which is an integer or float (`Union[int, float]`).
- The function returns a tuple where the first element is the string `k`, and the second element is the square of `v`, converted to a float.

**Usage**:

To test the function, use the provided main script (`7-main.py`):

File: `7-main.py`

```python
#!/usr/bin/env python3

to_kv = __import__('7-to_kv').to_kv

print(to_kv.__annotations__)
print(to_kv("eggs", 3))
print(to_kv("school", 0.02))
```

Run the main script:

```bash
chmod +x 7-main.py
./7-main.py
```

Expected Output:

```
{'k': <class 'str'>, 'v': typing.Union[int, float], 'return': typing.Tuple[str, float]}
('eggs', 9.0)
('school', 0.0004)
```

This output confirms that the function correctly returns a tuple with a string and the square of an int/float as a float, and that the annotations are set as expected.

</details>

### Task 8: Complex Types - Functions

<details>
  <summary>Click to expand</summary>

**Objective**: Write a type-annotated function `make_multiplier` that takes a float `multiplier` as an argument and returns a function that multiplies a float by the given multiplier.

**Code**:

File: `8-make_multiplier.py`

```python
#!/usr/bin/env python3
'''Defines a type-annotated function that returns a multiplier function.'''
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''Return a function that multiplies a float by the given multiplier.'''
    def multiplier_function(value: float) -> float:
        return value * multiplier
    return multiplier_function
```

**Explanation**:
- The function `make_multiplier` takes a parameter `multiplier`, annotated as a float.
- It returns another function `multiplier_function` that takes a float and returns the product of the float and the multiplier, both annotated as floats.

**Usage**:

To test the function, use the provided main script (`8-main.py`):

File: `8-main.py`

```python
#!/usr/bin/env python3

make_multiplier = __import__('8-make_multiplier').make_multiplier
print(make_multiplier.__annotations__)
fun = make_multiplier(2.22)
print("{}".format(fun(2.22)))
```

Run the main script:

```bash
chmod +x 8-main.py
./8-main.py
```

Expected Output:

```
{'multiplier': <class 'float'>, 'return': typing.Callable[[float], float]}
4.928400000000001
```

This output confirms that the function correctly returns a function that multiplies a float by the specified multiplier, and that the annotations are set as expected.

</details>

### Task 9: Let's Duck Type an Iterable Object

<details>
  <summary>Click to expand</summary>

**Objective**: Annotate the function `element_length` to take an iterable of sequences and return a list of tuples containing each sequence and its length.

**Code**:

File: `9-element_length.py`

```python
#!/usr/bin/env python3
'''
Defines a type-annotated function to return lengths of iterable sequences.
'''
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''Return a list of tuples with each sequence and its length.'''
    return [(i, len(i)) for i in lst]
```

**Explanation**:
- The function `element_length` takes a parameter `lst`, which is annotated as an iterable containing sequences (`Iterable[Sequence]`).
- The function returns a list of tuples, where each tuple contains a sequence and its length.

**Usage**:

To test the function, use the provided main script (`9-main.py`):

File: `9-main.py`

```python
#!/usr/bin/env python3

element_length =  __import__('9-element_length').element_length

print(element_length.__annotations__)
```

Run the main script:

```bash
chmod +x 9-main.py
./9-main.py
```

Expected Output:

```
{'lst': typing.Iterable[typing.Sequence], 'return': typing.List[typing.Tuple[typing.Sequence, int]]}
```

This output confirms that the function correctly annotates the parameters and return type as specified, handling any iterable of sequences and returning the appropriate types.

</details>
