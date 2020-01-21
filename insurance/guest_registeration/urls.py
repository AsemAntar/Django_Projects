from django.urls import path
from .views import guest_list, guest_register, guest_delete, guest_detail


app_name = 'guest_registeration'

urlpatterns = [
    path('', guest_list, name='guest_list'),
    path('<int:id>/', guest_register, name='guest_update'),
    path('delete/<int:id>/', guest_delete, name='guest_delete'),
    path('detail/<int:id>/', guest_detail, name='guest_detail'),
    path('register/', guest_register, name='register'),
]
