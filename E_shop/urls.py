"""
URL configuration for E_shop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static 
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin', admin.site.urls),    
    path('master/',views.master,name = 'master'),
    path('',views.index,name = 'index'),
    path('index',views.index,name = 'index'),
    path('signup',views.signup,name='signup'),
    path('account/',include('django.contrib.auth.urls')),
    path('contact',views.contact_view,name= 'contact'),
    path('cart',views.cart,name= 'cart'),
    path('checkout',views.checkout,name= 'checkout'),
    path('products',views.products,name= 'products'),
    path('login_1',views.login_1,name= 'login_1'),
    # path('logout', views.logout, name='logout'),
    path('wishlist',views.wishlist,name= 'wishlist'),
    path('logout',auth_views.LogoutView.as_view(next_page = 'login_1'),name='logout'),
    path('login_1',auth_views.LoginView.as_view(template_name = 'login_1.html'),name = 'login_1'),
    path('profile/',views.profile,name = 'profile'),





] + static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
