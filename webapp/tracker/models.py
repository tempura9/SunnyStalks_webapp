from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

class Branch(models.Model):
    address = models.CharField(max_length=255)
    costs = models.DecimalField(max_digits=10, decimal_places=2)
    def getCosts():
        # compute average from purchases
        return;

class GroceryStore(models.Model):
    name = models.CharField(max_length=255)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, related_name='stores')

class Item(models.Model):
    name = models.CharField(max_length=255)
    brand = models.CharField(max_length=255)
    grocery_store = models.ForeignKey(GroceryStore, on_delete=models.CASCADE, related_name='items')
    price = models.DecimalField(max_digits=10, decimal_places=2)

class Purchase(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='purchases')
    grocery_store = models.ForeignKey(GroceryStore, on_delete=models.CASCADE, related_name='purchases')
    date = models.DateField(auto_now_add=True)
