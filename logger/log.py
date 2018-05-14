# -*- utf-8 -*-
# create by Administrator on 2018/5/14

import logging
import os
from logging.handlers import TimedRotatingFileHandler


def initLog(name, logFile=None, logLevel=logging.INFO):
    log = logging.getLogger(name)
    log.setLevel(logLevel)

    if logFile is None:
        logFile = './log/' + name

    if os.name is 'nt':  # 如果是windows操作系统
        if not os.path.exists(logFile):
            with open(logFile, 'w'):
                pass

    return log


defaultLog = initLog("default")
