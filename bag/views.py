from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.contrib import messages

from products.models import Product


def shopping_bag(request):
    """ View to render shopping bag page """

    return render(request, 'bag/bag.html')


def add_to_bag(request, product_id):
    """ Add specific quantity of product to shopping bag """

    product = get_object_or_404(Product, pk=product_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if product_id in list(bag.keys()):
        bag[product_id] += quantity
        messages.success(
            request, f'Another {product.name} was added to your shopping bag')
    else:
        bag[product_id] = quantity
        messages.success(
            request, f'{product.name} was added to your shopping bag')

    request.session['bag'] = bag
    return redirect(redirect_url)


def update_bag(request, product_id):
    """Update bag with new quantities"""

    product = get_object_or_404(Product, pk=product_id)
    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})

    if quantity > 0:
        bag[product_id] = quantity
        messages.success(
            request, f'Updated {product.name} quantity to {bag[product_id]}')
    else:
        bag.pop(product_id)
        messages.success(
            request, f'Removed {product.name} from your shopping bag')

    request.session['bag'] = bag
    return redirect(reverse('shopping_bag'))


def remove_from_bag(request, product_id):
    """ Remove item from shopping bag """

    try:
        product = get_object_or_404(Product, pk=product_id)
        bag = request.session.get('bag', {})

        bag.pop(product_id)
        messages.success(
            request, f'Removed {product.name} from your shopping bag')

        request.session['bag'] = bag
        return redirect(reverse('shopping_bag'))

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
