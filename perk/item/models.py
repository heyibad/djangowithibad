from django.db import models

# Create your models here.
# class Categorys(models.Model):
#     name=models.CharField(max_length=225)
class Category(models.Model):
    name=models.CharField(max_length=225)