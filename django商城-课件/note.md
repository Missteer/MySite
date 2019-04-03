#  Django商城- B2c商城
- django
- drf
- 前端页面技术
- 模仿小米商城

# 软件工程
- 软件工程：工程化方法解决软件问题

# 操作步骤
# 1. 需求分析
- 前台: 给基础用户使用的页面
- 后台：给操作者/admin等使用的页面系统
- 不是服务器前后台概念

- 小米前台
    - 商品展示
        - 商品详情
        - 商品分类
        - 商品图片
    - 广告位
    - 消息设置
    - 商品评论
    - 购物车
        - 显示定价
        - 商品列表
        - 商品的链接
        - 购物车内商品修改数量，删除
    - 订单
        - 显示价格
        - 商品列表
        - 商品详情链接
    - 结算系统
    - 用户注册
        - 注册表单
        - 防止机器人图片
    - 用户状态
        - 用户信息显示
        - 用户信息修改
        
- 小米后台
    - 前台各种信息对应的管理页面
    - 控制页面，比如权限等
   
# 2. 确定相应模块
- 根据逻辑或者业务，将需求进行相应归类
- 根据业务： 比如新闻类，商品类，用户管理，订单系统
- 根据逻辑：前台，后台
- 根据现状：有些模块可能已经有，直接复用
- 本系统采用前后台模块
- 一个app负责前台，一个app负责后台
 
# 3. 确定数据库信息
- 找出对应名词,对应成数据库表格
- 确定相互之间的关系
- 需要的表可能有： 用户，商品，订单，新闻


# 4. 确定后的程序结构大致如图所示
- 代码结构

        
         /TulingXueyuan/
        ├── manage.py
        ├── myobject
        │   ├── __init__.py
        │   ├── settings.py
        │   ├── urls.py
        │   └── wsgi.py
        ├── myadmin 
        │   ├── admin.py
        │   ├── apps.py
        │   ├── __init__.py
        │   ├── migrations
        │   │   └── __init__.py
        │   ├── models.py
        │   ├── tests.py
        │   ├── urls.py
        │   └── views.py 后台管理视图
        │   └── viewsgoods.py 商品管理视图
        │   └── viewsorders.py 订单管理视图
        └── myweb  
        │    ├── admin.py
        │    ├── apps.py
        │    ├── __init__.py
        │    ├── migrations
        │    │   └── __init__.py
        │    ├── models.py
        │    ├── tests.py
        │    ├── urls.py
        │    └── views.py 网站首页，商品列表与详情
        │    └── viewsusers.py 会员相关操作视图
        │    └── viewsorders.py 购物车和订单处理视图
        |
        ├── templates 模板目录
        |    |--myadmin 后台模板总目录
        |    |    |--users/ 后台会员管理
        |    |    |    |--index.html         
        |    |    |    |--add.html         
        |    |    |    |--edit.html         
        |    |    |    |--repass.html         
        |    |    |--type/ 后台类别管理模板
        |    |    |    |--index.html         
        |    |    |    |--add.html         
        |    |    |    |--edit.html         
        |    |    |--goods/ 商品信息管理模板
        |    |    |    |--index.html         
        |    |    |    |--add.html         
        |    |    |    |--edit.html          
        |    |    |--orders/ 订单信息管理模板
        |    |    |    |--index.html                 
        |    |    |    |--edit.html         
        |    |    |--index.html
        |    |    |--login.html
        |    |    |--base.html
        |    |
        |    |--myweb 前台模板目录
        |
        ├── static 静态资源目录
        |    |--myadmin 后台静态资源 
        |    |    |--
        |    |    |--
        |    |
        |    |
        |    |--myweb 网站前台静态资源
        |    |    |--
        |    |    |--
        
# 5. 操作步骤
## 5.1  创建环境
    
        conda create -n beijing_tuling python=3.6
        activate beijing_tuling
        pip install django=1.11.18
        
## 5.2 创建空系统并测试
- 创建空系统
    
        django-admin startproject bjtlxy 
        //(bjtlxy=北京图灵学院的缩写)
- 配置系统
     1. 创建相应文件和文件夹

            //创建两个app：myweb，myadmin
            python manage.py startapp  myadmin
            python manage.py startapp  myweb
            //创建模板和静态文件文件夹，并分别为每个app创建相应
            //的子文件夹
            mkdir templates
            cd templates
            mkdir myweb
            mkdir myadmin
            
            mkdir static
            cd static
            mkdir myweb
            mkdir myadmin
        
     2. 拷贝子路由文件
     
            # 拷贝bjtlxy/urls.py 到 myadmin和myweb 文件夹下
            # 本操作可以手动操作，也可以再pycharm右边浏览器直接复制粘贴
            # 也可以使用命令行cp命令
            cp bjtlxy/urls.py myadmin/urls.py
            
     3. 配置pycharm环境
     
     
        # pycharm进行配置环境
        # 需要根据不同系统进行操作
        # windows的anaconda不太好找
        # win：可能再用户文件夹的隐藏文件夹下
        # linux：相应的安装目录下
        
        # File-settings-project xxx-porject interpr....-add - conda...
     
   ![pic1](.\pic\111.png) 
    4.  配置项目运行环境 - manage.py 
   ![pic2](.\pic\222.png)
    5. settings 设置
   - 导入myweb，myadmin
   
   
    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'myweb',
        'myadmin',
    ]
    6. 再主路由./bjtlxy/urls.py 中 导入子路由urls
        
            from django.conf.urls import url, include
            from django.contrib import admin

            urlpatterns = [
                url(r'^admin/', admin.site.urls),
                url(r'^myweb/', include('myweb.urls')),
                url(r'^myadmin/', include('myadmin.urls')),
                url(r'^', include('myweb.urls')),
    7. myweb/urls.py 和 myadmin/urls.py 中分别设置
    
        from django.conf.urls import url, include
        from django.contrib import admin

        from .views import t

        urlpatterns = [
            url(r'^', t),
        ]
            
    8. myweb/views.py 和 myadmin/views.py中分别设置返回测试函数
            
        from django.shortcuts import render
        from django.http.response import HttpResponse

        # Create your views here.


        def t(request):
            return HttpResponse("Hello world")
            
    9. 测试模板系统
        1. 在模板文件夹下的myweb添加模板test.html
        2. test.html是一个完整的html页面
                
                <!DOCTYPE html>
                <html lang="en">
                <head>
                    <meta charset="UTF-8">
                    <title>Title</title>
                </head>
                <body>
                <h1>你好，北京图灵学院！！！</h1>
                </body>
                </html>
                
        3. myweb/views下编写返回函数 t2
        
            # Create your views here.
            from django.http.response import HttpResponse
            from django.shortcuts import render_to_response

            # Create your views here.


            def t2(reqest):
                return render_to_response("./myweb/test.html")

            def t(request):
                return HttpResponse("Hello world")
                    
        4. 配置settings.TEMPLATES.DIRS
        
                TEMPLATES = [
                    {
                        'BACKEND': 'django.template.backends.django.DjangoTemplates',
                        'DIRS': [os.path.join(BASE_DIR, "templates")],
                        'APP_DIRS': True,
                        'OPTIONS': {
                            'context_processors': [
                                'django.template.context_processors.debug',
                                'django.template.context_processors.request',
                                'django.contrib.auth.context_processors.auth',
                                'django.contrib.messages.context_processors.messages',
                            ],
                        },
                    },
                ]
        5. myweb/urls配置更改
        
                    from django.conf.urls import url, include
                    from django.contrib import admin

                    from .views import *

                    urlpatterns = [
                        url(r'^/', t),
                        url(r'^t2/', t2),
                    ]
                            
            
            
        
- 测试系统
    - 空项目主页应该显示成功页面
     ![pic3](.\pic\33.png)
    - 设置子路由后，确定app功能正常
        -  访问 127.0.0.1:7852 应该显示 “Hello world"
        -  访问 127.0.0.1:7852/myweb/ 应该显示 “Hello world"
        -  访问 127.0.0.1:7852/myadmin/ 应该显示 “Hello world"
    - 测试模板
        - 访问 /myweb/t2/应该能返回测试页面

#5.3  用户系统
- 大致过程
    - 确定数据库表
    - 确定对数据库表的操作
    - 确定路由和对应试图内容
    - 编写视图实现
    - 确定相应界面
    - 测试
    
# 5.3.1 确定用户表
- myadmin/models文件编辑
- 代码如下

        class Users(models.Model):
            username = models.CharField(max_length=32)
            name = models.CharField(max_length=16)
            password = models.CharField(max_length=32)
            gender = models.IntegerField(default=1)
            address = models.CharField(max_length=255)
            phone = models.CharField(max_length=16)
            email = models.CharField(max_length=50)
            state = models.IntegerField(default=1)
            # 需要留意 auto_now, auto_now_add的区别
            # http://blog.sina.com.cn/s/blog_9e2e84050101iltd.html
            update_time = models.DateTimeField(auto_created=True, auto_now=True)
            create_time = models.DateTimeField(auto_created=True, auto_now_add=True)

            class Meta:
                db_table = "tlxy_users"  # 更改表名

# 5.3.2 确定数据库表的操作
- 增删改查，作为后台必须的
- 用户注册需不需要？？？如果需要，属于前台还是后台
        
# 5.3.3 确定路由和试图内容
- 见路由文件
- 原则：
    - 返回网页一个路由
    - 网页提交内容一个路由，由post中的action确定
# 5.3.4 实现试图
- 信息摘要md5
# 5.3.5 模板实现     
- 拷贝相应模板

# 5.3.6 测试
- 数据库迁移
     ![pic3](.\pic\121212.png)
- 对照url表逐个测试