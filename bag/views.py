from django.shortcuts import render, redirect


def shopping_bag(request):
    """ View to render shopping bag page """

    return render(request, 'bag/bag.html')


def add_to_bag(request, product_id):
    """ Add specific quantity of product to shopping bag """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if product_id in list(bag.keys()):
        bag[product_id] += quantity
    else:
        bag[product_id] = quantity

    request.session['bag'] = bag
    return redirect(redirect_url)
