# Generated by Django 2.0.6 on 2018-06-14 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20180614_0139'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='img_src',
            field=models.CharField(default='images/pic01.jpg', max_length=30),
        ),
    ]
