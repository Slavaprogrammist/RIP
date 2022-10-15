from django.db import models
from django.db import models


class Stock(models.Model):
    avto_name = models.CharField(max_length=50, verbose_name="Название автомобиля")
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Цена аренды за час")
    arenda = models.BooleanField(verbose_name="Можно ли арендовать в данный момент?")
    date_modified = models.DateTimeField(auto_now=True, verbose_name="Когда последний раз была в аренде?")
