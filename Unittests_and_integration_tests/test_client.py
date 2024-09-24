#!/usr/bin/env python3
'''
Unit tests for the client module.
Making sure everything runs as smooth as chocolate mousse!
'''

import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


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
        result = client.org

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

        client = GithubOrgClient("google")

        result = client.public_repos()

        self.assertEqual(result, ["repo_1", "repo_2", "repo_3"])

        mock_public_repos_url.assert_called_once()

        mock_get_json.assert_called_once_with("https://mocked_url.com")

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


if __name__ == "__main__":
    unittest.main()
