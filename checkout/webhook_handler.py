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
        print(intent)

        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_payment_failed(self, event):
        """handle failed payment intent webhooks from stripe"""
        return HttpResponse(
            content=f'failed Webhook received: {event["type"]}',
            status=200
        )
