# Generated by Django 4.0 on 2024-02-08 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bake', '0006_ingredients_recipe_remove_ingredients_fat_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingredients_recipe',
            name='dry',
            field=models.FloatField(default=0),
        ),
    ]
