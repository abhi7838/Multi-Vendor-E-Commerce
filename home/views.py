from django.shortcuts import render
from .models import Brands,Category,Product
from django.contrib.auth.decorators import login_required



# Create your views here.


def master(request):
    return render(request, 'master.html')


def profile(request):
    return render(request, 'profile.html')


def index(request):
    brands = Brands.objects.all()
    category = Category.objects.all()
    product = Product.objects.all()
    category_ID = request.GET.get('category')

    if category_ID:
        product = Product.objects.filter(Sub_Category=category_ID)
    else:
        product = Product.objects.all()
    context = {
        'category':category,'brands':brands,'product':product
    }
    return render(request,'index.html',context)


