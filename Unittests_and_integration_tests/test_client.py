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
