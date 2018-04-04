from spider.downloader import SVzDownloader
from spider.parser import SVzParser
from spider.saver import SVzSaver
from spider.urlManager import SVzUrlManager


class SVzSpider():

    def __init__(self, name, rootUrl, urls, *, urlManager=SVzUrlManager, downloader=SVzDownloader, parser=SVzParser, saver=SVzSaver):
        self.name = name
        self.urlManager = urlManager(rootUrl, urls)
        self.downloader = downloader()
        self.parser = parser()
        self.saver = saver()

    def craw(self):
        while self.urlManager.has_url():
            url = self.urlManager.get_url()
            print(f'{self.name} crawing {url}')
            content = self.downloader.download(url)
            urls, datas = self.parser.parse(content)
            self.urlManager.add_urls(urls)
            self.saver.save(datas)

