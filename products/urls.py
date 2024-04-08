from django.urls import path
from .views import(
    ListProductsApiView,
    CreateProductApiView,
    RetrieveProductApiView,
    UpdateProductApiView,
    DestroyProductApiView)


urlpatterns = [
    path('products/', ListProductsApiView.as_view(), name='products-list'),
    path('products/create/', CreateProductApiView.as_view(), name='products-create'),
    path('products/retrieve/<slug:slug>/', RetrieveProductApiView.as_view(), name='products-retrieve'),
    path('products/update/<slug:slug>/', UpdateProductApiView.as_view(), name='products-update'),
    path('products/destroy/<slug:slug>/', DestroyProductApiView.as_view(), name='products-destroy'),
]