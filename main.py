import re

from saver import Saver
from spider.parser import SVzParser
from spider.svz import SVzSpider
from bs4 import BeautifulSoup
import matplotlib


class Paser(SVzParser):
    def parse(self, content):
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
depth = 100
spider = SVzSpider('svz', rootUrl, urls, depth, parser=Paser)
spider.craw()
