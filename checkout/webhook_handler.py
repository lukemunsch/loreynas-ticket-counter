from django.http import HttpResponse


class StripeWH_Handler:
    """handle stripe webhooks"""
    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """handle generic/unknown/unexpect webhooks events"""
        return HttpResponse(
            content=f'Unhandled Webhook received: {event["type"]}',
            status=200
        )

    def handle_payment_intent_succeeded(self, event):
        """handle successful payment intent webhooks from stripe"""
        intent = event.data.object
        pid = intent.id
        wallet = intent.metadata.wallet
        save_info = intent.metadata.save_info

        billing_details = intent.charges.data[0].billing_details
        grand_total = round(intent.charges.data[0].amount / 100, 2)

        order_exists = False
        try:
            order = Order.object.get(
                full_name__iexact=billing_details.name,
                email__iexact=billing_details.email,
                phone_number__iexact=billing_details.phone,
                town_or_city__iexact=billing_details.address.city,
                country__iexact=billing_details.address.country,
                grand_total=grand_total,
            )

            order_exists = True
            return HttpResponse(
                content=(
                    f'Webhook received: {event["type"]} | SUCCESS: '
                    'Verified order already in database'
                ), status=200
            )
        except Order.DoesNotExist:
            try:
                order = Order.object.create(
                    full_name=billing_details.name,
                    email=billing_details.email,
                    phone_number=billing_details.phone,
                    town_or_city=billing_details.address.city,
                    country=billing_details.address.country,
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
                    
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_payment_failed(self, event):
        """handle failed payment intent webhooks from stripe"""
        return HttpResponse(
            content=f'failed Webhook received: {event["type"]}',
            status=200
        )
