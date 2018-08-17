# -*- encoding:utf-8 -*-
# create by qianyue on 2018/5/13
# 全局配置模块 通过读取conf.ini读取相关配置参数
import ConfigParser

# 这里应该是全路径 因为别的模块在导入的时候使用相对路径是不准的 根据自己的位置修改
initFile = r'H:\coding\pythonpro\Reptile\globalConstant\conf.ini'


class Config(object):
    def __init__(self):
        self.parser = ConfigParser.ConfigParser()
        pass

    def parse(self, iniFile):
        self.parser.read(iniFile)

    def getDatabaseParam(self):
        result = {'host': self.parser.get('database', 'host'), 'port': self.parser.getint('database', 'port'),
                  'user': self.parser.get('database', 'user'), 'db': self.parser.get('database', 'db'),
                  'passwd': self.parser.get('database', 'passwd'), 'charset': self.parser.get('database', 'charset')}
        return result

    # 获取超时时间
    def getTimeout(self):
        timeout = self.parser.get('request', 'timeout')
        return float(timeout) if timeout else float(10000)


config = Config()
config.parse(initFile)
