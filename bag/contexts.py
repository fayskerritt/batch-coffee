from decimal import Decimal
from django.conf import settings


def bag_contents(request):

    bag_items = []
    total = 0
    product_count = 0
    delivery = settings.DELIVERY_COST

    if total > settings.DISCOUNT_THRESHOLD:
        discount = Decimal(settings.DISCOUNT_AMOUNT)
    else:
        discount = 0

    grand_total = (delivery + total) + discount

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'discount_threshold': settings.DISCOUNT_THRESHOLD,
        'discount': settings.DISCOUNT_AMOUNT,
        'grand_total': grand_total,
    }

    return context
