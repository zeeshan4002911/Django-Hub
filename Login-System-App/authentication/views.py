from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login


# Create your views here.


def home(request):
    return render(request, "authentication/index.html")

def signup(request):
    if request.method == 'POST':
        try:
            username = request.POST['username']
            firstname = request.POST['firstname']
            lastname = request.POST['lastname']
            email = request.POST['email']
            password = request.POST['password']
            confirm_password = request.POST['confirm-password']

            user = User.objects.create_user(username, email, password)
            user.first_name = firstname
            user.last_name = lastname
            user.save()

            messages.success(request, "Account created Successfully")

            return redirect('signin')
        except Exception as err:
            print("Error", err)

    return render(request, "authentication/signup.html")

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(request, "authentication/index.html", {'firstname': user.first_name})
        else:
            messages.error(request, "Bad Credential")
            return redirect('home')
        
    return render(request, "authentication/signin.html")


def signout(request):
    pass
