from urllib.parse import urljoin


class TaskManager:
    def __init__(self, tasks):
        self.newTask = set()
        self.oldTask = set()
        self.push_tasks(tasks)

    def has_task(self):
        return len(self.newTask) != 0

    def pop_task(self):
        task = self.newTask.pop()
        self.newTask.add(task)
        return task

    def push_task(self, task):
        self.newTask.add(task)

    def push_tasks(self, tasks):
        for task in tasks:
            self.push_task(task)
