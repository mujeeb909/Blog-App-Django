from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

class RegisterForm(UserCreationForm):

  email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': "Enter Email Address"}))
  username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Enter Username"}))
  password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': "Enter Password"}))
  password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': "Confirm Password"}))

  class Meta:
    model = get_user_model()
    fields = ['email', 'username', 'password1','password2']


class UpdateProfileForm(forms.ModelForm):

  first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Enter First Name"}))
  last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Enter Last Name"}))
  email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': "Enter Email Address"}))
  username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Enter Username"}))
  phone = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Enter Phone"}))
  address = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Enter Address"}))
  bio = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': "Enter Bio"}))
  role = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Enter Role"}))
  profile_pic = forms.ImageField(widget=forms.FileInput(attrs={"class": "form-control", "placeholder": "Upload image"}))

  class Meta:
    model = get_user_model()
    fields = ['first_name', 'last_name', 'username', 'email','phone', 'address', 'bio', 'role', 'profile_pic']

