# coding=utf-8
from __future__ import unicode_literals

from django.db import models


class Server(models.Model):
    name = models.CharField(max_length=30)
    token = models.CharField(max_length=30)
    vnc_password = models.CharField(max_length=30)
    