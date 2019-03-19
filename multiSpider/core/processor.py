import requests


class Processor:
    def do(self, obj):
        raise NotImplementedError

    def __eq__(self, other):
        return self.__class__ == other.__class__


class Downloader(Processor):
    def download(self, url):
        raise NotImplementedError

    def do(self, obj):
        return self.download(obj)


class Parser(Processor):
    def parse(self, content):
        raise NotImplementedError

    def do(self, obj):
        return self.parse(obj)


class Saver(Processor):
    def save(self, datas):
        raise NotImplementedError

    def do(self, obj):
        return self.save(obj)
