from django.db import models


# Create your models here.


class Dish(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    type = models.IntegerField(default=1)

    def __str__(self):  # determine that return name if thing regarding our movie
        return self.name


class Recipe(models.Model):
    recipe_id = models.ForeignKey(Dish, on_delete=models.CASCADE)
    step_number = models.PositiveIntegerField(blank=True, null=True)
    instruction = models.CharField(max_length=255)
    time = models.IntegerField(default=0)
    support_id = models.PositiveIntegerField(blank=True, null=True)

    def __str__(self):  # determine that return name if thing regarding our movie
        return_str = (lambda x: str(self.recipe_id) + " support step" if x is None
                                else str(self.recipe_id) + " " + str(self.step_number))

        return return_str(self.step_number)


class Ingredient(models.Model):
    name = models.CharField(max_length=50)
    type = models.IntegerField(default=1)


class DishCategory(models.Model):
    name = models.CharField(max_length=50)


class IngredientType(models.Model):
    types = models.CharField(max_length=50)


class CulturalCategory(models.Model):
    name = models.CharField(max_length=50)
