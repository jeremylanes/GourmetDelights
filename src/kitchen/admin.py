from django.contrib import admin

from kitchen.models import Ingredient, CookingStep, Information, Recipe


@admin.register(Ingredient)
class AdminIngredient(admin.ModelAdmin):
    list_display = ['name']
    list_per_page = 20


@admin.register(CookingStep)
class AdminCookingStep(admin.ModelAdmin):
    list_display = ['state']
    list_per_page = 20


@admin.register(Information)
class AdminInformation(admin.ModelAdmin):
    list_display = ['cooking_method', 'preparation_time', 'cooking_time']
    list_per_page = 20


@admin.register(Recipe)
class AdminRecipe(admin.ModelAdmin):
    list_display = ['title']
    list_per_page = 20
    filter_horizontal = ['ingredients', 'cooking_stapes']
