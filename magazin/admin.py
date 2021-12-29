from django.contrib import admin
from .models import Category, Product, ItemImage
# Register your models here.
admin.register(Category)
admin.register(Product)
admin.register(ItemImage)

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(ItemImage)