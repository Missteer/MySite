from django.conf.urls import url
from . import views

from .views import index

app_name ='[studyapp]'
urlpatterns =[
    url(r'^$',views.index,name='index'),

    #显示所有主题
    url(r'^topics/$',views.topics,name='topics'),

    #显示特定主题的页面
    url(r'^topics/(?P<topic_id>\d+)/$',views.topic,name='topic'),

    #显示添加主题
    url(r'^topic_new/$',views.topic_new,name='topic_new'),

    #显示添加条目
    url(r'^add_entry/(?P<topic_id>\d+)/$',views.add_entry,name='add_entry'),

]