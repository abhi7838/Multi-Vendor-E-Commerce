from django.urls import path,include
from django.shortcuts import redirect
from . import views
from django.contrib import admin


app_name = 'home'

urlpatterns = [
    path('admin', admin.site.urls),    
    path('master/',views.master,name = 'master'),
    path('',views.index,name = 'index'),
    path('index',views.index,name = 'index'), #for logo refresh page when someone clicks on logo page will be refreshed 
]


