from django.shortcuts import render,HttpResponse
from django.contrib.auth import authenticate, logout
from django.shortcuts import render, redirect
from django.conf import settings
from .models import UserCreateForm,ContactFormSubmission,UserProfile
from django.db import models
import datetime
from django.contrib.auth.decorators import login_required

app_name = 'user'


def profile(request):
    return render(request, 'profile.html')



def wishlist(request):
    return render(request, 'wishlist.html')


@login_required
def profile_view(request):
    try:
        profile = request.user.profile

    except UserProfile.DoesNotExist:
        profile = None
    return render(request,'profile.html',{'user':request.user, 'profile':profile})


def contact_view(request):
    if request.method == "POST":
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        country   = request.POST.get('country')
        subject = request.POST.get('subject')
        print('post')

        ContactFormSubmission.objects.create(
            firstname= firstname,  # The value from request.POST
            lastname = lastname,    # The value from request.POST
            country = country,        # The value from request.POST
            subject = subject          # The value from request.POST

        )
        return render(request, 'contact.html', {'message': 'Thank you for your message!'})
    else:
        # Display the contact form
        return render(request, 'contact.html')

