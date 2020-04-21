from django.forms import ModelForm
from market.models import Order

class Checkout(ModelForm):
    class Meta:
        model = Order
        fields = ['address']
