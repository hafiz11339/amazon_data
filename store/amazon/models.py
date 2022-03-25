from operator import mod
from re import M
from django.db import models


# Create your models here.
class amazon_data(models.Model):
    title = models.CharField(max_length=264)
    img = models.CharField(max_length=264)
    price = models.DecimalField(max_digits=10, decimal_places=3)
    link = models.CharField(max_length=150)
