from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Product, Category, Variety
from .forms import ProductForm

from comments.models import Comment
from comments.forms import CommentForm
from accounts.models import UserAccount


def all_products(request):
    """
    View to show all products,
    with sort and search functionality
    """

    products = Product.objects.all()
    query = None
    category = None
    variety = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))

            if sortkey == 'category':
                sortkey = 'category__name'

            if sortkey == "strength":
                sortkey = 'lower_strength'
                products = products.annotate(lower_strength=Lower("strength"))

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'category' in request.GET and 'variety' not in request.GET:
            category = request.GET['category']
            products = products.filter(category__name__icontains=category)
            category = Category.objects.get(name=category)

        elif 'variety' in request.GET and 'category' not in request.GET:
            variety = request.GET['variety'].split(',')
            products = products.filter(variety__name__icontains=variety[0])
            variety = Variety.objects.filter(name__in=variety)

        elif 'category' in request.GET and 'variety' in request.GET:
            category = request.GET['category']
            variety = request.GET['variety']
            products = products.filter(
                category__name__contains=category).filter(
                variety__name__contains=variety)
            category = Category.objects.get(name=category)
            variety = Variety.objects.filter(name=variety)
        # else:
        #     messages.error(request, 'No matching products!')

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.warning(request, 'No search criteria entered!')
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(
                description__icontains=query) | Q(
                    region__icontains=query) | Q(
                        category__name__icontains=query) | Q(
                            variety__name__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'
    varieties = Variety.objects.all()

    if request.user.is_authenticated:
        user = UserAccount.objects.get(user=request.user)
        saved_list = Product.objects.filter(saved_items__user_account=user)
    else:
        user = None
        saved_list = None

    context = {
        'products': products,
        'search_term': query,
        'current_category': category,
        'current_variety': variety,
        'varieties': varieties,
        'current_sorting': current_sorting,
        'saved_list': saved_list,
    }

    return render(request, 'products/shop.html', context)


def product_detail(request, product_id):
    """
    View to show all individual product details
    """

    product = get_object_or_404(Product, pk=product_id)
    saved = False
    if request.user.is_authenticated:
        user = UserAccount.objects.get(user=request.user)
        saved_list = Product.objects.filter(saved_items__user_account=user)
        if product in saved_list:
            saved = True

    comments = Comment.objects.filter(product=product_id)

    form = CommentForm()
    if request.method == 'POST':
        form_data = {
            'comment': request.POST['comment'],
        }

        comment_form = CommentForm(form_data)

        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.product = product
            new_comment.user = UserAccount.objects.get(user=request.user)
            new_comment.post = product
            new_comment.save()
            messages.success(request, 'Your comment has been posted')

    if request.user.is_authenticated:
        user = UserAccount.objects.get(user=request.user)
    else:
        user = "Anonymous"

    context = {
        'product': product,
        'saved': saved,
        'comments': comments,
        'user': user,
        'form': form,
    }

    return render(request, 'products/product_detail.html', context)


def add_product(request):
    """ Add a product to the site """

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product added!')
            return redirect(reverse('add_product'))
        else:
            messages.error(
                request, 'Failed to add product. Please ensure form is valid')
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
