from django.contrib import admin

# Register your models here.
from .models import Unit, Category, Product




admin.site.register(Unit)
admin.site.register(Category)
admin.site.register(Product)

