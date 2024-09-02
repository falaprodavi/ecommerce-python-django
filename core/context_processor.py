from core.models import Category, Product, Vendor, CartOrder, ProductReview, CartOrderItems, ProductImages, Wishlist, Address

def default(request):
    
    categories = Category.objects.all()
    
    return {
        'categories':categories,
    }