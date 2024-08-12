from django import forms
from .models import Signup

class SignupForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput(), label="Password")
    password2 = forms.CharField(widget=forms.PasswordInput(), label="Confirm Password")

    class Meta:
        model = Signup
        fields = ['username', 'email', 'password1', 'password2']
