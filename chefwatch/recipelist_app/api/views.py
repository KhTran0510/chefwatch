import csv
import json
import os

from django.http import HttpResponse

from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from ..models import Dish, Recipe
from .serializers import DishSerializer
from .serializers import RecipeSerializer

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


class InstructionStep(APIView):
    #def get(self, request):
     #   recipe = Recipe.objects.all()
      #  serializer = DishSerializer(recipe, many=True)
       # return Response(serializer.data)

    def get(self, request, dish):
        Recipe.objects.all().delete()
        csv_filepath = "../instructions/" + dish
        # dataReader = csv.reader(open(csv_filepath), delimiter=',', quotechar='"')

        data = []
        with open(csv_filepath, encoding='utf-8') as csvf:
            csv_reader = csv.DictReader(csvf)
            for rows in csv_reader:
                recipe = Recipe()

                recipe.instruction = rows['instruction']
                recipe.time_or_not = rows['time_or_not']
                recipe.time = rows['time']
                recipe.id_support = rows['id_support']
                recipe.save()
                #print(rows['instruction'])

        recipe = Recipe.objects.all()
        serializer = RecipeSerializer(recipe, many=True)
        return Response(serializer.data)
        '''       
        for row in dataReader:
            recipe = Recipe()

            recipe.instructions = row[1]
            recipe.time_or_not = row[2]
            recipe.time = row[3]
            recipe.id_support = row[4]
            recipe.save()
            print(row)
        '''

    '''
    def get(self, request, dish):
        csv_filepath = "../instructions/" + dish
        json_temp_filepath= "../instructions/temp.json"
        # print("open " + csv_filepath)
        # print(os.listdir("../instructions/"))

        data = []

        with open(csv_filepath, encoding='utf-8') as csvf:
            csv_reader = csv.DictReader(csvf)

            for rows in csv_reader:
                # print(rows)
                data.append(rows)
        # print(data)

        #with open(json_temp_filepath, 'w', encoding='utf-8') as jsonf:
        #    jsonString = json.dumps(data, indent=4)
        #    print(jsonString)
        #    jsonf.write(jsonString)

        return Response(data)
        #return HttpResponse(json.dumps(data, indent=4), content_type = "application/json")
    '''





