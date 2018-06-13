from django.db import models
import datetime
# Create your models here.

class Item(models.Model):
	name = models.CharField(max_length=50)
	description = models.CharField(max_length=100)

class Customer(models.Model):
    table = models.CharField(max_length=3)
    password = models.CharField(max_length=16)

class Order(models.Model):
    order_id = models.IntegerField()

class SingleOrder(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
	#table = models.ForeignKey(Customer, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    temp_choices = (
        ("iced", "正常冰"),
        ("little-iced", "少冰"),
        ("cool", "去冰"),
        ("hot", "熱"),
    )
    temp = models.CharField(max_length=4, choices=temp_choices)
    sugar_choices = (
        ("normal", "正常糖"),
        ("little", "少糖"),
        ("no", "無糖"),
    )
    sugar = models.CharField(max_length=4, choices=sugar_choices)
    count = models.IntegerField()
    status_choices = (
        ("unsent", "未下單"),
        ("unconfirmed", "服務生未確認"),
		("confirmed", "服務生已確認"),
        ("payed", "已付款")
    )
    status = models.CharField(max_length=4, choices=status_choices, default="unsent")
    # comment = models.CharField(max_length=100, blank=True)
