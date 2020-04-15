from django import forms

class ProductForm(forms.Form):
    title = forms.CharField(max_length=100)
    description = forms.CharField(max_length=500)
    image_url = forms.ImageField()
    price = forms.IntegerField()

   