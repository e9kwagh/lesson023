from django.db import models

# Create your models here.
from django.db import models

class Teacher(models.Model):

    name = models.CharField(max_length=200)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    gameid = models.PositiveIntegerField(unique=True)
    email = models.EmailField(unique=True, null=True)
    dob =models.DateField()
    platform = models.CharField(max_length = 200)

    def _str__(self):
     return self.name



class Student(models.Model):
    name = models.CharField(max_length=200)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    gameid = models.PositiveIntegerField(unique=True)
    email = models.EmailField(unique=True, null=True)
    dob =models.DateField()
    platform = models.CharField(max_length = 200)


    def _str__(self):
        return self.name


