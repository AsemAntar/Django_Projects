from django.shortcuts import render
from .models import Post, Category


def post_list(request):
    post_list = Post.objects.all()
    context = {
        'post_list': post_list
    }
    return render(request, 'blog/post_list.html', context)


def post_detail(request, id):
    post_detail = Post.objects.get(id=id)
    context = {
        'post_detail': post_detail,
    }
    return render(request, 'blog/post_detail.html', context)