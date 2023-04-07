from django.urls import path
from . import views

urlpatterns = [
#    path('create-user/', views.create_user_view1, name='create-user'),
    path('join/',views.signup,name='join'),
    # path('join1/',views.signup1,name='join1'),
   path('join2/',views.signup2,name='join2'),
]