#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/27 18:47
# @Author  : chenzejin
# @Site    : 
# @File    : celeryconfig.py
# @Software: PyCharm




from datetime import timedelta
from celery.schedules import crontab

# Broker and Backend
BROKER_URL = 'redis://192.168.1.71:6379/0'               # 指定 Broker
CELERY_RESULT_BACKEND = 'redis://192.168.1.71:6379/1'  # 指定 Backend

# Timezone
CELERY_TIMEZONE='Asia/Shanghai'    # 指定时区，不指定默认为 'UTC'
# CELERY_TIMEZONE='UTC'

# import
CELERY_IMPORTS = (
    'celery_app.task1',
    'celery_app.task2'
)

# schedules
CELERYBEAT_SCHEDULE = {
    'add-every-30-seconds': {
         'task': 'celery_app.task1.add',
         'schedule': timedelta(seconds=30),       # 每 30 秒执行一次
         'args': (5, 8)                           # 任务函数参数
    },
    'multiply-at-some-time': {
        'task': 'celery_app.task2.multiply',
        'schedule': crontab(hour=19, minute=07),   # 每天早上 9 点 50 分执行一次
        'args': (3, 7)                            # 任务函数参数
    }
}
