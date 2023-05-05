from django.db import models
from user.models import Vendor, Customer
from django_filters import rest_framework as filters


class Category(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)

    def str(self):
        return self.name


class Product(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=False, blank=False)
    description = models.TextField()
    price = models.IntegerField(null=False, blank=False)

    def __str__(self):
        return self.name


class Cart(models.Model):
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE)
    product = models.ManyToManyField(Product)

    def __str__(self):
        return self.customer.email


class Accounting(models.Model):
    date = models.DateField()
    description = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    is_expense = models.BooleanField()

