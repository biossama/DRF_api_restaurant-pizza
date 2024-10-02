from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import AnonymousUser
from authentication.models import User
from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .serializers import OrderSerializer, OrderUpdateStatusSerializer, OrderDetailSerializer
from .models import Order
from drf_yasg.utils import swagger_auto_schema
# Create your views here.

class GetCreateOrder(generics.GenericAPIView):

	queryset = Order.objects.all()
	serializer_class = OrderSerializer
	permission_classes = [IsAuthenticated]

	@swagger_auto_schema(operation_summary="List Orders")
	def get(self, request):
		orders = Order.objects.all()
		serializer = self.serializer_class(instance=orders, many=True)
		return Response(serializer.data, status = status.HTTP_200_OK)

	@swagger_auto_schema(operation_summary="Create a new order")
	def post(self, request):
		user = request.user
		serializer = self.serializer_class(data=request.data)
		if serializer.is_valid():
			serializer.save(customer=user)
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class OrderDetails(generics.GenericAPIView):
	serializer_class = OrderSerializer
	permission_classes = [IsAuthenticated]


	@swagger_auto_schema(operation_summary="Get an order by id")
	def get(self, request, pk):
		order = get_object_or_404(Order, id=pk)
		serializer = self.serializer_class(instance=order ,many=False)
		return Response(serializer.data, status=status.HTTP_200_OK)

	@swagger_auto_schema(operation_summary="Update an order by id")
	def put(self, request, pk):
		order = get_object_or_404(Order, id=pk)
		serializer = self.serializer_class(data=request.data, instance=order)
		if serializer.is_valid():
			serializer.save(customer=request.user)
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	@swagger_auto_schema(operation_summary="Update an element of order by id")
	def patch(self, request, pk):
		order = get_object_or_404(Order, id=pk)
		serializer = self.serializer_class(data=request.data, instance=order, partial=True)
		if serializer.is_valid():
			serializer.save(customer=request.user, **request.data)
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	@swagger_auto_schema(operation_summary="Delete order by id")
	def delete(self, request, pk):
		order = get_object_or_404(Order, id=pk)
		order.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)


class OrderUpdateStatus(generics.GenericAPIView):
	serializer_class = OrderUpdateStatusSerializer


	def get(self, request, pk):
		order = get_object_or_404(Order, id=pk)
		serializer = self.serializer_class(instance=order)
		return Response(serializer.data, status=status.HTTP_200_OK)

	def put(self, request, pk):
		order = get_object_or_404(Order, id=pk)
		serializer = self.serializer_class(instance=order, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserOrders(generics.GenericAPIView):
	queryset = Order.objects.all()
	permission_classes = [IsAuthenticated, IsAdminUser]
	serializer_class = OrderSerializer

	@swagger_auto_schema(operation_summary="Get all orders of a specific user")
	def get(self, request, user_id):
		user = get_object_or_404(User, id=user_id)
		#print(user)
		orders =  Order.objects.all().filter(customer=user)
		serializer = self.serializer_class(instance=orders, many=True)
		return Response(serializer.data, status=status.HTTP_200_OK)
	#	return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

class UserOrderDetail(generics.GenericAPIView):

	serializer_class = OrderDetailSerializer
	permission_classes = [IsAuthenticated, IsAdminUser]

	@swagger_auto_schema(operation_summary="Check the order of specific user")
	def get(self, request, user_id, order_id):
		user = get_object_or_404(User, id=user_id)
		order_by_customer = Order.objects.all().filter(customer=user)
		order= get_object_or_404(order_by_customer, id=order_id)
#		if order  is not None:
		serializer = self.serializer_class(instance=order)
		return Response(serializer.data, status=status.HTTP_200_OK)
#		return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

