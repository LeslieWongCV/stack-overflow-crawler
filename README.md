# Stack Overflow Crawler

<p align="center">
  <a href="https://stackoverflow.com/questions/tagged/android?tab=newest&page=50&pagesize=50">
    <img src='/imgs/Pasted Graphic 9.png' width="400"/>
  </a>
</p>




Powerful tool for collecting top 10 voted and 10 Newest featured Questions on Stack Overflow
Features:

 * Switch between the time window of 7 days and 1 month
 * Configurable pool size
 * Speed Contral
 * Rendering Web Page with Django

This is a task last for 48 hours.
Thanks to [Scrapy Docs](https://docs.scrapy.org/en/latest/) and [The Django Book](http://djangobook.py3k.cn/2.0/)

## Usage
NOTE: These instructions assume that you have Scrapy and Django installed.
go to the directory:

```sh
$ cd ~/Stack_Overflow_crawler-master/Scrapy_module
```
The easiest way to get started is using the init.py:

##step 1/2

```sh
$ python init.py
```
NOTE: This step will crawl the information on the website, sort them by time and number of comments, and then build a python dictionary for input to Django backend.



<p align="center">
  <a href="https://stackoverflow.com/questions/tagged/android?tab=newest&page=50&pagesize=50">
    <img src='/imgs/result1.png' width="250"/>
  </a>
</p>
Sorted data


##step 2/2

go the the directory:
```sh
$ cd ~/Stack_Overflow_crawler-master/django_st
```
and start the server:

```sh
$ python manage.py runserver 0.0.0.0:8000
```
go to http://0.0.0.0:8000/

##note

You are able to swtich between 7 days and 30 days

<p align="center">
  <a href="https://stackoverflow.com/questions/tagged/android?tab=newest&page=50&pagesize=50">
    <img src='/imgs/Pasted Graphic 11.png' width="600"/>
  </a>
</p>


##License
MIT
If you do find this script useful, a link back to this repository would be appreciated. Thanks!
## Basic usage
