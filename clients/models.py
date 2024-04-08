from django.db import models

# Create your models here.


class Client(models.Model):
    name = models.CharField(max_length=255)
    phone = models.IntegerField()
    fax = models.IntegerField()
    email = models.EmailField()
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.name