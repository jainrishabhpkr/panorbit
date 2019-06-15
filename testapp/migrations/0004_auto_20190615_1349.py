# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-06-15 08:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0003_discount_value'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productcategory',
            name='discount',
        ),
        migrations.AddField(
            model_name='discount',
            name='product_category',
            field=models.ManyToManyField(blank=True, null=True, related_name='product_category', to='testapp.ProductCategory'),
        ),
    ]
