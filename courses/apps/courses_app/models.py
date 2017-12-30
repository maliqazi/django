from __future__ import unicode_literals

from django.db import models

class CoursesManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['course_name']) < 1:
            errors["course_name"] = "Name field cannot be left blank"
        return errors

class Courses(models.Model):
    course_name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CoursesManager()
