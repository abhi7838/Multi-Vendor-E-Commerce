from django.shortcuts import render,get_object_or_404,redirect
from .models import *
from django.contrib.auth.decorators import login_required
from cart.cart import Cart
from django.http import HttpRequest, HttpResponse,request

app_name = 'user_profile'

# Create your views here.
def cart(request):
    return render(request,'cart.html')  # prof

def wishlist(request):
    return render(request,'wishlist.html')  # favourite products of user 

def products(request):
    return render(request,'products.html') # list of all available products

def checkout(request):
    return render(request,'checkout.html')




def add_to_cart(request,product_id):
    if request.method == 'POST':
        product = get_object_or_404(Product, id= product_id)
        form = AddToCartForm(request.POST)

        if form.is_valid():
            quantity = form.changed_data['quantity']
            cart = request.session.get('cart',{})

        if str(product_id) in cart:
            cart[str(product.id)]['quantity'] += quantity

        else:
            cart[str(product.id)] = {'quantity':quantity, 'price':str(product.price), 'name':str(product.name)}

        request.session['cart'] = cart
        return redirect('product_detail',product_id=product_id)
    
    
def cart_page(request):
    cart = request.session.get('cart',[])
    cart_items = []
    total_price = 0

    for product_id, item_data in cart.items():
        try:
            product = Product.objects.get(id=product_id)
            items = {
                'product' : product,
                'quantity':item_data['quantity'],
                'price'   :item_data['price'],
                'total'   :float(item_data['total']) *item_data['quantity']
            }
            cart_items.append(items)
            total_price += items['price']

        except Product.DoesNotExist:
            del request.session['cart'][product_id]
            request.session.modified = True

    context = {'cart_items':cart_items, 'total_price':total_price}
    return render(request,'cart/cart.html',context)


# @login_required(login_url='/user/login_1')
def cart_add(request,id):
    print(request)
    cart = CartItem(request)
    # print(type(id))
    product = Product.objects.get(id=id)
    return redirect('index')

@login_required(login_url='/user/login_1')
def item_clear(request,id):
    cart = CartItem(request)
    product=Product.objects.get(id=id)
    cart.remove(product)
    return redirect('cart_detail')

@login_required(login_url='/user/login_1')
def item_increment(request,id):
    cart = CartItem(request)
    product = Product.objects.get(id=id)
    cart.add(product = product)
    return redirect('cart_detail')

@login_required(login_url='/user/login_1')
def item_decrement(request,id):
    cart = CartItem(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect('cart_detail')

@login_required(login_url='/user/login_1')
def cart_clear(request):
    cart=CartItem(request)
    cart.clear()
    return redirect('cart_detail')

@login_required(login_url='/user/login_1')
def cart_detail(request):
    return render(request, 'cart/cart_detail.html')



# copied from home.views 
def master(request):
    return render(request, 'master.html')


def profile(request):
    return render(request, 'profile.html')

def index(request):
    return render(request,'index')


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







