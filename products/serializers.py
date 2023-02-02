from rest_framework import serializers

from . import models


class ProductImageSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)

    class Meta:
        model = models.ProductImage
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)

    class Meta:
        model = models.Product
        fields = '__all__'


class RetrieveProductSerializer(ProductSerializer):
    product_images = ProductImageSerializer(many=True, read_only=True)
