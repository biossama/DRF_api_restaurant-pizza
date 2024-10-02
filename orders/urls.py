from django.urls import path
from . import views


urlpatterns = [

	path('orders/', views.GetCreateOrder.as_view(), name="orders"),
	path('order/<int:pk>', views.OrderDetails.as_view(), name="order"),
	path('update/<int:pk>', views.OrderDetails.as_view()),
	path('order/update-status/<int:pk>', views.OrderUpdateStatus.as_view()),
	path('user/<int:user_id>/', views.UserOrders.as_view()),
	path('user/<int:user_id>/detail/<int:order_id>', views.UserOrderDetail.as_view()),
	path('partial-update/<int:pk>', views.OrderDetails.as_view()),
	path('delete/<int:pk>', views.OrderDetails.as_view()),
]
