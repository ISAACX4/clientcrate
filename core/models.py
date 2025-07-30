from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import User
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
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    item_description = models.TextField()
    status = models.CharField(max_length=100, choices=ORDER_STATUS, default='pending')  # ✅ FIXED
    delivery_date = models.DateField()
    is_paid = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
