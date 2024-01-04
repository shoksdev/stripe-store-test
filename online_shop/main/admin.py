from django.contrib import admin

from .models import CustomUser, Item, Order


@admin.register(CustomUser)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'currency')


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price',)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', )
