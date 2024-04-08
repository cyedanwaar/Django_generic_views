from django.db import models

# Create your models here.


class Client(models.Model):
    projectname = models.CharField(max_length=255)
    solicitationnumber = models.IntegerField()
    taskauthnumber = models.IntegerField()
    
    name = models.CharField(max_length=255)
    phone = models.IntegerField()
    fax = models.IntegerField()
    email = models.EmailField()
    address = models.CharField(max_length=255)