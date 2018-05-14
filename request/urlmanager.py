# -*- encoding:utf-8 -*-
# create by Administrator on 2018/5/14
# url管理器


class UrlManager(object):
    def __init__(self):
        self.new_urls = set()
        self.old_urls = set()

    def addNew(self, newurl):
        if newurl not in self.new_urls and newurl not in self.old_urls:
            self.new_urls.add(newurl)

    # 是否有新的待下载的url
    def hasNewUrl(self):
        return len(self.new_urls) > 0

    def getNewUrl(self):
        newUrl = self.new_urls.pop()
        if newUrl not in self.old_urls:
            self.old_urls.add(newUrl)
        return newUrl
