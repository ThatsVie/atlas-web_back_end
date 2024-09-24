<p align="center">
  <img src="https://github.com/user-attachments/assets/e42b6a69-0c9d-45c8-85f1-64f399f1d0b1" alt="smartpuggywuggy" />
</p>

<h1 align="center">Unittests and Integration Tests</h1>


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

### Setup

To run the tests, make sure the following dependencies are installed:

1. **unittest**: Python’s built-in testing library.
   - `unittest` comes pre-installed with Python, so no additional installation is necessary. You can check it by running:
   ```bash
   python3 -m unittest --help
   ```

2. **parameterized**: If not installed, run:
   ```bash
   pip3 install parameterized
   ```

## Executing Tests
Run your tests with the following command:
```bash
python3 -m unittest path/to/test_file.py
```
#### Example Output:
```bash
vie@ThatsVie:~/pug/atlas-web_back_end/Unittests_and_integration_tests$ python3 -m unittest test_utils.py
.....
----------------------------------------------------------------------
Ran 3 tests in 0.000s

OK
vie@ThatsVie:~/pug/atlas-web_back_end/Unittests_and_integration_tests$
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

#### Code:
```python
#!/usr/bin/env python3
'''
Unit tests for the access_nested_map function from the utils module.
'''

import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    '''Test cases for access_nested_map'''

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        '''
        Test access_nested_map with various nested dictionaries and paths.
        '''
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

####  Output:
```bash
vie@ThatsVie:~/pug/atlas-web_back_end/Unittests_and_integration_tests$ python3 -m unittest test_utils.py
.....
----------------------------------------------------------------------
Ran 3 tests in 0.000s

OK
```
</details>

### Task 1: Parameterize a Unit Test for Handling Exceptions

In this task, we extend our unit test for the `utils.access_nested_map` function to check for exceptions, specifically ensuring that a `KeyError` is raised for invalid inputs.

<details>
  <summary><strong>Curriculum Instruction</strong></summary>

Implement `TestAccessNestedMap.test_access_nested_map_exception`. Use the `assertRaises` context manager to test that a `KeyError` is raised for the following inputs (use `@parameterized.expand`):

- `nested_map={}, path=("a",)`
- `nested_map={"a": 1}, path=("a", "b")`

Also, make sure that the exception message is as expected.

</details>

<details>
  <summary><strong>Steps and Code Implementation</strong></summary>

### Steps:

1. **Extend the Test Class**: Add a new method `test_access_nested_map_exception` in the `TestAccessNestedMap` class to handle cases where an exception is expected.
  
2. **Use the assertRaises Context Manager**: This will check if the correct exception (`KeyError`) is raised for invalid inputs.

3. **Use Parameterized Testing**: Apply the `@parameterized.expand` decorator to test multiple cases where a `KeyError` should be raised.

4. **Test Cases**:
   - **Case 1**: `nested_map={}, path=("a",)` — Expected to raise `KeyError("a")`.
   - **Case 2**: `nested_map={"a": 1}, path=("a", "b")` — Expected to raise `KeyError("b")`.

#### Code:
```python
#!/usr/bin/env python3
'''
Unit tests for the access_nested_map function from the utils module.
'''

import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    '''Test cases for access_nested_map'''

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        '''
        Test access_nested_map with various nested dictionaries and paths.
        '''
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), 'a'),
        ({"a": 1}, ("a", "b"), 'b'),
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected_error):
        '''
        Test that KeyError is raised for invalid paths in access_nested_map.
        '''
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)
        self.assertEqual(str(context.exception), f"'{expected_error}'")


if __name__ == "__main__":
    unittest.main()
```

#### How to Run the Test:
```bash
python3 -m unittest test_utils.py
```

####  Output:
```bash
vie@ThatsVie:~/pug/atlas-web_back_end/Unittests_and_integration_tests$ python3 -m unittest test_utils.py
.....
----------------------------------------------------------------------
Ran 5 tests in 0.000s

OK
```

</details>

### Task 2: Mock HTTP Calls

In this task, we test the `utils.get_json` function while avoiding actual HTTP requests by using `unittest.mock.patch`.

