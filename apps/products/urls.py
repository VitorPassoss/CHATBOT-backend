from django.urls import path
from . import views


urlpatterns = [
    path("", views.ProductHandler.as_view(), name='all_products'),
    path("details/<pk>", views.ProductHandler.as_view(), name='all_products'),
    path("supplie/", views.SupplieHandler.as_view(), name='all_supplies'),
    path("supplie/<pk>", views.SupplieHandler.as_view(), name='supplie')
]