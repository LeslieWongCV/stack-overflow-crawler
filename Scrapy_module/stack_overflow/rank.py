# -*- coding: utf-8 -*-
# @Time    : 2020/3/11 11:22 PM
# @Author  : Yushuo Wang
# @FileName: rank.py
# @Software: PyCharm
# @Blog    ：https://lesliewongcv.github.io/

import json
import os

path = os.path.abspath(os.path.dirname(os.path.dirname(__file__))) + '/stack_of.json'
#path = "~/stack_overflow/stack_of.json"  # NOTE: Change the path to where .json~/Stack_Overflow_crawler-master/Scrapy_module/

"""

"""
class Question:
    """
"""
    def __init__(self,title,url,vote):
        self.title=title
        self.url=url
        self.vote=vote
    def __eq__(self,other):
        return self.vote==other.vote
    def __le__(self,other):
        return self.vote<other.vote
    def __gt__(self,other):
        return self.vote>other.vote



quesList=[]
print('path==',path)
with open(path) as f:

    pop_data=json.load(f)
    for pop_dict in pop_data:
        title=pop_dict['title']
        url=pop_dict['url']
        vote=pop_dict['vote']
        ques=Question(title,url,vote)
        quesList.append(ques)
            #quesList.sort()

dict_url = {}
dict_title = {}
dict_vote = {}
quesList_7 = quesList[:2500]

for i in range(10):
    dict_url['u%d'%(i+1)] = quesList_7[i].url
    dict_title['t%d'%(i+1)] = quesList_7[i].title

topList=[]
#toplist is an array of the top ten likes, which consumes space to store the current data.
#Sorting while reading will cause the list to be empty (I don’t know what is going on)
quesList_7.sort(reverse=True)

for ques in quesList:
    pass
  # print(ques.title+" "+ques.url+' '+ques.vote)

for i in range(10,20):
    dict_url['u%d'%(i+1)] = quesList_7[i-10].url
    dict_title['t%d'%(i+1)] = quesList_7[i-10].title
    dict_vote['v%d'%(i+1)] = quesList_7[i-10].vote
dict_context_7 = dict(dict_title,**dict_url,**dict_vote)

dict_url = {}
dict_title = {}
dict_vote = {}

quesList.sort(reverse=True)
#print(quesList_7[2499])
for ques in quesList:
    pass
  # print(ques.title+" "+ques.url+' '+ques.vote)

for i in range(10,20):
   dict_url['uh%d'%(i+1)] = quesList[i-10].url
   dict_title['th%d'%(i+1)] = quesList[i-10].title
   dict_vote['vh%d'%(i+1)] = quesList[i-10].vote

dict_context_20 = dict(dict_title,**dict_url,**dict_vote)
dict_context = dict(dict_context_7,**dict_context_20)
#f = open('dict_context7.txt','w')
#f.write(str(dict_context_7))
#f = open('dict_context20.txt','w')
#f.write(str(dict_context_20))
f = open('dict_context.txt','w')
f.write(str(dict_context))

f.close()







#topList = topList[:9]

#print(topList[0].title)
#print(type(topList[0]))

                            #keys_url = ('u1','u2','u3','u4','u5','u6','u7','u8','u9','u10','u11','u12','u13','u14','u15','u16','u17','u18','u19','u20')
#keys_title = ('t1','t2','t3','t4','t5','t6','t7','t8','t9','t10','t11','t12','t13','t14','t15','t16','t17','t18','t19','t20')