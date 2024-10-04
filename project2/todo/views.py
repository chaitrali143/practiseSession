from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'todo/home.html')

def detail(request):
    return render(request,'todo/detail.html')

def list(request):
    return render(request,'todo/list.html')