from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Blog(models.Model):
    author = models.ForeignKey(User)
    title = models.CharField(max_length=80, unique=True)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    author = models.ForeignKey(User)
    blog = models.ForeignKey(Blog)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
