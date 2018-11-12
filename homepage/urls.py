# -*- coding: utf-8 -*-
# @Author: ZhuZefeng
# @Date:   2018-11-09 10:42:41
# @Last Modified by:   ZhuZefeng
# @Last Modified time: 2018-11-09 11:12:54


"""
为应用程序lhomepage定义URL模式
"""

from django.urls import path
from .           import views

app_name = 'homepage'

urlpatterns = [
               #网站的主页
               path('',views.homepage, name='homepage'),
              ]