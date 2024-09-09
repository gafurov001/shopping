from django.contrib import admin

from apps.models import Product, User, Cart


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    pass
