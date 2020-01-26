from django.urls import path
from .views import (
    GuestList,
    guest_register,
    guest_delete,
    guest_detail,
    delete_drug,
)


app_name = 'guest_registeration'

urlpatterns = [
    path('', GuestList.as_view(), name='guest_list'),
    path('register/', guest_register, name='register'),
    path('<int:id>/', guest_register, name='guest_update'),
    path('delete/<int:id>/', guest_delete, name='guest_delete'),
    path('detail/<int:id>/', guest_detail, name='guest_detail'),
    path('delete_drug/<int:id>/<int:p_id>', delete_drug, name='delete_drug'),
]
