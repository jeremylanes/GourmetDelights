from django.urls import path

from scraper.views import cake_scrap

app_name = 'scraper'
urlpatterns = [
    path('', cake_scrap, name='cake_scrap')
]
