from rest_framework import serializers

from MySer.models import *

#序列化器
class StudentSer(serializers.ModelSerializer):
    #学生的序列化器

    class Meta:

        model = Student
        #fields = ['name','age','score']
        fields = '__all__'

        name = serializers.CharField(label="姓名",max_length=20)

        age = serializers.IntegerField(label="年龄")

        score = serializers.IntegerField(label="分数")