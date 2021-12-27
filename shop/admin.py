from django.contrib import admin

from shop.models import Category, Item, ItemImage


class CategoryAdmin(admin.ModelAdmin):
    pass


class ItemAdmin(admin.ModelAdmin):
    pass


class ItemImageAdmin(admin.ModelAdmin):
    pass


admin.site.register(Category)
admin.site.register(Item)
admin.site.register(ItemImage)
