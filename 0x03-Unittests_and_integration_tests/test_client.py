#!/usr/bin/env python3
"""
This module provides utilities for testing client.py.
"""
import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized

GithubOrgClient = __import__('client').GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """
    Methods to test the GithubOrgClient class.

    Methods:
        - test_org: Test the org method of the GithubOrgClient class.
        - test_repos_payload: Test the repos_payload method of the
            GithubOrgClient class.
        - test_public_repos: Test the public_repos method of the
            GithubOrgClient class.
        - test_has_license: Test the has_license method of the
            GithubOrgClient class.
    """

    @parameterized.expand([
        ("google"),
        ("abc"),
    ])
    @patch('client.get_json')
    def test_org(self, org_name: str, mock_get_json: Mock):
        """
        Tests the org method of the GithubOrgClient class.

        Returns:
            None
        """
        test_class = GithubOrgClient(org_name)
        test_class.org()
        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}"
        )

    @parameterized.expand([
        ("google"),
        ("abc"),
    ])
    @patch('client.get_json')
    def test_repos_payload(self, org_name: str, mock_get_json: Mock):
        """
        Tests the repos_payload method of the GithubOrgClient class.

        Returns:
            None
        """
        test_class = GithubOrgClient(org_name)
        test_class.repos_payload()
        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}"
        )

    @parameterized.expand([
        ("google", None),
        ("abc", None),
        ("google", "mit"),
        ("abc", "mit"),
    ])
    @patch('client.GithubOrgClient.repos_payload')
    def test_public_repos_url(
        self, org_name: str, license: str, mock_repos_payload):
        """
        Tests the public_repos method of the GithubOrgClient class.

        Returns:
            None
        """
        test_class = GithubOrgClient(org_name)
        test_class.public_repos(license)
        mock_repos_payload.assert_called_once()

    @parameterized.expand([
        ("google", "mit"),
        ("abc", "mit"),
    ])
    @patch('client.access_nested_map')
    @patch('client.GithubOrgClient.repos_payload')
    def test_has_license(self, org_name, license, mock_repos_payload,
                         mock_access_nested_map):
        """
        Tests the has_license method of the GithubOrgClient class.

        Returns:
            None
        """
        test_class = GithubOrgClient(org_name)
        test_class.has_license
