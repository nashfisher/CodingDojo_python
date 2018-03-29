# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from .models import Users
from django.contrib import messages
from django.contrib.messages import error
import bcrypt



def index(request):
    
    return render(request, 'index.html')

def register(request):
    errors = Users.objects.basic_validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags = tag)
        return redirect('/')
    else:
        user =  Users.objects.create(
            first_name = request.POST['first_name'],
            last_name = request.POST['last_name'],
            email = request.POST['email'],
            password = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
        )
        request.session['logged_user'] = request.POST['first_name']
    context = {
        
    }
    return redirect ('/success', context)

def login(request):
    
    if Users.objects.filter(email = request.POST['email_login']):
        user_check = Users.objects.get(email = request.POST['email_login'])
        errors = Users.objects.basic_validator(request.POST)
        User_id = Users.objects.get(email = request.POST['email_login'])
        if request.POST['email_login'] == User_id.email and bcrypt.checkpw(request.POST['password_login'].encode(), user_check.password.encode()):
            request.session['logged_user'] = User_id.first_name
            return redirect('/success')
        else:
            errorlog = {
                'error' : 'Invalid password.'
            } 
            for tag, error in errorlog.iteritems():
                messages.error(request, error, extra_tags = tag)
                return redirect('/')
    else:
        errorlog = {
            'error' : 'No registered user with the given email.'
        }
        for tag, error in errorlog.iteritems():
            messages.error(request, error, extra_tags = tag)
            return redirect('/')

def success(request):
    context = {
        'logged_in' : request.session['logged_user']
    }
    return render(request, 'success.html', context)

# Create your views here.
