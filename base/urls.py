from django.urls import path

from . import views as base_views

urlpatterns = [
    path('', base_views.getRoutes, name='routes'),
    path('products/', base_views.getProducts, name='products'),
    path('products/<str:pk>', base_views.getProduct, name='product'),
]