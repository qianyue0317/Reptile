# -*- encoding:utf-8 -*-
# create by Administrator on 2018/5/14

import logging
import os
from logging.handlers import TimedRotatingFileHandler
import time
from functools import wraps

'''
导入此模块的log变量 用其打印日志
'''


def initLog(name, logLevel=logging.INFO):
    log = logging.getLogger(name)
    log.setLevel(logLevel)

    logDir = '../log/'
    logFile = logDir + name + '.log'
    if os.name is 'nt':  # 如果是windows操作系统
        if not os.path.exists(logDir):
            os.mkdir(logDir)
    fh = TimedRotatingFileHandler(logFile, when='midnight')
    fh.setLevel(logLevel)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    log.addHandler(fh)
    return log


# 默认的日志
_log = initLog("default")


class Logger(object):
    def __init__(self, log):
        self.log = log

    def info(self, message):
        if self.log:
            self.log.info(message)


# 如果传入None就是取消日志打印
log = Logger(_log)


# 计算时间的装饰器
def countTime(log=None):
    def tmp(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            beginTime = time.time()
            print(beginTime)
            result = func(*args, **kwargs)
            endTime = time.time()
            print(endTime)
            costTime = int(endTime * 1000 - beginTime * 1000)
            if log:
                log.info('%s called cost time : %sms' % (func.__name__, costTime))
            return result

        return wrapper

    return tmp


if '__main__' == __name__:
    log.info("测试")


    @countTime()
    def testCountTime():
        for i in range(100000):
            print(i)
            # pass


    testCountTime()
