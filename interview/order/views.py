from interview.order.models import OrderTag
from interview.order.serializers import OrderTagSerializer
from rest_framework import generics
from django.utils import timezone
from interview.order.models import Order
from interview.order.serializers import OrderSerializer

# Create your views here.
class OrderListCreateView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    

class OrderTagListCreateView(generics.ListCreateAPIView):
    queryset = OrderTag.objects.all()
    serializer_class = OrderTagSerializer


class OrderListBetweenDatesView(generics.ListAPIView):
    serializer_class = OrderSerializer

    def get_queryset(self):
        # Get the start and embargo date from the query parameters
        start_date = self.request.query_params.get('start_date')
        embargo_date = self.request.query_params.get('embargo_date')

        # Convert date strings to datetime objects
        start_date = timezone.datetime.strptime(start_date, '%Y-%m-%d')
        embargo_date = timezone.datetime.strptime(embargo_date, '%Y-%m-%d')

        # Filter orders between the start and embargo date
        queryset = Order.objects.filter(date__range=[start_date, embargo_date])
        return queryset
