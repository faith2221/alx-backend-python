#!/usr/bin/env python3
"""
Test client.py
"""
import unittest
from unittest.mock import patch, PropertyMock, MagicMock
from parameterized import parameterized, parameterized_class
from urllib.error import HTTPError
from fixtures import TEST_PAYLOAD
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """
    Test org
    """
    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch("client.get_json", result_value={"payload": True})
    def test_org(self, org_name, mock_get_json):
        """
        Test GithubClient.org
        """
        client = GithubOrgClient(org_name)
        result = client.org
        self.assertEqual(result, mock_get_json.result_value)
        mock_get_json.assert_called_once

    def test_public_repos_url(self):
        """
        Test public_repos_url property
        """

        with patch(
            "client.GithubOrgClient.org",
            new_callable=PropertyMock
        ) as mock_org_url:
            mock_org_url.result_value = {
                'repos_url': "https://api.github.com/users/google/repos",
            }
            self.assertEqual(
                GithubOrgClient("google")._public_repos_url,
                "https://api.github.com/users/google/repos",
            )

    @patch("client.get_json", result_value=[{"name": "Google"}])
    def test_public_repos(self, mock_get_json: MagicMock):
        """
        Test public_repos
        """
        with patch.object(
            GithubOrgClient,
            "_public_repos_url",
            new_callable=PropertyMock,
            result_value="https://api.github.com/users/google/repos"
        ) as mock_org:
            client = GithubOrgClient("Google")
            result = client.public_repos()
            self.assertEqual(result, ["Google"])
            mock_get_json.assert_called_once
            mock_org.assert_called_once

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
        ])
    def test_has_license(self, repo, license_key, expected_result):
        """
        Test GithubOrgClient.has_license
        """
        client = GithubOrgClient("Google")
        result = client.has_license(repo, license_key)
        self.assertEqual(expected_result, result)


@parameterized_class(
    ("org_payload", "repos_payload", "expected_repos", "apache2_repos"),
    TEST_PAYLOAD
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """
    Integration test GithubOrgClient.public_repos
    """

    @classmethod
    def SetUpClass(cls):
        """
        SetUp
        """
        cls.get_patcher = patch("requests.get", side_effect=HTTPError)

    @classmethod
    def tearDownClass(cls):
        """
        teardown
        """
        cls.get_patcher.stop()

    deg test_public_repos(self):
        """
        test public repo: integration
        """
        self.assertEqual(
            GithubOrgClient("Google").public_repos(),
            self.expected_repos,
        )

    def test_public_repos_with_license(self):
        """
        test
        """
        self.assertEqual(
            GithubOrgClient("Google").public_repos(license="apache-2.0"),
            self.apache2_repos,
        )
