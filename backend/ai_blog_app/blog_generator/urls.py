from django.urls import path
from . import views

#listing all the urls for the projects
urlpatterns=[
    path('', views.index, name="index"),#the url specified to the homepage
    path('login', views.user_login, name="login"),
    path('signup', views.user_signup, name="signup"),
    path('logout', views.user_logout, name="logout")

]