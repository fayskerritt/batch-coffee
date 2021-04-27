from django.shortcuts import render


def account(request):
    """Display the user's account"""

    template = 'accounts/account.html'
    context = {}

    return render(request, template, context)
