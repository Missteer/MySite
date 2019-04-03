from django.shortcuts import render, redirect, reverse
from django.http.response import HttpResponse

# Create your views here.
from myadmin.models import Users
import time

#执行分页操作
def users(request,pIndex=1):
    # 获取会员信息
    list = Users.objects.filter()
    #判断并封装搜索条件
    #定义一个用于维持搜索条件的变量
    where = []
    if request.GET.get('name','') != '':
        list = list.filter(name__contains=request.GET.get('name'))
        where.append('name='+request.GET.get('name'))
    if request.GET.get('sex','') != '':
        list = list.filter(sex=request.GET['sex'])
        where.append('sex='+request.GET.get('sex'))
    # 传入数据和页大小来创建分页对象
    p = Paginator(list, 4)
    # 判断页号没有值时初始化为1
    if pIndex == '':
        pIndex = '1'
    pIndex = int(pIndex) #类型转换int
    list2 = p.page(pIndex) #获取当前页数据
    plist = p.page_range #获取页码信息
    #封装分页信息
    context = {'userslist':list2,'plist': plist, 'pIndex': pIndex,'where':where}
    return render(request,"myadmin/users/index.html",context)

#后台首页
def index(request):
    return render(request,'myadmin/index.html')

# ==============后台会员管理======================
# 浏览会员
def usersindex(request):
    # 执行数据查询，并放置到模板中
    list = Users.objects.all()
    context = {"userslist":list}
    return render(request,'myadmin/users/index.html',context)

# 会员信息添加表单
def usersadd(request):
    return render(request,'myadmin/users/add.html')

#执行会员信息添加
def usersinsert(request):
    try:
        ob = Users()
        ob.username = request.POST['username']
        ob.name = request.POST['name']

        #获取密码并md5
        # md5 的用法
        # 没有加盐
        import hashlib
        m = hashlib.md5()
        m.update(bytes(request.POST['password'],encoding="utf8"))
        ob.password = m.hexdigest()


        ob.gender = request.POST['sex']
        ob.address = request.POST['address']
        ob.state = 1
        ob.save()
        context = {'info':'添加成功！'}
    except:
        context = {'info':'添加失败！'}

    return render(request,"myadmin/info.html",context)

# 执行会员信息删除
def usersdel(request,uid):
    # 为什么用try
    # filter用法 的区别`
    try:
        ob = Users.objects.get(id=uid)
        ob.delete()
        context = {'info':'删除成功！'}
    except:
        context = {'info':'删除失败！'}
    return render(request,"myadmin/info.html",context)

# 打开会员信息编辑表单
def usersedit(request,uid):
    try:
        ob = Users.objects.get(id=uid)
        context = {'user':ob}
        return render(request,"myadmin/users/edit.html",context)
    except:
        context = {'info':'没有找到要修改的信息！'}
    return render(request,"myadmin/info.html",context)

# 执行会员信息编辑
def usersupdate(request,uid):
    try:
        ob = Users.objects.get(id=uid)
        ob.name = request.POST['name']
        ob.gender = request.POST['sex']
        ob.address = request.POST['address']
        ob.state = request.POST['state']
        ob.save()
        context = {'info':'修改成功！'}
    except:
        context = {'info':'修改失败！'}
    return render(request,"myadmin/info.html",context)



#后台管理员操作
# 会员登录表单
def login(request):
    return render(request,'myadmin/login.html')

# 会员执行登录
def dologin(request):
    # 校验验证码
    verifycode = request.session['verifycode']
    code = request.POST['code'].lower()
    if verifycode != code:
        context = {'info':'验证码错误！'}
        return render(request,"myadmin/login.html",context)
    try:
        #根据账号获取登录者信息
        user = Users.objects.get(username=request.POST['username'])
        #判断当前用户是否是后台管理员用户
        if user.state == 0:
            # 验证密码
            import hashlib
            m = hashlib.md5()
            m.update(bytes(request.POST['password'],encoding="utf8"))
            if user.password == m.hexdigest():
                # 此处登录成功，将当前登录信息放入到session中，并跳转页面
                request.session['adminuser'] = user.name
                #print(json.dumps(user))
                return redirect(reverse('myadmin_index'))
            else:
                context = {'info':'登录密码错误！'}
        else:
            context = {'info':'此用户非后台管理用户！'}
    except:
        context = {'info':'登录账号错误！'}
    return render(request,"myadmin/login.html",context)

# 会员退出
def logout(request):
    # 清除登录的session信息
    del request.session['adminuser']
    # 跳转登录页面（url地址改变）
    return redirect(reverse('myadmin_login'))
