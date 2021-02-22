from django.db import models

# Create your models here.

class Customer(models.Model):

    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.EmailField(max_length=254, null=True)
    date_created  = models.DateTimeField(auto_now_add=True, null=True)
    
    def calculateOrders(self):
        return Order.objects.filter(customer=self).count()

    num_of_orders = property(calculateOrders)

    def __str__(self):
        return self.name

class Tag(models.Model):

    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    CATEGORY = (
        ('Indoor', 'Indoor'),
        ('Out Door', 'Out Door'),
    )
    name = models.CharField(max_length=200, null=True)
    price = models.FloatField(max_length=200)
    category = models.CharField(max_length=200, null=True, choices=CATEGORY)
    description = models.CharField(max_length=200, blank=True, null=True)
    date_created  = models.DateTimeField(auto_now_add=True, null=True)
    tag = models.ManyToManyField(Tag)
    
    def __str__(self):
        return self.name

class Order(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Out for delivery', 'Out for delivery'),
        ('Delivered', 'Delivered'),
    )
    customer = models.ForeignKey(Customer,null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product,null=True, on_delete=models.SET_NULL)
    
    date_created  = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)
    
    def __str__(self):
        return self.product.name