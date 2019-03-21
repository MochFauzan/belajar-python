# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from contact.models import Contact

# Create your views here.
def tampilkan_kontak(request):
    # select * from Contact
    contact = Contact.objects.all()
    return render(request, 'layout/contact.html', {'contact':contact})
