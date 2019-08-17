from django import forms
from Registrationapp.models import Registration

class Registrationform(forms.ModelForm):
    class Meta:
        model= Registration
        fields="__all__"

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(forms.ModelForm):
    FirstName = forms.CharField(max_length=30, required=False, help_text='Optional.')
    LastName = forms.CharField(max_length=30, required=False, help_text='Optional.')
    Username = forms.CharField(max_length=60, required=False, help_text='Optional.')
    Email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    Password1 = forms.CharField(max_length=30, required=False, help_text='Optional.')
    Password2 = forms.CharField(max_length=30, required=False, help_text='Optional.')

    class Meta:
        model = Registration
        fields = ( 'FirstName', 'LastName', 'Username','Email', 'Password1', 'Password2', )




