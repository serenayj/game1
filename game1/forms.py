from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import HID

class hidForm(ModelForm):
	class Meta:
		model = HID 
		#fields = ("hitid","turkid","assid","provisional","username",)
		fields = ("username",)


class UserForm(ModelForm):
    username = forms.CharField(help_text="Please enter a username.")
    email = forms.CharField(help_text="Please enter your email.")
    password = forms.CharField(widget=forms.PasswordInput(), help_text="Please enter a password.")

    class Meta:
        model = User
        fields = ('username', 'email', 'password',)


"""
from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)
"""