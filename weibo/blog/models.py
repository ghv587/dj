#coding=utf-8

from __future__ import unicode_literals

from django.db import models

# Create your models here.

#user (yonghu)
class User(models.Model):
    username = models.CharField(max_length=30, verbose_name="yonghu")

    class Meta:
        verbose_name = "yonghu"
        verbose_name_plural = verbose_name


