from django.db import models

# Create your models here.
class Listings(models.Model):
    title=models.CharField(name="title")
    price=models.IntegerField(name="price")
    image=models.ImageField(name="image",upload_to='./uploads')
        