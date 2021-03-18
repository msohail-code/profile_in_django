from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import userFile#, comment

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField() #default is true
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class fileForm(forms.ModelForm):
    class Meta:
        model = userFile
        fields = ('title', 'permissionToDownload','permissionToSeeUser','FileType','realFile')

# class commentForm():
#     class Meta:
#         model = comment
#         fields = ('post','body','')