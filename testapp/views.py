from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework.views import APIView
from rest_framework.response import Response
from testapp.models import Discount,Store,ProductCategory
from testapp.serializers import DiscountSerializer, ProductSerializer, StoreSerializer



# Create your views here

@method_decorator(csrf_exempt,name = 'dispatch')
class FirstapiView(APIView):
    def get(self,request,*args,**kwargs):
        discount = Discount.objects.all()


        serializer = DiscountSerializer(discount, many=True)
        print(serializer.data)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = DiscountSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=404)

@method_decorator(csrf_exempt,name = 'dispatch')
class SecondapiView(APIView):
    def get(self,request,*args,**kwargs):
        pass
