from django.contrib import admin
from django.urls import path
from services import views

app_name= 'services'


urlpatterns = [
    path('', views.home_view, name='home_view'),
    path('categories/', views.category_view, name='category_view'),
    path('products/', views.products, name='products'),
    path('detail/<str:product_name>', views.product_detail, name='detail'),
    path('signup/', views.usersignup, name="usersignup"),
    path('login/', views.userlogin, name="userlogin"),
    path('logout/', views.userlogout, name="userlogout"),
]

