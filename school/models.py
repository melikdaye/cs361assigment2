
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class teacher(models.Model):
    first_name=models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    office_details = models.TextField()
    phone = models.IntegerField()
    email = models.EmailField()

    def __str__(self):
        return self.first_name +' '+ self.last_name

class student(models.Model):
    first_name=models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    course=models.ManyToManyField('course')

    def __str__(self):
        return self.first_name +' '+ self.last_name

class course(models.Model):
    course_name=models.CharField(max_length=50)
    code=models.CharField(max_length=30)
    classroom=models.CharField(max_length=30)
    time=models.TimeField()
    teacher=models.OneToOneField(teacher)
    def __str__(self):
        return  self.code +' '+self.course_name


