'''为应用程序users定义URL模式'''
from django.conf.urls import url
from django.contrib.auth import login
from django.contrib.auth.views import LoginView

from . import views
app_name = '[users]'
urlpatterns = [
    #登陆页面
    #url(r'^login/$',login,{'template_name':'users/login.html'},name='login'),
#登录界面  LoginView.as_view后面要加上()
    url(r'^login/$',LoginView.as_view(template_name='users/login.html'),name='login')


]