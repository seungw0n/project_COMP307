from django.db import models

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