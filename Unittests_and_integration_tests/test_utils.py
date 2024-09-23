#!/usr/bin/env python3
'''
Unit tests for the utils module.
'''

import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from utils import access_nested_map, get_json


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
    def test_access_nested_map_exception(self, nested_map, path,
                                         expected_error):
        '''
        Test that KeyError is raised for invalid paths in access_nested_map.
        '''
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)
        self.assertEqual(str(context.exception), f"'{expected_error}'")


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

        # call once with the correct URL
        mock_get.assert_called_once_with(test_url)


if __name__ == "__main__":
    unittest.main()
