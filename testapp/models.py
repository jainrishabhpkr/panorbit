from django.db import models

# Create your models here.

PRODUCT_CHOICES = [('phone','Phones'),('paint','Paint'),('jeans','Jeans'),('stationary','Stationary')]

class ProductCategory(models.Model):
    name = models.CharField(max_length=20, choices = PRODUCT_CHOICES)


    def __str__(self):
        return self.name


class Discount(models.Model):
    value = models.IntegerField(default=0)
    startdate = models.DateField()
    enddate = models.DateField()
    product_category = models.ManyToManyField(ProductCategory,related_name='product_category',blank = True, null = True)

    def __str__(self):
        return str(self.id)







class Store(models.Model):
    storename = models.CharField(max_length=50)
    products = models.ManyToManyField(ProductCategory, blank=True)
    def __str__(self):
        return self.storename
