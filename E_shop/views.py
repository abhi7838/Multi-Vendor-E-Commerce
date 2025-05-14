from django.shortcuts import render,HttpResponse,redirect
from app.models import Category, Sub_Category,Brands,Product


from django.contrib.auth import authenticate,login
from app.models import UserCreateForm


def master(request):
    return render(request, 'master.html')

def index(request):
    return render(request,'index.html')

def contact(request):
    return render(request, 'registration/contact.html')


def index(request):
    brands = Brands.objects.all()
    category = Category.objects.all()
    # product = Product.objects.all()
    category_ID = request.GET.get('category')

    if category_ID:
        product = Product.objects.filter(Sub_Category=category_ID)

    else:
        product = Product.objects.all()

    context = {
        'category':category,'brands':brands,'product':product
    }
    return render(request,'index.html',context)


def signup(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            new_user = authenticate(
                username = form.cleaned_data['username'],
                passsword = form.cleaned_data['password1'],
            )
            login(request,new_user)
            return redirect('index')
    else:
        form = UserCreateForm()

    context = {
        'form':form,
    }


    return render(request,'registration/signup.html',context)



    
 