<details>
  <summary><strong>Curriculum Instruction</strong></summary>

Familiarize yourself with the `utils.get_json` function.

Define the `TestGetJson(unittest.TestCase)` class and implement the `TestGetJson.test_get_json` method to test that `utils.get_json` returns the expected result.

We don’t want to make any actual external HTTP calls. Use `unittest.mock.patch` to patch `requests.get`. Make sure it returns a `Mock` object with a `json` method that returns `test_payload` which you parametrize alongside the `test_url` that you will pass to `get_json` with the following inputs:

- `test_url="http://example.com"`, `test_payload={"payload": True}`
- `test_url="http://holberton.io"`, `test_payload={"payload": False}`

Test that the mocked `get` method was called exactly once (per input) with `test_url` as an argument.

Test that the output of `get_json` is equal to `test_payload`.

</details>

<details>
  <summary><strong>Steps and Code Implementation</strong></summary>

### Steps:

1. **Patch the `requests.get` Method**: Instead of making an actual HTTP call, patch `requests.get` to return a mock response object.

2. **Mock the Response**: Create a mock response object with a `json` method that returns the test payload.

3. **Use Parameterized Inputs**: Test different URLs and payloads by using `@parameterized.expand`.

4. **Test Case Assertions**:
   - Check that `requests.get` was called exactly once with the correct `test_url`.
   - Ensure that the return value of `get_json` matches the expected `test_payload`.

#### Code:
```python
#!/usr/bin/env python3
'''
Unit tests for the utils module.
'''

import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from utils import get_json


class TestGetJson(unittest.TestCase):
    '''Test cases for get_json'''

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch('utils.requests.get')
    def test_get_json(self, test_url, test_payload, mock_get):
        '''
        Test that get_json returns the expected result
        and makes a single HTTP call.
        '''
        # Mock response object with a json method
        mock_response = Mock()
        mock_response.json.return_value = test_payload

        # Set mock to return mock response
        mock_get.return_value = mock_response

        result = get_json(test_url)
        self.assertEqual(result, test_payload)

        # Check that requests.get was called once with the correct URL
        mock_get.assert_called_once_with(test_url)


if __name__ == "__main__":
    unittest.main()
```

### How to Run the Test:
```bash
python3 -m unittest test_utils.py
```

#### Output:
```bash
vie@ThatsVie:~/pug/atlas-web_back_end/Unittests_and_integration_tests$ python3 -m unittest test_utils.py
.......
----------------------------------------------------------------------
Ran 7 tests in 0.001s

OK
```

</details>

### Task 3: Parameterize and Patch

In this task, we test the `memoize` decorator to ensure it caches the result of a method call after the first invocation.

<details>
  <summary><strong>Curriculum Instruction</strong></summary>

Read about memoization and familiarize yourself with the `utils.memoize` decorator.

Implement the `TestMemoize(unittest.TestCase)` class with a `test_memoize` method.

Inside `test_memoize`, define the following class:

```python
class TestClass:

    def a_method(self):
        return 42

    @memoize
    def a_property(self):
        return self.a_method()
```

Use `unittest.mock.patch` to mock `a_method`. Test that when calling `a_property` twice, the correct result is returned, but `a_method` is only called once using `assert_called_once`.

</details>

<details>
  <summary><strong>Steps and Code Implementation</strong></summary>

### Steps:

1. **Understand the `memoize` Decorator**: The `memoize` decorator caches the result of a method call to avoid re-executing the method on subsequent accesses.
  
2. **Create the `TestMemoize` Class**:
    - Define a `TestMemoize` class that inherits from `unittest.TestCase`.
    - Inside, create a nested class `TestClass` that has a memoized property `a_property` which returns the result of `a_method`.

3. **Mock `a_method`**: Use `patch.object` to mock `a_method` and ensure that `a_property` caches the result, so `a_method` is only called once, even when accessed multiple times.

4. **Assertions**:
    - Ensure the result of calling `a_property` is correct.
    - Ensure that `a_method` is only called once using `assert_called_once`.

### Code:

