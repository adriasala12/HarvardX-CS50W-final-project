from django.shortcuts import render
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.db import IntegrityError

from .models import User, Book
from .aux import getBooksByTitle, getBookById

def index(request):
    return render(request, "reading/index.html")


def user_view(request):
    return render(request, "reading/user.html")


def search(request):
    if request.method == 'POST':
        search = request.POST['search']

    context = {
        'books': getBooksByTitle(search),
    }

    return render(request, "reading/search.html", context)


def book(request, gid):

    context = {
        'book': getBookById(gid),
    }

    return render(request, "reading/book.html", context)


def add_book(request, gid):
    book = Book.objects.create(gid=gid, user=request.user)
    print(request.user.readingList.all())
    return HttpResponseRedirect(reverse('book', args=(gid,)))


def login_view(request):

    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('index'))
        else:
            return render(request, "reading/login.html", {'message': "Invalid username and/or password"})

    else:
        return render(request, "reading/login.html")


def register_view(request):

    if request.method == 'POST':

        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirmation = request.POST['confirmation']

        if password != confirmation:
            return render(request, "reading/register.html", {'message': "The passwords do not match."})

        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "reading/register.html", {'message': "This username is already taken."})

        login(request, user)
        return HttpResponseRedirect(reverse('index'))

    else:
        return render(request, "reading/register.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
