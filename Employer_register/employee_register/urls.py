from django.urls import path
from .views import employee_list, employee_form, delete_employee


urlpatterns = [
    path('', employee_form, name='employee_form'),
    path('<int:id>/', employee_form, name='employee_update'),
    path('delete/<int:id>/', delete_employee, name='delete'),
    path('list/', employee_list, name='employee_list'),
]
