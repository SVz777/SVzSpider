from urllib.parse import urljoin

class UrlManager:
    def __init__(self, rootUrl, urls, max_depth):
        self.max_depth = max_depth
        self.newUrls = dict(urls)
        self.oldUrls = list()
        self.rootUrl = rootUrl

    def has_url(self):
        return len(self.newUrls) != 0

    def get_url(self):
        url, depth = self.newUrls.popitem()
        self.oldUrls.append(url)
        return urljoin(self.rootUrl, url), depth

    def add_url(self, url, depth):
        if depth <= self.max_depth and url not in self.newUrls.keys() and url not in self.oldUrls:
            self.newUrls[url] = depth

    def add_urls(self, urls, depth=0):
        for url in urls:
            self.add_url(url, depth)
