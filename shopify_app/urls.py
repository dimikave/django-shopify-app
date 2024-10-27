"""
URL configuration for shopify_app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, re_path

from shopify_app import views

urlpatterns = [
    path("admin/", admin.site.urls),

    # Authentication endpoints (with re_path just to check a new way)
    re_path('login', views.login),
    re_path('signup', views.signup),
    re_path('test_token', views.test_token),

    # Product Endpoints
    path('products-list/', views.product_list, name='product_list'),
    path('products', views.get_product_list, name='get_product_list'), # GET
    path('product', views.create_product, name='create_product'),  # POST
    path('product/<int:pk>', views.get_product, name='get_product'),  # GET
    path('product/<int:pk>/update', views.update_product, name='update_product'),  # PUT
    path('product/<int:pk>/delete', views.delete_product, name='delete_product'),  # DELETE

    # Customer Endpoints
    path('customer', views.create_customer, name='create_customer'),         # POST
    path('customer/<int:pk>', views.get_customer, name='get_customer'),      # GET
    path('customer/<int:pk>/update', views.update_customer, name='update_customer'),  # PUT
    path('customer/<int:pk>/delete', views.delete_customer, name='delete_customer'),  # DELETE
]