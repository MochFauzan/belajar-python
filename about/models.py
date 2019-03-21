# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class About(models.Model):
    nama = models.CharField(max_length=50)
    biodata = models.CharField(max_length=100)
    publish = models.BooleanField(default=True)

    def __unicode__(self):
        return self.nama
