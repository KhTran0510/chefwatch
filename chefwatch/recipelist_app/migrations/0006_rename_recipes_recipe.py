# Generated by Django 4.0.3 on 2022-06-03 02:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipelist_app', '0005_recipes_delete_recipe'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Recipes',
            new_name='Recipe',
        ),
    ]
