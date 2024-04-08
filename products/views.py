from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView,
)
from .models import Product
from .serializers import ProductSerializer

class ListProductsApiView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CreateProductApiView(CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
     

class RetrieveProductApiView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'slug'


class UpdateProductApiView(UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'slug'


class DestroyProductApiView(DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'slug'