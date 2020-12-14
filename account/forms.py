from django import forms
from django.contrib.auth.models import User
from .models import EndUserProfile, EndUserInfo

class customerLoginForm(forms.Form):
    username = forms.CharField(
        max_length=16,
        widget=forms.TextInput({'placeholder': "(123)456-789"}))
    password = forms.CharField(widget=forms.PasswordInput)


class userLoginForm(forms.Form):
    username = forms.CharField(
        max_length=64,
        widget=forms.TextInput({'placeholder': "username"}))
    password = forms.CharField(widget=forms.PasswordInput)

class userRegistraionForm(forms.ModelForm):
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ("username", "email", "first_name", "last_name")

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError("password do not match.")
        return cd['password2']

class EndUserProfileForm(forms.ModelForm):
    class Meta:
        model = EndUserProfile
        fields = ("phone", "birth", "address")
    
class EndUserInfoForm(forms.ModelForm):
    
    class Meta:
        model = EndUserInfo
        fields = ("school", "company", "profession", "aboutme", "photo")

class EndUserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ("email", )


    