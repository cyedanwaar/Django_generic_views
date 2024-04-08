from django.urls import path
from .views import (
    ListCreateClientAPIView,
    RetrieveUpdateDestroyAPIView,
    )

from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('clients/', ListCreateClientAPIView.as_view(), name='client-list'),
    path('clients/<pk>/', RetrieveUpdateDestroyAPIView.as_view(), name='client-update'),
]