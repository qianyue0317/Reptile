# -*- encoding:utf-8 -*-
# create by Administrator on 2018/6/22

from celery import Celery
from celery import platforms
import os

app = Celery('mycelery')

app.config_from_object('Distributed.celery_config')
# 在linux系统上用root运行 需要设置C_FORCE_ROOT为true
if os.name is not 'nt':
    platforms.C_FORCE_ROOT = True


@app.task
def test_task():
    print('任务执行')
