from django.contrib import admin

from rent_app.models import Property, Renter, Request


@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    exclude = ['id']
    list_display = ['price', 'renter', 'address', 'space', 'phone_number']
    list_filter = ['renter', 'price', 'space']
    search_fields = ['address', 'phone_number']


@admin.register(Renter)
class RenterAdmin(admin.ModelAdmin):
    exclude = ['id']
    list_display = ['title', 'director']
    list_filter = ['director']
    search_fields = ['title']


@admin.register(Request)
class RequestAdmin(admin.ModelAdmin):
    exclude = []
    list_display = ['id', 'user', 'phone_number', 'property']
    list_filter = ['created_at', 'updated_at']
    search_fields = ['user', 'phone_number', 'property']
