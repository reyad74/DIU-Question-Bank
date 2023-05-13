from collections import UserDict
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages



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
    return render(request, "myApp/signin.html")

def signout(request):
    pass
    
