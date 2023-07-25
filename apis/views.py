from rest_framework import generics

from products.models import Products

from .serializers import ProductSerializer


class ProductAPIView(generics.ListAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer