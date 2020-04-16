from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

def get_upload_path(instance, filename):
    return 'user-' + str(instance.owner.id) + '/' + filename


# Create your models here.
class Product(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, default ='1')
    title = models.TextField()
    description = models.TextField(max_length=10000)
    image_url = models.FileField(upload_to=get_upload_path)
    price = models.IntegerField()

    # def add_to_cart(self):
        # self.published_date = timezone.now()
        # self.save()

    def __str__(self):
        return self.title

