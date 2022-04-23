from django.shortcuts import render, redirect, get_object_or_404
from destinations.models import Destination


def view_wallet(request):
    """set up our wallet view to hold our 
    tickets for purchasing when ready"""
    return render(request, 'wallet/wallet.html')


def add_to_wallet(request, ticket_id):
    """Add a quantity of a specific ticket to the wallet"""

    destination = get_object_or_404(Destination, pk=ticket_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    wallet = request.session.get('wallet', {})

    if ticket_id in list(wallet.keys()):
        wallet[ticket_id] += quantity
    else:
        wallet[ticket_id] = quantity
    
    request.session['wallet'] = wallet
    return redirect(redirect_url)
