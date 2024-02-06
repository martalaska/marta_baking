# Generated by Django 4.0 on 2024-01-24 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bake', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ingredients',
            old_name='sour_cream',
            new_name='milk_chocolate',
        ),
        migrations.AddField(
            model_name='ingredients',
            name='title',
            field=models.CharField(default='Ingredient', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='ingredients',
            name='image',
            field=models.URLField(blank=True),
        ),
    ]