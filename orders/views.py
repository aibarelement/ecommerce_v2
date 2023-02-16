from rest_framework import status
from rest_framework.mixins import RetrieveModelMixin, UpdateModelMixin, ListModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from utils import mixins

from . import models, serializers, permissions, services


class OrderItemViewSet(RetrieveModelMixin,
                       UpdateModelMixin,
                       ListModelMixin,
                       GenericViewSet):
    serializer_class = serializers.OrderItemSerializer
    queryset = models.OrderItem.objects.all()
    permission_classes = permissions.IsCustomer,


class OrderViewSet(mixins.ActionSerializerMixin, ModelViewSet):
    ACTION_SERIALIZERS = {
        'create': serializers.CreateOrderSerializer,
    }
    order_services: services.OrderReposInterface = services.OrderReposV1()
    serializer_class = serializers.OrderSerializer
    queryset = order_services.get_orders()
    permission_classes = permissions.IsCustomer,

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        order = self.order_services.create_order(data=serializer.validated_data)
        data = serializers.RetrieveOrderSerializer(order).data

        return Response(data, status=status.HTTP_201_CREATED)
