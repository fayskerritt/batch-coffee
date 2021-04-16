from django.shortcuts import render
from .models import Product


def all_products(request):
    """
    View to show all products,
    with sort and search functionality
    """

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/shop.html', context)
