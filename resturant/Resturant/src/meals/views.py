from django.shortcuts import render
from .models import Meals, Category


def meals_list(request):
    meals_list = Meals.objects.all()
    categories = Category.objects.all()
    context = {
        'meals_list': meals_list,
        'categories': categories,
        'active:': 'active',
    }

    return render(request, 'meals/list.html', context)


def meal_detail(request, slug):
    meal_detail = Meals.objects.get(slug=slug)
    context = {
        'meal_detail': meal_detail,
    }

    return render(request, 'meals/detail.html', context)
