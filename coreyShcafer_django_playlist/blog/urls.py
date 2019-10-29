from django.urls import path
from .views import (
    PostListViews,
    PostDetailViews,
    PostCreateViews,
    PostUpdateViews,
    PostDeleteViews
)
from . import views

urlpatterns = [
    path('', PostListViews.as_view(), name='blog-home'),
    path('post/<int:pk>/', PostDetailViews.as_view(), name='post-detail'),
    path('post/new/', PostCreateViews.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateViews.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteViews.as_view(), name='post-delete'),
    path('about/', views.about, name='blog-about'),
]
