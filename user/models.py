from django.db import models
from django import forms


class PostForm(forms.Form):
    # froms.Form 을 상속받습니다.
    title = forms.CharField(max_length=50, label='제목')
    content = forms.CharField(label="내용", widget=forms.Textarea)

class UserModel(models.Model):
    class Meta:
        db_table="my_user"
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(max_length=50, unique=True)
    password = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)
class UserModelCheck(UserModel):
    password1 = models.CharField(max_length=20)
    password2 = models.CharField(max_length=20)

# Create your models here.
