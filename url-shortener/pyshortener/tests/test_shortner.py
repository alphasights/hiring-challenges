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

    def test_returns_404_for_url_that_hasnt_been_shortened(self):
        response = requests.get(f'{self.host}/doesntexist')

        self.assertEqual(response.status_code, 404)

    def test_list_shortened_urls(self):
        verge = 'http://theverge.com'
        nyt = 'http://nytimes.com'
        the_post = 'http://washingtonpost.com'

        requests.post(f'{self.host}/shorten', json={'url': verge})
        requests.post(f'{self.host}/shorten', json={'url': nyt})
        requests.post(f'{self.host}/shorten', json={'url': the_post})

        response = requests.get(f'{self.host}/list')
        items = response.json()

        self.assertIn({'GX879XJ': {'original': verge, 'shortened': 'http://localhost:5000/GX879XJ'}}, items)
        self.assertIn({'g3NN2No': {'original': nyt, 'shortened': 'http://localhost:5000/g3NN2No'}}, items)
        self.assertIn({'mY52dyb': {'original': the_post, 'shortened': 'http://localhost:5000/mY52dyb'}}, items)

    # noinspection SpellCheckingInspection
    def test_remove_shortened_url(self):
        io9 = 'http://io9.com'
        gizmodo = 'http://gizmodo.com'

        requests.post(f'{self.host}/shorten', json={'url': io9})
        requests.post(f'{self.host}/shorten', json={'url': gizmodo})

        response = requests.get(f'{self.host}/list')

        self.assertIn({'NMy0Jgj': {'original': io9, 'shortened': 'http://localhost:5000/NMy0Jgj'}}, response.json())
        shortened_gizmodo = 'http://localhost:5000/7xKJ1k2'
        shortened_gizmodo_url = {'7xKJ1k2': {'original': gizmodo, 'shortened': shortened_gizmodo}}

        self.assertIn(shortened_gizmodo_url, response.json())

        requests.delete(shortened_gizmodo)

        response = requests.get(f'{self.host}/list')

        self.assertNotIn(shortened_gizmodo_url, response.json())
