import requests
from bs4 import BeautifulSoup

from multiSpider.core.model import Task
from multiSpider.core.processor import Downloader, Parser, Saver
from collections import namedtuple


class SVzDownloader(Downloader):
    def __init__(self, headers=None):
        baseheaders = {
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2986.0 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate, sdch',
            'Accept-Language': 'zh-CN,zh;q=0.8',
        }
        if headers is not None:
            baseheaders.update(headers)
        self.rq = requests.session()
        self.rq.headers.update(baseheaders)

    def download(self, url):
        if url is None:
            return None
        content = self.rq.get(url)
        return [Task(SVzParser(), content.content.decode())]


item = namedtuple('item', ['title', 'name', 'content'])


class SVzParser(Parser):
    def parse(self, content):
        bs = BeautifulSoup(content, 'html.parser')
        urls = [f"http://127.0.0.1:8888{i['href']}" for i in bs.select('a[href^=/]')]
        cont = bs.select_one('p')
        datas = []

        if cont:
            title = cont.text
            datas.append(item(title=title, name=title, content=title))

        tasks = [
            Task(SVzSaver(), tuple(datas))
        ]

        for url in urls:
            tasks.append(Task(SVzDownloader(), url))

        return tasks


class SVzSaver(Saver):
    def save(self, datas):
        for data in datas:
            print(data)