```python
#!/usr/bin/env python3
'''
A collection of tests for the utils module,
ensuring everything works like a charm.
'''

import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    '''
    Ensuring access_nested_map fetches the right value,
    like a pug fetching a treat!
    '''

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        '''
        Test access_nested_map with various paths through nested dictionaries.
        Think of it like a pug navigating through a maze of treats.
        '''
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), 'a'),
        ({"a": 1}, ("a", "b"), 'b'),
    ])
    def test_access_nested_map_exception(self, nested_map, path,
                                         expected_error):
        '''
        Test that KeyError is raised for invalid paths in access_nested_map.
        Like a pug looking for a treat that’s not there.
        '''
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)
        self.assertEqual(str(context.exception), f"'{expected_error}'")


class TestGetJson(unittest.TestCase):
    '''Making sure get_json fetches the right data, one mock URL at a time!'''

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch('utils.requests.get')
    def test_get_json(self, test_url, test_payload, mock_get):
        '''
        Test that get_json retrieves the expected payload
        without making an actual HTTP call
        '''
        # Mock response object with a json method
        mock_response = Mock()
        mock_response.json.return_value = test_payload

        # Set mock to return mock response
        mock_get.return_value = mock_response

        result = get_json(test_url)
        self.assertEqual(result, test_payload)

        # Ensure that requests.get was called once with the correct URL
        mock_get.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    '''Testing memoization, so we only call once but get the value every time.
    Like a pug who only needs one sniff to remember its home!'''

    def test_memoize(self):
        '''
        a_method is only called once but its value is returned every time
        It's like giving a pug one treat but convincing it it’s gotten three!
        '''

        class TestClass:
            '''Test class with a memoized property'''

            def a_method(self):
                '''Method to be memoized'''
                return 42

            @memoize
            def a_property(self):
                '''Memoized property'''
                return self.a_method()

        with patch.object(
            TestClass, 'a_method', return_value=42
        ) as mock_method:
            test_obj = TestClass()

            # Access a_property twice
            result_1 = test_obj.a_property
            result_2 = test_obj.a_property

            # Assert results are correct
            self.assertEqual(result_1, 42)
            self.assertEqual(result_2, 42)

            # a_method is called only once
            mock_method.assert_called_once()


if __name__ == "__main__":
    unittest.main()

```

### How to Run the Test:
```bash
python3 -m unittest test_utils.py
```

#### Output:
```bash
vie@ThatsVie:~/pug/atlas-web_back_end/Unittests_and_integration_tests$ python3 -m unittest test_utils.py
........
----------------------------------------------------------------------
Ran 8 tests in 0.003s

OK
```

</details>

### Task 4: Parameterize and Patch as Decorators

In this task, we write tests for the `GithubOrgClient.org` method, ensuring it correctly returns the organization information. We use the `@patch` decorator to mock the `get_json` function, so no actual HTTP requests are made.

<details>
  <summary><strong>Curriculum Instruction</strong></summary>

Familiarize yourself with the `client.GithubOrgClient` class.

In a new `test_client.py` file, declare the `TestGithubOrgClient(unittest.TestCase)` class and implement the `test_org` method.

This method should test that `GithubOrgClient.org` returns the correct value.

Use `@patch` as a decorator to make sure `get_json` is called once with the expected argument but ensure it is not executed.

Use `@parameterized.expand` as a decorator to parametrize the test with a couple of org examples to pass to `GithubOrgClient`, in this order:
- google
- abc

Of course, no external HTTP calls should be made.

</details>

<details>
  <summary><strong>Steps and Code Implementation</strong></summary>

### Steps:

1. **Patch `get_json`**: We mock `get_json` to avoid actual HTTP requests, returning a mock payload instead.
2. **Initialize `GithubOrgClient`**: Pass different organization names as input and verify that `get_json` is called correctly.
3. **Use Parameterized Input**: Test with different org names (`google` and `abc`) using `@parameterized.expand`.
4. **Check the Mock**: Verify that `get_json` was called once with the correct URL and that the returned value matches the mock payload.

#### Code:

