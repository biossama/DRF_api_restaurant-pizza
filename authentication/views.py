from django.shortcuts import render
from .serializers import UserSerializer
from rest_framework import generics, status
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
# Create your views here.

class UserCreate(generics.GenericAPIView):
	serializer_class = UserSerializer
	@swagger_auto_schema(operation_summary="Create your account")
	def post(self, request):
		serializer = self.serializer_class(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
