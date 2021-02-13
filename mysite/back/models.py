from django.db import models
import uuid

# Create your models here.
class Person(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    password = models.CharField(max_length=150)
    permission = models.BooleanField()
    phone = models.CharField(max_length=100)
