from django.urls import path
from . import views

app_name = 'loginapp'
urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.loginuser, name='login'),
    path('logout/', views.logoutuser, name='logout'),
    path('profile/', views.userprofile, name='profile'),

]
