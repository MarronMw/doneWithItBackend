from django.db import models

# Create your models here.


class Listings(models.Model):
    title = models.CharField(name="title")
    price = models.IntegerField(name="price")
    image = models.ImageField(name="image", upload_to='./uploads')

    def __str__(self):
        return self.title+" - $" + str(self.price)

    class Meta:
        verbose_name = "Listing"
        verbose_name_plural = "Listings"
        ordering = ['-id']
