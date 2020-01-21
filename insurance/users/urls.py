from django.urls import path
from .views import register_users


app_name = 'users'

urlpatterns = [
    path('', register_users, name='register_users'),
]
