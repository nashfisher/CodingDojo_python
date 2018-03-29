# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import datetime
from ..login_reg_app.models import Users

class CourseManager(models.Manager):
    def course_validator(self, postData):
        errors = {}
        if len(postData['name']) < 1:
            errors['name'] = 'Course name cannot be left blank.'
        
        return errors

class Courses(models.Model):
    name = models.CharField(max_length = 250)
    description = models.CharField(max_length = 250)
    created_at = models.DateTimeField(auto_now_add = True)
    course_creator = models.CharField(max_length = 250)

    coursetakers = models.ManyToManyField(Users, related_name = 'registered_courses')

    objects = CourseManager()

# Create your models here.
