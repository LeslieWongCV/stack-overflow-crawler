# -*- coding: utf-8 -*-
# @Time    : 2020/3/12 7:33 PM
# @Author  : Yushuo Wang
# @FileName: start_crawling.py
# @Software: PyCharm
# @Blog    ：https://lesliewongcv.github.io/

import os
import subprocess
import json
import time


# Step1/2 get the data from Stack OverFlow.
subprocess.Popen('scrapy crawl stack_of -o stack_of.json',shell=True,cwd= '')
#os.popen('python /Users/leslie/django_st/manage.py runserver 8001')

time.sleep(14)
print('*'*200,'exit when process finished, ignore the "BrokenPipeError: [Errno 32] Broken pipe"','*'*200)
time.sleep(3)
exit()