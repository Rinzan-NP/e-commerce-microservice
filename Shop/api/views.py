from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from  rest_framework.generics import CreateAPIView
from .serializer import ProductSerializer
from .models import Product


class ProductAddView(CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer



