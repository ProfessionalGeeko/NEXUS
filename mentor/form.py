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


class PostsForm(forms.ModelForm):
    post_caption = forms.CharField(required=False, widget=forms.TextInput({'class': 'form-control'}))
    post_image = forms.ImageField(required=False, widget=forms.FileInput({'id': 'photo'}))
    post_video = forms.FileField(required=False, widget=forms.FileInput({'id': 'video'}))
    post_text = forms.CharField(required=False, widget=forms.Textarea({'class': 'form-control', 'id': 'blash',
                                                                       'placeholder': "Let's have a Discussion!!!",
                                                                       'width': '918', 'height': '100'
                                                                       }))

    class Meta:
        model = Post
        fields = ['post_caption', 'post_image', 'post_video', 'post_text']


class CommentForm(forms.ModelForm):
    body = forms.CharField(required=True, widget=forms.TextInput({'class': 'form-control rounded-corner',
                                                                          'name': 'body',
                                                                          'placeholder': 'Write a Comment.....'}))


    class Meta:
        model = Comment
        fields = ['body']