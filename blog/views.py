# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse
from.models import Artikel

# Create your views here.

def index(request):
    nama = 'Moch.Fauzan'
    buah = ['Apel','Jeruk','Tomat']
    return render(request, 'layout/index.html',{'nama':nama, 'buah':buah})

def about(request):
    return render(request, 'layout/about.html')

def contact(request):
    return render(request, 'layout/contact.html')

def blog(request):
    blogs = Artikel.objects.all()
    return render(request, 'layout/blog.html', {'blogs':blogs})