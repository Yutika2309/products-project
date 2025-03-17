from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from api.serializers import ProductSerializer
from api.models import Product

# Create your views here.

@api_view(['GET'])
def product_list(request):
    products = Product.objects.all() #this is a queryset
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def product_detail(request, pk):
    products = get_object_or_404(Product, pk=pk) #this is a single object
    serializer = ProductSerializer(products)
    return Response(serializer.data)
