from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, OrderItem, Order
from .forms import ProductForm, CartForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages

def home(request):
    # products = Product.objects.all()
    # return render(request, 'home.html', {'products': products})
    context = {'products': Product.objects.all()}
    if request.user.is_authenticated:
        orders = Order.objects.all().filter(user=request.user, ordered=False)
        if orders.exists():
            order = orders[0]
            context['order'] = order
        
    return render(request, 'home.html', context)
    
def category(request, cat=None):
    context = {'products': Product.objects.all().filter(category=cat)}
    if request.user.is_authenticated:
        orders = Order.objects.all().filter(user=request.user, ordered=False)
        if orders.exists():
            order = orders[0]
            context['order'] = order
        
    return render(request, 'category.html', context)

@login_required
def cart(request):
    context = {}
    orders = Order.objects.all().filter(user=request.user, ordered=False)
    if orders.exists():
        order = orders[0]
        context['order'] = order
    
    return render(request, 'cart.html', context)

@login_required
def myspace(request):
    context = {'products': Product.objects.all().filter(owner=request.user)}
    orders = Order.objects.all().filter(user=request.user, ordered=False)
    if orders.exists():
        order = orders[0]
        context['order'] = order
    order_history = Order.objects.all().filter(user=request.user, ordered=True)
    if order_history.exists():
        context['order_history'] = order_history
        
    return render (request, 'myspace.html', context)

@login_required
def addItem(request):
    context = {'product': Product.objects.all()}
    orders = Order.objects.all().filter(user=request.user, ordered=False)
    if orders.exists():
        order = orders[0]
        context['order'] = order
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            prod = form.save(commit=False)
            prod.owner = request.user
            prod.save()
        context['form'] = form
    return render(request, 'addItem.html', context)

def productPage(request, product_id=None):
    products = Product.objects.all().filter(id=product_id)
    if not products:
        return HttpResponseNotFound('<h1>Page not found</h1>')
    product = products[0]
    context = {'product': product}
    if request.user.is_authenticated:
        orders = Order.objects.all().filter(user=request.user, ordered=False)
        if orders.exists():
            order = orders[0]
            context['order'] = order
    return render(request, 'productPage.html', context)

@login_required
def addToCart(request, product_id=None):
    products = Product.objects.all().filter(id=product_id)
    if not products:
        return HttpResponseNotFound('<h1>Page not found</h1>')
    product = products[0]
    context = {'product': product}
    if request.user.is_authenticated:
        orders = Order.objects.all().filter(user=request.user, ordered=False)
        if orders.exists():
            order = orders[0]
            context['order'] = order
    if request.method == 'POST':
        form = CartForm(request.POST)
        if form.is_valid():
            context['product'] = Product.objects.all().filter(id=form.data['product'])[0]
            item = get_object_or_404(Product, id=form.data['product'])
            order_item, created = OrderItem.objects.get_or_create(
                product = item,
                user = request.user,
                ordered = False
            )
            order_set = Order.objects.filter(user=request.user, ordered=False)
            if order_set.exists():
                order = order_set[0]
                if order.products.filter(product__id=item.id).exists():
                    order_item.quantity += int(form.data['quantity'])
                    order_item.save()
                    print("Added to existing item in existing order")
                    return render(request, 'cart_confirmation.html', context)
                else:
                    order_item.quantity = int(form.data['quantity'])
                    order_item.save()
                    order.products.add(order_item)
                    print("Added new item to existing order")
                    return render(request, 'cart_confirmation.html', context)
            else:
                order_item.quantity = int(form.data['quantity'])
                order_item.save()
                order = Order.objects.create(user = request.user)
                order.products.add(order_item)
                order.save()
                print("Created order")
                context['order'] = order
                return render(request, 'cart_confirmation.html', context)
    return HttpResponseRedirect(reverse('productPage'))


@login_required
def changeQuantity(request):
    if request.method == 'POST':
        form = CartForm(request.POST)
        if form.is_valid():
            product_id = form.data['product']
            item = get_object_or_404(Product, id=product_id)
            order_item = OrderItem.objects.get(product=item, user=request.user)
            order_set = Order.objects.filter(user=request.user, ordered=False)
            if order_set.exists():
                order = order_set[0]
                if order.products.filter(product__id=item.id).exists():
                    order_item.quantity = int(form.data['quantity'])
                    order_item.save()
                    print("Edited the quantity of existing item in existing order")        
    return HttpResponseRedirect(reverse('cart'))


@login_required
def removeFromCart(request):
    if request.method == 'POST':
        form = CartForm(request.POST)
        if form.is_valid():
            print("FORM IS VALID")
            product_id = form.data['product']
            item = get_object_or_404(Product, id=product_id)
            order_item = OrderItem.objects.get(product=item, user=request.user)
            order_set = Order.objects.filter(user=request.user, ordered=False)
            if order_set.exists():
                order = order_set[0]
                if order.products.filter(product__id=item.id).exists():
                    order.products.remove(order_item)
                    order_item.delete()
                    if order.products.count() == 0:
                        order.delete()
                        print("Order deleted because there is no more item left in the order.")
                    messages.info(request, "The item has been removed from your cart.")
                    print("Deleted the existing item from existing order") 
                else:
                    messages.info(request, "The item is not in your cart.")
            else:
                messages.info(request, "You do not have an active order.")
                
    return HttpResponseRedirect(reverse('cart'))


@login_required
def modifyProduct(request, product_id=None):
    products = Product.objects.all().filter(id=product_id)
    if not products:
        return HttpResponseNotFound('<h1>Page not found</h1>')
    product = products[0]
    context = {'product': product}
    orders = Order.objects.all().filter(user=request.user, ordered=False)
    if orders.exists():
        order = orders[0]
        context['order'] = order
    if request.method == 'POST':
        form = ProductForm(request.POST or None,request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('home')
        context['form'] = form
    return render(request, 'modifyProduct.html', context)

@login_required
def deleteProduct(request, product_id=None):
    products = Product.objects.all().filter(id=product_id)
    if not products:
        return HttpResponseNotFound('<h1>Page not found</h1>')
    product = products[0]
    product.delete()
    context = {}
    return render(request, 'deleteProduct.html', context)
