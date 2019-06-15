from django.contrib import admin
from testapp.models import ProductCategory, Discount, Store

# Register your models here.

admin.site.register(ProductCategory)
admin.site.register(Discount)
admin.site.register(Store)
