# -*- encoding:utf-8 -*-
# create by qianyue on 2018/5/13
# 从代理网站抓取代理地址生成列表 代理模块
import requests
from bs4 import BeautifulSoup as BS
import time
from logger import logger


def get_ip_list(origin_page=1, page_count=1):
    """
    从提供ip代理的网站抓取代理ip
    :param origin_page:初始页码
    :param page_count: 要加载多少页
    :return:ip列表  e.g.['192.156.15.1']
    """
    page_temp = origin_page
    ip_list = []
    for i in range(page_count):
        page_temp += i
        try:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) \
                AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
            }
            response = requests.get(r'https://www.kuaidaili.com/free/inha/%s/' % page_temp, headers=headers)
            if response.status_code == 200:
                bs = BS(response.content, 'lxml')
                trs = bs.select(r'#list > table > tbody > tr')
                for tr in trs:
                    ip_list.append(tr.td.next_element)
        except Exception as e:
            logger.info(e)
        # 为防止503错误,间隔两秒请求
        time.sleep(2)
    return ip_list


if '__main__' == __name__:
    print(len(get_ip_list(page_count=5)))
