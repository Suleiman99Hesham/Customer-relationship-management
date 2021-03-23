from django.urls import path
from django.contrib.auth import views as auth_views
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
    path("user/<str:name>", views.user_page, name="user-page"),
    path("settings/", views.account_settings, name="accounts-settings"),
    path(
        "reset_password/",
        auth_views.PasswordResetView.as_view(template_name='accounts/password_reset.html'),
        name="password_reset"
        ),
    path(
        "reset_password_sent/", 
        auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_sent.html'), 
        name="password_reset_done"
        ),
    path(
        "reset/<uidb64>/<token>", 
        auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_form.html'), 
        name="password_reset_confirm"
        ),
    path(
        "reset_password_complete/", 
        auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_done.html'), 
        name="password_reset_complete"
        ),
    path("update_customer/<int:id>", views.update_customer, name="update_customer")
]
