# Generated by Django 4.2.3 on 2023-07-06 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kitchen', '0002_rename_title_information_cooking_method_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='cooking_stapes',
            field=models.ManyToManyField(to='kitchen.cookingstep', verbose_name='étapes de cuisson'),
        ),
    ]
