from django.shortcuts import render, redirect
from .models import Product
from .models import CartItem
from .forms import ProductForm
from django.contrib.auth.decorators import login_required

def home(request):
    # products = Product.objects.all()
    # return render(request, 'home.html', {'products': products})
    context = {'products': Product.objects.all()}
    return render(request, 'home.html', context)

def cart(request):
    context = {'products': CartItem.objects.all().filter(owner=request.user)}
    return render(request, 'cart.html', context)

@login_required
def myspace(request):
    products = Product.objects.all().filter(owner=request.user)
    return render (request, 'myspace.html', {'products': products})

def productPage(request, product_id=None):
    products = Product.objects.all().filter(id=product_id)
    if not products:
        return HttpResponseNotFound('<h1>Page not found</h1>')
    product = products[0]
    context = {'product': product}
    return render(request, 'productPage.html', context)

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

@login_required
def addToCart(request):
    context = {}
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            context['product'] = Product.objects.all().filter(id=form.get('product'))
            prod = form.save(commit=False)
            prod.owner = request.user
            prod.save()
        context['form'] = form
    return render(request, 'productPage.html', context)
