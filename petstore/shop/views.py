from django.shortcuts import render
from .models import Products
# Create your views here.

def home(request):
    context = {}
    products = Products.objects.all()
    print(products)
    context['t'] = products
    return render(request,'shop/home.html',context)