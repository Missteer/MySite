"""Typeidea URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path
from .custom_site import custom_site,CustomSite
from django.conf.urls import url

from blog.views import post_list,post_detail
from config.views import links


urlpatterns = [
    path('super_admin/', admin.site.urls),

    url(r'^$',post_list),
    url(r'^category/(?P<category_id>\d+)/$',post_list),
    url(r'^tag/(?P<tag_id>\d+)/$',post_list),
    url(r'^post/(?P<post_id>\d+).html$',post_detail),
    url(r'^links/$',links),
    url(r'^super_admin/',admin.site.urls),
    url(r'^admin/',custom_site.urls),

]
'''
我们可以将 URL 的定义理解为是一个路径（正则字符串）对应一个函数的映射，
比如 url(r ' "$ ' , post_list ）意味着如果用户访问博客首页，
就把请求传递到 post_list 这个函 数中
'''