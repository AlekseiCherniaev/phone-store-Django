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
    search_fields = ['name']
    list_filter = ['category__name']
    prepopulated_fields = {'slug': ('name',)}
    @admin.display(description='Описание')
    def brief_info(self, obj):
        return obj.description

    @admin.action(description='Изменить кол-во на 0')
    def set_quantity_1(self, request, queryset):
        count = queryset.update(quantity=0)
        self.message_user(request, f'Изменено {count} записей')


@admin.register(models.PhoneCategory)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')


@admin.register(models.PhoneTag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'tag')
    list_display_links = ('id', 'tag')
