from django.urls import path
from shop.views import index, detail, checkout,confirmation
from .views import products
from .views import load_products

urlpatterns = [
    path('', index, name='home'),
    path('<int:myid>', detail, name="detail"),
    path('checkout',checkout, name="checkout"),
    path('confirmation', confirmation, name="confirmation"),
    path('products/', products, name='products'),
     path('load_products/', load_products, name='load_products'),
    
]