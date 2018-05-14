# -*- encoding:utf-8 -*-

import requests
from globalConstant.config import config


class ReptileRequest(object):
    def __init__(self, url, handler=None):
        self.checkUrl(url)
        self.url = url
        self.headers = {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT'}
        self.handler = handler
        pass

    # 添加其他的头部
    def addHeader(self, key=None, value=None):
        if not key:
            self.headers[key] = value
        return self

    # 发起get请求
    def get(self, params=None):
        response = requests.get(self.url, params, headers=self.headers, timeout=config.getTimeout())
        content = response.content
        if hasattr(self, '_callback'):
            self._callback(content)
        return content

    # 发起post请求
    def post(self, params=None, body=None):
        response = requests.post(self.url, params, body, headers=self.headers, timeout=config.getTimeout())
        return response.content

    # 检查url的合法性 需要打印日志
    def checkUrl(self, url):
        pass

    # 通过装饰器的方式添加处理器
    def wrapHandleCallback(self, handleCallback):
        self._callback = handleCallback

    pass


if '__main__' == __name__:
    request = ReptileRequest("https://www.baidu.com")


    @request.wrapHandleCallback
    def callBack(html):
        print("装饰得到的" + str(html))


    print(request.get())
