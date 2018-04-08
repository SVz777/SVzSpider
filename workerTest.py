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
from multiSpider.worker import Worker

workers =[]
d= {}

for i in range(5):
    w=Worker(str(i))
    w.start()
    workers.append(w)

for i in workers:
    i.join()


print('end')