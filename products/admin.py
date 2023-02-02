from django.contrib import admin
from . import models


class ProductImageInline(admin.TabularInline):
    model = models.ProductImage
    extra = 0


class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active', 'is_top')
    list_filter = ('is_active', 'is_top')
    list_editable = ('is_active', 'is_top')
    search_fields = ('title', 'body')
    inlines = (ProductImageInline,)


admin.site.register(models.ProductImage)
admin.site.register(models.Product, ProductAdmin)
