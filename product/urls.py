from django.urls import path
from . import views

urlpatterns = [
#    path('create-user/', views.create_user_view1, name='create-user'),
    path('product/',views.create_product,name='join'),
    ]