from django.db import models

# Create your models here.
class Image(models.Model):
    name = models.CharField(max_length=200)
    file = models.ImageField('Bild', upload_to="", blank=True, null=True)


class Meal(models.Model):
    name = models.CharField(max_length=200)
    ingredients = models.CharField(max_length=200)


class Ingredient(models.Model):
    name = models.CharField(max_length=200)