import unittest

from models import URI


class TestURIModel(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.original_url = 'https://docs.python.org/3/library/urllib.parse.html'
        cls.uri = URI(cls.original_url)

    def test_exists(self):
        assert self.uri

    def test_can_shrink(self):
        self.assertEqual(self.uri.shrink(), 'http://localhost:5000/8NK6mP1')

    def test_has_an_id_based_on_hash(self):
        self.assertEqual(self.uri.id, '8NK6mP1')

    def test_has_the_original_url(self):
        self.assertEqual(self.uri.url, self.original_url)

    def test_short_domain_can_be_customized(self):
        custom_short_domain_uri = URI('https://google.com', short_domain='https://as.co')
        self.assertEqual(custom_short_domain_uri.shrink(), 'https://as.co/0YRNJKP')
