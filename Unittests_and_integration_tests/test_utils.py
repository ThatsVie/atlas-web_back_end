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
