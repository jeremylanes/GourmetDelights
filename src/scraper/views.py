from django.shortcuts import render, redirect
from django.urls import reverse

from kitchen.models import Information, Recipe, Ingredient, CookingStep
from scraper.jonathant_cake_srap_script.main import get_recipes


def cake_scrap(request):
    recipes = get_recipes()
    """print("-----------------------------")
    test=recipes[0]
    print(f"type {type(test)}")
    print(f"tile: {test['recette']['titre']}")
    print(f"url : {test['url']}")"""
    for recipe in recipes:
        information = Information.objects.get_or_create(
            cooking_method=recipe['recette']['infos']['methode_cuisson'],
            preparation_time=recipe['recette']['infos']['duree_preparation'],
            cooking_time=recipe['recette']['infos']['duree_cuisson'],
            rest_period=recipe['recette']['infos']['duree_repos'],
            source=recipe['url']
        )
        """print('****************************************')
        print(information)"""

        recipe_object = Recipe.objects.get_or_create(
            title=recipe['recette']['titre'],
            information=information[0],
            thumbnail=recipe['url_image']
        )
        for ingredient in recipe['recette']['ingredients']:
            ingredient_object = Ingredient.objects.get_or_create(name=ingredient)
            recipe_object[0].ingredients.add(ingredient_object[0])
            """print()
            print(f'recipe {recipe_object[0]}')
            print(f'recipe type  {type(recipe_object[0])}')"""

        for cooking_step in recipe['recette']['etapes']:
            cooking_step_object = CookingStep.objects.get_or_create(state=cooking_step)
            recipe_object[0].cooking_stapes.add(cooking_step_object[0])
    return redirect(reverse('home:index'))
