from django.urls import path

from kitchen.views import RecipeDetailView, RecipeListView, find

app_name = 'kitchen'
urlpatterns = [
    path('recipes/', RecipeListView.as_view(), name='recipes'),
    path('recipe/<str:slug>/', RecipeDetailView.as_view(), name='recipe'),
    path('find/', find, name='find')
]
