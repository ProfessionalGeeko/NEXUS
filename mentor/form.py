from django import forms
from django.contrib.auth.forms import UserCreationForm
from mentor.models import *


class DateInput(forms.DateInput):
    input_type = 'date'


class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=20, widget=forms.TextInput({'placeholder': 'Enter Username', 'class': 'mb-2',
                                                                      'id': 'un'}))
    email = forms.EmailField(max_length=40, widget=forms.EmailInput({'class': 'mb-2', 'placeholder': 'Email'}))
    password1 = forms.CharField(widget=forms.PasswordInput({'placeholder': 'Enter Password', 'class': 'mb-2',
                                                            'id': 'up1', 'minlength': '8'}))
    password2 = forms.CharField(widget=forms.PasswordInput({'placeholder': 'Confirm Password', 'class': 'mb-2',
                                                            'id': 'up', 'minlength': '8'}))
    first_name = forms.CharField(max_length=32, widget=forms.TextInput({'class': 'mb-2', 'placeholder': 'First Name'}))
    last_name = forms.CharField(max_length=32, widget=forms.TextInput({'class': 'mb-2', 'placeholder': 'Last Name'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'first_name', 'last_name']


class MentorProfileForm(forms.ModelForm):
    dop = forms.ImageField(widget=forms.FileInput({'id': 'upload'}))
    gender = forms.ChoiceField(widget=forms.Select(), choices=GENDER_CHOICES)
    mobile = forms.CharField(widget=forms.TextInput({'class': 'form-control'}))
    qualification = forms.CharField(widget=forms.TextInput({'class': 'form-control'}))
    profession = forms.CharField(widget=forms.TextInput({'class': 'form-control'}))

    class Meta:
        model = MentorInfo
        fields = ['dop', 'dob', 'gender', 'mobile', 'qualification', 'profession']
        widgets = {'dob': DateInput()}


class MenteeProfileForm(forms.ModelForm):
    dop = forms.ImageField(required=False, widget=forms.FileInput({'id': 'upload', 'name': 'dop'}))
    gender = forms.ChoiceField(widget=forms.Select(), choices=GENDER_CHOICES)
    mobile = forms.CharField(widget=forms.TextInput({'class': 'form-control'}))
    institute = forms.CharField(widget=forms.TextInput({'class': 'form-control'}))

    class Meta:
        model = MenteeInfo
        fields = ['dop', 'dob', 'gender', 'mobile', 'institute']
        widgets = {'dob': DateInput()}
