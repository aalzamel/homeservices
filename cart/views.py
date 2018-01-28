from django.shortcuts import render
from .models import Cart, CartItem
from services.models import Product

def cart(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    item_id = request.GET.get("item")
    qty = request.GET.get("qty", 1)
    if item_id:
        product = Product.objects.get(id=item_id)
        cart_item, created = CartItem.objects.get_or_create(cart=cart, item=product)
        if int(qty) < 1:
            cart_item.delete()
        else:
            cart_item.quantity = int(qty)
            cart_item.save()
    return render(request, 'cart.html', {'cart': cart})
