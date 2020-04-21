from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

def get_upload_path(instance, filename):
    return 'user-' + str(instance.owner.id)+ '/' + filename


# Create your models here.


class Product(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, default ='1')
    title = models.TextField()
    description = models.TextField(max_length=10000)
    image_url = models.FileField(upload_to=get_upload_path)
    inventoryCount = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    price = models.FloatField()
    category = models.TextField()

    # def add_to_cart(self):
        # self.published_date = timezone.now()
        # self.save()

    def __str__(self):
        return self.title

class OrderItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    ordered = models.BooleanField(default=False)

    # def __str__(self):
    #     return self.product
    
    def get_total_price_true(self):
        return self.quantity * self.product.price

    def get_total_price(self):
        return "%.2f"%round(self.quantity * self.product.price, 2)

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(OrderItem)
    ordered = models.BooleanField(default=False)
    address = models.TextField(default="")
    orderDate = models.DateTimeField(auto_now_add=True, blank=True)

    # def __str__(self):
    #     return self.user

    def get_total_price(self):
        total = 0
        for item in self.products.all():
            total += item.get_total_price_true()
        return "%.2f"%round(total,2)
        
    def get_total_price_stripe(self):
        total = 0
        for item in self.products.all():
            total += item.get_total_price_true()
        return total * 100
