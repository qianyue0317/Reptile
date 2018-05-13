# -*- encoding:utf-8 -*-
# create by qianyue on 2018/5/13
# 全局配置模块

class Config(object):
    def __init__(self):
        self._timeout = 10000
        pass

    def setTimeout(self,timeout):
        if timeout >= 0:
            self._timeout = timeout

    # 获取超时时间
    def getTimeout(self):
        return self._timeout


config = Config()
