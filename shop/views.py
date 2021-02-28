
from rest_framework.generics import (
    CreateAPIView, RetrieveAPIView, ListAPIView, DestroyAPIView)
from .models import Product
from .serializers import *


class ProductCreateView(CreateAPIView):
    serializer_class = ProductSerializer


class ProductListView(ListAPIView):
    serializer_class = ProductListSerializer
    queryset = Product.objects.all()


class ProductRetrieveView(RetrieveAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class ProductDestroyView(DestroyAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
