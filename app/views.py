from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet
from app.models import *
from app.serializers import *

class Product(ModelViewSet):
    queryset =Product.objects.all()
    serializer_class=ProductModelSerializer

