from django_filters import FilterSet, DateFilter, CharFilter
from django import forms

from .models import Order

class DateTypeInput(forms.DateInput):
    input_type = 'date'

class orderFilter(FilterSet):
    start_date = DateFilter(widget=DateTypeInput(), field_name="date_created", lookup_expr='gte')
    end_date = DateFilter(widget=DateTypeInput(), field_name="date_created", lookup_expr='lte')
    note = CharFilter(field_name="note", lookup_expr='icontains')
    class Meta:
        model = Order
        fields = '__all__'
        exclude = ['customer', 'date_created']