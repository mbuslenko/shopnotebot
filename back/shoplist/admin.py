from django.contrib import admin
from shoplist.models import Profile, Item, Category, Month


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'external_id', 'name')


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('profile', 'name', 'price', 'link')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('profile', 'name')


admin.site.register(Month)
