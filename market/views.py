from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, OrderItem, Order
from .forms import ProductForm, CartForm
from django.contrib.auth.decorators import login_required

def home(request):
    # products = Product.objects.all()
    # return render(request, 'home.html', {'products': products})
    context = {'products': Product.objects.all()}
    return render(request, 'home.html', context)

@login_required
def cart(request):
    # context = {'products': Order.objects.get(user=request.user).products.all()}
    context = {}
    orders = Order.objects.all().filter(user=request.user)
    if orders.exists():
        order = orders[0]
        # context = {'products': order.products.all(), 'order':order}
        context = {'order' : order}
        print(context)
    
    return render(request, 'cart.html', context)

@login_required
def myspace(request):
    products = Product.objects.all().filter(owner=request.user)
    return render (request, 'myspace.html', {'products': products})

@login_required
def addItem(request):
    context = {'product': Product.objects.all()}
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
    return render(request, 'productPage.html', context)

@login_required
def addToCart(request, product_id=None):
    products = Product.objects.all().filter(id=product_id)
    if not products:
        return HttpResponseNotFound('<h1>Page not found</h1>')
    product = products[0]
    context = {'product': product}
    # context = {}
    if request.method == 'POST':
        form = CartForm(request.POST)
        if form.is_valid():
            context['product'] = Product.objects.all().filter(id=form.data['product'])
            item = get_object_or_404(Product, id=form.data['product'])
            order_item, created = OrderItem.objects.get_or_create(
                product = item,
                user = request.user,
                ordered = False
            )
            order_set = Order.objects.filter(user=request.user, ordered=False)
            # all_orders = Order.objects.get(user=request.user, ordered=False);
            # print(all_orders.user)
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
                    # print(order_item.quantity)
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
                return render(request, 'cart_confirmation.html', context)
    return render(request, 'productPage.html', context)

@login_required
def modifyProduct(request, product_id=None):
    products = Product.objects.all().filter(id=product_id)
    if not products:
        return HttpResponseNotFound('<h1>Page not found</h1>')
    product = products[0]
    context = {'product': product}
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
