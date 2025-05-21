from django.shortcuts import render
from .models import *
from django.contrib.auth.decorators import login_required

app_name = 'cart'

# Create your views here.
def cart(request):
    return render(request,'cart.html')  # prof

def wishlist(request):
    return render(request,'wishlist.html')  # favourite products of user 

def products(request):
    return render(request,'products.html') # list of all available products

def checkout(request):
    return render(request,'checkout.html')
