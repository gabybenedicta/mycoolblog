from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

import datetime

from django.db import models
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length=100)
    created_at= models.DateTimeField(timezone.now())
    class Meta:
        verbose_name_plural = 'Categories'
    def __str__(self):
        return self.name

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.CharField(max_length=1000)
    likes =models.IntegerField(default = 0)
    def __str__(self):
        return self.title  

class Comment(models.Model):
    user =models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.CharField(max_length=1000)
    ishidden= models.BooleanField(default = False)
    def __str__(self):
        return self.content

    