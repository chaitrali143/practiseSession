from django.shortcuts import render


# Create your views here.

def signup(request):
    return render(request,'user/login.html')

def login(request):
    return render(request,'user/login.html')