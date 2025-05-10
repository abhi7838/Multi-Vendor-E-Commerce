from django.shortcuts import render,HttpResponse
from app.models import Category, Sub_Category,Brands,Product



def master(request):
    return render(request, 'master.html')


def index(request):
    brands = Brands.objects.all()
    category = Category.objects.all()
    product = Product.objects.all()
    context = {
        'category':category,'brands':brands,'product':product
    }
    return render(request,'index.html',context)

# def test(request):
    # return render(request,'test.html')

# def master(request):
#     return ('HELLO ')
