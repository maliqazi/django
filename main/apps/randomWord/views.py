from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string




def index(request):
    context = {
        'counter': request.session['count'],
        'randomWord': request.session['word']
    }
    return render(request, "randomWord/index.html", context)

def gen(request):
    request.session['count'] = request.session['count']+1
    request.session['word'] = get_random_string(length=14)
    return redirect("/")

def reset(request):
    request.session['count'] = 0
    request.session['word'] = ''
    return redirect('/')
