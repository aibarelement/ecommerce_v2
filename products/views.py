from django.db.models import Min, Q
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from utils import mixins
from . import models, serializers, permissions


class ProductImageViewSet(mixins.ActionSerializerMixin, ModelViewSet):
    serializer_class = serializers.ProductImageSerializer
    queryset = models.ProductImage.objects.all()


class ProductViewSet(mixins.ActionSerializerMixin, ModelViewSet):
    ACTION_SERIALIZERS = {
        'retrieve': serializers.RetrieveProductSerializer,
    }
    serializer_class = serializers.ProductSerializer
    queryset = models.Product.objects.annotate(
        min_amount=Min('seller_products__amount', filter=Q(seller_products__is_active=True)),
    )

    # def get_permissions(self):
    #     if self.action in ('list', 'retrieve'):
    #         return IsAuthenticated(),
    #
    #     return permissions.IsMe(),

    @action(['get'], detail=False, url_path='top-products')
    def top_products(self, request, *args, **kwargs):
        print(self.action)
        return super().list(request, *args, **kwargs)

    @action(['get'], detail=True, url_path='top-product')
    def top_product(self, request, *args, **kwargs):
        print(self.action)
        return super().retrieve(request, *args, **kwargs)
