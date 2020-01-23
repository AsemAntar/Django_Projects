from django.urls import path
from django.contrib.auth import views as auth_views
from .views import register_users, profile, pharmacist_delete


app_name = 'users'

urlpatterns = [
    path('signup/', register_users, name='register_users'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('profile/', profile, name='profile'),
    path('delete/<int:id>/', pharmacist_delete, name='pharmacist_delete'),
]
