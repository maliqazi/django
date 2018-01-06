from django.shortcuts import render, redirect
from .models import Users, Books, Reviews
from django.contrib import messages
from django.db.models.base import ObjectDoesNotExist
import bcrypt

def index(request):
    context = {
        'dummykey' : 'dummyvalue'
    }
    return render(request, 'belt_app/index.html', context)

def add(request):
    errors = Users.objects.registration_validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request,error,extra_tags=tag)
        return redirect('/')
    else:
        hashpwd = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
        Users.objects.create(name=request.POST['name'],
                            alias=request.POST['alias'],
                            email=request.POST['email'],
                            password=hashpwd)
        request.session['name'] = request.POST['name']
        request.session['password'] = hashpwd
        return redirect('/books')

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

        if bcrypt.checkpw(request.POST['login_pwd'].encode(), p.password.encode()): 
            request.session['name'] = p.name
            request.session['password'] = p.password
            return redirect('/books')
        else:
            messages.error(request,"Wrong password")
            return redirect('/')

def books(request):
    if len(request.session['name']) < 1:
        return redirect('/')
    elif len(request.session['password']) < 1:
        return redirect('/')
    books = Books.objects.all()
    reviews = Reviews.objects.raw("""
                        SELECT
                            r.id,
                            r.review as review,
                            b.title as title,
                            r.rating as rating,
                            u.name as name,
                            u.id as user_id,
                            r.book_id as book_id,
                            r.created_at as created_at
                        FROM belt_app_reviews as r
                        join belt_app_books as b
                        on r.book_id=b.id
                        join belt_app_reviews_user as ur
                        on r.id = ur.reviews_id
                        join belt_app_users as u
                        on ur.users_id = u.id
                        order by r.created_at desc LIMIT 3""")
    context = {
        'user_info' : request.session['name'],
        'books' : books,
        'reviews' : reviews
    }
    return render(request, 'belt_app/books.html', context)

def addbook(request):
    if len(request.session['name']) < 1:
        return redirect('/')
    elif len(request.session['password']) < 1:
        return redirect('/')
    books = Books.objects.all()
    context = {
        'books' : books
    }
    return render(request, 'belt_app/addbook.html', context)

def enterbook(request):
    if len(request.session['name']) < 1:
        return redirect('/')
    elif len(request.session['password']) < 1:
        return redirect('/')
    author_post = request.POST['d_author']
    if len(request.POST['author'])>0:
        author_post = request.POST['author']
    Books.objects.create(title= request.POST['booktitle'], author=author_post)
    b = Books.objects.get(title=request.POST['booktitle'])
    Reviews.objects.create(review=request.POST['review'],
                            rating=request.POST['stars'],
                            book_id=b.id)
    r = Reviews.objects.get(review=request.POST['review'])
    u = Users.objects.get(name=request.session['name'])
    r.user.add(u)
    return redirect('/books/'+str(b.id))

def addreview(request,number):
    if len(request.session['name']) < 1:
        return redirect('/')
    elif len(request.session['password']) < 1:
        return redirect('/')
    book = Books.objects.get(id=number)
    reviews = Reviews.objects.filter(book_id=number)
    reviews = Reviews.objects.raw("""
                            SELECT
                                r.id,
                                r.review as review,
                                r.rating as rating,
                                u.name as name,
                                u.id as user_id,
                                r.created_at as created_at
                            FROM belt_app_reviews as r
                            join belt_app_reviews_user as ur
                            on r.id = ur.reviews_id
                            join belt_app_users as u
                            on ur.users_id = u.id
                            where r.book_id = """ + number + """
                            order by r.created_at desc""")
    context = {
        'book_info' : book,
        'reviews' : reviews
    }
    return render(request, 'belt_app/addreview.html', context)

def enterreview(request,number):
    if len(request.session['name']) < 1:
        return redirect('/')
    elif len(request.session['password']) < 1:
        return redirect('/')
    Reviews.objects.create(review=request.POST['review'],
                            rating=request.POST['stars'],
                            book_id=number)
    r = Reviews.objects.get(review=request.POST['review'])
    u = Users.objects.get(name=request.session['name'])
    r.user.add(u)
    return redirect('/books/'+str(number))

def users(request,number):
    if len(request.session['name']) < 1:
        return redirect('/')
    elif len(request.session['password']) < 1:
        return redirect('/')
    user = Users.objects.get(id=number)
    total_reviews = user.reviews.count()
    books = Reviews.objects.raw ("""
                        SELECT distinct b.id as id, b.title as title
                        FROM belt_app_books as b
                        join belt_app_reviews as r
                        on r.book_id = b.id
                        join belt_app_reviews_user as ur
                        on r.id = ur.reviews_id
                        join belt_app_users as u
                        on ur.users_id = u.id
                        where u.id =""" + number)
    context = {
        'user_info' : user,
        'total_reviews' : total_reviews,
        'books' : books
    }
    return render(request, 'belt_app/users.html', context)

def logout(request):
    request.session['name']=''
    request.session['password']=''
    return redirect('/')
