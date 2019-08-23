from models import URI

STORAGE = {}


# noinspection PyMethodMayBeStatic
class URIRepository:
    def create(self, uri: URI):
        STORAGE[uri.id] = uri

    def find(self, id_: object) -> URI: 
        return STORAGE.get(id_)


repo = URIRepository()
