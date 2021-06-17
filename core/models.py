from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.translation import gettext_lazy as _

# Create your models here.


class Product(models.Model):
    image      = models.ImageField(_("Image"), upload_to="product-image/")
    name       = models.CharField(_("Name"), max_length=250)
    short_info = models.TextField(_("Short Info"), blank=True, null=True)
    price      = models.IntegerField(_("Price"), default=0, validators=(MinValueValidator(0), MaxValueValidator(10000000000)))

    def __str__(self):
        return self.name
    
    @property
    def imageURL(self):
        try:
            url=self.image.url
        except:
            url=''
        return url


class OrderedProduct(models.Model):
    order_title         = models.CharField(_("Order Title"), max_length=250) 
    order_products_info = models.TextField(_("Ordered Products"),)
    order_total_price   = models.IntegerField(_("Total Price"), default=0, validators=(MinValueValidator(0), MaxValueValidator(10000000000)))

    added_at            = models.DateTimeField(_("Added Date"), auto_now_add=True)
    updated_at          = models.DateTimeField(_("Updated Date"), auto_now=True)

    def __str__(self):
        return self.order_title
