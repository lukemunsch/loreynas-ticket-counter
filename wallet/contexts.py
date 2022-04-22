from decimal import Decimal
from django.conf import settings

def wallet_contents(request):
    """set up the context for our wallet"""
    wallet_tickets = []
    total = 0
    ticket_count = 0

    if ticket_count >= settings.DISCOUNT_WALLET_THRESHOLD:
        discount = total * Decimal(settings.STANDARD_DISCOUNT_PERCENTAGE / 100)
        discount_wallet_delta = settings.DISCOUNT_WALLET_THRESHOLD - ticket_count
    else:
        discount = 0

    grand_total = total

    context = {}
    return context