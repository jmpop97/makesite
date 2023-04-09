from django.shortcuts import render, redirect
# from . forms import PostForm
from django.contrib.auth import views, models, login
from django.shortcuts import render, redirect
from .forms import UserForm, UserForm2, LogInForm
from .models import UserModel
from django.contrib import auth
from django.http import HttpResponse


# Create your views here.
# def create_user_view(request):
#     return render(request, 'user/create_user.html')
#
# def create_user_view1(request):
#     post_form = PostForm()
#     return render(request,'user/create_user1.html',{'form': post_form})

def home(request):
    user = request.user.is_authenticated
    if user:
        return redirect('base')
    else:
        return redirect('log-in')
def base(request):
    user = request.user.is_authenticated
    if user:
        return render(request, 'base.html')
    else:
        return redirect('log-in')

def signup(request):
    form = UserForm()
    print("work")

    if request.method == "POST":  # 1
        form_check = UserForm(request.POST)
        print(form_check.username)
        if form_check.is_valid():  # 2

            password1 = form_check.cleaned_data['password1']
            password2 = form_check.cleaned_data['password2']
            if password1 == password2:
                new_user = UserModel()
                new_user.username = form_check.cleaned_data['username']
                print(form_check.cleaned_data['username'])
                new_user.email = form_check.cleaned_data['email']
                new_user.password = password1
                new_user.save()
                return render(request, 'base.html')
        else:
            print(form_check.errors)
    else:
        pass
    return render(request, 'user/create_user2.html', {'form': form})  # 4


#
# def signup1(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         message = request.POST.get('message')
#
#         # 받은 데이터 처리 로직
#         # ...
#
#         return HttpResponse('Thank you for contacting us!')
#     else:
#         form = UserForm1()
#     return render(request, 'user/create_user2.html',{'form':form})
def signup2(request):
    if request.method == "POST":  # 1
        form = UserForm2(request.POST)

        if form.is_valid():  # 2
            new_user = models.User.objects.create_user(**form.cleaned_data)  # 5
            login(request, new_user)

        return redirect('user/create_user.html')

    else:  # 3
        form = UserForm2()
    print("form.as_p")
    print(type(form))
    print(form)
    return render(request, 'user/create_user2.html', {'form': form})  # 4


def signin(request):
    if request.method == 'POST':
        form=LogInForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        me = auth.authenticate(request, username=username, password=password)
        print(me)
        print(username)
        print(password)
        if me is not None:
            print("login완료")
            auth.login(request, me)
            return redirect('')
        else:
            return redirect('/log-in', {'error': '유저이름 혹은 패스워드를 확인 해 주세요'})
    elif request.method == 'GET':
        user = request.user.is_authenticated
        if user:
            return redirect('/')
        else:
            pass
    form = LogInForm()
    return render(request, 'user/log_in.html',{'form':form})
