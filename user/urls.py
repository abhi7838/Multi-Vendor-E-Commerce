from . import views
from django.conf import settings
from django.urls import path, include

urlpatterns = [
    path("login_1",views.login_1, name = 'login_1'),
    path("logout",views.logout, name = 'logout'), 
    path('profile',views.profile_view,name = 'profile'),
    path('account/',include('django.contrib.auth.urls')),
    path('signup',views.signup,name='signup'),
    path('contact',views.contact_view,name= 'contact'),

]
