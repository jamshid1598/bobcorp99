from django.contrib import admin

# Register your models here.

from .models import OrderedProduct, Product


class ProductAdmin(admin.ModelAdmin):
    list_display=('name', 'price',)
    list_display_links=('name',)
    list_editble=('price',)
    list_ordering=('name', 'price',)
    search_fields=('name', 'price',)

    fieldsets = (
        ("Product Info", {
            "fields": (
                'image', 'name', 'price', 'short_info',
            ),
        }),
    )

admin.site.register(Product, ProductAdmin)


class OrderedProductAdmin(admin.ModelAdmin):
    list_display=('order_title', 'order_products_info', 'total_price', 'added_at', 'updated_at',)
    list_display_links=('order_title', 'order_products_info', 'total_price', 'added_at', 'updated_at',)
    # list_editble=('order_title', 'order_products_info', 'order_total_price',)
    list_ordering=('order_title', 'order_products_info', 'total_price', 'added_at', 'updated_at',)
    search_fields=('order_title', 'order_products_info', 'total_price', 'added_at', 'updated_at',)

    def total_price(self, obj):
        return str(obj.order_total_price)+" so'm"

    fieldsets = (
        ("Ordered Product Info", {
            "fields": (
                'order_title', 'order_products_info', 'order_total_price', 
            ),
        }),
    )

admin.site.register(OrderedProduct, OrderedProductAdmin)