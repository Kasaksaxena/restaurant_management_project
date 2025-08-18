from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Item
from .serializers import ItemSerializer

'''
NOTE: Conside this as a reference and follow this same coding structure or format to work on you tasks
'''

# Create your views here.
class ItemView(APIView):

    def get(self, request):
        items = Item.objects.all()
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MenuListView(APIView):   
    def  get(self,request):
        menu_items=[
            {"id":1,"name":"Margherita Pizza","price":8.99},
            {"id":2,"name":"White Sauce Pasta","price":12.00},
            {"id":3,"name":"Red Sauce Pasta","price":12.00},
            {"id":4,"name":"Burger","":8.00},
            {"id":5,"name":"Grilled Salad","price":8.23},

        ]
        return Response(menu_items,status=status.HTTP_200_OK)