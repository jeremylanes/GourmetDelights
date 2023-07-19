from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import DetailView, ListView

from kitchen.models import Recipe
from kitchen.script import get_jonathan_format
from scraper.jonathant_cake_srap_script.cake_scrap_lib import trier_recettes_par_liste_ingredients

"""def recipes(request):
    recipes = Recipe.objects.all()
    context = {
        'recipes': recipes
    }
    return render(request, 'kitchen/recipes.html', context=context)"""


class RecipeListView(ListView):
    queryset = Recipe.objects.all().order_by('?')
    paginate_by = 6
    context_object_name = 'recipes'
    template_name = 'kitchen/recipes.html'


class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'kitchen/detail.html'
    context_object_name = 'recipe'


def find(request):
    recipes_list = Recipe.objects.all()

    if request.method == "POST":
        ingredients_str = request.POST.get('ingredients')

        ingredients = ingredients_str.split(', ')

        recipes_jonathan_format = get_jonathan_format(recipes_list)
        recipes_rates = trier_recettes_par_liste_ingredients(liste_recettes=recipes_jonathan_format,
                                                             liste_ingredients=ingredients)
        recipes = [x for x in recipes_rates if len(x['ingredients_correspondants']) > 1]

        context = {
            'recipes': recipes
        }
        print('--------------------------------------')
        print(recipes)
        print('--------------------------------------')
        return render(request, 'kitchen/recipe_finded.html', context=context)

    return render(request, 'kitchen/find.html')
