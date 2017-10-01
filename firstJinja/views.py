# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'personal/home.html')

def information(request):
    return render(request, 'personal/information.html', {'info': ['This is List Item 1','This is List Item 2','This is List Item 3']})
