from django.db import models
import datetime
# Create your models here.

class Item(models.Model):
	name = models.CharField(max_length=50)
	description = models.CharField(max_length=100)

class Table(models.Model):
    table_id = models.CharField(max_length=3)
    password = models.CharField(max_length=16)

class Order(models.Model):
    order_id = models.IntegerField()

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
        ("normal", "正常糖"),
        ("little", "少糖"),
        ("no", "無糖"),
    )
    sugar = models.CharField(max_length=4, choices=sugar_choices)
    count = models.IntegerField()
    status_choices = (
        ("ongoing", "未送出"),
        ("submitted", "已送出"),
        ("payed", "已付款"),
        ("done", "已完成")
    )
    status = models.CharField(max_length=4, choices=status_choices, default="ongoing")
    # comment = models.CharField(max_length=100, blank=True)
