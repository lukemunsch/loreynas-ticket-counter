from django.shortcuts import render


def profile(request):
    """display the user's profle"""
    template = 'profiles/profile.html'
    context = {}

    return render(request, template, context)
