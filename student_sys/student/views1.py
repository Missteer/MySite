from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Student
from .form1 import StudentForm
# Create your views here.
def index(request):
    students = Student.get_all()
    #GET - 从指定的资源(例如服务器等，但不一定是服务器，也可能是数据库sql)请求数据。
    #POST - 向指定的资源(例如服务器)提交要被处理的数据
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(reverse('index'))
    else:
        form = StudentForm()

    context = {
            'students':students,
            'form':form,

        }
    return render(request,'student/index.html',context=context)