from rest_framework.viewsets import ModelViewSet

from utils import mixins
from . import models, serializers, permissions


class SellerProductViewSet(mixins.ActionSerializerMixin,
                           mixins.ActionPermissionMixin,
                           ModelViewSet):
    ACTION_SERIALIZERS = {
        'create': serializers.CreateSellerProductSerializer,
        'update': serializers.UpdateSellerProductSerializer,
        'partial_update': serializers.UpdateSellerProductSerializer,
    }
    ACTION_PERMISSIONS = {
        'update': (permissions.IsSellerAndOwner(),),
        'partial_update': (permissions.IsSellerAndOwner(),),
        'destroy': (permissions.IsSellerAndOwner(),),
    }
    serializer_class = serializers.SellerProductSerializer
    queryset = models.SellerProduct.objects.filter(is_active=True)
    permission_classes = permissions.IsSellerOrReadOnly,
