
from django.urls import path
from interview.order.views import OrderListCreateView, OrderTagListCreateView,OrderListBetweenDatesView


urlpatterns = [
    path('tags/', OrderTagListCreateView.as_view(), name='order-detail'),
    path('orders-between-dates/',OrderListBetweenDatesView.as_view(),name='orders-between-dates'),
    path('', OrderListCreateView.as_view(), name='order-list'),

]