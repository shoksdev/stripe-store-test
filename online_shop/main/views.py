import stripe
from django.conf import settings
from django.http.response import JsonResponse
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView, ListView, CreateView
from django.views.generic.base import TemplateView

from .forms import OrderForm
from .models import Item, Order


class HomeView(TemplateView):
    template_name = 'home.html'


class ItemListView(ListView):
    model = Item
    template_name = 'items/items_list.html'
    context_object_name = 'items_list'


class ItemDetailView(DetailView):
    model = Item
    template_name = 'items/item_detail.html'
    context_object_name = 'item'


class OrderListView(ListView):
    model = Order
    template_name = 'orders/orders_list.html'
    context_object_name = 'orders_list'


class OrderDetailView(DetailView):
    model = Order
    template_name = 'orders/order_detail.html'
    context_object_name = 'order'


class OrderCreateView(CreateView):
    model = Order
    template_name = 'orders/order_create.html'
    form_class = OrderForm
    success_url = reverse_lazy('orders_list')


class SuccessView(TemplateView):
    template_name = 'stripe_templates/success.html'


class CancelledView(TemplateView):
    template_name = 'stripe_templates/cancelled.html'


@csrf_exempt
def stripe_config(request):
    if request.method == 'GET':
        stripe_config = {'publicKey': settings.STRIPE_PUBLISHABLE_KEY}
        return JsonResponse(stripe_config, safe=False)


@csrf_exempt
def create_item_checkout_session(request, pk):
    try:
        item = Item.objects.get(id=pk)
        domain_url = 'http://127.0.0.1:8000/'
        stripe.api_key = settings.STRIPE_SECRET_KEY

        checkout_session = stripe.checkout.Session.create(
            success_url=domain_url + 'success?session_id={CHECKOUT_SESSION_ID}',
            cancel_url=domain_url + 'cancelled/',
            payment_method_types=['card'],
            mode='payment',
            currency=request.user.currency,
            line_items=[
                {
                    'price': item.stripe_price,
                    'quantity': 1,
                }

            ],
        )

        return JsonResponse({'sessionId': checkout_session['id']})

    except Exception as e:
        return JsonResponse({'error': str(e)})



@csrf_exempt
def create_order_checkout_session(request, pk):
    try:
        order_items = Order.objects.get(id=pk).items.all()
        domain_url = 'http://127.0.0.1:8000/'
        stripe.api_key = settings.STRIPE_SECRET_KEY
        line_items_list = []

        for item in order_items:
            line_items_list.append(
                {
                    'price': item.stripe_price,
                    'quantity': 1
                }
            )

        checkout_session = stripe.checkout.Session.create(
            success_url=domain_url + 'success?session_id={CHECKOUT_SESSION_ID}',
            cancel_url=domain_url + 'cancelled/',
            payment_method_types=['card'],
            mode='payment',
            currency=request.user.currency,
            line_items=line_items_list,
        )

        return JsonResponse({'sessionId': checkout_session['id']})

    except Exception as e:
        return JsonResponse({'error': str(e)})
