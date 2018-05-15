# -*- encoding:utf-8 -*-
# create by Administrator on 2018/5/15
# 数据库连接

from globalConstant.config import config
import MySQLdb


class MySQLConnection(object):
    def __init__(self, conn):
        self.conn = conn
        self.insert_tmpl = r'insert into %s (date,province,city,country,name,' \
                           r'address,estate_type,house_type,acreage,price,source,' \
                           r'ctime,state) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'

    def __create_table(self, tableName):
        pass

    def insertDetail(self, **kwargs):
        sql = self.insert_tmpl % (kwargs['date'],)
        pass


if '__main__' == __name__:
    connection = MySQLdb.Connection()
    cursor = connection.cursor()

    pass
