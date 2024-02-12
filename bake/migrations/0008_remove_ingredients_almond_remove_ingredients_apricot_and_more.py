# Generated by Django 4.0 on 2024-02-09 03:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bake', '0007_ingredients_recipe_dry'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ingredients',
            name='almond',
        ),
        migrations.RemoveField(
            model_name='ingredients',
            name='apricot',
        ),
        migrations.RemoveField(
            model_name='ingredients',
            name='cointerau',
        ),
        migrations.RemoveField(
            model_name='ingredients',
            name='grapefruit',
        ),
        migrations.RemoveField(
            model_name='ingredients',
            name='image',
        ),
        migrations.RemoveField(
            model_name='ingredients',
            name='milk_chocolate',
        ),
        migrations.RemoveField(
            model_name='ingredients',
            name='strawberry',
        ),
        migrations.RemoveField(
            model_name='ingredients',
            name='vanilla',
        ),
        migrations.AddField(
            model_name='ingredients',
            name='matches',
            field=models.CharField(default='', max_length=2000),
        ),
    ]
