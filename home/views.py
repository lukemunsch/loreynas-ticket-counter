from django.shortcuts import render


def index(request):
    """set up our index view"""
    return render(request, 'home/index.html')
