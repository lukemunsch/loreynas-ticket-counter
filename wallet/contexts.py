from decimal import Decimal
from django.conf import settings

def wallet_contents(request):
    """set up the context for our wallet"""
    wallet_tickets = []
    total = 0
    ticket_count = 0
    wallet = request.session.get('wallet', {})

    if ticket_count >= settings.DISCOUNT_WALLET_THRESHOLD:
        discount = total * Decimal(settings.STANDARD_DISCOUNT_PERCENTAGE / 100)
        discount_wallet_delta = settings.DISCOUNT_WALLET_THRESHOLD - ticket_count
    else:
        discount = 0
        discount_wallet_delta = 0

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