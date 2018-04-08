import pymysql

from spider.saver import SVzSaver


class Saver(SVzSaver):
    def __init__(self):
        db={
            'host':'10.96.109.86',
            'user':'root',
            'password':'beatlesapi20161206',
            'db':'test',
            'charset':'utf8'
        }
        self.conn = pymysql.connect(**db)

    def save(self, datas):
        self.insert_datas(datas)

    def insert_datas(self,datas):
        for data in datas:
            self.insert_data(data)

    def insert_data(self,data):
        cur = self.conn.cursor()
        sql = f"insert into poet(`name`,`dynasty`,`image`,`href`) VALUES ('{data['name']}','{data['dynasty']}','{data['image']}','{data['href']}')"
        cur.execute(sql)
        self.conn.commit()
