from django.db import models

# Create your models here.


class Dish(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    type = models.IntegerField(default=1)

    def __str__(self):  # determine that return name if thing regarding our movie
        return self.name


class Ingredient(models.Model):
    name = models.CharField(max_length=50)
    type = models.IntegerField(default=1)


class DishCategory(models.Model):
    name = models.CharField(max_length=50)


class IngredientType(models.Model):
    types = models.CharField(max_length=50)


class CulturalCategory(models.Model):
    name = models.CharField(max_length=50)


class Recipe(models.Model):
    instruction = models.CharField(max_length=200)
    time_or_not = models.BooleanField()
    time = models.IntegerField(default=0)
    id_support = models.IntegerField(default=0)



