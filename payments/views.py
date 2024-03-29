from django.shortcuts import render, redirect
from market.models import Product, OrderItem, Order
from django.contrib.auth.decorators import login_required
from datetime import datetime
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
        orders = Order.objects.all().filter(user=request.user)
        size = len(Order.objects.all().filter(user=request.user))
        order =orders[size-1]
        for item in order.products.all():
            item.product.inventoryCount = item.product.inventoryCount - item.quantity
            item.product.save()
        price = int(order.get_total_price_stripe())
        print(price)
        order.ordered = True
        order.orderDate = datetime.now()
        order.save()
        charge = stripe.Charge.create(
            amount= price,
            currency='cad',
            description='PAYMENT',
            source=request.POST['stripeToken']
        )
        return render(request, 'charge.html')

@login_required
def detail(request):
    context = {}
    if request.method == 'GET':
        orders = Order.objects.all().filter(user=request.user)
        if orders.exists():
                order = orders[0]
                order.address = request.user.profile.address
                order.save()
                context = {'order' : order}
        return render(request, 'details.html', context)
