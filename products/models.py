from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=260)
    display_name = models.CharField(max_length=260, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_display_name(self):
        return self.display_name


class Product(models.Model):
    BAG_SIZES = (
        ('250g', '250 grams'),
        ('500g', '500 grams'),
    )
    category = models.ForeignKey(
        'Category', null=True, on_delete=models.CASCADE)
    sku = models.CharField(max_length=254, null=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    bag_size = models.CharField(max_length=4, choices=BAG_SIZES)
    region = models.CharField(max_length=254, null=True, blank=True)
    variety = models.CharField(max_length=254, null=True)
    altitude = models.CharField(max_length=20, null=True, blank=True)
    strength = models.DecimalField(
        null=True, max_digits=2, decimal_places=0, validators=[
            MinValueValidator(0), MaxValueValidator(10)])
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)

    def __str__(self):
        return self.name
