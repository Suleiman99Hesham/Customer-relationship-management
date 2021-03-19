from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .filters import orderFilter
from .forms import orderForm, customerOrderForm, createUserForm
from django.forms import inlineformset_factory
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from .decorators import unauthenticated_user, allowed_users, admin_only

# Create your views here.

@unauthenticated_user
def register(request):
    form = createUserForm()
    if request.method == 'POST':
        form = createUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            group = Group.objects.get(name='customer')
            user.groups.add(group)
            messages.success(request, 'Account is created successfully for '+ username)
            return redirect('login')
    context = {
        'form' : form
        }
    return render(request, 'accounts/register.html', context)
@unauthenticated_user
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username OR Password is incorrect')
    context = {}
    return render(request, 'accounts/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
@admin_only
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

@login_required(login_url='login')
def user_page(request):
    context = {}
    return render(request, 'accounts/user-page.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def products(request):
    products = Product.objects.all()
    return render(request, 'accounts/products.html', {'products':products})

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def customer(request, id):
    customer = Customer.objects.get(id=id)
    total_orders = customer.order_set.all().count()
    orders = customer.order_set.all()
    myFilter = orderFilter(request.GET, queryset=orders)
    orders = myFilter.qs
    context = {
        'customer' : customer,
        'orders' : orders,
        'total_orders' : total_orders,
        'myFilter' : myFilter,
    }
    return render(request, 'accounts/customer.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
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
        return redirect('customer', customer.id)
    context = {
        'formset' : formset
    }
    return render(request, 'accounts/order_form.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def updateCustomerOrder(request, id):
    order = Order.objects.get(id=id)
    form = customerOrderForm(instance=order)
    if request.method == 'POST':
        form = customerOrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
        return redirect('customer' ,order.customer.id)
    context ={
        'form' : form
    }
    return render(request, 'accounts/update_customer_order.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
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
    return render(request, 'accounts/update_order.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def deleteOrder(request, id):
    order = Order.objects.get(id=id)
    if request.method == "POST":
        order.delete()
        return redirect('/')
    context={
        'order' : order
    }
    return render(request, 'accounts/delete.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def deleteCustomerOrder(request, id):
    order = Order.objects.get(id=id)
    if request.method == "POST":
        order.delete()
        return redirect('customer' ,order.customer.id)
    context={
        'order' : order
    }
    return render(request, 'accounts/delete_customer_order.html', context)
