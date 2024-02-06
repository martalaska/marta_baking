from django.db import models

class Ingredients(models.Model):
    title = models.CharField(max_length = 100, default = "Ingredients", primary_key = True)
    image = models.URLField(blank = True)
    strawberry = models.FloatField()
    apricot = models.FloatField()
    cointerau = models.FloatField()
    almond = models.FloatField()
    milk_chocolate = models.FloatField()
    vanilla = models.FloatField()
    grapefruit = models.FloatField()
    

# Create your models here.
