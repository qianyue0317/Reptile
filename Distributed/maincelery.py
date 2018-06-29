# -*- encoding:utf-8 -*-
# create by Administrator on 2018/6/22

from celery import Celery

app = Celery('mycelery')

app.config_from_object('Reptile.Distributed.celeryconfig')


@app.task
def test_task():
    print('任务执行')
