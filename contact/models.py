# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Contact(models.Model):
    email = models.CharField(max_length=30)
    twitter = models.CharField(max_length=30)
    github = models.CharField(max_length=30)
    no_hp = models.CharField(max_length=12)

    def __unicode__(self):
        return self.email