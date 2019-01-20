from django.db import models

# Create your models here.
class Customer(models.Model):
    customer_name = models.CharField(max_length=10)
    phone = models.CharField(max_length=10)
    city = models.CharField(max_length=10)
    def __str__(self):
        return self.customer_name

class Product(models.Model):
    product_name = models.CharField(max_length=20)
    purchase_price = models.IntegerField( )
    order_cost = models.IntegerField()
    holding_cost = models.IntegerField( )
    selling_price = models.IntegerField( )
    inventory_quantity = models.IntegerField( )
    order_time = models.IntegerField( )
    def __str__(self):
        return self.product_name

class Order(models.Model):
    order_No = models.IntegerField()
    created_time = models.DateField()
    product = models.ForeignKey('Product')
    quantity = models.IntegerField()  
    customer_name = models.ForeignKey('Customer')
    def __str__(self):
        order_str = str(self.customer_name)+ ',' + str(self.quantity) + '台 ' + str(self.product)
        return order_str
