from django.db import models

# Create your models here.

class List(models.Model):
    name = models.CharField(max_length=64)
    slug = models.SlugField(max_length=64)

class Thing(models.Model):
    my_list = models.ForeignKey(List)
    name = models.CharField(max_length=64)
    slug = models.SlugField(max_length=64)
    done = models.BooleanField()

