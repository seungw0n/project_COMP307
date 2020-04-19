from django.forms import ModelForm
from .models import Product
from .models import CartItem

class ProductForm(ModelForm):
   class Meta:
        model = Product
        fields = ['title', 'description', 'image_url' , 'price', 'inventoryCount']
   

class CartForm(ModelForm):
    class Meta:
        model = CartItem
        fields = ['product', 'quantity']