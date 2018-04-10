from urllib.parse import urljoin
from redis import Redis


class UrlManager:
    def __init__(self, rootUrl, urls):
        self.redis = Redis(decode_responses=True)
        self.rootUrl = rootUrl
        self.newUrls = 'newUrls'
        self.oldUrls = 'oldUrls'
        self.add_urls(urls)

    def has_url(self):
        num = self.redis.scard(self.newUrls)
        return num if num else 'end'

    def get_url(self):
        url = self.redis.spop(self.newUrls)
        self.redis.sadd(self.oldUrls, url)
        return urljoin(self.rootUrl, url)

    def add_url(self, url):
        if self.redis.sismember(self.newUrls, url) or self.redis.sismember(self.oldUrls, url):
            return 0
        self.redis.sadd(self.newUrls, url)
        return 1

    def add_urls(self, urls):
        count = 0
        for url in urls:
            count += self.add_url(url)
        return count
