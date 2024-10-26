from django.shortcuts import render
from .models import Product  # Ensure this import is correct

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