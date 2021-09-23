from django.urls import path
from .views import register,login,index,prj_form, search,get_profile

urlpatterns = [
    path('register/',register,name='register'),
    path('',login,name='login'),
    path('home/',index,name='home'),
    path('post/',prj_form,name='post'),
    path('search/',search,name='search'),
    path('profile/',get_profile,name='profile')
]