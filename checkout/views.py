from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.contrib import messages
from django.conf import settings
from .forms import OrderForm

from wallet.contexts import wallet_contents
import stripe

from destinations.models import Destination
from .models import Order, OrderLineItem


def checkout(request):
    """set up our view for checking out our wallet"""
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        wallet = request.session.get('wallet', {})

        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'town_or_city': request.POST['town_or_city'],
            'country': request.POST['country'],
        }

        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save()
            for ticket_id, quantity in wallet.items():
                try:
                    destination = Destination.objects.get(id=ticket_id)
                    order_line_item = OrderLineItem(
                        order=order,
                        destination=destination,
                        quantity=quantity,
                    )
                    order_line_item.save()

                except Destination.DoesNotExist:
                    messages.error(
                        request,
                        ("One of the destinations in your wallet wasn't found in our database."
                        "Please call us for assistance!")
                    )
                    order.delete()
                    return redirect(reverse('view_wallet'))

            # Save the info to the user's profile if all is well
            request.session['save-info'] = 'save-info' in request.POST
            return redirect(reverse(
                'checkout_success',
                args=[order.order_number]
            ))
        else:
            messages.error(request, (
                'There was an error with your form. '
                'Please double check your information.'))

    else:
        wallet = request.session.get('wallet', {})

        if not wallet:
            messages.error(request, 'You have forgotten to add tickets to your wallet!')
            return redirect(reverse('destinations'))

        current_wallet = wallet_contents(request)
        total = current_wallet['grand_total']
        stripe_total = round(total * 100)

        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

        order_form = OrderForm()

    if not stripe_public_key:
        messages.warning(request, 'Your Public Key is missing; did you forget to set it in your environement?')

    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'stripe_public_key',
        'client_secret': 'intent.client_secret',
    }
    return render(request, template, context)


def checkout_success(request, order_number):
    """set up the view for when our payments are successful"""
    save_info = request.session.get('save-info')
    order = get_object_or_404(Order, order_number=order_number)

    messages.success(request, f'Order successfully Processed! \
        Your order number is {order_number}. A confirmation \
        email will be sent to {order.email}')

    if 'wallet' in request.session:
        del request.session['wallet']

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }
    return render(request, template, context)
