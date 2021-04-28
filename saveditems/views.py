from django.shortcuts import render, reverse, redirect, get_list_or_404, get_object_or_404

from django.http import HttpResponseRedirect
from accounts.models import UserAccount
from .models import Product, SavedList, SavedItems


def saved_items(request):
    """A view to display saved items"""

    user = UserAccount.objects.get(user=request.user)
    print(f"USER {user}")
    saved_list = Product.objects.filter(saved_items__user_account=user)
    print(f'SAVED LIST {saved_list}')
    context = {
        'saved_list': saved_list,
    }

    return render(request, 'saveditems/saveditems.html', context)


def add_save(request, product_id):
    """Add and remove items from saved list"""

    item = get_object_or_404(Product, pk=product_id)
    user = UserAccount.objects.get(user=request.user)
    user_list, created = SavedList.objects.get_or_create(user_account=user)
    saved_items = Product.objects.filter(saved_items__user_account=user)

    if created:
        item.saved_items.add(user_list.id)
    else:
        if item in saved_items:
            item.saved_items.remove(user_list.id)
        else:
            item.saved_items.add(user_list.id)

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
