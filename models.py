from distutils.command.upload import upload
from enum import unique
from django.db import models

# Create your models here.


class Employee(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=30, unique=True)
    phone = models.CharField(max_length=15)
    img = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.first_name
