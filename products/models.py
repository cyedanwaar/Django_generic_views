from django.db import models

# Create your models here.

class Product(models.Model):
    slug = models.SlugField(unique=True)
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    