```python
#!/usr/bin/env python3
'''
Unit tests for the client module.
Making sure everything runs as smooth as chocolate mousse!
'''

import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    '''
    Test cases for the GithubOrgClient class.
    Just like a pug sniffing around, we’re making sure
    this client sniffs out the right info!
    '''

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        '''
        Test that GithubOrgClient.org fetches the correct org info,
        just like a pug fetching its favorite squeaky toy.
        We’re making sure get_json is called once, no extra sniffs needed!
        '''
        # Mock response for get_json
        mock_get_json.return_value = {"payload": True}

        # Initialize the client
        client = GithubOrgClient(org_name)

        # Access the org attribute (not as a callable method)
        result = client.org

        # Ensure get_json was called with the correct URL
        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}"
        )

        # Assert the result is what we expect
        self.assertEqual(result, {"payload": True})


if __name__ == "__main__":
    unittest.main()
```

### How to Run the Test:

```bash
python3 -m unittest test_client.py
```

#### Issue Encountered:

Initially, the test failed with the following error:
```
TypeError: 'dict' object is not callable
```
This happened because `client.org()` was treated as a method call instead of a property.

#### Solution:
The error was fixed by removing the parentheses from `client.org`, treating it as a property rather than a callable method. We ensured that `client.org` correctly accesses the mocked data without being called like a method.

#### Output:

```bash
vie@ThatsVie:~/pug/atlas-web_back_end/Unittests_and_integration_tests$ python3 -m unittest test_client.py
..
----------------------------------------------------------------------
Ran 2 tests in 0.001s

OK
```

</details>

### Task 5: Mocking a Property

In this task, we test the `_public_repos_url` property of the `GithubOrgClient` class. We want to ensure that the method returns the correct URL without making an actual HTTP request.

<details>
  <summary><strong>Curriculum Instruction</strong></summary>

memoize turns methods into properties. Read up on how to mock a property (see resource).

- Implement the `test_public_repos_url` method to unit-test `GithubOrgClient._public_repos_url`.
- Use `patch` as a context manager to patch `GithubOrgClient.org` and make it return a known payload.
- Test that the result of `_public_repos_url` is the expected one based on the mocked payload.

</details>

<details>
  <summary><strong>Steps and Code Implementation</strong></summary>

### Steps:

1. **Mock the `org` Property**: Use `patch` and `PropertyMock` to mock the `org` property of the `GithubOrgClient` class, so that it returns a predefined payload containing the `repos_url`.

2. **Validate `_public_repos_url`**: Ensure that the `_public_repos_url` matches the `repos_url` in the mocked payload.

3. **Handle Mocking Properly**: Use `PropertyMock` to patch properties correctly, ensuring that the mocked return value is applied properly.

### Code:
```python
#!/usr/bin/env python3
'''
Unit tests for the client module.
Making sure everything runs as smooth as chocolate mousse!
'''

import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    '''
    Test cases for the GithubOrgClient class.
    Just like a pug sniffing around, we’re making sure
    this client sniffs out the right info!
    '''

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        '''
        Test that GithubOrgClient.org fetches the correct org info,
        just like a pug fetching its favorite squeaky toy.
        We’re making sure get_json is called once, no extra sniffs needed!
        '''
        mock_get_json.return_value = {"payload": True}

        client = GithubOrgClient(org_name)
        result = client.org  # Access as property, not a method call

        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}"
        )
        self.assertEqual(result, {"payload": True})

    @patch('client.GithubOrgClient.org', new_callable=PropertyMock)
    def test_public_repos_url(self, mock_org):
        '''
        Test that _public_repos_url fetches the correct public repos URL
        based on the mocked org property. Just like a pug chasing a ball,
        we expect it to fetch the correct one!
        '''
        mock_org.return_value = {
            "repos_url": "https://api.github.com/orgs/google/repos"
        }

        client = GithubOrgClient("google")
        result = client._public_repos_url

        # Check if the _public_repos_url matches the mocked repos_url
        self.assertEqual(result, "https://api.github.com/orgs/google/repos")


if __name__ == "__main__":
    unittest.main()
```

### How to Run the Test:
```bash
python3 -m unittest test_client.py
```

### Issues Encountered:

#### Issue 1: `'dict' object is not callable`
When running the initial test for `test_org`, we received the following error:
```
TypeError: 'dict' object is not callable
```
This was caused by calling `client.org()` as a method, even though `org` is a property. The fix was to access `client.org` as a property (without parentheses).

