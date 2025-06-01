from . import views
from django.conf import settings
from django.urls import path, include
from django.contrib.auth.views import LogoutView 

app_name = 'user'

urlpatterns = [
    path("login_1/",views.login_1, name = 'login_1'),
    path("logout",LogoutView.as_view(next_page = '/'), name = 'logout'), 
    path('profile',views.profile_view,name = 'profile'),
    path('account/',include('django.contrib.auth.urls')),
    path('signup',views.signup,name='signup'),
    path('contact',views.contact_view,name= 'contact'),
    path('sucessful_sign_up',views.sucessful_sign_up,name= 'sucessful_sign_up'),

]
