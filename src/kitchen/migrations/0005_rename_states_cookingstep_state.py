# Generated by Django 4.2.3 on 2023-07-07 00:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kitchen', '0004_alter_recipe_options_recipe_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cookingstep',
            old_name='states',
            new_name='state',
        ),
    ]