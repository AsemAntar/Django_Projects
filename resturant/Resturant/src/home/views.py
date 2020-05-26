from django.shortcuts import render
from about.models import WhyYouChooseUs
from blog.models import Post
from meals.models import Meals, Category


def home(request):
    meals = Meals.objects.all()
    meals_list = Meals.objects.all()
    categories = Category.objects.all()
    posts = Post.objects.all()
    latest_post = Post.objects.all().order_by('-created')[:3]
    why = WhyYouChooseUs.objects.all()
    context = {
        'meals': meals,
        'meals_list': meals_list,
        'categories': categories,
        'active': 'active',
        'posts': posts,
        'latest_post': latest_post,
        'why': why,
    }
    return render(request, 'home/index.html', context)
