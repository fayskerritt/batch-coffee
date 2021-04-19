from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category, Variety


def all_products(request):
    """
    View to show all products,
    with sort and search functionality
    """

    products = Product.objects.all()
    query = None
    category = None
    variety = None

    if request.GET:
        if 'category' in request.GET and 'variety' not in request.GET:
            category = request.GET['category']
            products = products.filter(category__name__icontains=category)
            category = Category.objects.get(name=category)
        elif 'variety' in request.GET and 'category' not in request.GET:
            variety = request.GET['variety'].split(',')
            products = products.filter(
                variety__name__in=variety)
            variety = Variety.objects.filter(name__in=variety)
        elif 'category' in request.GET and 'variety' in request.GET:
            category = request.GET['category']
            variety = request.GET['variety']
            products = products.filter(category__name__contains=category).\
                filter(variety__name__contains=variety)
            category = Category.objects.get(name=category)
            variety = Variety.objects.filter(name=variety)
        else:
            messages.error(request, 'No matching products!')

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, 'No search criteria entered!')
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(
                description__icontains=query) | Q(
                    region__icontains=query) | Q(variety__icontains=query)
            products = products.filter(queries)

    context = {
        'products': products,
        'search_term': query,
        'current_category': category,
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
