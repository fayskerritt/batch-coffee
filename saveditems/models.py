from django.db import models
from products.models import Product
from accounts.models import UserAccount


class SavedList(models.Model):
    """Display saved items by user"""
    user_account = models.OneToOneField(
        UserAccount, on_delete=models.CASCADE, null=False, blank=False,
        related_name='saved_list')
    items = models.ManyToManyField(Product, through='SavedItems',
                                   related_name='saved_items')

    def __str__(self):
        return f'Saved List ({self.user_account})'


class SavedItems(models.Model):
    saved_list = models.ForeignKey(SavedList, null=False, blank=False,
                                   on_delete=models.CASCADE,
                                   related_name='saved_list')
    product = models.ForeignKey(Product, null=False, blank=False,
                                on_delete=models.CASCADE,
                                related_name='saved_list')

    def __str__(self):
        return self.product.name
