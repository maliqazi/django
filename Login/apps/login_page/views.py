from django.shortcuts import render, redirect
from .models import Users
from django.contrib import messages
from django.db.models.base import ObjectDoesNotExist
import bcrypt

def index(request):
    context = {
        'user_info' : 'users'
    }
    return render(request, 'login_page/index.html', context)

def add(request):
    errors = Users.objects.registration_validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request,error,extra_tags=tag)
        return redirect('/')
    else:
        hashpwd = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
        Users.objects.create(first_name=request.POST['first_name'],
                            last_name=request.POST['last_name'],
                            email=request.POST['email'],
                            password=hashpwd) #password=request.POST['password'])
        return redirect('/success')

def login(request):
    errors = Users.objects.login_validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request,error,extra_tags=tag)
        return redirect('/')
    else:
        try:
            p = Users.objects.get(email=request.POST['login_email'])
        except ObjectDoesNotExist:
            messages.error(request,"User not found")
            return redirect('/')

        if bcrypt.checkpw(request.POST['login_pwd'].encode(), p.password.encode()): #request.POST['login_pwd'] == p.password:
            return redirect('/success/' + p.first_name)
        else:
            messages.error(request,"Wrong password")
            return redirect('/')

def success(request, firstname):
    context = {
        'user_info' : firstname
    }
    return render(request, 'login_page/success.html', context)