#### Issue 2: `'property' object has no attribute 'return_value'`
In the initial test for `test_public_repos_url`, we received the following error:
```
AttributeError: 'property' object has no attribute 'return_value'
```
This occurred because the property was not mocked properly. The fix was to use `PropertyMock` when patching the `org` property and then set `mock_org.return_value` to the desired mock data.

### Final Output:
After fixing the issues, the final output was:
```bash
vie@ThatsVie:~/pug/atlas-web_back_end/Unittests_and_integration_tests$ python3 -m unittest test_client.py
...
----------------------------------------------------------------------
Ran 3 tests in 0.001s

OK
```

</details>

### Task 6: More Patching

In this task, we tested the `GithubOrgClient.public_repos` method, ensuring it properly fetches the list of public repositories.

<details>
  <summary><strong>Curriculum Instruction</strong></summary>

Implement `TestGithubOrgClient.test_public_repos` to unit-test `GithubOrgClient.public_repos`.

- Use `@patch` as a decorator to mock `get_json` and make it return a payload of your choice.
- Use `patch` as a context manager to mock `GithubOrgClient._public_repos_url` and return a value of your choice.
- Test that the list of repos is what you expect from the chosen payload.
- Test that the mocked property and the mocked `get_json` were called once.

</details>

<details>
  <summary><strong>Steps and Code Implementation</strong></summary>

### Steps:

1. **Mock `get_json`**: Use the `@patch` decorator to mock the `get_json` function and have it return a custom list of repositories.
   
2. **Mock `_public_repos_url`**: Use the `@patch` decorator to mock `GithubOrgClient._public_repos_url` to return a custom URL.

3. **Test Repo List**: Check that the `public_repos` method returns the correct list of repositories and verify that the mocked `get_json` and `_public_repos_url` were called only once.

#### Code:
```python
#!/usr/bin/env python3
'''
Unit tests for the client module.
Making sure everything runs as smooth as chocolate mousse!
'''

import unittest
from unittest.mock import patch, PropertyMock
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    '''
    Test cases for the GithubOrgClient class.
    Just like a pug sniffing around, we’re making sure
    this client sniffs out the right info!
    '''

    @patch('client.get_json')
    @patch(
        'client.GithubOrgClient._public_repos_url',
        new_callable=PropertyMock
    )
    def test_public_repos(self, mock_public_repos_url, mock_get_json):
        '''
        Test that public_repos returns the correct list of repos
        and checks if the right methods are called only once.
        Just like how a pug only needs one sniff to find its favorite spot!
        '''
        # Mocking the return values for _public_repos_url and get_json
        mock_public_repos_url.return_value = "https://mocked_url.com"
        mock_get_json.return_value = [
            {"name": "repo_1"},
            {"name": "repo_2"},
            {"name": "repo_3"}
        ]

        # Initialize the client
        client = GithubOrgClient("google")

        # Call public_repos and capture the result
        result = client.public_repos()

        # Verify that the result matches the expected list of repo names
        self.assertEqual(result, ["repo_1", "repo_2", "repo_3"])

        # Check that _public_repos_url was called once
        mock_public_repos_url.assert_called_once()

        # Check that get_json was called once with the correct URL
        mock_get_json.assert_called_once_with("https://mocked_url.com")


if __name__ == "__main__":
    unittest.main()
```

### How to Run the Test:
```bash
python3 -m unittest test_client.py
```

#### Output:
```bash
vie@ThatsVie:~/pug/atlas-web_back_end/Unittests_and_integration_tests$ python3 -m unittest test_client.py
....
----------------------------------------------------------------------
Ran 4 tests in 0.001s

OK
```

</details>

### Task 7: Parameterize `has_license`

In this task, we implement a unit test for the `GithubOrgClient.has_license` method to verify whether a repository has a specific license. The test is parameterized to check multiple input cases.

<details>
  <summary><strong>Curriculum Instruction</strong></summary>

Implement `TestGithubOrgClient.test_has_license` to unit-test `GithubOrgClient.has_license`.

