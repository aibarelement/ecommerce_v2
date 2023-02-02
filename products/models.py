import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _


class Product(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    title = models.CharField(max_length=255, verbose_name=_('Title'))
    body = models.TextField(verbose_name=_('Body'))
    main_image = models.ImageField(upload_to='products/%Y/%m/%d', verbose_name=_('Main image'))
    is_active = models.BooleanField(default=True, verbose_name=_('Is active?'))
    is_top = models.BooleanField(default=False, verbose_name=_('Is top?'))
    data = models.JSONField(default=dict, null=True, blank=True, verbose_name=_('Data'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created at'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Updated at'))

    class Meta:
        ordering = ('is_top', '-created_at')
        verbose_name = _('Product')
        verbose_name_plural = _('Products')


class ProductImage(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    product = models.ForeignKey(
        to=Product,
        on_delete=models.CASCADE,
        verbose_name=_('Product'),
        related_name='product_images'
    )
    image = models.ImageField(upload_to='product-images/%Y/%m/%d', verbose_name=_('Image'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created at'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Updated at'))

    class Meta:
        ordering = ('-created_at',)
        verbose_name = _('Product Image')
        verbose_name_plural = _('Product Images')
