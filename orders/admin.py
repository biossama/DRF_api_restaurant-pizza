from django.contrib import admin
from .models import Order
# Register your models here.


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
	list_display = ['customer', 'size', 'order_status', 'quantity', 'create_at']
	list_filter = ['create_at', 'customer', 'order_status', 'size']
