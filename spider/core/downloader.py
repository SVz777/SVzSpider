import requests


class SVzDownloader:
    def __init__(self,headers=None):
        baseheaders={
            'Connection':'keep-alive',
            'Upgrade-Insecure-Requests':'1',
            'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2986.0 Safari/537.36',
            'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Encoding':'gzip, deflate, sdch',
            'Accept-Language':'zh-CN,zh;q=0.8',
        }
        if headers is not None:
            baseheaders.update(headers)
        self.rq=requests.session()
        self.rq.headers.update(baseheaders)

    def download(self, url):
        if url is None:
            return None
        content=self.rq.get(url)
        return content.content.decode()

if __name__ == '__main__':
    d = SVzDownloader()
    d.download('https://so.gushiwen.org/authors/')
