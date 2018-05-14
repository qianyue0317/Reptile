# -*- encoding:utf-8 -*-
# create by qianyue on 2018/5/13
# 全局配置模块 通过读取conf.ini读取相关配置参数
import ConfigParser


class Config(object):
    def __init__(self):
        self.parser = ConfigParser.ConfigParser()
        pass

    def parse(self, iniFile):
        self.parser.read(iniFile)

    # 获取超时时间
    def getTimeout(self):
        timeout = self.parser.get('request', 'timeout')
        return timeout if timeout else 10000


config = Config()
config.parse('./conf.ini')
