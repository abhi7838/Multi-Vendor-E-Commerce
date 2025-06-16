from django import forms


class CheckoutForm(forms.Form):
    first_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'First Name'}))
    last_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Last Name'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Email'}))
    address = forms.CharField(max_length=250, widget = forms.TextInput(attrs={'class':'form-control','placeholder':'address'}))
    postal_code = forms.CharField(max_length=20,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'postal Code'}))
    city = forms.CharField(max_length=30,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'city'}))

