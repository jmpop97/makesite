from django.urls import path
from . import views

urlpatterns = [
    path('create-user/', views.create_user_view, name='create-user'),
    path('create-user1/', views.create_user_view1, name='create-user'),
    path('join/',views.signup,name='join')
]