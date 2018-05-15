# -*- encoding:utf-8 -*-
# create by Administrator on 2018/5/14
# 存储管理器

import abc



class StoreMan(object):
    # 全局的实例池子 根据不同的表格
    instance_pool = []

    def store(self, **kwargs):
        """存储一条数据"""
        pass


if '__main__' == __name__:
    pass
