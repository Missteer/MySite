from django.db import models

# Create your models here.
class Room(models.Model):
    roomName = models.CharField(max_length=20)
    roomLoc = models.CharField(max_length=20)

class Student(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()

    def __str__(self):

        return self.name

class Teacher(models.Model):
    course = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    age = models.IntegerField()
