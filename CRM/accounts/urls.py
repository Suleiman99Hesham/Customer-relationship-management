from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name = 'home'),
    path('products/',views.products, name = 'products'),
    path('customer/<int:id>',views.customer, name = 'customer'),
    path('create_order/<int:id>', views.createOrder, name='create_order'),
    path('update_order/<int:id>', views.updateOrder, name='update_order'),
    path('update_customer_order/<int:id>', views.updateCustomerOrder, name='update_customer_order'),
    path('delete_order/<int:id>', views.deleteOrder, name='delete_order'),
    path('delete_customer_order/<int:id>', views.deleteCustomerOrder, name='delete_customer_order'),
    path("register/", views.register, name="register"),
    path("login/", views.loginPage, name="login"),
    path("logout/", views.logoutUser, name="logout"),
    path("user/", views.user_page, name="user-page"),
]
