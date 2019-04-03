from django.shortcuts import render
# Create your views here.
from rest_framework import viewsets
from MySer.序列化器 import *
from rest_framework.views import APIView


class StudentVS(viewsets.ModelViewSet):
    serializer_class = StudentSer
    queryset = Student.objects.all()


class StudentAPIView(APIView):
    '''
    处理用户的get请求
    '''
    def get(self,request):
        print("In APIWiew get")
        #return None
        stus = Student.objects.all()
        ser = StudentSer(stus,many=True)

        return Response(data=ser.data)