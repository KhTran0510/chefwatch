import csv
import json
import os

from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from ..models import Dish
from .serializers import DishSerializer

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
    def get(self, request, dish):
        csv_filepath = "../instructions/" + dish + ".csv"
        # print("open " + csv_filepath)
        # print(os.listdir("../instructions/"))

        data = []

        with open(csv_filepath, encoding='utf-8') as csvf:
            csv_reader = csv.DictReader(csvf)

            for rows in csv_reader:
                # print(rows)
                data.append(rows)
        # print(data)

        return Response(data)
