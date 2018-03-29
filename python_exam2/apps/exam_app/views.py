# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

def index(request):

    context = {

    }

    return render(request, 'exam_app/index.html', context)

def logout(request):
    request.session.clear()

    return redirect('/')

# Create your views here.
