from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Product, Customer
from .serializers import ProductSerializer, CustomerSerializer
import rest_framework.status as status
from django.core.exceptions import ObjectDoesNotExist

def product_list(request):
    try:
        products = Product.objects.all().order_by('-created_at')
        context = {
            'products': products,
        }
        return render(request, 'products/product_list.html', context)
    except Exception as e:
        print(f"Error: {e}")  # This will help debug
        return render(request, 'products/product_list.html', {'products': []})


# Create Product (POST)
@api_view(['POST'])
def create_product(request):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Read Product (GET)
@api_view(['GET'])
def get_product(request, pk=None):
    try:
        product = Product.objects.get(pk=pk)
    except ObjectDoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = ProductSerializer(product)
    return Response(serializer.data)

# Update Product (PUT)
@api_view(['PUT'])
def update_product(request, pk=None):
    try:
        product = Product.objects.get(pk=pk)
    except ObjectDoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = ProductSerializer(product, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Delete Product (DELETE)
@api_view(['DELETE'])
def delete_product(request, pk=None):
    try:
        product = Product.objects.get(pk=pk)
    except ObjectDoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    product.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

# Create Customer (POST)
@api_view(['POST'])
def create_customer(request):
    serializer = CustomerSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Read Customer (GET)
@api_view(['GET'])
def get_customer(request, pk=None):
    try:
        customer = Customer.objects.get(pk=pk)
    except ObjectDoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = CustomerSerializer(customer)
    return Response(serializer.data)

# Update Customer (PUT)
@api_view(['PUT'])
def update_customer(request, pk=None):
    try:
        customer = Customer.objects.get(pk=pk)
    except ObjectDoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = CustomerSerializer(customer, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Delete Customer (DELETE)
@api_view(['DELETE'])
def delete_customer(request, pk=None):
    try:
        customer = Customer.objects.get(pk=pk)
    except ObjectDoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    customer.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)