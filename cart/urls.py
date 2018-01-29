from django.contrib import admin
from django.urls import path
from cart import views

app_name= 'cart'


urlpatterns = [
    path('', views.cart, name='mycart'),
	path('cart_update/', views.recal_item, name='cart_update'),
	path('subtotal/', views.recal_total, name='subtotal'),

]

