from time import sleep

from application.model import SVzDownloader
from multiSpider.core.model import Task
from multiSpider.process.worker import Worker


class Producer(Worker):
    def run(self):
        self.manager.push_task(Task(SVzDownloader(), f'http://www.svz7.cn'))


class Customer(Worker):
    def run(self):
        while True:
            if not self.manager.has_task()._getvalue():
                print('no task')
                sleep(5)
                continue
            u: Task = self.manager.pop_task()._getvalue()
            newtasks = u.do()
            if newtasks:
                self.manager.push_tasks(newtasks)


c = Customer('c')
c.start()
