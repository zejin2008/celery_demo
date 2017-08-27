#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/27 18:47
# @Author  : chenzejin
# @Site    : 
# @File    : client.py
# @Software: PyCharm


from celery_app import task1
from celery_app import task2
import time

ret1 = task1.add.apply_async(args=[2, 8])        # 也可用 task1.add.delay(2, 8)
ret2 = task2.multiply.apply_async(args=[3, 7])   # 也可用 task2.multiply.delay(3, 7)




print 'hello world'


while not ret1.ready():
    time.sleep(1)

while not ret2.ready():
    time.sleep(1)

print ret1.get()
print ret2.get()
