from django.shortcuts import render


def index(request):
    """ View to return index page"""
    return render(request, 'home/index.html')
