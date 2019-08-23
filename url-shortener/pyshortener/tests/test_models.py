import unittest

from models import URL


class TestURLModel(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.original_url = 'https://docs.python.org/3/library/urllib.parse.html'
        cls.url = URL(cls.original_url)

    def test_with_the_same_id_are_considered_equal(self):
        self.assertEqual(self.url, URL(self.original_url))

    def test_can_shrink(self):
        self.assertEqual(self.url.shrink(), 'http://localhost:5000/8NK6mP1')

    def test_has_an_id_based_on_hash(self):
        self.assertEqual(self.url.id, '8NK6mP1')

    def test_has_the_original_url(self):
        self.assertEqual(self.url.original, self.original_url)

    def test_can_be_represent_as_a_dict(self):
        self.assertDictEqual(self.url.to_dict(),
                             {'8NK6mP1': {'original': self.original_url, 'shortened': self.url.shrink()}})

    def test_short_domain_can_be_customized(self):
        custom_short_domain_url = URL('https://google.com', short_domain='https://as.co')
        self.assertEqual(custom_short_domain_url.shrink(), 'https://as.co/0YRNJKP')

