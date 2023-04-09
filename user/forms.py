from django import forms
from django.contrib.auth.models import User
from django.forms.widgets import PasswordInput
from .models import UserModelCheck , UserModel


# class PostForm(forms.Form):
#     # froms.Form 을 상속받습니다.
#
#     title = forms.CharField(max_length=50, label='제목')
#     content = forms.CharField(label="내용", widget=forms.Textarea)

class UserForm(forms.ModelForm):
    class Meta:
        model =UserModelCheck
        fields = ['username','email','password1','password2']
        widgets ={"password1":PasswordInput(),"password2":PasswordInput()}
        help_texts={}
class LogInForm(forms.ModelForm):
    class Meta:
        model =UserModel
        fields = ['username','password']
        widgets = {"password": PasswordInput()}
        help_texts={}

class UserForm2(forms.ModelForm):
    class Meta:
        model =User
        fields = ['username','email','password']
        help_texts={'username':None}
# class UserForm1(forms.Form):
#     name = forms.CharField(max_length=15)
#     email = forms.EmailField(max_length=20)
#     message = forms.CharField(widget=forms.Textarea)
