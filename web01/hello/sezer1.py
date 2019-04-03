from rest_framework import serializers

from hello.models import *
#序列化器
class StudentSer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'