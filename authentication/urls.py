from django.urls import path
from .views import *

urlpatterns = [
	path('signup/', UserCreate.as_view(), name='signup'),
]
