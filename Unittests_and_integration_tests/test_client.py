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