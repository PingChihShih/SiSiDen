from django.db import models
import datetime
# Create your models here.

class Item(models.Model):
	name = models.CharField(max_length=50)
	description = models.CharField(max_length=100)

class Customer(models.Model):
    table_id = models.DecimalField(max_digits=2, decimal_places=0)
    password = models.CharField(max_length=30)

class Order(models.Model):
    order_id = models.DecimalField(max_digits=5, decimal_places=0)

class SingleOrder(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    temp_choices = (
        ("iced", "正常冰"),
        ("little-iced", "少冰"),
        ("cool", "去冰"),
        ("hot", "熱"),
    )
    temp = models.CharField(max_length=4, choices=temp_choices)
    sugar_choices = (
        ("normal-sugar", "正常糖"),
        ("little-sugar", "少糖"),
        ("no-sugar", "無糖"),
    )
    sugar = models.CharField(max_length=4, choices=sugar_choices)
    count = models.DecimalField(max_digits=2, decimal_places=0)
    # comment = models.CharField(max_length=100, blank=True)
