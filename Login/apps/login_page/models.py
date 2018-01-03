from __future__ import unicode_literals
from django.db import models
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

class UsersManager(models.Manager):
    def registration_validator(self, postData):
        errors = {}
        if len(postData['first_name']) < 1:
            errors["firstname"] = "first_name field cannot be left blank"
        elif len(postData['last_name']) < 1:
            errors["lastname"] = "last_name field cannot be left blank"
        elif not EMAIL_REGEX.match(postData['email']):
            errors["eml"] = "Invalid email address"
        elif not postData['password'] == postData['confirmpw']:
            errors["psswrd"] = "Passwords do not match"
        return errors
    def login_validator(self, postData):
        errors = {}
        if len(postData['login_email']) < 1:
            errors["loginemail"] = "Enter your email address to login"
        elif len(postData['login_pwd']) < 1:
            errors["loginpwd"] = "Enter a password"
        return errors

class Users(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UsersManager()
