from django.contrib import admin

from .models import Clients, Orders, Products, Category


@admin.action(description='Очистить склад')
def reset_quantity(modeladmin, request, queryset):
    queryset.update(quantity=0)


@admin.register(Products)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'quantity',
        'arrived_date',
        'price',
    )
    list_display_links = (
        'name',
    )
    list_filter = (
        'category',
    )
    ordering = (
        '-price',
    )
    search_fields = (
        'descr',
    )
    search_help_text = 'Поиск по описанию'
    actions = (
        reset_quantity,
    )
    fieldsets = (
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['name'],
            }
        ),
        (
            'Описание',
            {
                'classes': ['collapse'],
                'description': 'Категория и описание товара',
                'fields': ['category', 'descr']
            }
        ),
        (
            'Цена и количество',
            {
                'fields': ['price', 'quantity'],
            }
        ),
    )


@admin.register(Clients)
class ClientsAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone']


@admin.register(Orders)
class OrdersAdmin(admin.ModelAdmin):
    list_display = ['client_name', 'total_price', 'order_date']
    list_filter = ['order_date']

    def client_name(self, obj):
        return obj.client.name
    client_name.short_description = 'Имя клиента'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']