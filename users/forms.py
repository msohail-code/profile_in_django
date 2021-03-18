from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import userFile#, comment
from .models import Profile,Images

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

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email','first_name','last_name']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profession','twitter','instagram','image','biography']




class Uplaod_images(forms.ModelForm):
    class Meta:
        model = Images
        fields = ['image'] 