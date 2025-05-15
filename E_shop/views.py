from django.shortcuts import render,HttpResponse,redirect
from app.models import Category, Sub_Category,Brands,Product,ContactFormSubmission,UserCreateForm
from django.contrib import messages


from django.contrib.auth import authenticate,login



def master(request):
    return render(request, 'master.html')

# def contact(request):
#     return render(request, 'contact.html')


def cart(request):
    return render(request,'cart.html')


def wishlist(request):
    return render(request,'wishlist.html')

def products(request):
    return render(request,'products.html')


def checkout(request):
    return render(request,'checkout.html')


def login(request):
    return render(request,'login.html')


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

def contact_view(request):
    if request.method == "POST":
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        country   = request.POST.get('country')
        subject = request.POST.get('subject')
        print('post')

        ContactFormSubmission.objects.create(
            firstname= firstname,  # The value from request.POST
            lastname = lastname,    # The value from request.POST
            country = country,        # The value from request.POST
            subject = subject          # The value from request.POST

        )



        messages.success(request,'Your message has been submitted sucessfully')
        return redirect('contact')

    return render(request, 'contact.html')



    
 