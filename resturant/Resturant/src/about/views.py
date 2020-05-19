from django.shortcuts import render
from .models import AboutUs, WhyYouChooseUs, Chef


def about_us(request):
    aboutUs = AboutUs.objects.last()
    why = WhyYouChooseUs.objects.all()
    chefs = Chef.objects.all()

    context = {
        'aboutUs': aboutUs,
        'why': why,
        'chefs': chefs,
    }

    return render(request, 'about/about.html', context)
