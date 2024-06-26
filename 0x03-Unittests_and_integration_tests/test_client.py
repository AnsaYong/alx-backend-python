#!/usr/bin/env python3
"""
This module provides utilities for testing client.py.
"""
import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from parameterized import parameterized_class

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
        # Create an instance of the GithubOrgClient class
        test_class = GithubOrgClient(org_name)

        # Call the org method
        test_class.org()

        # Assert that the get_json method was called once with the expected
        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}"
        )

    @patch('client.GithubOrgClient.org',
           return_value={
               "repos_url": "https://api.github.com/orgs/google/repos"})
    def test_public_repos_url(self, mock_org: Mock):
        """
        Tests the _public_repos_url property of the GithubOrgClient class.

        Returns:
            None
        """
        # Create an instance of the GithubOrgClient class
        test_class = GithubOrgClient("google")

        # Assert that the _public_repos_url property returns the expected value
        self.assertEqual(test_class._public_repos_url,
                         "https://api.github.com/orgs/google/repos")

    @patch('client.GithubOrgClient._public_repos_url',
           return_value="https://api.github.com/orgs/google/repos")
    @patch('client.get_json',
           return_value=[{"name": "a"}, {"name": "b"}])
    def test_public_repos(self, mock_public_repos_url: Mock,
                          mock_get_json: Mock):
        """
        Tests the public_repos method of the GithubOrgClient class.

        Returns:
            None
        """
        # Create an instance of the GithubOrgClient class
        test_class = GithubOrgClient("google")

        # Call the public_repos method
        result = test_class.public_repos()

        # Assert that the public_repos method returns the expected value
        self.assertEqual(result, ["a", "b"])

        # Assert _public_repos_url prop and get_json func were called once
        mock_public_repos_url.assert_called_once()
        mock_get_json.assert_called_once_with(
            "https://api.github.com/orgs/google/repos")

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo: dict, license_key: str, expected: bool):
        """
        Tests the has_license method of the GithubOrgClient class.

        Returns:
            None
        """
        # Call the has_license method
        result = GithubOrgClient.has_license(repo, license_key)

        # Assert that the has_license method returns the expected value
        self.assertEqual(result, expected)


@parameterized_class(('org_payload', 'repos_payload', 'expected_repos',
                      'apache2_repos'), [("org_payload_example",
                                          "repos_payload_example",
                                          ["repo1", "repo2"],
                                          ["apache_repo1",
                                           "apache_repo2"]),
                                         ])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """
    Methods to test the GithubOrgClient class.

    Methods:
        - test_public_repos_with_license: Test the public_repos method of the
            GithubOrgClient class.
    """
    @classmethod
    def setUpClass(cls):
        """
        Set up the class with the required patchers.
        """
        # Mock requests.get to return org_payload and repos_payload
        cls.get_patcher = patch('client.requests.get')
        cls.mock_get = cls.get_patcher.start()
        cls.mock_get.side_effect = [cls.org_payload, cls.repos_payload]

    @classmethod
    def tearDownClass(cls):
        """
        Clean up the class by stopping the patchers.
        """
        cls.get_patcher.stop()

    def test_public_repos(self):
        """
        Tests the public_repos method of the GithubOrgClient class.

        Returns:
            None
        """
        # Create an instance of the GithubOrgClient class
        test_class = GithubOrgClient("google")

        # Call the public_repos method
        result = test_class.public_repos()

        # Assert that the public_repos method returns the expected value
        self.assertEqual(result, self.expected_repos)

    def test_public_repos_with_license(self):
        """
        Tests the public_repos method of the GithubOrgClient class with a
        license.

        Returns:
            None
        """
        # Create an instance of the GithubOrgClient class
        test_class = GithubOrgClient("google")

        # Call the public_repos method with a license
        result = test_class.public_repos(license="apache-2.0")

        # Assert that the public_repos method returns the expected value
        self.assertEqual(result, self.apache2_repos)
