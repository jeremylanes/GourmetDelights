from django.shortcuts import render

from kitchen.models import Recipe


def index(request):
    recipes = Recipe.objects.all().order_by('?')
    context = {
        'recipes': recipes
    }
    return render(request, 'home/index.html', context=context)
