from django.urls import path
from . import views 
from django.conf.urls.static import static
from django.contrib import admin

app_name = 'cart'

urlpatterns = [
    path('cart',views.cart,name= 'cart'),
    path('wishlist',views.wishlist,name= 'wishlist'),
    path('checkout',views.checkout,name= 'checkout'),
    path('products',views.products,name= 'products'),
    path('add_to_cart',views.add_to_cart,name= 'add_to_cart'),
    path('cart_page',views.cart_page,name='cart_page'),

]
