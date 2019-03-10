from django.db import models


# Create your models here.
class PizzaShop(models.Model):
    name = models.CharField(max_length=30, verbose_name="Pizza house")
    description = models.TextField(verbose_name="Description")
    rating = models.FloatField(verbose_name="Rating")
    url = models.URLField(verbose_name="Iternet address")

    class Meta:
        verbose_name = "Піццерія"
        verbose_name_plural = "Піцерії"

    def __str__(self):
        return self.name


class Pizza(models.Model):
    pizzashop = models.ForeignKey(PizzaShop, on_delete=models.CASCADE)
    name = models.CharField(max_length=30, verbose_name="Pizza name")
    short_description = models.CharField(max_length=30, verbose_name="Short desc")
    price = models.IntegerField(default=0, verbose_name="Price")
    photo = models.ImageField('Photo', upload_to='firstapp/photos', default='', blank=True)

    def __str__(self):
        return self.name
