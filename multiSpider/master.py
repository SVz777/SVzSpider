from multiprocessing.managers import BaseManager, ValueProxy, DictProxy

from multiprocessing import Process

import multiprocessing

from multiSpider.core.config import managerConfig
from multiSpider.core.saver import SVzSaver
from multiSpider.core.urlManager import UrlManager

class Master(Process):
    def __init__(self, rootUrl, urls, max_depth, *, urlManager=UrlManager, saver=SVzSaver):
        super().__init__()
        self.manager = BaseManager(**managerConfig)
        self.urlManager = urlManager(rootUrl, urls, max_depth)
        self.saver = saver()

    def initManager(self):
        self.manager.register('getUrl',callable=self.getUrl,proxytype=DictProxy)

    def start(self):
        self.initManager()
        self.manager.get_server().serve_forever()

    def getUrl(self):
        return {'a':1,'b':2}


    def initQueue(self):
        pass

    def loadData(self):
        pass

    def saveData(self):
        pass
