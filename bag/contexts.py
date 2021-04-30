from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product


def bag_contents(request):
    """Get the contents of the shopping bag"""
    bag_items = []
    total = 0
    product_count = 0
    delivery = settings.DELIVERY_COST
    bag = request.session.get('bag', {})

    for product_id, quantity in bag.items():
        product = get_object_or_404(Product, pk=product_id)
        total += quantity * product.price
        product_count += quantity
        bag_items.append({
            'product_id': product_id,
            'quantity': quantity,
            'product': product,
        })

    if total < settings.DISCOUNT_THRESHOLD:
        discount_difference = settings.DISCOUNT_THRESHOLD - total
        discount = 0
    else:
        discount = settings.DISCOUNT_AMOUNT
        discount_difference = 0

    discounted_total = Decimal(total) - Decimal(discount)

    grand_total = Decimal(discounted_total) + Decimal(delivery)

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'discount_threshold': settings.DISCOUNT_THRESHOLD,
        'discount': settings.DISCOUNT_AMOUNT,
        'discount_difference': discount_difference,
        'grand_total': grand_total,
    }

    return context
