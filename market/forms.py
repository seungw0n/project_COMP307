from django.forms import ModelForm
from .models import Product, OrderItem, Order

class ProductForm(ModelForm):
   class Meta:
        model = Product
        fields = ['title', 'description', 'image_url' , 'price', 'inventoryCount','category']
   

class CartForm(ModelForm):
    class Meta:
        model = OrderItem
        fields = ['quantity']