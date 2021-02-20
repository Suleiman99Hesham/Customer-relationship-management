from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.

def home(request):
    last_orders = Order.objects.all().order_by('-date_created')[0:5]
    customers_orders = {}
    total_orders = Order.objects.all().count()
    delivered = Order.objects.filter(status='Delivered').count()
    pending = Order.objects.filter(status='Pending').count()
    for order in Order.objects.all():
        if order.customer.name in customers_orders:
            customers_orders[order.customer.name] += 1
        else:
            customers_orders[order.customer.name] = 1
    context = {
        'customers_orders' : customers_orders,
        'last_orders' : last_orders,
        'total_orders' : total_orders,
        'delivered' : delivered,
        'pending' : pending,
    }
    return render(request, 'accounts/dashboard.html', context)

def products(request):
    products = Product.objects.all()
    return render(request, 'accounts/products.html', {'products':products})

def customer(request, id):
    customer = Customer.objects.get(id=id)
    total_orders = customer.order_set.all().count()
    orders = customer.order_set.all()
    context = {
        'customer' : customer,
        'orders' : orders,
        'total_orders' : total_orders,
    }
    return render(request, 'accounts/customer.html', context)
