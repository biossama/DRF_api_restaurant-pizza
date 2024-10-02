from rest_framework import serializers
from .models import Order


class OrderSerializer(serializers.ModelSerializer):
	size = serializers.CharField(max_length=30)
	order_status = serializers.HiddenField(default='PENDING')
	quantity = serializers.IntegerField()

	class Meta:
		model = Order
		fields = ['id', 'size', 'order_status','quantity']


class OrderUpdateStatusSerializer(serializers.ModelSerializer):

	order_status = serializers.CharField(default='PENDING')

	class Meta:
		model = Order
		fields = ['order_status']


class OrderDetailSerializer(serializers.ModelSerializer):

	class Meta:
		model = Order
		exclude=('customer',)
