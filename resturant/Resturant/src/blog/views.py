from django.db.models import Count
from django.shortcuts import render
from .models import Post, Category

from taggit.models import Tag


def post_list(request):
    post_list = Post.objects.all()
    context = {
        'post_list': post_list
    }
    return render(request, 'blog/post_list.html', context)


def post_detail(request, id):
    post_detail = Post.objects.get(id=id)
    categories = Category.objects.all().annotate(posts_count=Count('post'))
    all_tags = Tag.objects.all()

    context = {
        'post_detail': post_detail,
        'categories': categories,
        'all_tags': all_tags,
    }
    return render(request, 'blog/post_detail.html', context)


def post_by_tag(request, tag):
    post_by_tag = Post.objects.filter(tags__name__in=[tag])

    context = {
        'post_list': post_by_tag,
    }

    return render(request, 'blog/post_list.html', context)


def post_by_category(request, cat):
    post_by_category = Post.objects.filter(categories__name=cat)

    context = {
        'post_list': post_by_category,
    }

    return render(request, 'blog/post_list.html', context)
