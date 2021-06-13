from django.urls import path


from base.views import order_views

urlpatterns = [
    path('add/', order_views.addOrderItems, name='order-add'),
    path('<str:pk>/', order_views.getOrderById, name='user-order'),
    path('<str:pk>/pay/', order_views.updateOrderToPaid, name='pay'),
]
