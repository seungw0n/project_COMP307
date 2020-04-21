from django.shortcuts import render, redirect
from market.models import Product, OrderItem, Order
from django.contrib.auth.decorators import login_required
from .forms import Checkout
# # For stripe
import stripe
from django.conf import settings # to pass the key value
stripe.api_key = settings.STRIPE_SECRET_KEY


# @login_required
# def checkout(request):
#     context = {}
#     if request.method == 'GET':
#         orders = Order.objects.all().filter(user=request.user)
#         if orders.exists():
#             order = orders[0]
#             # context = {'products': order.products.all(), 'order':order}
#             context = {'order' : order}
#         return render(request, 'checkout.html', context)


# def get_context_data(self, **kwargs):
#     context = super().get_context_data(**kwargs)
#     context['key'] = settings.STRIPE_PUBLISHABLE_KEY
#     return context
@login_required
def charge(request):
    if request.method == 'POST':
        order = Order.objects.get(user=request.user)
        price = int(order.get_total_price())
        print(price)
        charge = stripe.Charge.create(
            amount= price,
            currency='cad',
            description='PAYMENT',
            source=request.POST['stripeToken']
        )
        return render(request, 'charge.html')

@login_required
def detail(request):
    if request.method == 'GET':
        form = Checkout()
        return render(request, 'details.html', {'form': form})
