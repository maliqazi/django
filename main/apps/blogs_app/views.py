from django.shortcuts import render, HttpResponse, redirect
# the index function is called when root is visited
def index(request):
    context = {
        'somekey':'somevalue'
    }
    return render(request, "blogs/index.html", context)

def new(request):
    response = "Placeholder for form to create new blog"
    return HttpResponse(response)

def create(request):
    if request.method == "POST":
        print "*"*50
        print request.POST
        print request.POST['name']
        print request.POST['desc']
        request.session['name'] = "test"  # more on session below
        print "*"*50
        return redirect("/")
    else:
        return redirect("/")

def show(request, number):
    response = "Placeholder to show blog {}".format(number)
    return HttpResponse(response)

def edit(request, number):
    response = "Placeholder to edit blog {}".format(number)
    return HttpResponse(response)

def delete(request, number):
    return redirect('/')
