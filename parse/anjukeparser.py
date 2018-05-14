# -*- utf-8 -*-
# create by Administrator on 2018/5/14
from parse.baseparser import HtmlParser


# 安居客html解析器
class Anjukeparser(HtmlParser):
    # 解析之后需要将html中新的url数组返回
    def parse(self, url, htmlcontent):
        # todo 需要写具体的实现
        print(htmlcontent)
        return []


anjukeparser = Anjukeparser()
