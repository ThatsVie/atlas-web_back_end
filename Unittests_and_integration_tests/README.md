# Unittests and Integration Tests

## Overview
This project focuses on creating unittests and integration tests to ensure that functions work as expected under different circumstances. You'll learn to use tools like `unittest` and `mock`, and follow best practices for testing, including mocking external dependencies and writing integration tests to validate code paths end-to-end.

## Tools and Resources
- [unittest — Unit testing framework](https://docs.python.org/3/library/unittest.html)
- [unittest.mock — Mock object library](https://docs.python.org/3/library/unittest.mock.html)
- [How to mock a readonly property with mock?](https://stackoverflow.com/questions/11836436/how-to-mock-a-readonly-property-with-mock)
- [parameterized — Parameterization for unittest](https://pypi.org/project/parameterized/)
- [Memoization](https://en.wikipedia.org/wiki/Memoization)

## Learning Objectives

The difference between unit and integration tests.
Common testing patterns such as mocking, parametrizations and fixtures

  

## Requirements
- Python 3.9 on Ubuntu 20.04 LTS
- Ensure all Python files end with a new line.
- All code should be **executable**.
- Use **type annotations** for all functions and coroutines.
- Follow **pycodestyle** guidelines (version 2.5).
- Each file should start with the line `#!/usr/bin/env python3`.


## Testing Strategies

### Unit Tests
Unit tests focus on testing a specific function in isolation, assuming all external components work as expected. Key points:
- Use **mocking** to avoid actual network or database calls.
- Test different inputs, including corner cases.

### Integration Tests
Integration tests validate that all components work together as expected. Key points:
- Mock only low-level functions, such as HTTP requests or database I/O.
- Test interactions between components end-to-end.


## Executing Tests
Run your tests with the following command:
```bash
python3 -m unittest path/to/test_file.py
```


## Project Structure
- **`utils.py`**: Contains utility functions, such as `access_nested_map`, `get_json`, and `memoize`, which will be tested.
- **`client.py`**: Implements the `GithubOrgClient` class, which includes logic for interacting with the GitHub API (e.g., retrieving organization information and public repositories).
- **`fixtures.py`**: Contains predefined test data (fixtures) that will be used for testing purposes, such as mock responses for GitHub API calls.


## Tasks and Usage

### Task 0: Parameterize a Unit Test

In this task, we write a unit test for the `utils.access_nested_map` function using `parameterized` testing to check multiple cases in one method.

<details>
  <summary><strong>Curriculum Instruction</strong></summary>

Familiarize yourself with the `utils.access_nested_map` function and understand its purpose. Play with it in the Python console to make sure you understand.

In this task you will write the first unit test for `utils.access_nested_map`.

- Create a `TestAccessNestedMap` class that inherits from `unittest.TestCase`.
- Implement the `TestAccessNestedMap.test_access_nested_map` method to test that the method returns what it is supposed to.
- Decorate the method with `@parameterized.expand` to test the function for the following inputs:
  - `nested_map={"a": 1}, path=("a",)`
  - `nested_map={"a": {"b": 2}}, path=("a",)`
  - `nested_map={"a": {"b": 2}}, path=("a", "b")`
- For each of these inputs, test with `assertEqual` that the function returns the expected result.
- The body of the test method should not be longer than 2 lines.

</details>

<details>
  <summary><strong>Steps and Code Implementation</strong></summary>

### Steps:

1. **Understand the Function**: `utils.access_nested_map` retrieves values from a nested dictionary using a sequence of keys (path).
   - Example: 
     ```python
     nested_map = {"a": {"b": 2}}
     path = ("a", "b")
     result = access_nested_map(nested_map, path)
     print(result)  # Output: 2
     ```

2. **Create the Test Class**: Define a `TestAccessNestedMap` class that inherits from `unittest.TestCase`.

3. **Use Parameterized Testing**: Apply the `@parameterized.expand` decorator to test multiple inputs.

4. **Test Cases**: 
   - **Case 1**: `nested_map={"a": 1}, path=("a",)` — Expected result: `1`
   - **Case 2**: `nested_map={"a": {"b": 2}}, path=("a",)` — Expected result: `{"b": 2}`
   - **Case 3**: `nested_map={"a": {"b": 2}}, path=("a", "b")` — Expected result: `2`

5. **Test Method**: Use `assertEqual` to verify the expected results.

#### Example Code:
```python
#!/usr/bin/env python3
import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """Test cases for access_nested_map"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        self.assertEqual(access_nested_map(nested_map, path), expected)


if __name__ == "__main__":
    unittest.main()
```

#### Issue Encountered:
When running the tests, the following error occurred:
```
ModuleNotFoundError: No module named 'parameterized'
```

#### Solution:
To resolve this issue, the `parameterized` module was installed using `pip3`:
```bash
pip3 install parameterized
```

Once installed, the test was rerun successfully using:
```bash
python3 -m unittest test_utils.py
```
</details>
