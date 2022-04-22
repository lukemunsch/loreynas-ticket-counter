from django.shortcuts import render


def view_wallet(request):
    """set up our wallet view to hold our 
    tickets for purchasing when ready"""
    return render(request, 'wallet/wallet.html')
