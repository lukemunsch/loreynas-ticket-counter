from django.http import HttpResponse
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings

from .models import Order, OrderLineItem
from profiles.models import UserProfile
from destinations.models import Destination

import json
import time


class StripeWH_Handler:
    """handle stripe webhooks"""
    def __init__(self, request):
        self.request = request

    def _send_confirmatin_email(self, order):
        """send the user a confirmation email about their order"""
        cust_email = order.email
        subject = render_to_string(
            'checkout/confirmation_emails/confirmation_email_subject.txt',
            {'order': order})
        body = render_to_string(
            'checkout/confirmation_emails/confirmation_email_body.txt',
            {'order': order, 'contact_email': settings.DEFAULT_FROM_EMAIL})

        send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            [cust_email]
        )

    def handle_event(self, event):
        """handle generic/unknown/unexpect webhooks events"""
        return HttpResponse(
            content=f'Unhandled Webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """handle successful payment intent webhooks from stripe"""
        intent = event.data.object
        pid = intent.id
        wallet = intent.metadata.wallet
        save_info = intent.metadata.save_info

        billing_details = intent.charges.data[0].billing_details
        grand_total = round(intent.charges.data[0].amount / 100, 2)

        # Update profile information if save_info was checked
        profile = None
        username = intent.metadata.username
        if username != 'AnonymousUser':
            profile = UserProfile.objects.get(user__username=username)
            if save_info:
                profile.default_phone_number = billing_details.phone
                profile.default_town_or_city = billing_details.address.city
                profile.default_country = billing_details.address.country
                profile.save()                

        order_exists = False
        attempt = 1
        while attempt <= 5:
            try:
                order = Order.objects.get(
                    full_name__iexact=billing_details.name,
                    email__iexact=billing_details.email,
                    phone_number__iexact=billing_details.phone,
                    town_or_city__iexact=billing_details.address.city,
                    country__iexact=billing_details.address.country,
                    grand_total=grand_total,
                    original_wallet=wallet,
                    stripe_pid=pid,
                )

                order_exists = True
                break
                
            except Order.DoesNotExist:
                attempt += 1
                time.sleep(1)
        if order_exists:
            self._send_confirmatin_email(order)
            return HttpResponse(
                    content=(
                        f'Webhook received: {event["type"]} | SUCCESS: '
                        'Verified order already in database'
                    ), status=200)
        else:
            order = None
            try:
                order = Order.objects.create(
                    full_name=billing_details.name,
                    user_profile=profile,
                    email=billing_details.email,
                    phone_number=billing_details.phone,
                    town_or_city=billing_details.address.city,
                    country=billing_details.address.country,
                    original_wallet=wallet,
                    stripe_pid=pid,
                )
                for ticket_id, quantity in json.loads(wallet).items():
                    destination = Destination.objects.get(id=ticket_id)
                    order_line_item = OrderLineItem(
                        order=order,
                        destination=destination,
                        quantity=quantity,
                    )
                    order_line_item.save()
            except Exception as e:
                if order:
                    order.delete()
                return HttpResponse(
                    content=f'Webhook received: {event["type"]} | ERROR: {e}',
                    status=500)

        self._send_confirmatin_email(order)
        return HttpResponse(
            content=(f'Webhook received: {event["type"]} | SUCCESS: '
                     'Created order in webhook'),
            status=200)

    def handle_payment_intent_payment_failed(self, event):
        """handle failed payment intent webhooks from stripe"""
        return HttpResponse(
            content=f'failed Webhook received: {event["type"]}',
            status=200)
