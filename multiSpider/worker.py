from multiprocessing.managers import BaseManager

from multiprocessing import Process
from time import sleep

from multiSpider.core.config import *
from multiSpider.core.downloader import Downloader
from multiSpider.core.parser import Parser


class Worker(Process):
    def __init__(self, name, *, downloader=Downloader, parser=Parser):
        super().__init__()
        self.name=name
        self.manager=BaseManager(**managerConfig)
        self.downloader = downloader()
        self.parser = parser()

    def initManager(self):
        for action in managerAction:
            print(action)
            self.manager.register(action['typeid'])
        self.manager.connect()

    # def initQueue(self):
    #     self.newUrls = self.manager.getUrl()
    #     self.oldUrls = self.manager.getOldUrls()

    def run(self):
        self.initManager()
        # self.initQueue()
        while True:
            u = self.manager.getUrl()
            print(u)
            u['c']=1
            print(u['a'])
            sleep(1)
