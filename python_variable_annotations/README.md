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

## Project Overview

This project focuses on understanding and applying variable annotations in Python. Python is a dynamically-typed language, meaning variable types are set at runtime upon assignment. In Python 3, type annotations allow developers to specify expected types for variables, parameters, and return values, enhancing code readability and validation.


## Concepts

### Advanced Python

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

## Learning Objectives

By the end of this project, you should be able to:

- Explain type annotations in Python 3.
- Use type annotations to specify function signatures and variable types.
- Understand the concept of Duck typing.
- Validate code with `mypy`.

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
''' Defines a type-annotated function to return the string representation of a float.'''


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
