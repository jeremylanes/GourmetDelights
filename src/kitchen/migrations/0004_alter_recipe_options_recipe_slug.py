# Generated by Django 4.2.3 on 2023-07-07 00:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kitchen', '0003_recipe_cooking_stapes'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='recipe',
            options={'verbose_name': 'recette'},
        ),
        migrations.AddField(
            model_name='recipe',
            name='slug',
            field=models.SlugField(blank=True, max_length=128),
        ),
    ]
