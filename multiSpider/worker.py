from multiprocessing import Process

from multiSpider.core.downloader import Downloader
from multiSpider.core.parser import Parser
from multiSpider.core.saver import Saver
from multiSpider.core.urlManager import UrlManager



class Worker(Process):
    def __init__(self, name, rootUrl, urls, *, urlManager=UrlManager, downloader=Downloader, parser=Parser, saver=Saver):
        super().__init__()
        self.name=name
        self.urlManager=urlManager(rootUrl,urls)
        self.downloader = downloader()
        self.parser = parser()
        self.saver = saver()

    def run(self):
        self.craw()

    def craw(self):
        while self.urlManager.has_url() != 'end':
            url = self.urlManager.get_url()
            print(f'{self.name} crawing {url}')
            try:
                content = self.downloader.download(url)
                urls, datas = self.parser.parse(content)
                self.urlManager.add_urls(urls)
                self.saver.save(datas)
            except Exception as e:
                print(e)

