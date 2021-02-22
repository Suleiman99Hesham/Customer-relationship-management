from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name = 'home'),
    path('products/',views.products, name = 'products'),
    path('customer/<int:id>',views.customer, name = 'customer'),
    path('create_order/<int:id>', views.createOrder, name='create_order'),
    path('update_order/<int:id>', views.updateOrder, name='update_order'),
    path('delete_order/<int:id>', views.deleteOrder, name='delete_order'),
]
