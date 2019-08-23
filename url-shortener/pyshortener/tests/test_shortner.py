import unittest

import requests


class TestBasicShortener(unittest.TestCase):

    host = 'http://localhost:5000'

    def test_home_exists(self):
        response = requests.get(f'{self.host}')
        assert response.status_code == 200, response.status_code

    def test_shorten_url(self):
        original_url = 'https://www.alphasights.com/careers/open-positions'

        response = requests.post(f'{self.host}/shorten', json={'url': original_url})

        self.assertDictEqual(response.json(), {'short_url': 'http://localhost:5000/6KJG6wk'})

    def test_redirects_url(self):
        original_url = 'https://www.alphasights.com'

        response = requests.post(f'{self.host}/shorten', json={'url': original_url})
        short_url = response.json().get('short_url')

        response = requests.get(short_url)

        self.assertEqual(response.url, original_url)

    # def test_redir_url(self):
    #     response = requests.get(f'{self.host}/some/url')
    #     assert response.status_code == 200, response.status_code

    # def test_redirects_to_original_based_on_short_url(self):
    #     raise NotImplementedError()
