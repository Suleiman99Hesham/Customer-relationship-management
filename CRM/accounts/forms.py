from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


from .models import Order, Customer, Product

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

class productForm(ModelForm):
    
    class Meta:
        model = Product
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Name',
            }),
            'price': forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Price',
            }),
            'category': forms.Select(attrs={
            'id': 'inlineFormCustomSelectPref',
            'style': 'background-color: light',
            }),
            'description': forms.TextInput(attrs={
            'class': 'form-control',
            'style': 'background-color: light',
            'placeholder': 'Description',
            }),
            'tag': forms.CheckboxSelectMultiple(attrs={
            'class': 'form-check-input',
            'style': 'background-color: light',
            'placeholder': 'Description',
            }),
        }
