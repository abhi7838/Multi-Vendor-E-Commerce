from django.shortcuts import render,get_object_or_404,redirect
from .models import *
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib import messages
from .cart import *
from django.http import JsonResponse
from .form import CheckoutForm 
from .models import Order, OrderItem 

app_name = 'user_profile'

# Create your views here.
def cart(request):
    return render(request,'cart.html')  # prof

def wishlist(request):
    return render(request,'wishlist.html')  # favourite products of user 

def products(request):
    return render(request,'products.html') # list of all available products

@login_required(login_url='/user/login')
def checkout(request):
    cart_items = CartItem.objects.filter(user=request.user)
    if not cart_items.exists():
        messages.warning(request,"your cart is empty. Please add items befor checkout")
        return redirect('user_profile:cart_detail') #redirect if cart is empty 
    
    total_price = sum(item.total_item_price for item in cart_items)
    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            order=Order.objects.create(
                user=request.user,
                first_name=form.cleaned_data['first_name'],
                last_name = form.cleaned_data['last_name'],
                email = form.cleaned_data['email'],
                address = form.cleaned_data['address'],
                postal_code = form.cleaned_data['postal_code'],
                city = form.cleaned_data['city'],
                total_amount = total_price
            )

            for cart_item in cart_items:
                OrderItem.objects.create(
                    order = order,
                    product = cart_item.product,
                    price=cart_item.product.price,
                    quantity = cart_item.quantity
                )
            cart_items.delete()

            messages.success(request,"your order have been placed sucessfully")
            return redirect(reverse('user_profile:order_confirmation', args=[order.id]))

    else:
        initial_data = {}
        if  request.user.is_authenticated:
            initial_data['email'] = request.user.email
            form = CheckoutForm(initial = initial_data)
    context = {
        'form':form,
        'cart_items':cart_items,
        'total_price':total_price,
    }
    return render(request, 'checkout.html',context)
@login_required(login_url='/user/login')
def order_confirmation(request, order_id):
    order = get_object_or_404(Order, id = order_id,user=request.user)
    return render(request, 'order_confirmation.html', {'order':order})

@login_required(login_url='/user/login')
def my_order(request):
    orders = Order.objects.filter(user=request.user).order_by('-created')
    return render(request, 'my_order.html', {'orders':orders})








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


# @login_required(login_url='/user/login')
# def cart_add(request,id):
#     print(request)
#     cart = CartItem(request)
#     product = Product.objects.get(id=id)
#     return redirect(reverse('user_profile:index'))

@login_required(login_url='/user/login')
def cart_add(request, id):
    product = get_object_or_404(Product, id=id)
    user = request.user

    try:
        # Check if the item is already in the user's cart
        cart_item = CartItem.objects.get(user=user, product=product)
        cart_item.quantity += 1
        cart_item.save()
        messages.success(request, f"{product.name} quantity updated in your cart.")
    except CartItem.DoesNotExist:
        # If the item is not in the cart, create a new CartItem
        CartItem.objects.create(user=user, product=product)
        messages.success(request, f"{product.name} added to your cart.")

    # Redirect the user to the cart page or wherever you want
    return redirect(reverse('user_profile:cart_detail')) # Replace 'your_cart_view_name' with the actual URL name of your cart view




# @login_required(login_url='/user/login')
# def item_clear(request,id):
#     cart = CartItem(request)
#     product=Product.objects.get(id=id)
#     Cart.remove(product)
#     return redirect('user_profile:cart_detail')

@login_required(login_url='/user/login')
def item_clear(request, id):
    try:
        cart_item = CartItem.objects.get(user=request.user, product__id=id)
        cart_item.delete()
        messages.success(request, f"{cart_item.product.name} removed from your cart.")
    except CartItem.DoesNotExist:
        messages.error(request, "Item not found in your cart.")
    return redirect('user_profile:cart_detail')

@login_required(login_url='/user/login')
def item_increment(request,id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=id)
    cart.add(product = product)
    
    return redirect(reverse('user_profile:cart_detail'))

@login_required(login_url='/user/login')
def item_decrement(request,id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=id)
    cart.decrement(product=product)
    return redirect(reverse('user_profile:cart_detail'))

@login_required(login_url='/user/login')
def cart_clear(request):
    cart=CartItem(request)
    cart.clear()
    return redirect('cart_detail')

@login_required(login_url='/user/login')
def cart_detail(request):
    cart_items = CartItem.objects.filter(user=request.user).order_by('date_added')
    total_price = sum(item.total_item_price for item in cart_items)
    context = {'cart_items': cart_items, 'total_price': total_price}
    return render(request, 'cart_detail.html', context)


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







