# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Contact(models.Model):
    email = models.CharField(max_length=30)
    twitter = models.CharField(max_length=30, null=True) # Jika twitter boleh tidak di isi 
    github = models.CharField(max_length=30)
    no_hp = models.CharField(max_length=12)
    publish = models.BooleanField(default=True)

    def __unicode__(self):
        return self.email