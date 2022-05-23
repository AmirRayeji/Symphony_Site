from django import forms

from account.models import Profile

class SignupForm(forms.ModelForm):
    first_name=forms.CharField(max_length=100)
    last_name=forms.CharField(max_length=100)
    username=forms.CharField(max_length=100)
    password=forms.CharField(widget=forms.PasswordInput)
    email=forms.CharField(widget=forms.EmailInput)

    class Meta:
        model=Profile
        fields=['profile', 'gender']
