from django.urls import path
from core.views import index, product_list_view, category_list_view, category_product_list_view, vendor_list_view

app_name = 'core'

urlpatterns = [
    # Homepage
    path('', index, name='index'),
    path('products/', product_list_view, name='products'),
        
    # Category
    path('category/', category_list_view, name='category-list'),
    path('category/<cid>', category_product_list_view, name='category-product-list'),
    
    # Vendor
    path('vendors/', vendor_list_view, name='vendor-list'),
    
    
    
]