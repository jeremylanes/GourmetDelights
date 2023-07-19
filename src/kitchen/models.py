from django.db import models
from django.shortcuts import reverse
from django.utils.text import slugify


class Ingredient(models.Model):
    name = models.CharField(max_length=128, unique=True)

    class Meta:
        verbose_name = 'ingrédient'


class CookingStep(models.Model):
    state = models.CharField(max_length=512, unique=True)


class Information(models.Model):
    cooking_method = models.CharField(max_length=128)
    preparation_time = models.CharField(max_length=128)
    cooking_time = models.CharField(max_length=128)
    rest_period = models.CharField(max_length=128)
    source = models.URLField(verbose_name='source')


class Recipe(models.Model):
    title = models.CharField(max_length=128, verbose_name='titre')
    slug = models.SlugField(max_length=128, blank=True)
    information = models.ForeignKey(to=Information, on_delete=models.CASCADE)
    thumbnail = models.URLField(verbose_name='image')
    ingredients = models.ManyToManyField(to=Ingredient, verbose_name='ingrédients')
    cooking_stapes = models.ManyToManyField(to=CookingStep, verbose_name='étapes de cuisson')

    class Meta:
        verbose_name = 'recette'

    def get_absolute_url(self):
        return reverse('kitchen:recipe', kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
