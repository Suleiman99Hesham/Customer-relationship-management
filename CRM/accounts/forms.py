from django.forms import ModelForm
from .models import Order
class orderForm(ModelForm):
    
    class Meta:
        model = Order
        fields = '__all__'

class customerOrderForm(ModelForm):
    
    class Meta:
        model = Order
        fields = ['product', 'status']
