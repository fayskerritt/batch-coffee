from django.shortcuts import render


def shopping_bag(request):
    """ View to render shopping bag page """

    return render(request, 'bag/bag.html')
