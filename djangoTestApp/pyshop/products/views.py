from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

# Create your views here.
def index(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})

def new(request):
    return HttpResponse("Hello New Product")

def new2(request):
    return HttpResponse("Hello New 2 Product")