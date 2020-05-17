from taggit.models import Tag
from django.db.models import Count
from django.shortcuts import render, redirect
from .models import Post, Category, Comment
from.forms import CommentForm


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
    comments = Comment.objects.filter(post=post_detail).order_by('-created')
    comments_count = Comment.objects.filter(post=post_detail).count()

    new_comment = None

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.user = request.user
            new_comment.post = post_detail
            new_comment.save()
        return redirect('blog:post_detail', id=id)
    else:
        comment_form = CommentForm()

    context = {
        'post_detail': post_detail,
        'categories': categories,
        'all_tags': all_tags,
        'comments': comments,
        'comments_count': comments_count,
        'new_comment': new_comment,
        'comment_form': comment_form,
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
