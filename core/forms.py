from django import forms
# from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _


class UserLoginForm(forms.Form):
	username = forms.CharField(widget=forms.TextInput(attrs={"id":"id_username", "name":"username", "type":"text", 'placeholder': 'username', }))
	password = forms.CharField(widget=forms.PasswordInput(attrs={"id":"id_password", "name":"password", "type":"password", 'placeholder': 'password',}))
