from django.shortcuts import render
from django.http import HttpResponse,Http404,HttpResponseRedirect
# Create your views here.
from rest_framework import viewsets

from hello.sezer1 import *

#from hello.serializer import *

from hello.models import Student

class StudentVS(viewsets.ModelViewSet):

    serializer_class = StudentSer
    queryset = Student.objects.all()