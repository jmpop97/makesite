from django import forms
from django.contrib.auth.models import User

class PostForm(forms.Form):
    # froms.Form 을 상속받습니다.

    title = forms.CharField(max_length=50, label='제목')
    content = forms.CharField(label="내용", widget=forms.Textarea)

class UserForm(forms.ModelForm):
    class Meta:
        model =User
        fields = ['username','email','password']
        help_texts={'username':None}

class UserForm3(forms.ModelForm):
    class Meta:
        model =User
        fields = ['username','email','password']
        help_texts={'username':None}
class UserForm1(forms.Form):
    name = forms.CharField(max_length=15)
    email = forms.EmailField(max_length=20)
    message = forms.CharField(widget=forms.Textarea)
