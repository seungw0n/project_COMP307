from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm
    
def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products': products})

def cart(request):
    return render(request, 'cart.html', {})

def myspace(request):
    products = Product.objects.all()
    return render (request, 'myspace.html', {'products': products})

def addItem(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            form.clean()
            return redirect('home')
    else:
        form = ProductForm()
    return render(request, 'addItem.html', {'form': form})