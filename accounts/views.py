from django.shortcuts import render, get_object_or_404

from .models import UserAccount


def account(request):
    """Display the user's account"""

    account = get_object_or_404(UserAccount, user=request.user)

    template = 'accounts/account.html'
    context = {
        'account': account,
    }

    return render(request, template, context)
