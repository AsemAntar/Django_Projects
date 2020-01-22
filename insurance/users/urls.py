from django.urls import path
from django.contrib.auth import views as auth_views
from .views import register_users


app_name = 'users'

urlpatterns = [
    path('', register_users, name='register_users'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
]
