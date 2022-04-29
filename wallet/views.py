from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.contrib import messages

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
        messages.success(request, (
            f'We have updated {destination.name} ticket '
            f'quantity to {wallet[ticket_id]}'))
    else:
        wallet[ticket_id] = quantity
        messages.success(request, (
            f'We have successfully added {destination.name} x{wallet[ticket_id]} '
            f'to your wallet!'))
    
    request.session['wallet'] = wallet
    return redirect(redirect_url)


def update_wallet(request, ticket_id):
    """Update quantity of a specific ticket in the wallet"""

    destination = get_object_or_404(Destination, pk=ticket_id)
    quantity = int(request.POST.get('quantity'))
    wallet = request.session.get('wallet', {})

    if quantity > 0:
        wallet[ticket_id] = quantity
        messages.success(request, (
            f'We have updated {destination.name} ticket '
            f'quantity to {wallet[ticket_id]}'))
    else:
        wallet.pop(ticket_id)
        messages.warning(request, (
            f'We have removed {destination.name} '
            f'from your wallet'))
    
    request.session['wallet'] = wallet
    return redirect(reverse('view_wallet'))


def remove_from_wallet(request, ticket_id):
    """Remove specific ticket in the wallet when clicking remove"""
    try:
        destination = get_object_or_404(Destination, pk=ticket_id)
        quantity = int(request.POST.get('quantity'))
        wallet = request.session.get('wallet', {})

        wallet.pop(ticket_id)
        
        request.session['wallet'] = wallet
        return redirect(reverse('view_wallet'))

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
