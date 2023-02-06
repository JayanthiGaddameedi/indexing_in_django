import csv
import datetime
import random

from django.shortcuts import render, HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Product


# Create your views here.

@api_view(['POST'])
def create_data(request):
    data = []
    start_time = datetime.datetime.now()
    for i in range(0, 100000):
        data = [
            Product(name=i,
                    price=i + 1)
        ]
        new_record = Product.objects.bulk_create(data)
    content = {'message': "added"}
    end_time = datetime.datetime.now()
    print(f" Created in {end_time - start_time}")
    return Response(content, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_data(request):
    # temp = random.randint(50000, 51000)
    temp = random.randint(90000, 99999)
    get_product = Product.objects.get(name=temp)
    content = {'data': get_product.name}
    return Response(content, status=status.HTTP_200_OK)

