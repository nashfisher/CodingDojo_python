# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

def index(request):
    if request.session.get('submissions') is None:
       request.session['submissions'] = 0
    return render(request, 'index.html')

def process(request):
    if request.method == 'POST':
        
        context = {
            'name' : request.POST['name'],
            'location' : request.POST['location'],
            'language' : request.POST['language'],
            'comment' : request.POST['comment']
        }
        request.session['data'] = context
        print context
        request.session['submissions'] += 1
    if len(request.POST['name']) == 0:
        return redirect('/')

    return redirect('/result')


def result(request):
    context = request.session['data']
    return render(request, 'result.html', context)
# Create your views here.
