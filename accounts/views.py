from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import UserAccount
from .forms import UserAccountForm

from checkout.models import Order
# from datetime import date


@login_required
def account(request):
    """Display the user's account"""

    account = get_object_or_404(UserAccount, user=request.user)

    form = UserAccountForm(instance=account)
    orders = account.orders.all()

    template = 'accounts/account.html'
    context = {
        'form': form,
        'orders': orders,
        'on_account_page': True,
    }

    return render(request, template, context)


@login_required
def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order no. {order_number}. '
        'A confirmation email was sent to you on the order date.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)


@login_required
def account_details(request):
    """Return account details page"""

    account = get_object_or_404(UserAccount, user=request.user)

    if request.method == 'POST':
        form = UserAccountForm(request.POST, instance=account)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your details were updated successfully')

    form = UserAccountForm(instance=account)

    template = 'accounts/account_details.html'
    context = {
        'form': form,
        'on_account_page': True,
    }

    return render(request, template, context)


@login_required
def account_orders(request):
    """Return account details page"""

    account = get_object_or_404(UserAccount, user=request.user)
    orders = account.orders.all()

    template = 'accounts/account_orders.html'
    context = {
        'orders': orders,
        'from_profile': True,
    }

    return render(request, template, context)
