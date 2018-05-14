# -*- encoding:utf-8 -*-

import requests
from globalConstant.config import config

'''
html下载器
'''


class HtmlDownloader(object):
    def __init__(self, url):
        self.checkUrl(url)
        self.url = url
        self.headers = {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT'}
        pass

    # 添加其他的头部
    def addHeader(self, key=None, value=None):
        if not key:
            self.headers[key] = value
        return self

    # 发起get请求
    def get(self, params=None):
        response = requests.get(self.url, params, headers=self.headers, timeout=config.getTimeout())
        if response.status_code is 200:
            response.status_code = 'UTF-8'
            return response.content
        else:
            return None

    # 发起post请求
    def post(self, params=None, body=None):
        response = requests.post(self.url, params, body, headers=self.headers, timeout=config.getTimeout())
        if response.status_code is 200:
            response.encoding = "UTF-8"
            return response.content
        else:
            return None

    # 检查url的合法性 需要打印日志
    def checkUrl(self, url):
        pass


if '__main__' == __name__:
    request = HtmlDownloader("https://www.baidu.com")
    print(request.get())
