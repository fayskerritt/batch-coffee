from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Comment
from .forms import CommentForm
from accounts.models import UserAccount
from .models import Product


def comments(request, product_id):
    """View and post comments to product_detail page"""

    # item = get_object_or_404(Product, pk=product_id)
    # user = UserAccount.objects.get(user=request.user)
    # comments = Comment.objects.order_by('_comment_date')

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
