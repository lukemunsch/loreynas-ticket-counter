from django.shortcuts import render, reverse, redirect
from django.contrib import messages
from .forms import OrderForm


def checkout(request):
    """set up our view for checking out our wallet"""
    wallet = request.session.get(wallet, {})
    if not wallet:
        messages.error(request, 'You have forgotten to add tickets to your wallet!')
        return redirect(reverse('destinations'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
    }
    return render(request, template, context)
