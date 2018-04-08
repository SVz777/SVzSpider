# from urllib.parse import quote
#
# urls=[
#     '先秦',
#     '两汉',
#     '魏晋',
#     '南北朝',
#     '隋代',
#     '唐代',
#     '五代',
#     '宋代',
#     '金朝',
#     '元代',
#     '明代',
#     '清代',
# ]
# for u in urls:
#     print("'Default.aspx?p=1&c="+quote(u).lower()+"',#"+u)

# import multiprocessing
# from multiprocessing.managers import BaseManager, SyncManager, ListProxy, DictProxy
#
# from multiSpider.core.config import managerConfig
#
# t = SyncManager()
# a = multiprocessing.Manager()
# d = a.dict()
# l = a.list()
# for i in range(10000):
#     d[i]=i
#     l.append(i)
# class A:
#     def test(cls):
#         return 'z'
#
# a = A()
# manager=BaseManager(**managerConfig)
# # manager.register('getUrl',callable=lambda :d,proxytype=DictProxy)
# manager.register('getUrl',callable=a.test,proxytype=ListProxy)
# manager.get_server().serve_forever()

from multiSpider.master import Master
from multiprocessing import sharedctypes

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

master = Master(rootUrl,urls,depth)
master.start()