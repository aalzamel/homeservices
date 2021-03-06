from django.db import models
from services.models import Product
from django.contrib.auth.models import User
from django.db.models.signals import pre_save, post_save, post_delete
from decimal import Decimal


class CartItem(models.Model):
    cart = models.ForeignKey("Cart", on_delete=models.CASCADE)
    item = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    line_item_total = models.DecimalField(decimal_places = 3, max_digits = 20)

    def __str__(self):
        return self.item.name

def cart_item_pre_save_receiver(sender, instance, *args, **kwargs):
    qty = instance.quantity
    if Decimal(qty) >= 1:
        price = instance.item.price
        line_item_total = Decimal(qty)*Decimal(price)
        instance.line_item_total = line_item_total

pre_save.connect(cart_item_pre_save_receiver, sender=CartItem)

def cart_item_post_save_receiver(sender, instance, *args, **kwargs):
    instance.cart.update_subtotal()

post_save.connect(cart_item_post_save_receiver, sender=CartItem)
post_delete.connect(cart_item_post_save_receiver, sender=CartItem)

class Cart(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.PROTECT)
    items = models.ManyToManyField(Product, through=CartItem)
    subtotal = models.DecimalField(decimal_places = 3, max_digits = 50, default=2.000)
    delivery_total = models.DecimalField(decimal_places = 3, max_digits = 50, default=2.000)
    total = models.DecimalField(decimal_places = 3, max_digits = 50, default=2.000)

    def __str__(self):
        return str(self.id)

    def update_subtotal(self):
        subtotal = 0
        items = self.cartitem_set.all()
        for item in items:
            subtotal += item.line_item_total
        self.subtotal = "%.3f"%subtotal
        self.save()

def do_delivery_and_total(sender, instance, *args, **kwargs):
    subtotal = Decimal(instance.subtotal)
    delivery_total = Decimal(3.000)
    total = subtotal + delivery_total
    instance.delivery_total = "%.3f"%delivery_total
    instance.total = "%.3f"%total

pre_save.connect(do_delivery_and_total, sender=Cart)
# Create your models here.
