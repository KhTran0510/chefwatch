

from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from ..models import Dish, Recipe
from .serializers import DishSerializer, RecipeSerializer

# Create your views here.


class DishesList(APIView):
    def get(self, request):
        dishes = Dish.objects.all()
        serializer = DishSerializer(dishes, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = DishSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)


class RecipeProcessListAll(APIView):
    def get(self, request):
        recipes = Recipe.objects.all()
        serializer = RecipeSerializer(recipes, many=True)
        return Response(serializer.data)


class RecipeProcess(APIView):
    def get(self, request, rec_id):
        recipe = Recipe.objects.filter(recipe_id=rec_id)
        serializer = RecipeSerializer(recipe, many=True)
        return Response(serializer.data)




