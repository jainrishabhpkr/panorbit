from rest_framework import serializers
from testapp.models import Discount, ProductCategory, Store



class DiscountSerializer(serializers.ModelSerializer):
    # productcategory = serializers.SerializerMethodField('product_list')

    # def product_list(self, obj):
    #     discounts = Discount.objects.all()
    #     products = ProductCategory.objects.all()
    #     prod_list = []
    #
    #     for discount_123 in discounts:
    #         for product in products:
    #             if product.discount.value == discount_123.value:
    #                 list.append(discount_123)
    #
    #     return prod_list
    class Meta:
        model = Discount
        fields = '__all__'


class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = '__all__'



class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = '__all__'
