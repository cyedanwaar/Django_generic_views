from rest_framework.generics import(
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView
)
from .models import Client
from .serializers import ClientSerializer


class ListCreateClientAPIView(ListCreateAPIView):
     queryset = Client.objects.all()
     serializer_class = ClientSerializer


class RetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
     queryset = Client.objects.all()
     serializer_class = ClientSerializer
     lookup_field = 'pk'
