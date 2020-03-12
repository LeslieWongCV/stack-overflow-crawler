# -*- coding: utf-8 -*-
# @Time    : 2020/3/11 1:07 AM
# @Author  : Yushuo Wang
# @FileName: stk_spider.py
# @Software: PyCharm
# @Blog    ：https://lesliewongcv.github.io/

import scrapy
from stack_overflow.items import StackOverflowItem
import os
import time
import subprocess
class DmozSpider(scrapy.Spider):
    name = "stack_of"
    allowed_domains = ["stackoverflow.com"]
    start_urls = [
        "https://stackoverflow.com/questions/tagged/android?tab=newest&page=1&pagesize=50"
      #  "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
    ]
    Dm = 0
    #page = 10
    def parse(self, response):
        item = StackOverflowItem()
        response.xpath('/html/body/div[4]/div[2]/div[1]/div[6]/a[6]').extract()
        info = response.css('.question-summary')
        for a in info:
            title = a.css('.question-hyperlink::text').extract_first()
            vote = a.css('.vote-count-post').extract_first()
            vote = vote.split('strong>', 2)[1].split('<')[0]
            des = a.css('.excerpt::text').extract_first()
            url = a.css('a[href*="/questions/"]').extract_first()
            url = url.split('"', 2)[1]
            url = 'https://stackoverflow.com' + url
            item['title'] = title
            item['url'] = url
            item['vote'] = vote
           # item['des'] = des  not for now
            yield item
        for count in range (10):
            page = count +2
           # time.sleep(random.randint(0, 1))
            next_url = 'https://stackoverflow.com/questions/tagged/android?tab=newest&page='+str(page)+'&pagesize=50'

            yield scrapy.Request(url = next_url,callback=self.parse)
        DmozSpider.Dm += 1
        #print('Dm=',DmozSpider.Dm)
        print('Dm=',DmozSpider.Dm)
        if DmozSpider.Dm == 11 :
            time.sleep(1)
            #subprocess.Popen('python /Users/leslie/python_coding/stackoverflow_wong/stack_overflow/stack_overflow/rank.py',shell=True, cwd= '/Users/leslie/python_coding/stackoverflow_wong/stack_overflow')
            print('Path222=',os.getcwd())
            os.popen('python /Users/leslie/python_coding/stackoverflow_wong/stack_overflow/stack_overflow/rank.py')
            #time.sleep(1)
       #     print("Opening Server...")
      #      DmozSpider.Dm += 1

            #subprocess.Popen('exit',shell=True)
            #subprocess.Popen('exit', shell=True)
     #   print('Dm=',DmozSpider.Dm)
      #  if DmozSpider.Dm == DmozSpider.page+2 :
       #     subprocess.Popen('python /Users/leslie/django_st/manage.py runserver 8001',
        #               shell=True)
        #os.popen('python /Users/leslie/django_st/manage.py')







            #print('*' * 40, 'Ready to launch the Web', '*' * 40)
            #rank_on = rank.rank()
        #if count == 28 or count==58 or count == 88 or count == 118 or count == 148:
        #    time.sleep(5)
        #     count += 1
        # if count == 149:
        #     rank_on = rank.main()
        #     print('*'*40, 'Ready to launch the Web','*'*40)


'''

        for count in range(28):
            # if count ==
            page = count + 2
            # time.sleep(random.randint(0, 1))
            next_url = 'https://stackoverflow.com/questions/tagged/android?tab=newest&page=' + str(page) + '&pagesize=50'
            # count += 1
            yield scrapy.Request(url=next_url, callback=self.parse)
            if count == 28:
                time.sleep(5)
            count += 1

'''

'''
        for count in range(28,58):
            page = count +2

            next_url = 'https://stackoverflow.com/questions/tagged/android?tab=newest&page='+str(page)+'&pagesize=50'

            yield scrapy.Request(url = next_url,callback=self.parse)

'''
        # if count == 58:
        #     time.sleep(5)
        #     count += 1

        # for count in range(58,88):
        #     page = count +2
        #
        #     next_url = 'https://stackoverflow.com/questions/tagged/android?tab=newest&page='+str(page)+'&pagesize=50'
        #
        #     yield scrapy.Request(url = next_url,callback=self.parse)
        #
        # if count == 88:
        #     time.sleep(5)
        #     count += 1
        #
        # for count in range(88,118):
        #     page = count +2
        #
        #     next_url = 'https://stackoverflow.com/questions/tagged/android?tab=newest&page='+str(page)+'&pagesize=50'
        #
        #     yield scrapy.Request(url = next_url,callback=self.parse)


        # beforeurl = response.url
        # pat1 = r"page=(\d)"
        # page = re.search(pat1, beforeurl).group(1)

        # page = int(page) + 1  # 获取下一页请求的page信息

           # i = i+1

            #page = int(page) + 1
            #  for i in range(5):
       # next = response.xpath('/html/body/div[4]/div[2]/div[1]/div[6]/a[6]').extract_first() #           // *[ @ id = "mainbar"] / div[6] / a[6]
      #  next = str(next)
        #next = next.split('"', 2)[1]

         #   next_url = response.urljoin(next)

        #next_url = 'https://stackoverflow.com' + next

