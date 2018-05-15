# -*- encoding:utf-8 -*-
# create by Administrator on 2018/5/15
# 数据库连接

from globalConstant.config import config
import MySQLdb


class MySQLConnection(object):
    def __init__(self, conn):
        self.conn = conn
        self.insert_tmpl = r'insert into'

    def __create_table(self,tableName):
        pass

    def insert(self, tableName, **kwargs):
        pass


if '__main__' == __name__:
    connection = MySQLdb.Connection()
    cursor = connection.cursor()

    pass
