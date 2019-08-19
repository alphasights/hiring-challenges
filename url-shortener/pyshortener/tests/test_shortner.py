import unittest
import requests


class TestBasicShortener(unittest.TestCase):

    def test_home_exists(self):
        response = requests.get('http://localhost:5000')
        assert response.status_code == 200, response.status_code

    def test_creates_small_url(self):
        raise NotImplementedError()

    def test_redirects_to_original_based_on_short_url(self):
        raise NotImplementedError()
