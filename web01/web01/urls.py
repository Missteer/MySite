"""web01 URL Configuration

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
from django.conf.urls import url,include
#导入视图
#from web01.hello import views
#from web01.hello import views
#from web01.miss import views
from hello import views as v



#导入路由
from rest_framework import routers

router = routers.SimpleRouter()

router.register(r'student',v.StudentVS)
urlpatterns = [
    path('admin/', admin.site.urls),
    #需要把drf路由当作子路由，配置好
    url(r'^api/',include(router.urls))
]