from time import sleep

from application.model import SVzDownloader
from multiSpider.core.model import Task
from multiSpider.process.worker import Worker


class Producer(Worker):
    def run(self):
        self.manager.push_task(Task(SVzDownloader(), f'http://127.0.0.1:8888/1'))


class Customer(Worker):
    def run(self):
        while True:
            u = self.manager.pop_task()._getvalue()
            if not u:
                print('no task')
                sleep(1)
                continue

            newtasks = u.do()
            if newtasks:
                self.manager.push_tasks(newtasks)


p = Producer('p')
p.start()
#
c=[]
for i in range(3):
    customer = Customer(f'c{i}')
    c.append(customer)
    customer.start()

for i in c:
    i.join()
