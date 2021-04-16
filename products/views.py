from django.shortcuts import render, get_object_or_404
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


def product_detail(request, product_id):
    """
    View to show all individual product details
    """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)
