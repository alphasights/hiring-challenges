import zlib
from urllib.parse import urlparse, urljoin

from hashids import Hashids


class URI:
    def __init__(self, value, short_domain=None):
        self.domain = short_domain or 'http://localhost:5000'
        self._o = urlparse(value)

        # Adler is poor, but good enough
        # Domain can be used as a salt, for fun
        self.url = value
        self.id = Hashids(salt='a grain of').encode(zlib.adler32(self._o.geturl().encode()))

    def shrink(self):
        return urljoin(self.domain, self.id)
