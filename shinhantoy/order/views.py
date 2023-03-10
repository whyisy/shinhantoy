from rest_framework import generics, mixins

from .models import Order, Comment
from .serializers import OrderSerializer, CommentSerializer, CommentCreateSerializer


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


class OrderDetailView(
    mixins.RetrieveModelMixin,
    generics.GenericAPIView
):
    serializer_class = OrderSerializer

    def get_queryset(self):
        return Order.objects.all()

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, args, kwargs)


class CommentListView(
    mixins.ListModelMixin,
    generics.GenericAPIView
):
    serializer_class = CommentSerializer
    def get_queryset(self):
        order_id = self.kwargs.get('order_id')
        if order_id:
            return Comment.objects.filter(order_id=order_id) \
                .select_related('member','order')\
                .order_by('-id')   \
                
        return Comment.objects.none()

    
    def get(self, request, *args, **kwargs):
        return self.list(request, args, kwargs)


class CommentCreateView(
    mixins.CreateModelMixin,
    generics.GenericAPIView
):
    serializer_class = CommentCreateSerializer
 
    # def get_queryset(self):   #안써도 됨
    #     return Comment.objects.all()

    def post(self,request, *args, **kwargs):
        return self.create(request, args, kwargs)