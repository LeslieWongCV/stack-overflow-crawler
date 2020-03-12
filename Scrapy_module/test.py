# -*- coding: utf-8 -*-
# @Time    : 2020/3/11 9:48 AM
# @Author  : Yushuo Wang
# @FileName: test.py
# @Software: PyCharm
# @Blog    ：https://lesliewongcv.github.io/
# -*- coding: utf-8 -*-
# @Time    : 2020/3/11 3:14 AM
# @Author  : Yushuo Wang
# @FileName: test.py
# @Software: PyCharm
# @Blog    ：https://lesliewongcv.github.io/

import scrapy
url =  str('<a '
        'href="/questions/60622156/how-can-i-parse-the-value-to-previous-activity-by-using-back-icon-on-action-bar" '
        'class="question-hyperlink">How can I parse the value to previous '
        'activity by using back icon on action bar (android studio)</a>')

url = url.split('"',2)[1]
url = 'https://stackoverflow.com'+ url
#url = url.split('')[0].split('"')[0]

print(url)
next = '<a href="/questions/tagged/android?tab=newest&amp;page=2" rel="next" title="go to page 2"><span class="page-numbers next"> next</span></a>'

next = next.split('"', 2)[1]
next = 'https://stackoverflow.com'+ next
print(next)

######

page_link=set() #保存下一页页面url

content_link=set() #保存页面内所有可获得的url

#rules={'page':LinkExtractor(allow=(r'^http://www.bjnews.com.cn/\w+/2016/\d{2}/\d{2}/\d{6}.html))}

#start_urls={'http://www.bjnews.com.cn/news/list-43-page-1.html'}


#
# for i in range(5):
#         print(i)
#
# beforeurl = response.url
# pat1 = r"page = (\d)"
# page = re.search(pat1, beforeurl).group(1)
# page = int(page) + 1  # 获取下一页请求的page信息

h = '<span class="vote-count-post "><strong>0</strong></span>'

h = h.split('strong>',2)[1].split('<')[0]


print(h)


import django

#print(django.get_version())    html = t.render(Context({'current_date': now}))


import datetime
time = datetime.datetime.now()
print(time)
#time_dict = {time}
#print=(time_dict)
#print(type(time_dict))

print(locals())

from django.conf import settings

#settings.configure()
#from django.db import connection
#cursor = connection.cursor()



import os
os.openpty()
dict_url = {}
list1 = [1,2,3,4,5,6,7,8,9,0]
for i in range(0,10):
    dict_url['u%d'%(i+1)] =  list1[i]
print(dict_url)