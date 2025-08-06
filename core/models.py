from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Define status choices
ORDER_STATUS = [
    ('pending', 'Pending'),
    ('processing', 'Processing'),
    ('delivered', 'Delivered'),
    ('cancelled', 'Cancelled'),
]

class BusinessProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    business_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    logo = models.ImageField(upload_to='logos/', blank=True)

    def __str__(self):
        return self.business_name

class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return self.name

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.CharField(max_length=100)
    status = models.CharField(
        max_length=20,
        choices=ORDER_STATUS,
        default='pending'  # You can change this default if needed
    )
    delivery_date = models.DateField(null=True, blank=True)
    item_description = models.TextField(null=True, blank=True)
    is_paid = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.customer} - {self.product}"


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField(default=0)
    category = models.CharField(max_length=100, blank=True)
    image = models.ImageField(upload_to='product_images/', null=True, blank=True) 

    def __str__(self):
        return self.name