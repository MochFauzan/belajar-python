# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from about.models import About

# Create your views here.
def about(request):
    abouts = About.objects.filter(publish=True)
    return render(request, 'layout/about.html', {'abouts':abouts})