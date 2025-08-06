from django.contrib import admin
from .models import BusinessProfile, Customer, Order

@admin.register(BusinessProfile)
class BusinessProfileAdmin(admin.ModelAdmin):
    list_display = ['business_name', 'phone', 'user']

@admin.register(Customer)# This connects the Customer model to the admin panel using the CustomerAdmin settings
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'email']
    search_fields = ['name', 'phone']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['customer', 'status', 'delivery_date', 'is_paid', 'created_at']
    list_filter = ['status', 'is_paid']
    search_fields = ['customer__name', 'item_description']