Parametrize the test with the following inputs:

- `repo={"license": {"key": "my_license"}}, license_key="my_license"`
- `repo={"license": {"key": "other_license"}}, license_key="my_license"`

You should also parameterize the expected returned value.

</details>

<details>
  <summary><strong>Steps and Code Implementation</strong></summary>

### Steps:

1. **Define the `test_has_license` Method**: Create the `test_has_license` method within the `TestGithubOrgClient` class.
   
2. **Use `@parameterized.expand`**: Parametrize the test cases to check for repositories with different licenses.

3. **Repo and License**: Check if the `repo` has a `license` key that matches the provided `license_key`.

4. **Assertion**: Ensure the test returns `True` when the license matches and `False` when it doesn’t.

#### Example Code:
```python
@parameterized.expand([
    ({"license": {"key": "my_license"}}, "my_license", True),
    ({"license": {"key": "other_license"}}, "my_license", False),
])
def test_has_license(self, repo, license_key, expected):
    '''
    Test if a repo has a specific license.
    Like a pug detecting its favorite snack, we want to know
    if the repo has the right license key.
    '''
    client = GithubOrgClient("google")
    result = client.has_license(repo, license_key)
    self.assertEqual(result, expected)
```

### How to Run the Test:
```bash
python3 -m unittest test_client.py
```

### Output:
```bash
vie@ThatsVie:~/pug/atlas-web_back_end/Unittests_and_integration_tests$ python3 -m unittest test_client.py
......
----------------------------------------------------------------------
Ran 6 tests in 0.001s

OK
```

</details>

### Task 8: Integration Test - Fixtures

In this task, we wrote an integration test for the `GithubOrgClient.public_repos` method using payload fixtures. The test patches `requests.get` to mock the responses from the GitHub API.

<details>
  <summary><strong>Curriculum Instruction</strong></summary>

We want to test the `GithubOrgClient.public_repos` method in an integration test. That means we will only mock code that sends external requests.

- Create the `TestIntegrationGithubOrgClient(unittest.TestCase)` class.
- Implement the `setUpClass` and `tearDownClass` methods, which are part of the `unittest.TestCase` API.
- Use `@parameterized_class` to decorate the class and parameterize it with fixtures found in `fixtures.py`.
- Patch `requests.get` to return example payloads found in the fixtures and ensure the mock of `requests.get(url).json()` returns the correct values based on the anticipated URL.
- Implement the `tearDownClass` method to stop the patcher.

</details>

<details>
  <summary><strong>Steps and Code Implementation</strong></summary>

### Steps:

1. **Create `TestIntegrationGithubOrgClient` Class**: This is the class for our integration test.
   
2. **Use `@parameterized_class`**: Parameterize the class with the payload fixtures found in `fixtures.py`. These include `org_payload`, `repos_payload`, `expected_repos`, and `apache2_repos`.

3. **Patch `requests.get`**: In the `setUpClass` method, patch `requests.get` and mock the `.json()` method to return the appropriate fixtures.

4. **Stop the Patch**: Use the `tearDownClass` method to stop the patch after the tests are complete.

5. **Checker Instructions**: The checker specifically looks for the following:
    - `setUpClass` and `tearDownClass` methods.
    - `@parameterized_class` decorator with the appropriate payloads.
    - `self.get_patcher` as the patcher for `requests.get`.

### Code Implementation:

```python
#!/usr/bin/env python3
'''
Unit tests for the client module.
Making sure everything runs as smooth as chocolate mousse!
'''

import unittest
from unittest.mock import patch
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


@parameterized_class(
    ("org_payload", "repos_payload", "expected_repos", "apache2_repos"),
    TEST_PAYLOAD
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    '''Integration test for GithubOrgClient.'''

    @classmethod
    def setUpClass(cls):
        '''Set up the patchers for requests.get'''
        cls.get_patcher = patch('requests.get')
        cls.mock_get = cls.get_patcher.start()

        # Set the .json() method to return the org_payload and repos_payload
        cls.mock_get.return_value.json.side_effect = [
            cls.org_payload,  # First call returns org_payload
            cls.repos_payload  # Second call returns repos_payload
        ]

    @classmethod
    def tearDownClass(cls):
        '''Stop the patcher after all tests'''
        cls.get_patcher.stop()
```

