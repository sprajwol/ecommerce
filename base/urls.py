from django.urls import path


from . import views as base_views

urlpatterns = [
    path('users/login/', base_views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('', base_views.getRoutes, name='routes'),

    path('users/profile/', base_views.getUserProfile, name='user-profile'),

    path('products/', base_views.getProducts, name='products'),
    path('products/<str:pk>', base_views.getProduct, name='product'),
]