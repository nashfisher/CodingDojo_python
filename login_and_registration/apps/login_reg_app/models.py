# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

class RegManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['first_name']) < 2:
            errors['first_name'] = "First name value cannot be less than 2 characters."
        if len(postData['last_name']) < 2:
            errors['last_name'] = "Last name value cannot be less than 2 characters."
        if len(postData['email']) < 1:
            errors['email'] = 'Email field cannot be blank.'
        try:
            validate_email(postData['email'])
        except ValidationError:
            errors['email'] = 'Invalid email'
        else:
            if Users.objects.filter(email = postData['email']):
                errors['email'] = "Email already in use."
        if postData['password'] != postData['password_confirm'] or len(postData['password']) < 8:
            errors['password'] = 'Passwords do not match'
        if len(postData['password']) < 8:
            errors['password'] = 'Passwords must be at contain at least 8 characters.'
        return errors
class Users(models.Model):
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    email = models.CharField(max_length = 100)
    password = models.CharField(max_length = 25)

    objects = RegManager()
# Create your models here.
