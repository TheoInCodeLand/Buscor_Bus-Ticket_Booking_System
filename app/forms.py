# myapp/forms.py

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(max_length=254, required=True)
    gender = forms.CharField(max_length=10, required=True)
    address = forms.CharField(max_length=255, required=True)
    cellphone = forms.CharField(max_length=15, required=True)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super(SignUpForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            profile = Profile(
                user=user,
                gender=self.cleaned_data['gender'],
                address=self.cleaned_data['address'],
                cellphone=self.cleaned_data['cellphone']
            )
            profile.save()
        return user
