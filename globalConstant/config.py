# -*- encoding:utf-8 -*-
# create by qianyue on 2018/5/13
# 全局配置模块

class Config(object):

    def __init__(self):
        self._timeout = 10000
        self._log = True
        pass

    def setTimeout(self,timeout):
        if timeout >= 0:
            self._timeout = timeout

    # 获取超时时间
    def getTimeout(self):
        return self._timeout

    # 是否打印日志
    def isLog(self):
        return self._log


config = Config()
