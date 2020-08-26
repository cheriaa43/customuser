from django import forms
from user_custom.models import CustomUser

class LoginForm(forms.Form):
    username = forms.CharField(max_length=250)
    password = forms.CharField(widget=forms.PasswordInput)


class SignupForm(forms.Form):
    display_name = forms.CharField()
    username = forms.CharField(max_length=250)
    password = forms.CharField(widget=forms.PasswordInput)
    age = forms.IntegerField()
    homepage = forms.URLField()
