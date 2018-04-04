from urllib.parse import urljoin

class SVzUrlManager:
    def __init__(self, rootUrl, urls):
        self.newUrls = set(urls)
        self.oldUrls = set()
        self.rootUrl = rootUrl
    def has_url(self):
        return len(self.newUrls) != 0

    def get_url(self):
        url = self.newUrls.pop()
        self.oldUrls.add(url)
        return urljoin(self.rootUrl,url)

    def add_url(self, url):
        if url not in self.newUrls and url not in self.oldUrls:
            self.newUrls.add(url)

    def add_urls(self, urls):
        for url in urls:
            self.add_url(url)
