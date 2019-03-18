import random
from multiprocessing.managers import BaseManager,AutoProxy

from multiprocessing import Process
from time import sleep

from multiSpider.core.config import *
from multiSpider.core.model import Task
from multiSpider.core.processor import Downloader, Parser


class Worker(Process):
    def __init__(self, name):
        super().__init__()
        self.name=name
        self.manager=BaseManager(**managerConfig)
        self.init_manager()

    def init_manager(self):
        for action in managerAction:
            self.manager.register(action.typeid,proxytype=action.proxy)
        self.manager.connect()