from django.db import models
from django.forms import ModelForm


# Create your models here.
class Product(models.Model):
    title = models.TextField()
    description = models.TextField()
    image_url = models.TextField()
    price = models.IntegerField()

    # def add_to_cart(self):
        # self.published_date = timezone.now()
        # self.save()

    def __str__(self):
        return self.title

class Meta:
        model : Product
        fields : ['title', 'description', 'image_url' , 'price']
   
