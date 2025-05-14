"""this page is used to create a from for getting data from html form here we can perfrom 
various operation on data validation such as checking the email is name is proper valid or not"""

from django import forms
from .models import ContactFormSubmission

class ContactForm(forms.ModelForm):
    class Meta:
        form = ContactFormSubmission
        fields = ['firstname','lastname','country','subject']

