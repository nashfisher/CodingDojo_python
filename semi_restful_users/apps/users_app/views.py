# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from .models import Users

def index(request):
    print 'made it to index'
    context = {
        'Users' : Users.objects.all()
    }
    return render(request, 'users_app/index.html', context)

def new(request):
    print 'made it to user create'
    context = {

    }
    return render(request, 'users_app/new_user.html', context)

def edit(request, id):
    print 'edit has been reached'
    context = {
        'user' : Users.objects.get(id = id)
    }
    return render(request, 'users_app/editor.html', context)

def show(request, id):
    print 'real showy'
    user_show = Users.objects.get(id=id)
    context = {
        'user' : user_show
    }
    return render(request, 'users_app/profile_page.html', context)

def create(request):
    print 'creator created'
    Users.objects.create(
        first_name = request.POST['first_name'],
        last_name = request.POST['last_name'],
        email = request.POST['email'],
    )
    return redirect('/users') #do extra stuff

def destroy(request, id):
    print 'from destruction comes creation'
    deleter = Users.objects.get(id = id)
    deleter.delete()
    return redirect('/users')

def update(request, id):
    print 'update is functional-ish'
    if request.method == 'POST':
        user = Users.objects.get(id = id)
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.email = request.POST['email']
        user.save()
    context = {   
        'user' : user
    }
    return redirect('/users/{}'.format(user.id)) #do more stuff
# Create your views here.
