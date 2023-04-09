from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('log-in/', views.signin, name='log-in'),
    path('join/',views.signup,name='join'),
    path('join2/',views.signup2,name='join2'),
    path('base/',views.base,name='base'),
]