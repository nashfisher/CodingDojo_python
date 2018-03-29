# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.shortcuts import render, HttpResponse, redirect
from ..login_reg_app.models import Users
from django.contrib import messages
from django.contrib.messages import error
from .models import Courses

def index(request):
    
    context = {
        'All_Courses' : Courses.objects.all()
    }
    return render(request, 'courses_app/index.html', context)

def create(request):
    print 'made it to create'
    errors = Courses.objects.course_validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags = tag)
        return redirect('/courses')
    else:
        course = Courses.objects.create(
            name = request.POST['name'],
            description = request.POST['description'],
            course_creator = request.session['logged_user']
        )

        return redirect('/courses')

def show(request, id):
    print 'made it to show'
    course_profile = Courses.objects.get(id = id)
    courses = Courses.objects.all()
    context = {
        'Course' : course_profile,
        'Coursetakers' : courses,
    }

    return render(request, 'courses_app/course_page.html', context)

def edit(request, id):
    print 'edit has been reached'
    context = {
        'course' : Courses.objects.get(id = id)
    }
    return render(request, 'courses_app/editor.html', context)

def update(request, id):
    print 'update is functional-ish'
    if request.method == 'POST':
        course = Courses.objects.get(id = id)
        course.name = request.POST['name']
        course.description = request.POST['description']
        course.save()
    
    return redirect('/courses/{}/show'.format(id))

def join(request, id):
    print 'made it to join'

    current_user = Users.objects.get(username = request.session['logged_user'])
    course_to_join = Courses.objects.get(id = id)
    course_to_join.coursetakers.add(current_user)
    course_to_join.save()

    return redirect('/courses/{}/show'.format(id))

def destroy(request, id):
    print 'made it to destroy'
    print request.session['logged_user']
    print id

    target_course = Courses.objects.get(id = id)

    if target_course.course_creator == request.session['logged_user']:
        target_course.delete()
    else:
        print 'wrong user'
    return redirect('/courses')

def logout(request):
    request.session.clear()

    return redirect('/')
# Create your views here.
