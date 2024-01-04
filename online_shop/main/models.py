from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    CURRENCY_CHOICES = (
        ('rub', 'Russian Ruble'),
        ('usd', 'American Dollar'),
    )
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES, default=CURRENCY_CHOICES[0][0],
                                verbose_name='Currency')

    def __str__(self):
        return self.username


class Item(models.Model):
    name = models.CharField(max_length=50, verbose_name='Name')
    description = models.TextField(verbose_name='Description')
    price = models.IntegerField(default=0, verbose_name='Price')
    stripe_price = models.CharField(max_length=250, verbose_name="Stripe Price's ID")

    def __str__(self):
        return self.name


class Order(models.Model):
    items = models.ManyToManyField(Item, verbose_name='Items')
