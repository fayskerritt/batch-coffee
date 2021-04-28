from django.shortcuts import render, get_list_or_404

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
