"""django_st URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path
#from django_st.views import hello, current_datetime_03, hours_ahead
from django_st.views import  Seven_days, Thirty_days



urlpatterns = [
    path('admin/', admin.site.urls),
  #  path('hello/', hello, name='home'),
    path('', Seven_days, name='7'),
   # re_path(r'time/plus/(\d{1,2})/', hours_ahead, name='plus'),
    path('30/',Thirty_days, name='20'),
]

