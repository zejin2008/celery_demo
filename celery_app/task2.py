#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/27 18:47
# @Author  : chenzejin
# @Site    : 
# @File    : task2.py
# @Software: PyCharm

import time
from celery_app import app

@app.task
def multiply(x, y):
    time.sleep(2)
    return x * y


