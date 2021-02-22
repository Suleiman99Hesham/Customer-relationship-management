from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import orderForm
from django.forms import inlineformset_factory

# Create your views here.

def home(request):
    customers = Customer.objects.all()
    last_orders = Order.objects.all().order_by('-date_created')[0:5]
    # customers_orders = {}
    total_orders = Order.objects.all().count()
    delivered = Order.objects.filter(status='Delivered').count()
    pending = Order.objects.filter(status='Pending').count()
    # for order in Order.objects.all():
    #     if order.customer.name in customers_orders:
    #         customers_orders[order.customer.name] += 1
    #     else:
    #         customers_orders[order.customer.name] = 1
    context = {
        'customers' :customers,
        # 'customers_orders' : customers_orders,
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

def createOrder(request, id):
    customer = Customer.objects.get(id=id)
    OrderFormSet = inlineformset_factory(Customer, Order, fields=('product', 'status'), extra=7)
    formset = OrderFormSet(queryset=Order.objects.none(), instance=customer)
    # form = orderForm(initial={'customer':customer})
    if request.method == 'POST':
        # form = orderForm(request.POST)
        formset = OrderFormSet(request.POST, instance=customer)
        if formset.is_valid():
            formset.save()
        return redirect('/')
    context = {
        'formset' : formset
    }
    return render(request, 'accounts/order_form.html', context)


def updateOrder(request, id):
    order = Order.objects.get(id=id)
    form = orderForm(instance=order)
    if request.method == 'POST':
        form = orderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
        return redirect('/')
    context = {
        'form': form
        }
    return render(request, 'accounts/order_form.html', context)

def deleteOrder(request, id):
    order = Order.objects.get(id=id)
    if request.method == "POST":
        order.delete()
        return redirect('/')
    context={
        'order' : order
    }
    return render(request, 'accounts/delete.html', context)
