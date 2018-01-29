from django.shortcuts import render, redirect
from .models import Cart, CartItem
from services.models import Product
from django.http import JsonResponse

def cart(request):
    if request.user.is_anonymous:
        return redirect("services:userlogin")


    cart, created = Cart.objects.get_or_create(user=request.user)
    item_id = request.GET.get("item_id")
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




def recal_item(request):
    item_id = request.GET.get("item_id")
    pre_delete = item_id
    qty = request.GET.get("qty")
    item = CartItem.objects.get(id=item_id)
    status = ""
    item.quantity=qty
    if int(qty) <= 0:
        status="delete"
        item.delete()
    else:
        item.save()

    resp = {
        "id":item.id,
        "quantity": item.quantity,
        "total": item.line_item_total,
        "status":status,
        "pre_delete":pre_delete,
    }

    return JsonResponse(resp, safe=False)


def recal_total(request):
    cart_id = request.GET.get("cart_id")
    current_cart = Cart.objects.get(id=cart_id)
    total = current_cart.total
    subtotal = current_cart.subtotal

    context = {
        'cart_id': cart_id,
        'subtotal': subtotal,
        'total': total,
    }
    return JsonResponse(context, safe=False)
