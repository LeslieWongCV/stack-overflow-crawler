# -*- coding: utf-8 -*-
# @Time    : 2020/3/11 5:34 PM
# @Author  : Yushuo Wang
# @FileName: views.py
# @Software: PyCharm
# @Blog    ：https://lesliewongcv.github.io/

from django.http import HttpResponse, Http404
import datetime
from django.template.loader import get_template
from django.shortcuts import render


def Seven_days(request):

    f = open('/Users/leslie/python_coding/stackoverflow_wong/stack_overflow/dict_context.txt', 'r')
    # change to '~/Stack_Overflow_crawler-master/Scrapy_module/stack_overflow/dict_context.txt '
    a = f.read()
    dict_context = eval(a)
    f.close()
    time = datetime.datetime.now()
    dict_context['time'] = time
    return render(request,'base.html',dict_context )

def Thirty_days(request):
    f = open('/Users/leslie/python_coding/stackoverflow_wong/stack_overflow/dict_context.txt', 'r')
    # change to '~/Stack_Overflow_crawler-master/Scrapy_module/stack_overflow/dict_context.txt '
    a = f.read()
    dict_context = eval(a)
    f.close()
    time = datetime.datetime.now()
    dict_context['time'] = time
    return render(request,'base_20.html',dict_context )


   # return render(request, 'myapp/index.html', { 'foo': 'bar',  }, content_type='application/xhtml+xml')
