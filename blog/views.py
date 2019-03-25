# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse
from blog.models import Artikel
from about.models import About
from blog.form import FormTambahArtikel

# Create your views here.

def index(request):
    nama = 'Moch.Fauzan'
    buah = ['Apel','Jeruk','Tomat']
    return render(request, 'layout/index.html',{'nama':nama, 'buah':buah})

def about(request):
    abouts = About.objects.filter(publish=True)
    return render(request, 'layout/about.html', {'abouts':abouts})

def contact(request):
    return render(request, 'layout/contact.html')

def blog(request):
    #select * from Artikel where publish=true
    blogs = Artikel.objects.filter(publish=True)
    return render(request, 'layout/blog.html', {'blogs':blogs})

def tambah_artikel(request):
    form = FormTambahArtikel
    return render(request, 'layout/tambah_artikel.html', {'form':form})