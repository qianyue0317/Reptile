# -*- encoding:utf-8 -*-
# create by Administrator on 2018/5/14

import logging
import os
from logging.handlers import TimedRotatingFileHandler
from logging import StreamHandler
import time
from functools import wraps

'''
导入此模块的log变量 用其打印日志
'''


# console 设置是否打印控制台日志
def initLog(name, logLevel=logging.INFO, console=True):
    log = logging.getLogger(name)
    log.setLevel(logLevel)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # 如果name是None就没有本地日志
    if name is None:
        logDir = '../log/'
        logFile = logDir + name + '.log'
        if os.name is 'nt':  # 如果是windows操作系统
            if not os.path.exists(logDir):
                os.mkdir(logDir)
        fh = TimedRotatingFileHandler(logFile, when='midnight')
        fh.setLevel(logLevel)
        fh.setFormatter(formatter)
        log.addHandler(fh)

    # 输出到控制台
    sh = StreamHandler()
    sh.setLevel(logLevel)
    sh.setFormatter(formatter)
    if console:
        log.addHandler(sh)
    return log


class Logger(object):
    def __init__(self, log):
        self._log = log

    def info(self, message):
        if self._log:
            self._log.info(message)


# 计算时间的装饰器
def countTime(log=None):
    def tmp(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            beginTime = time.time()
            result = func(*args, **kwargs)
            endTime = time.time()
            costTime = int(endTime * 1000 - beginTime * 1000)
            if log:
                log.info('%s called cost time : %sms' % (func.__name__, costTime))
            return result

        return wrapper

    return tmp


# 默认的日志
_log = initLog("default")
_consoleLog = initLog("console")

# 如果传入None就是取消日志打印
log = Logger(_log)
# 只在控制台输出的日志
consoleLog = Logger(_consoleLog)

if '__main__' == __name__:
    consoleLog.info("测试控制台输出")
    # log.info("测试")
    #
    #
    # @countTime(log)
    # def testCountTime():
    #     for i in range(100000):
    #         # print(i)
    #         pass
    #
    #
    # testCountTime()
