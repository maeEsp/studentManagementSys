from django.db import models

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    course = models.CharField(max_length=4)
    gender = models.CharField(max_length=1)
    age = models.IntegerField()
