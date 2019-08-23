import zlib
from urllib.parse import urlparse, urljoin

from hashids import Hashids


class URL:
    def __init__(self, value, short_domain=None):
        self.domain = short_domain or 'http://localhost:5000'
        self._o = urlparse(value)

        # Adler is poor, but good enough
        # Domain can be used as a salt, for fun
        self.original = value
        self.id = Hashids(salt='a grain of').encode(zlib.adler32(self._o.geturl().encode()))

    def __eq__(self, o):
        return self.id == o.id

    def shrink(self):
        return urljoin(self.domain, self.id)

    def to_dict(self):
        return {self.id: {'original': self.original, 'shortened': self.shrink()}}
