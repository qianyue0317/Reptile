# -*- encoding:utf-8 -*-
# create by Administrator on 2018/6/25
from functools import wraps

"""
 装饰器
"""


def eval_now(func):
    """
    立即执行
    :param func:
    :return:
    """
    return func()


def repeat(count):
    """
    重复执行指定函数的装饰器
    :param count:
    :return:
    """
    def wrapper1(func):
        @wraps(func)
        def wrapper2(*args, **kwargs):
            for i in range(count):
                func(args, kwargs)

        return wrapper2

    return wrapper1
