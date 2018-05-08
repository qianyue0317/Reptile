# -*- encoding:utf-8 -*-

# 数据库相关
import pymysql

import time
import functools

# 使用装饰器绑定回调函数
class Test():

    # /**feature将调用callback(), 但是在Test中并没有真正的定义callback**/
    def feature(self):
        self.callback()

    def decorate(self, func):
        self.callback = func
        return func


test = Test()

# /**将foo注册为回调函数*//
@test.decorate
def foo():
    print 'in foo()'



# /**调用feature将触发回调函数**/
test.feature()