### How to Run the Test:
```bash
python3 -m unittest test_client.py
```

### Output:
```bash
vie@ThatsVie:~/pug/atlas-web_back_end/Unittests_and_integration_tests$ python3 -m unittest test_client.py
.......
----------------------------------------------------------------------
Ran 8 tests in 0.005s

OK
```

### Issues Encountered

Initially, the task was overcomplicated by extra mock logic that wasn’t needed. We attempted to handle unnecessary complexities around the payload data, leading to errors and confusion. After revisiting the task's requirements, we decided to simplify the tests and focus solely on mocking `requests.get` and checking the correct return values. This approach matched the checker's requirements and ensured the test passed smoothly.

</details>

### Task 9: Integration tests

In this task, we implement integration tests for the `GithubOrgClient.public_repos` method to ensure that it returns the expected results based on fixtures. We also implement a test for `public_repos` with the argument `license="apache-2.0"` to verify that the method correctly filters repositories by license.

<details>
  <summary><strong>Curriculum Instruction</strong></summary>

Implement the `test_public_repos` method to test `GithubOrgClient.public_repos`.

Make sure that the method returns the expected results based on the fixtures.

Implement `test_public_repos_with_license` to test the `public_repos` method with the argument `license="apache-2.0"` and ensure the result matches the expected value from the fixtures.

</details>

<details>
  <summary><strong>Steps and Code Implementation</strong></summary>

### Steps:

1. **Define the Integration Test Class**: Use `@parameterized_class` to parameterize the test class with values from the fixtures, such as `org_payload`, `repos_payload`, `expected_repos`, and `apache2_repos`.

2. **Mock `requests.get`**: In the `setUpClass` method, use `patch` to mock the `requests.get` method to simulate API responses for `org` and `repos`.

3. **Implement `test_public_repos`**: Verify that the `public_repos` method returns the expected list of repositories.

4. **Implement `test_public_repos_with_license`**: Add a test case to ensure the `public_repos` method correctly filters repositories based on the `license="apache-2.0"` argument.

#### Code:
```python
@parameterized_class([
    {"org_payload": TEST_PAYLOAD[0][0],
     "repos_payload": TEST_PAYLOAD[0][1],
     "expected_repos": TEST_PAYLOAD[0][2],
     "apache2_repos": TEST_PAYLOAD[0][3]}
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    '''Integration test for GithubOrgClient.'''

    @classmethod
    def setUpClass(cls):
        '''Set up the patchers for requests.get'''
        cls.get_patcher = patch('requests.get')
        cls.mock_get = cls.get_patcher.start()

        class MockResponse:
            '''Mock response class to simulate the .json() method.'''
            def __init__(self, json_data):
                self.json_data = json_data

            def json(self):
                return self.json_data

        def mock_get_json(url, *args, **kwargs):
            '''Side effect for mocking get requests.'''
            if url == "https://api.github.com/orgs/google":
                return MockResponse(cls.org_payload)
            if url == "https://api.github.com/orgs/google/repos":
                return MockResponse(cls.repos_payload)
            return MockResponse(None)

        cls.mock_get.side_effect = mock_get_json

    @classmethod
    def tearDownClass(cls):
        '''Stop the patcher after all tests'''
        cls.get_patcher.stop()

    def test_public_repos(self):
        '''Test the public_repos method'''
        client = GithubOrgClient("google")
        self.assertEqual(client.public_repos(), self.expected_repos)

    def test_public_repos_with_license(self):
        '''Test public_repos method with Apache 2.0 license filtering.'''
        client = GithubOrgClient("google")
        self.assertEqual(
            client.public_repos(license="apache-2.0"),
            self.apache2_repos
        )
```

### How to Run the Test:
```bash
python3 -m unittest test_client.py
```

### Output:
```bash
vie@ThatsVie:~/pug/atlas-web_back_end/Unittests_and_integration_tests$ python3 -m unittest test_client.py
........
----------------------------------------------------------------------
Ran 8 tests in 0.002s

OK
```

</details>
