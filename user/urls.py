from . import views
from django.conf import settings
from django.urls import path, include
from django.contrib.auth.views import LogoutView 

app_name = 'user'

urlpatterns = [
    path('account/',include('django.contrib.auth.urls')),
    path('wishlist/',views.wishlist,name = 'wishlist'),
    path('contact',views.contact_view,name= 'contact'),

]
