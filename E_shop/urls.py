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
    path('',include('home.urls')), # all pages of home is included #index,master,views,admin 
    path('',include('cart.urls')), # included cart app pages included cart, products, wishlist, checkout
    path('',include('user.urls')), # user app refrenced pages login, logout,profile,signup,contact,account
    path('admin', admin.site.urls),
    path('logout',auth_views.LogoutView.as_view(next_page = 'login_1'),name='logout'),
    path('login_1',auth_views.LoginView.as_view(template_name = 'login_1.html'),name = 'login_1'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
