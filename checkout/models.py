import uuid
from django.db import models
from django.db.models import Sum
from django.conf import settings

from destinations.models import Destination


class Order(models.Model):
    """set up an order model to handle the checkout info"""
    order_number = models.CharField(max_length=32, null=False, blank=False, editable=False)
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    town_or_city = models.CharField(max_length=50, null=False, blank=False)
    country = models.CharField(max_length=50, null=False, blank=False)
    date = models.DateTimeField(auto_now_add=True)
    total_count = models.IntegerField(null=False, blank=False, default=0)
    discount = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    order_total = models.DecimalField(max_digits=15, decimal_places=2, null=False, default=0)
    grand_total = models.DecimalField(max_digits=15, decimal_places=2, null=False, default=0)
    original_wallet = models.TextField(null=False, blank=False, default='')
    stripe_pid = models.CharField(max_length=254, null=False, blank=False, default='')

    def __str__(self):
        return self.order_number

    def _generate_order_number(self):
        """generate random unique order number"""
        return uuid.uuid4().hex.upper()

    def update_total(self):
        """update the grand total each time a line item is added
        accounting for discount"""
        self.order_total = self.lineitems.aggregate(Sum('lineitem_total'))['lineitem_total__sum'] or 0
        self.total_count = self.lineitems.aggregate(Sum('quantity'))['quantity__sum'] or 0
        if self.total_count > settings.DISCOUNT_WALLET_THRESHOLD:
            self.discount = self.order_total * settings.STANDARD_DISCOUNT_PERCENTAGE / 100
        else:
            self.discount = 0
        self.grand_total = self.order_total - self.discount
        self.save()

    def save(self, *args, **kwargs):
        """override save method to set order number if not already set"""
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)


class OrderLineItem(models.Model):
    """set up how we view the line items in our checkout app"""
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=False, blank=False, related_name='lineitems')
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE, null=False, blank=False)
    quantity = models.IntegerField(null=False, blank=False, default=0)
    lineitem_total = models.DecimalField(max_digits=15, decimal_places=2, null=False, blank=False, editable=False)

    def __str__(self):
        return f'{self.destination.slug} on order {self.order.order_number}'

    def save(self, *args, **kwargs):
        """override save method to set line item total price if not already set"""
        self.lineitem_total = self.destination.price * self.quantity
        super().save(*args, **kwargs)
