from django.contrib import admin
from django.contrib.admin.actions import delete_selected

from children.models import Child


@admin.register(Child)
class ChildAdmin(admin.ModelAdmin):
    delete_selected.short_description = "Удалить выбранных"

    # Какие поля показывать в списке
    list_display = [
        'full_name',
        'cyberons',
        'status',
        'created_at'
    ]

    # Фильтры справа
    list_filter = ['status', 'created_at']

    search_fields = ['last_name', 'first_name', 'middle_name']
    ordering = ['last_name', 'first_name']
    list_per_page = 20

    # Группировка полей на странице редактирования
    fieldsets = [
        ('Основная информация', {
            'fields': ['last_name', 'first_name', 'middle_name']
        }),
        ('Данные', {
            'fields': ['status', 'cyberons']
        }),
        ('Системные поля', {
            'fields': ['created_at', 'updated_at'],
            'classes': ['collapse']  # Сворачиваем по умолчанию
        })
    ]

    readonly_fields = ['created_at', 'updated_at']

    actions = ['make_clients', 'make_leads', 'delete_selected']

    def make_clients(self, request, queryset):
        """Сделать выбранных детей клиентами"""
        updated = queryset.update(status=Child.Status.CLIENT)
        self.message_user(request, f'{updated} детей стали клиентами')

    make_clients.short_description = "Сделать клиентами"

    def make_leads(self, request, queryset):
        """Сделать выбранных детей лидами"""
        updated = queryset.update(status=Child.Status.LEAD)
        self.message_user(request, f'{updated} детей стали лидами')

    make_leads.short_description = "Сделать лидами"
