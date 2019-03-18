from multiSpider.core.model import Task
from multiSpider.core.processor import Downloader, Parser


def p(func):
    a = func.__name__

    def wapper(*args,**kwargs):
        print(a)
        res = func(*args,**kwargs)
        return res

    return wapper

class TaskManager:
    def __init__(self, tasks):
        self.newTask = set()
        self.oldTask = set()
        self.push_tasks(tasks)
    @p
    def has_task(self):
        return len(self.newTask) != 0

    @p
    def pop_task(self):
        task = self.newTask.pop()
        self.oldTask.add(task)
        return task

    @p
    def push_task(self, task):
        if task not in self.oldTask or task not in self.newTask:
            print(task)
            self.newTask.add(task)

    @p
    def push_tasks(self, tasks):
        for task in tasks:
            self.push_task(task)


if __name__ == '__main__':
    tm = TaskManager([])
    tm.push_tasks([Task(Downloader, 'http://www.baidu.com'), Task(Parser, 'test')])
    tm.push_tasks([Task(Downloader, 'http://www.baidu.com'), Task(Parser, 'test')])
    while tm.has_task():
        a = tm.pop_task()
        print(a)
