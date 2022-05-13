from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from destinations.models import Destination


def wallet_contents(request):
    """set up the context for our wallet"""
    wallet_tickets = []
    total = 0
    ticket_count = 0
    wallet = request.session.get('wallet', {})

    for ticket_id, quantity in wallet.items():
        destination = get_object_or_404(Destination, pk=ticket_id)
        total += quantity * destination.price
        ticket_count += quantity
        wallet_tickets.append({
            'ticket_id': ticket_id,
            'quantity': quantity,
            'destination': destination,
        })

    if ticket_count >= settings.DISCOUNT_WALLET_THRESHOLD:
        discount = total * Decimal(settings.STANDARD_DISCOUNT_PERCENTAGE / 100)
        discount_wallet_delta = 0
    else:
        discount = 0
        discount_wallet_delta = settings.DISCOUNT_WALLET_THRESHOLD - ticket_count

    grand_total = total - discount

    context = {
        'wallet_tickets': wallet_tickets,
        'total': total,
        'ticket_count': ticket_count,
        'discount': discount,
        'discount_wallet_delta': discount_wallet_delta,
        'discount_wallet_threshold': settings.DISCOUNT_WALLET_THRESHOLD,
        'standard_discount_percentage': settings.STANDARD_DISCOUNT_PERCENTAGE,
        'grand_total': grand_total,
    }
    return context
