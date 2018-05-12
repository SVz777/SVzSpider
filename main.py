import re

from spider.parser import SVzParser
from spider.svz import SVzSpider
from bs4 import BeautifulSoup

class Paser(SVzParser):
    def parse(self, content, **kwargs):
        urls=[]
        datas=[]
        bs = BeautifulSoup(content,'html.parser')
        datas_info = bs.select('div.sonspic div.cont')
        urls_info = bs.select('div.pages a')
        for url in urls_info:
            urls.append(url['href'])
        for i in datas_info:
            data={}
            data['name']=i.select_one('b').get_text()
            data['image']=i.select_one('img')['src']
            data['href']=i.find('a',attrs={'href':re.compile(r'/authors/authorvsw_(.*?).aspx')})['href']
            datas.append(data)
        return urls,datas



urls = ['https://so.gushiwen.org/authors/']
spider = SVzSpider('svz',urls[0],urls,parser=Paser)
spider.craw()

