from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
)

from . import views as base_views

urlpatterns = [
    path('users/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('', base_views.getRoutes, name='routes'),
    path('products/', base_views.getProducts, name='products'),
    path('products/<str:pk>', base_views.getProduct, name='product'),
]