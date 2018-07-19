# -*- encoding:utf-8 -*-
# create by Administrator on 2018/6/25

from celery.schedules import crontab
from kombu import Queue
from kombu import Exchange


# redis作为消息代理
BROKER_URL = 'redis://123456@182.61.34.169:6379/0'

# rabbitmq作为消息代理
# BROKER_URL = r'amqp://%s:%s@%s:%s/' % (conf.c_rbmq_celery_user, conf.c_rbmq_celery_passwd, conf.c_rbmq_celery_host, conf.c_rbmq_celery_port)

# 把任务结果存在Redis
CELERY_RESULT_BACKEND = 'redis://123456@182.61.34.169:6379/1'

# 引入任务列表
CELERY_IMPORTS = ('Distributed.tasks',)

# celery worker的并发数 也是命令行-c指定的数目,事实上实践发现并不是worker也多越好,保证任务不堆积,加上一定新增任务的预留就可以
CELERYD_CONCURRENCY = 5

default_exchange = Exchange('tasks', 'topic')

# 定义任务队列
CELERY_QUEUES = (
    Queue('default', default_exchange, routing_key='task.#'),  # 路由键以 'task.'开头的消息都进入default队列
    Queue('spider', default_exchange, routing_key='spider.#'),  # 路由键以 'spider.'开头的消息都进入spider_tasks队列
)
CELERY_DEFAULT_QUEUE = 'default'  # 默认的队列
CELERY_TASK_SERIALIZER = 'json'  # 传递参数序列化方式
CELERY_RESULT_SERIALIZER = 'json'  # 任务执行结果序列化方式
CELERY_DEFAULT_EXCHANGE = 'tasks'  # 默认的交换机名字为 tasks
CELERY_DEFAULT_ROUTING_KEY = 'task.default'  # 默认的路由键为default,符合上边的default队列

# 限制执行频率
CELERY_ANNOTATIONS = {
    # 'celeryContainer.tasks.helloCelery': {'rate_limit': '1/m'},
    # 'celeryContainer.mycelery.helloInCeleryFile': {'rate_limit': '1/m'}
}

# 路由
CELERY_ROUTES = {
    'celeryContainer.tasks.read_email_task': {
        'queue': 'email_tasks',
        'routing_key': 'email.read_send'
    }
}

# 定时任务
CELERYBEAT_SCHEDULE = {
    # 发送邮件任务
    'send_email': {
        'task': 'celeryContainer.tasks.read_email_task',
        'schedule': 10,
    }
}

# 时区设置
CELERY_TIMEZONE = 'Asia/Shanghai'
