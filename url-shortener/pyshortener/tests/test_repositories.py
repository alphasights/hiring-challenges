import unittest

from models import URL
from repositories import URLRepository


# noinspection PyMethodMayBeStatic


class TestURLRepository(unittest.TestCase):
    def setUp(self):
        super().setUp()
        self.repo = URLRepository()

    def test_creates_a_new_url(self):
        url = URL('http://slashdot.org')

        self.repo.create(url)

        self.assertListEqual(self.repo.STORAGE, [url])

    def test_retrieves_an_url(self):
        url = URL('http://nasa.gov')

        self.repo.create(url)

        retrieved = self.repo.find('aZYPaKg')  # url.id

        self.assertIn(url, retrieved)

    def test_knows_how_many_items_exists(self):
        url1 = URL('http://google.com.br')
        url2 = URL('http://google.com.ar')
        url3 = URL('http://google.com.ch')

        self.repo.create(url1)
        self.repo.create(url2)
        self.repo.create(url3)

        self.assertEqual(self.repo.count(), 3)

    def test_doesnt_add_the_same_url_twice(self):
        url1 = URL('http://google.com.br')
        url2 = URL('http://google.com.br')
        url3 = URL('http://google.com.ch')

        self.repo.create(url1)
        self.repo.create(url2)
        self.repo.create(url3)

        self.assertEqual(self.repo.count(), 2)

    def test_delete_url(self):
        url1 = URL('http://bitly.com')
        url2 = URL('http://g.com')

        self.repo.create(url1)
        self.repo.create(url2)
        self.assertEqual(self.repo.count(), 2)

        self.repo.delete(url2)

        self.assertEqual(self.repo.count(), 1)

    def test_lists_all_urls(self):
        url1 = URL('http://spacex.com')
        url2 = URL('http://neuralink.com')
        url3 = URL('http://tesla.com')

        self.repo.create(url1)
        self.repo.create(url2)
        self.repo.create(url3)

        retrieved = self.repo.all()  # url.id

        self.assertIn(url1, retrieved)
        self.assertIn(url2, retrieved)
        self.assertIn(url3, retrieved)
