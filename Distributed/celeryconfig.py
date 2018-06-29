# -*- encoding:utf-8 -*-
# create by Administrator on 2018/6/25

# redis作为消息代理
BROKER_URL = 'redis://localhost:6379/2'

# 引入任务列表
CELERY_IMPORTS = ('Distributed.tasks',)

# 把任务结果存在Redis
CELERY_RESULT_BACKEND = 'redis://localhost:6379/3'

# celery worker的并发数 也是命令行-c指定的数目,事实上实践发现并不是worker也多越好,保证任务不堆积,加上一定新增任务的预留就可以
CELERYD_CONCURRENCY = 20

# 定义任务队列
CELERY_QUEUES = (
)

# 任务执行频率
CELERY_ANNOTATIONS = {
}

# 周期任务
CELERYBEAT_SCHEDULE = {
}

# 任务路由
CELERY_ROUTES = {

}

CELERY_TIMEZONE = 'Asia/Shanghai'
