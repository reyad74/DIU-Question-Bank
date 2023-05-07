from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
   return render(request,"myApp/home.html")
def signup(request):
    return render(request,"myApp/signup.html")

def signin(request):
    return render(request,"myApp/signin.html")

def signout(request):
    pass
    
