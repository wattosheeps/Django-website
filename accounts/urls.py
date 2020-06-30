from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views
urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name="login"),
    path('logout', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    path('signup',views.sign_up, name="signup")
    
]