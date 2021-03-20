from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


from .models import Order, Customer

class CustomerForm(ModelForm):
    
    class Meta:
        model = Customer
        fields = '__all__'
        exclude = ['user']


class orderForm(ModelForm):
    
    class Meta:
        model = Order
        fields = '__all__'

class customerOrderForm(ModelForm):
    
    class Meta:
        model = Order
        fields = ['product', 'status']

class createUserForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
