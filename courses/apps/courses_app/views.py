from django.shortcuts import render, redirect
from .models import Courses
from django.contrib import messages

def index(request):
    context = {
        'courses' : Courses.objects.all()
    }
    return render(request, 'courses_app/index.html', context)

def add(request):
    errors = Courses.objects.basic_validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request,error,extra_tags=tag)
    else:
        Courses.objects.create(course_name=request.POST['course_name'], description=request.POST['desc'])
    return redirect('/courses/')

def destroy(request, number):
    context = {
        'del_course' : Courses.objects.get(id=number)
    }
    return render(request, 'courses_app/destroy.html', context)

def delete_course(request,number):
    del_course = Courses.objects.get(id=number)
    del_course.delete()
    return redirect('/courses/')
