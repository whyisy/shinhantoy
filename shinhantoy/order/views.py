from rest_framework import generics, mixins

from .models import Order
from .serializers import OrderSerializer


class OrderListView(
    mixins.ListModelMixin,
    generics.GenericAPIView
):

    serializer_class = OrderSerializer

    def get_queryset(self):
        orders = Order.objects.all()
        return orders
    
    def get(self, request, *args, **kwargs):
        return self.list(request, args, kwargs)