from kitchen.models import Recipe


def get_jonathan_format(recipes: Recipe):
    recipes_jonathant_format = []

    for recipe in recipes:
        jonathan_format = {
            # recette['absolute_url'] = recette.get_absolute_url()
            "absolute_url": recipe.get_absolute_url(),
            "titre": recipe.title,
            "url": recipe.information.source,
            "url_image": recipe.thumbnail,
            "recette": {
                "titre": recipe.title,
                "infos": {
                    "duree_preparation": recipe.information.preparation_time,
                    "methode_cuisson": recipe.information.cooking_method
                },
                "ingredients": [x.name for x in recipe.ingredients.all()],
                "etapes": [x.state for x in recipe.cooking_stapes.all()]
            }
        }
        recipes_jonathant_format.append(jonathan_format)
    return recipes_jonathant_format
