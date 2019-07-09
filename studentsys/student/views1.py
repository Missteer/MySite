from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Student
from .forms import studentForm
# Create your views here.
def index(request):
    students = Student.objects.all()
    if request.method == 'POST':
        form = studentForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            student = Student()
            student.name = cleaned_data['name']
            student.sex = cleaned_data['sex']
            student.email = cleaned_data['email']
            student.profession = cleaned_data['profession']
            student.qq = cleaned_data['qq']
            student.phone = cleaned_data['phone']
            student.save()
            return HttpResponseRedirect(reverse('index'))
    else:
        form = studentForm()

    context = {
            'students':students,
            'form':form,

        }
    return render(request,'student/index.html',context=context)