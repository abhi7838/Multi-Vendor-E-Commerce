from django.urls import path,include
from . import views 
from django.conf.urls.static import static
from django.contrib import admin

app_name = 'user_profile'

urlpatterns = [
    path('cart',views.cart,name= 'cart'),
    path('wishlist',views.wishlist,name= 'wishlist'),
    path('checkout',views.checkout,name= 'checkout'),
    path('products',views.products,name= 'products'),
    path('add_to_cart',views.add_to_cart,name= 'add_to_cart'),
    path('cart_page',views.cart_page,name='cart_page'),

    # new path for add to cart 
    path('cart_add/<int:id>/',views.cart_add, name = 'cart_add'),
    path('item_clear/<int:id>/',views.item_clear,name = 'item_clear'),
    path('item_increment/<int:id>/',views.item_increment,name = 'item_increment'),
    path('item_decrement/<int:id>/',views.item_decrement,name='item_decrement'),
    path('clear_cart',views.cart_clear,name='cart_clear'),
    path('cart_detail',views.cart_detail,name='cart_detail'),

    path('admin/', admin.site.urls),    
    path('master/',views.master,name = 'master'),
    path('',views.index,name = 'index'),
    path('index',views.index,name = 'index'), #for logo refresh page when someone clicks on logo page will be refreshed 

]
