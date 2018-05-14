# -*- utf-8 -*-
# create by Administrator on 2018/5/14
# 调度器
from request.urlmanager import UrlManager
from request.downloader import HtmlDownloader
from parse.anjukeparser import anjukeparser

# 调度
class SpiderMan(object):
    def __init__(self):
        self.urlman = UrlManager()
        self.parser = None
        pass

    def setHtmlParser(self, parser):
        self.parser = parser

    def start(self, root_url):
        self.urlman.addNew(root_url)
        while self.urlman.hasNewUrl():
            url = self.urlman.getNewUrl()
            downloader = HtmlDownloader(url)
            htmlContent = downloader.get()
            if self.parser and htmlContent:
                self.parser.parse(url, htmlContent)

if '__main__' == __name__:
    man = SpiderMan()
    man.setHtmlParser(anjukeparser)
    man.start(r'https://www.baidu.com')