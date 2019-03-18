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

    def init_manager(self):
        for action in managerAction:
            self.manager.register(action.typeid)
        self.manager.connect()

    def run(self):
        self.init_manager()
        while True:
            u = self.manager.get_task()
            print(u)
