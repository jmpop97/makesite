from django.shortcuts import render
from . forms import PostForm
from django.contrib.auth import views, models, login
from django.shortcuts import render, redirect
from . forms import UserForm,UserForm1
from django.http import HttpResponse
# Create your views here.
def create_user_view(request):
    return render(request, 'user/create_user.html')

def create_user_view1(request):
    post_form = PostForm()
    return render(request,'user/create_user1.html',{'form': post_form})


def signup(request):
    if request.method == "POST":  # 1
        form = UserForm(request.POST)

        if form.is_valid():  # 2
            new_user = models.User.objects.create_user(**form.cleaned_data)  # 5
            login(request, new_user)

        return redirect('user/create_user.html')

    else:  # 3
        form = UserForm()
    print("form.as_p")
    print(type(form))
    print(form)
    return render(request, 'user/create_user2.html', {'form': form})  # 4

def signup1(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # 받은 데이터 처리 로직
        # ...

        return HttpResponse('Thank you for contacting us!')
    else:
        form = UserForm1()
    return render(request, 'user/create_user2.html',{'form':form})