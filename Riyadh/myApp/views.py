from collections import UserDict
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout



# Create your views here.
def home(request):
   return render(request, "myApp/home.html")
def signup(request):

    if request.method == "post":
        username = request.post['username']
        firstname = request.post['first name']
        lastname = request.post['last name']
        email = request.post['email']
        password= request.post['password']
        Cpassword = request.post['Cpassword']

        myuser = User.object.create_user(username, email, password)
        myuser.first_name = firstname
        myuser.last_name = lastname

        myuser.save()

        messages.success(request, "Your Account has been successfully created. ")

        return redirect("signin")



    return render(request, "myApp/signup.html")

def signin(request):
    if request.method == 'post':
        username = request.post['username']
        password = request.post['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            firstname = user.first_name
            return render(request, "myApp/home.html", {'firstname': firstname})
        else:
            messages.error(request,"Bad Credentials!")
            return redirect('home')
    return render(request, "myApp/signin.html")


def signout(request):
    logout(request)
    messages.success(request, "Logged Out Successfully:")
    return redirect('home')
    
