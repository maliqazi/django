from django.shortcuts import render, redirect
from .models import Users
from django.contrib import messages

class UserInfo(object):
    def __init__(self, fullname, email, created_at):
        self.fullname = fullname
        self.email = email
        self.created_at = created_at

def index(request):
    print Users.objects.all()
    context = {
        'somevalue' :  Users.objects.all() #list_users
    }
    return render(request, "rest_users/index.html", context)

def new(request):
    context = {
        'userinfo' : 'user'
    }
    return render(request, "rest_users/new.html", context)

def create(request):
    errors = Users.objects.basic_validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request,error,extra_tags=tag)
        return redirect('/users/new')
    else:
        Users.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'])
        return redirect ('/users')

def show(request, number):
    print "this is show" + number
    context = {
        'show_user' : Users.objects.get(id=number)
    }
    return render(request, "rest_users/show.html", context)

def edit(request, number):
    context = {
        'edit_user' : Users.objects.get(id=number)
    }
    return render(request, "rest_users/edit.html", context)

def destroy(request, number):
    delete_info = Users.objects.get(id=number)
    delete_info.delete()
    return redirect ('/users')

def update(request):
    errors = Users.objects.basic_validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request,error,extra_tags=tag)
        return redirect('/users/' + request.POST['id'] + '/edit')
        updated_info = Users.objects.get(id = request.POST['id'])
    updated_info.first_name = request.POST['first_name']
    updated_info.last_name = request.POST['last_name']
    updated_info.email = request.POST['email']
    updated_info.save()
    redir = '/users/' + request.POST['id'] + '/'
    return redirect (redir)
