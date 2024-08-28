# Python - Variable Annotations

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


