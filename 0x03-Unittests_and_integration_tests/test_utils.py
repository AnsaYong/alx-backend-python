#!/usr/bin/env python3
"""
This module provides utilities for testing.
"""
import unittest
from parameterized import parameterized
access_nested_map = __import__('utils').access_nested_map


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
