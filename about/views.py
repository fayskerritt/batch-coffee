from django.shortcuts import render


def about(request):
    """View to return the about page"""

    return render(request, 'about/about.html')
