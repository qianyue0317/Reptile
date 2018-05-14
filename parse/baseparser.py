# -*- encoding:utf-8 -*-
# create by qianyue on 2018/5/13
# 结果处理器的

import abc


class HtmlParser(object):
    def __init__(self):
        pass

    # 解析 抽象方法 子类需实现
    @abc.abstractmethod
    def parse(self, url, htmlcontent):
        pass
