#!/usr/bin/env python3
"""
This module provides utilities for testing.
"""
import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized

access_nested_map = __import__('utils').access_nested_map
get_json = __import__('utils').get_json
memoize = __import__('utils').memoize


class TestAccessNestedMap(unittest.TestCase):
    """
    Methods to test the access_nested_map function.

    Methods:
        - test_access_nested_map: Test the access_nested_map function.
        - test_access_nested_map_exception: Test the access_nested_map
            function raises the expected exception.
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map: dict, path: list,
                               expected: any):
        """
        Tests the access_nested_map function returns what it is expected
        to return.

        Returns:
            None
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError),
    ])
    def test_access_nested_map_exception(self, nested_map: dict, path: list,
                                         expected: any):
        """
        Tests the access_nested_map function raises the expected exception.

        Returns:
            None
        """
        with self.assertRaises(expected):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """
    Methods to test the get_json function.

    Methods:
        - test_get_json: Test the get_json function.
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, test_url: str, test_payload: dict):
        """
        Tests if the get_json function returns what it is expected to return.

        Returns:
            None
        """
        with patch('utils.requests.get') as mock_get:
            # Create a Mock response object with the specified json method
            mock_response = Mock()
            mock_response.json.return_value = test_payload
            mock_get.return_value = mock_response

            # Call the function with test_url
            result = get_json(test_url)

            # Assert that requests.get was called exactly once with test_url
            mock_get.assert_called_once_with(test_url)
            # Assert that the result of get_json is equal to test_payload
            self.assertEqual(result, test_payload)


class TestMemoize(unittest.TestCase):
    """
    Methods to test the memoize function.

    Methods:
        - test_memoize: Test the memoize function.
    """
    def test_memoize(self):
        """
        Tests if the memoize function returns what it is expected to return.

        Returns:
            None
        """
        class TestClass:
            """
            A test class
            """
            def a_method(self):
                """
                A method
                """
                return 42

            @memoize
            def a_property(self):
                """
                A property
                """
                return self.a_method()

        with patch.object(
                TestClass, 'a_method', return_value=42) as mock_method:
            test_instance = TestClass()

            # Access a_property twice
            result1 = test_instance.a_property
            result2 = test_instance.a_property

            # Assert that the results are correct
            self.assertEqual(result1, 42)
            self.assertEqual(result2, 42)

            # Assert a_method is only called once
            mock_method.assert_called_once()
