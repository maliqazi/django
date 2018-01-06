from __future__ import unicode_literals
from django.db import models
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

class UsersManager(models.Manager):
    def registration_validator(self, postData):
        errors = {}
        if len(postData['name']) < 1:
            errors["name"] = "Name field cannot be left blank"
        elif not EMAIL_REGEX.match(postData['email']):
            errors["eml"] = "Invalid email address"
        elif len(postData['password']) < 8:
            errors["pwdlen"] = "Password must be 8 characters long"
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
    name = models.CharField(max_length=255)
    alias = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UsersManager()

class Bks_RevsManager(models.Manager):
    def books_validator(self, postData):
        errors = {}
        if len(postData['title']) < 1:
            errors["name"] = "Name field cannot be left blank"
        if len(postData['author']) < 1:
            errors["name"] = "Name field cannot be left blank"
        return errors
    def reviews_validator(self, postData):
        errors = {}
        if len(postData['review']) < 1:
            errors["review"] = "Name field cannot be left blank"
        return errors

class Books(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = Bks_RevsManager()

class Reviews(models.Model):
    review = models.TextField()
    user = models.ManyToManyField(Users, related_name="reviews")
    book = models.ForeignKey(Books, related_name="book")
    rating = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = Bks_RevsManager()
