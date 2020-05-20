from django.urls import path
from . import views


app_name = 'contact_us'
urlpatterns = [
    path('', views.send_email, name='send_email'),
]
