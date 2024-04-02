from django.contrib import admin
from product import models


@admin.register(models.PhoneProduct)
class PhoneProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'brief_info')
    list_display_links = ('name',)
    ordering = ['name']
    list_editable = 'price',
    list_per_page = 5
    actions = ['set_quantity_1']

    @admin.display(description='Описание')
    def brief_info(self, obj):
        return obj.description

    def set_quantity_1(self, request, queryset):
        queryset.update(quantity=1)


@admin.register(models.PhoneCategory)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')


@admin.register(models.PhoneTag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'tag')
    list_display_links = ('id', 'tag')
