# Generated by Django 4.2.3 on 2023-07-06 23:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CookingStep',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('states', models.CharField(max_length=512, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Information',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('preparation_time', models.PositiveIntegerField(default=0)),
                ('cooking_time', models.PositiveIntegerField(default=0)),
                ('rest_period', models.PositiveIntegerField(default=1)),
                ('source', models.URLField(verbose_name='image')),
            ],
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
            ],
            options={
                'verbose_name': 'ingrédient',
            },
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='titre')),
                ('thumbnail', models.URLField(verbose_name='image')),
                ('information', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kitchen.information')),
                ('ingredients', models.ManyToManyField(to='kitchen.ingredient', verbose_name='ingrédients')),
            ],
        ),
    ]
