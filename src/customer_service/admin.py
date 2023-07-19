from django.contrib import admin

from customer_service.models import Message


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'subject', 'read', 'author']
    list_editable = ['read']
    empty_value_display = 'Inconu'
    #filters
    list_filter = ['read']
    list_per_page = 10
