from multiprocessing.managers import BaseManager

from multiprocessing import Process

import multiprocessing

from multiSpider.core.config import managerConfig, managerAction
from multiSpider.core.saver import SVzSaver
from multiSpider.core.taskManager import TaskManager


class Master(Process):
    def __init__(self, tasks, *, task_manager=TaskManager, saver=SVzSaver):
        super().__init__()
        self.manager = BaseManager(**managerConfig)
        self.task_manager = task_manager(tasks)
        self.saver = saver()

    def init_manager(self):
        for action in managerAction:
            self.manager.register(action.typeid, callable=getattr(self.task_manager, action.action))

    def start(self):
        self.init_manager()
        self.manager.get_server().serve_forever()
