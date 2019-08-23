import unittest

from models import URI
from repositories import repo, STORAGE


# noinspection PyMethodMayBeStatic


class TestURIRepository(unittest.TestCase):
    def test_creates_a_new_uri(self):
        uri = URI('http://slashdot.org')

        repo.create(uri)

        self.assertDictEqual(STORAGE, {'2jd7k8Q': uri})

    def test_retrieves_an_uri(self):
        uri = URI('http://nasa.gov')

        repo.create(uri)

        retrieved = repo.find('aZYPaKg')  # uri.id

        self.assertEqual(uri, retrieved)
