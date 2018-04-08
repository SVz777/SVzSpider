from spider.downloader import SVzDownloader
from spider.parser import SVzParser
from spider.saver import SVzSaver
from spider.urlManager import SVzUrlManager


class SVzSpider():
    def __init__(self, name, rootUrl, urls, depth, *, urlManager=SVzUrlManager, downloader=SVzDownloader, parser=SVzParser, saver=SVzSaver):
        self.name = name
        self.urlManager = urlManager(rootUrl, urls, depth)
        self.downloader = downloader()
        self.parser = parser()
        self.saver = saver()

    def craw(self):
        while self.urlManager.has_url():
            url, depth= self.urlManager.get_url()
            print(f'{self.name} crawing {url}')
            try:
                content = self.downloader.download(url)
                urls, datas = self.parser.parse(content)
                self.urlManager.add_urls(urls,depth+1)
                self.saver.save(datas)
            except Exception as e:
                print(e)
