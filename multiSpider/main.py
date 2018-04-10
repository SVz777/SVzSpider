import re
from time import time

import pymysql
from bs4 import BeautifulSoup

from multiSpider.core.parser import Parser
from multiSpider.core.saver import Saver
from multiSpider.worker import Worker


class SVzPaser(Parser):
    def parse(self, content):
        return self.parseAuthor(content)

    def parseAuthor(self, content):
        urls = []
        datas = []
        bs = BeautifulSoup(content, 'html.parser')
        datas_info = bs.select('div.sonspic div.cont')
        urls_info = bs.select('div.pages a')
        for url in urls_info:
            urls.append(url['href'])
        for i in datas_info:
            data = {}
            data['name'] = i.select_one('b').get_text()
            data['image'] = i.select_one('img')['src']
            data['dynasty'] = bs.select_one('div.sright span').get_text()
            data['href'] = i.find('a', attrs={'href': re.compile(r'/authors/authorvsw_(.*?).aspx')})['href']
            datas.append(data)
        return urls, datas

class SVzSaver(Saver):
    def __init__(self):
        db = {
            #'host': '10.96.109.86',
            'host':'lmc.svz7.cn',
            'user': 'root',
            'password': 'svz7777777',
            'db': 'test',
            'charset': 'utf8'
        }
        self.conn = pymysql.connect(**db)

    def save(self, datas):
        self.insert_datas(datas)

    def insert_datas(self, datas):
        for data in datas:
            self.insert_data(data)

    def insert_data(self, data):
        cur = self.conn.cursor()
        sql = f"insert into poet(`name`,`dynasty`,`image`,`href`) VALUES ('{data['name']}','{data['dynasty']}','{data['image']}','{data['href']}')"
        cur.execute(sql)
        self.conn.commit()


rootUrl = 'https://so.gushiwen.org/authors/'
urls = {
    'Default.aspx?p=1&c=%e5%85%88%e7%a7%a6': 0,  # 先秦
    'Default.aspx?p=1&c=%e4%b8%a4%e6%b1%89': 0,  # 两汉
    'Default.aspx?p=1&c=%e9%ad%8f%e6%99%8b': 0,  # 魏晋
    'Default.aspx?p=1&c=%e5%8d%97%e5%8c%97%e6%9c%9d': 0,  # 南北朝
    'Default.aspx?p=1&c=%e9%9a%8b%e4%bb%a3': 0,  # 隋代
    'Default.aspx?p=1&c=%e5%94%90%e4%bb%a3': 0,  # 唐代
    'Default.aspx?p=1&c=%e4%ba%94%e4%bb%a3': 0,  # 五代
    'Default.aspx?p=1&c=%e5%ae%8b%e4%bb%a3': 0,  # 宋代
    'Default.aspx?p=1&c=%e9%87%91%e6%9c%9d': 0,  # 金朝
    'Default.aspx?p=1&c=%e5%85%83%e4%bb%a3': 0,  # 元代
    'Default.aspx?p=1&c=%e6%98%8e%e4%bb%a3': 0,  # 明代
    'Default.aspx?p=1&c=%e6%b8%85%e4%bb%a3': 0,  # 清代
}
spiders = []
s = time()
for i in range(8):
    spider = Worker(f'svz{i}', rootUrl, urls, parser=SVzPaser, saver=SVzSaver)
    spiders.append(spider)
    spider.start()

for i in spiders:
    i.join()

print(time() - s)
