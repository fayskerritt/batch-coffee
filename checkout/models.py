import uuid

from django.db import models
from django.db.models import Sum
from django.conf import settings
from datetime import timedelta, date

from django_countries.fields import CountryField

from products.models import Product
from accounts.models import UserAccount


class Order(models.Model):
    order_number = models.CharField(max_length=32, null=False, editable=False)
    user_account = models.ForeignKey(UserAccount, on_delete=models.SET_NULL,
                                     null=True, blank=True,
                                     related_name='orders')
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    county = models.CharField(max_length=80, null=True, blank=True)
    postcode_zipcode = models.CharField(max_length=20, null=True, blank=True)
    country = CountryField(blank_label='Country *', null=False, blank=False)
    date = models.DateTimeField(auto_now_add=True)
    expected_delivery_date = models.DateField(null=True, blank=True)
    delivery_cost = models.DecimalField(
        max_digits=6, decimal_places=2, null=False, default=0)
    sub_total = models.DecimalField(
        help_text="Total before discount IF order qualifies for disount",
        max_digits=10, decimal_places=2, null=False, default=0)
    order_total = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=0)
    grand_total = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=0)
    original_bag = models.TextField(null=False, blank=False, default='')
    stripe_pid = models.CharField(
        max_length=254, null=False, blank=False, default='')

    def _generate_order_number(self):
        """Generate random unique order number using UUID"""

        return uuid.uuid4().hex.upper()

    def update_total(self):
        """Update grand total each time a line item is added inc delivery"""

        self.order_total = self.lineitems.aggregate(Sum('lineitem_total'))[
            'lineitem_total__sum'] or 0
        if self.order_total > settings.DISCOUNT_THRESHOLD:
            self.sub_total = self.lineitems.aggregate(Sum('lineitem_total'))[
                'lineitem_total__sum'] or 0
            self.order_total = self.order_total - settings.DISCOUNT_AMOUNT
            self.delivery_cost = settings.DELIVERY_COST
        else:
            self.delivery_cost = settings.DELIVERY_COST
        self.grand_total = self.order_total + self.delivery_cost
        self.save()

    def save(self, *args, **kwargs):
        """
        Override original save method to set order number if not already set
        """

        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

        delivery_time = timedelta(days=2)
        self.expected_delivery_date = self.date + delivery_time

    def get_total_items(self):
        """Get total no. of items in order"""
        total_items = self.lineitems.aggregate(Sum('quantity'))[
            'quantity__sum']
        return total_items

    def get_delivery_status(self):
        """Is item past delivery date"""
        delivery_status = 0
        if date.today() > self.expected_delivery_date:
            delivery_status = 3
        if date.today() <= self.expected_delivery_date:
            delivery_status = 2
        elif date.today() == self.date:
            delivery_status = 1
        return delivery_status

    def __str__(self):
        return self.order_number


class OrderLineItem(models.Model):
    order = models.ForeignKey(
        Order, null=False, blank=False, on_delete=models.CASCADE,
        related_name='lineitems')
    product = models.ForeignKey(
        Product, null=False, blank=False, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, blank=False, default=0)
    lineitem_total = models.DecimalField(
        max_digits=6, decimal_places=2, null=False,
        blank=False, editable=False)

    def save(self, *args, **kwargs):
        """
        Override original save method to set lineitem total
        and update order total
        """

        self.lineitem_total = self.product.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f'SKU {self.product.sku} on order {self.order.order_number}'
