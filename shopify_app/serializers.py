# shopify_app/serializers.py
from rest_framework import serializers
from .models import Product, Customer

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'  # Includes all fields in the Product model

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'  # Includes all fields in the Product model
