from django.shortcuts import render
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.db import IntegrityError

from .models import User

def index(request):
    return render(request, "reading/index.html")


def user_view(request):
    return render(request, "reading/user.html")


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