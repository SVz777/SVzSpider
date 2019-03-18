import random

from multiSpider.core.processor import Downloader


class Task:
    def __init__(self, processor, obj):
        self.processor = processor
        self.obj = obj

    def do(self):
        return self.processor.do(self.obj)

    def __repr__(self):
        return f'{self.processor}'

    def __eq__(self, other):
        return self.processor == other.processor and self.obj == other.obj

    def __hash__(self):
        return hash(self.processor.__class__) + hash(self.obj)


if __name__ == '__main__':
    t = Task(Downloader(), 'http://www.svz7.cn')
    print(t.do())