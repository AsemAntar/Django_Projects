from django.urls import path
from .views import index, addTodo, completeTodo, deleteCompleted, deleteAllItems


urlpatterns = [
    path('', index, name="index"),
    path('add', addTodo, name='add_todo'),
    path('complete/<int:todo_id>/', completeTodo, name='complete'),
    path('deletecompleted/', deleteCompleted, name='delete_completed'),
    path('deleteall/', deleteAllItems, name='delete_all'),
]
