from models import URL


# noinspection PyMethodMayBeStatic
class URLRepository:
    def __init__(self):
        self.STORAGE = []

    def create(self, url: URL):
        if url not in self.STORAGE:
            self.STORAGE.append(url)

    def find(self, id_: object):
        return [url for url in self.STORAGE if url.id == id_]

    def all(self):
        return self.STORAGE

    def count(self):
        return len(self.STORAGE)

    def delete(self, url):
        self.STORAGE.remove(url)


repo = URLRepository()
